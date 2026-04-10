---
name: gda-analyze
description: Android APK analysis using GDA.exe. AI drives analysis by tracing code paths, extracting IOCs (including encrypted), and producing structured malware reports.
argument-hint: [apk_path] [analysis_goal_or_focus]
disable-model-invocation: true
allowed-tools: Bash
---

## Overview

This skill performs malware analysis on Android APKs using GDA.exe. The workflow is: **Recon -> Trace -> Extract -> Decrypt -> Report**.

**GDA.exe Path**: `GDA_EXE="${CLAUDE_SKILL_DIR}/bin/gda.exe"`

---

## Analysis Workflow

### Phase 1: Recon

```bash
python gda_analyze.py sample.apk binfo
python gda_analyze.py sample.apk permission
python gda_analyze.py sample.apk axml
```

### Phase 2: Trace

```bash
# 1. Attack surface - exported components
python gda_analyze.py sample.apk attsf

# 2. Malware scan - automated detection
python gda_analyze.py sample.apk malscan

# 3. Trace suspicious components
python gda_analyze.py sample.apk "listm com.suspicious.Class"
python gda_analyze.py sample.apk "dec -c com.suspicious.Class"
python gda_analyze.py sample.apk "xref -c com.suspicious.Class"
python gda_analyze.py sample.apk "dasm method@xxxxx"
```

### Phase 3: Extract

```bash
# Network IOCs
python gda_analyze.py sample.apk sensinf
python gda_analyze.py sample.apk "find -s http"
python gda_analyze.py sample.apk "find -s 192"
python gda_analyze.py sample.apk "find -s socket"
python gda_analyze.py sample.apk uri

# Encryption strings
python gda_analyze.py sample.apk "find -s Base64"
python gda_analyze.py sample.apk "find -s DES"
python gda_analyze.py sample.apk "find -s AES"
python gda_analyze.py sample.apk "find -s RC4"
```

### Phase 4: Decrypt

```bash
# Find encryption-related method calls
python gda_analyze.py sample.apk "find -m getInstance"
python gda_analyze.py sample.apk "find -m doFinal"
python gda_analyze.py sample.apk "find -m SecretKeySpec"
python gda_analyze.py sample.apk "find -m IvParameterSpec"

# Trace encryption class
python gda_analyze.py sample.apk "dec -c com.malware.CryptoClass"

# Find key storage
python gda_analyze.py sample.apk "find -s SharedPreferences"
python gda_analyze.py sample.apk "find -s getString"

# If key found, generate Python decrypt script
```

---

## Malware Analysis Report Template

```
# [APK Name] - Malware Analysis Report

## 1. Sample Overview

| Attribute | Value |
|-----------|-------|
| Package Name | from binfo |
| File Size | from binfo |
| MD5 | from binfo |
| SHA256 | from binfo |
| DEX Info | class count, method count from binfo |

## 2. Plaintext IOCs

- C2 Addresses: [from sensinf/find -s]
- URLs: [from find -s http]
- IPs: [from find -s 192]
- Paths: [from uri]

## 3. Encrypted IOCs & Decryption

| IOC Type | Cipher | Mode | Key Source | Encrypted Value |
|----------|--------|------|------------|----------------|
| C2 URL | AES | CBC | hardcoded | [base64] |

### Decryption Script

```python
#!/usr/bin/env python3
"""Decrypt [IOC type] from [APK Name]"""
from Crypto.Cipher import AES
import base64

# Key: [extracted as hex or base64]
key = b'[16-byte key]'
# IV: [extracted or None for ECB]
iv = b'[16-byte iv]'  # or None

cipher = AES.new(key, AES.MODE_CBC, iv)
encrypted = base64.b64decode('[encrypted]')
decrypted = cipher.decrypt(encrypted)
print(decrypted.decode(errors='replace').rstrip('\x00'))
```

## 4. Suspicious Components

| Component | Class Index | Key Methods | Risk |
|-----------|-------------|-------------|------|
| [name] | class@xxxxx | method@xxxxx | High |

## 5. Code Analysis

**[Component Name]**
- File: com/package/ClassName.class
- Evidence: [relevant code snippet from dec]
- Call Chain: [xref results]

## 6. Persistence Mechanism

- Boot: [receiver/service for BOOT_COMPLETED]
- Service: [from axml]
- Anti: [from code analysis]

## 7. Conclusion

**Threat Type**: [Trojan/Spyware/Adware/etc]
**Risk Level**: [Critical/High/Medium/Low]
```

---

## Command Reference

### Recon Commands (Phase 1)

| Command | Purpose |
|---------|---------|
| `binfo` | File hashes, size, package, DEX info |
| `permission` | All permissions |
| `axml` | AndroidManifest.xml |

### Trace Commands (Phase 2)

| Command | Usage | Purpose |
|---------|-------|---------|
| `attsf` | `attsf` | Exported components - attack entry points |
| `malscan` | `malscan` | Malicious pattern detection |
| `listm` | `listm com.example.Class` | List methods in class |
| `dec` | `dec -c com.example.Class` | Decompile class |
| `xref` | `xref -c ClassName` | Find class references |
| `dasm` | `dasm method@xxxxx` | Disassemble method |
| `native` | `native` | Native methods |

### IOC Extract Commands (Phase 3)

| Command | Usage | Purpose |
|---------|-------|---------|
| `sensinf` | `sensinf` | API keys, passwords, tokens |
| `find -s` | `find -s pattern` | Search strings |
| `uri` | `uri` | File paths, content URIs |
| `api` | `api` | Sensitive API calls |

### Decrypt Commands (Phase 4)

| Command | Usage | Purpose |
|---------|-------|---------|
| `find -m` | `find -m methodName` | Find method calls |
| `find -s` | `find -s CryptoClass` | Find crypto classes |
| `dec` | `dec -c CryptoClass` | Analyze crypto implementation |
| `xref` | `xref -m methodName` | Trace method usage |

---

## Encryption Analysis Guide

### Step 1: Identify Encryption

Search strings:
```bash
python gda_analyze.py sample.apk "find -s Base64"
python gda_analyze.py sample.apk "find -s AES"
python gda_analyze.py sample.apk "find -s DES"
python gda_analyze.py sample.apk "find -s RC4"
```

Search methods:
```bash
python gda_analyze.py sample.apk "find -m getInstance"
python gda_analyze.py sample.apk "find -m doFinal"
python gda_analyze.py sample.apk "find -m SecretKeySpec"
python gda_analyze.py sample.apk "find -m IvParameterSpec"
```

### Step 2: Trace Encryption Flow

```bash
# Find encryption utility class
python gda_analyze.py sample.apk "dec -c com.malware.CryptoUtil"

# Trace key/IV extraction
python gda_analyze.py sample.apk "find -s getBytes"
python gda_analyze.py sample.apk "find -s SharedPreferences"
```

### Step 3: Extract Parameters

From decompiled code, identify:
- **Algorithm**: AES/DES/RC4 (from `Cipher.getInstance`)
- **Mode**: ECB/CBC/GCM (from `Cipher.getInstance` string)
- **Key**: hardcoded string, byte array, or SharedPreferences
- **IV**: hardcoded or derived
- **Padding**: PKCS5/PKCS7/NoPadding

Example `Cipher.getInstance` string pattern:
```
"Cipher.getInstance(\"AES/CBC/PKCS5Padding\")"
```

### Step 4: Generate Decrypt Script

```python
from Crypto.Cipher import AES
import base64
import binascii

# Parameters from code analysis
key = binascii.unhexlify('[hex key]')  # or base64.b64decode
iv = binascii.unhexlify('[hex iv]')    # or None for ECB

cipher = AES.new(key, AES.MODE_CBC, iv)
encrypted = base64.b64decode('[base64 encrypted]')
decrypted = cipher.decrypt(encrypted)
print(decrypted.decode(errors='replace').rstrip('\x00'))
```

---

## Malware Pattern Commands

### SMS Malware
```bash
python gda_analyze.py sample.apk "find -m sendTextMessage"
python gda_analyze.py sample.apk "find -m abortBroadcast"
python gda_analyze.py sample.apk "dec -c com.package.SmsReceiver"
```

### Banking Trojan
```bash
python gda_analyze.py sample.apk "find -m WindowManager"
python gda_analyze.py sample.apk "find -s TYPE_TEXT_VARIATION_PASSWORD"
```

### Spyware/RAT
```bash
python gda_analyze.py sample.apk "find -s http"
python gda_analyze.py sample.apk "find -s socket"
python gda_analyze.py sample.apk "dec -c com.spy.DataSender"
```

### Adware
```bash
python gda_analyze.py sample.apk "find -s admob"
python gda_analyze.py sample.apk "find -s mopub"
```

---

## Analysis Principles

1. **Recon first** - Gather context before deep analysis
2. **Trace suspicious components** - attsf/malscan reveal malicious code
3. **Search encryption patterns** - Many malware encrypt C2/config
4. **Generate decrypt scripts** - When key+ciphertext found
5. **Cite evidence** - Always include class@xxxxx and method@xxxxx
6. **Be adaptive** - Different malware types need different focus

## Constraints

1. GDA closes connection after each command
2. Class index: 6-digit hex from attsf/listm (e.g., `0002d3`)
3. Method ID: `method@xxxxx` from listm
4. Quote commands: `"find -s 192.168"`
5. `find -m` searches method names, `find -s` searches strings
