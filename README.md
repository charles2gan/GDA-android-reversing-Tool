
[![image](https://img.shields.io/badge/website-GDA-brightgreen?logo=groupon)](http://www.gda.wiki:9090/?language=en)
[![image](https://img.shields.io/badge/download-GDAE%20pro-ff69b4?logo=SoundCloud)](http://www.gda.wiki:9090/?language=en)
[![image](https://img.shields.io/badge/Guide-Brief-brightgreen?logo=Talend&logoColor=red)](https://github.com/charles2gan/GDA-android-reversing-Tool/wiki)
[![image](https://img.shields.io/badge/Guide-Script-brightgreen?logo=Talend&logoColor=red)](https://github.com/charles2gan/GDA-android-reversing-Tool/wiki/GDA-Python-scripts)
[![image](https://img.shields.io/badge/Guide-taint%20analysis-brightgreen?logo=Talend&logoColor=red)](https://github.com/charles2gan/GDA-android-reversing-Tool/wiki/GDA-Static-Taint-analysis)
[![image](https://img.shields.io/badge/Update-History-brightgreen?logo=Apache-Cassandra&logoColor=red)](http://www.gda.wiki:9090/update_list.php?language=en)
[![image](https://img.shields.io/badge/Chat-Zhihu-brightgreen?logo=Zhihu)](https://www.zhihu.com/people/gjden)

![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/GDA_PIC/mainpage.png)


# ˇ GDA(GJoy Dex Analysizer)

GDA, a new Dalvik bytecode decompiler, is implemented in C++ to provide more sophisticated, fast and convenient decompilation support. GDA is completely self-independent and stable. It supports APK, DEX, ODEX, OAT files(supports jar, class and aar files since 3.79), and run without installation and Java VM support. And you can use it in any newly installed windows system and virtual machine system without additional configuration. GDA original file is 2m, and the size of the new version is increased to 5M after VMP protection.

GDA is not only a decompiler, but also a powerful and fast reverse analysis platform. It supports not only routine analysis operations, but also malicious behavior detection, URL extraction, packer identification, variable tracking analysis, deobfuscation, Python& Java scripts, device memory extraction, dex extraction etc.

In addition, GDA has more excellent features as follows:



```
𝕬 Interactive operation:
    1.Cross-references for strings, classes, methods and fields;
    2.Searching for strings, classes methods and fields;
    3.Comments for java code;
    4.Rename methods,fields and classes;
    5.Save the analysis results in gda db file.
    ...
  
𝕭 Utilities for Assisted Analysis:
    1.Extracting DEX from ODEX;
    2.Extracting DEX from OAT;
    3.XML Decoder (Component filter);
    4.Algorithm tool(Support rolling encryption and almost all popular encryption algorithms);
    5.Device memory dump(Dump so, odex, dex, oat file);
    ...
    
𝕮 New features:
    1.Brand new dalvik decompiler in c++ with friendly GUI;
    2.Support python script and Java script;
    3.Packers Recognition;
    4.Multi-DEX supporting;
    5.Making and loading signature of the method;
    6.Malicious Behavior Scanning by API chains;
    7.Taint analysis to preview the behavior of variables;
    8.Taint analysis to trace the path of variables;
    9.De-obfuscate;
    10.API view with x-ref;
    11.Association of permissions with modules;
    12.Extract all the urls in APK.
    13.Apk Forensics Analysis.
    14.A rule-based static vulnerability scanner.
    15.Smart Rename.
    16.Support for .jar files, .class files and .aar files.
    17.Dual decompiler mode.
    18.Deep URL extraction.
    19.Multi-DEX Merge.
    20.Personalized and Customizable UI.
    ...
```  


`𝕲𝕯𝕬 shortcut key`

|shortcut    |description|
|:-|:-|
|F5   |Switch java to smali, pressing it again for back to java|
|F    |Trace the args and return-value by dataflow analysis|
|X    |Cross-referencing, locating callers (of strings, classes, methods, field)|
|Esc/◄/Backspace    |Back to the last visit|
|►    |Forward to the next visit|
|G    |Jump to somewhere by you inputting offset |
|N    |Rename the variable/method/class name|
|S    |Search for all the elements by the given string|
|C    |Comments. Only supports the Java code|
|DoubleClick    |The cursor's placed at the method/str/field/class, and double-click to access objects|
|M    |The cursor's placed at the Smali line and pressing the key 'M' to edit the instruction|
|▲ UP   |Press 'up' key to access the up-method in the tree control|
|▼ Down  |Press 'down' key to access the down-method in the tree control|
|D    |Dump the binary data of methods, only supports the Smali window|
|Enter     |The modification of edit boxes take effect|
|H    |Show data in Hex|
|Ctr+H    |Pop searching history window|
|Ctr+A    |Select all|
|Ctr+C    |Copy|
|Ctr+V    |Paste, only for editable boxes|
|Ctr+X    |Cut|
|Ctr+F    |Find out the string of the code area|
|Ctr+S    |Save the modifications into the GDA database file|


# ˇ Installing

  Not yet, just double-click the bin and you can enjoy it.
  
# ˇ False positive report
  
  For copyright protection, GDA is protected by an authorized VMP(http://vmpsoft.com/), which may lead to false positives of some anti-virus software. Please ignore or add GDA to the white list. GDA does not have any malicious behavior.

# ˇ Supported platforms

  Only for windows

# ˇ Usage:

  Drag file into GDA, if you wanna analyze `.jar/.class/.aar` file, please convert the `jar/class/aar` to `DEX` by `dx tool` in android sdk path `android-sdk/build-tools/{sdkversion}/`
  ```
  dx --dex --output=<target.dex> <origin.jar>
  ```
  Since GDA3.79, the automatic conversion of the above files is supported. You just need to choose the correct dx.bat path(JUST ONCE) when open the `.jar/.class/.aar` file. If you don't have Android SDK in your system, you can try this one(https://github.com/charles2gan/GDA-android-reversing-Tool/tree/master/dx_tool). Please make sure that the dx.bat works properly.
  
  
  Brief guide: https://github.com/charles2gan/GDA-android-reversing-Tool/wiki
  
  Python script: https://github.com/charles2gan/GDA-android-reversing-Tool/wiki/GDA-Python-scripts
  
  GDA static taint analysis: https://github.com/charles2gan/GDA-android-reversing-Tool/wiki/GDA-Static-Taint-analysis
  
  Batch decryption of APP strings: https://github.com/charles2gan/GDA-android-reversing-Tool/wiki/Batch-decryption-of-APP-strings
  
# ˇ Shows:
  
  ☰ File loading and decompiling:
  
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/gif/load.gif)
  
  ☱ MalScan, API search, x-ref...
  
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/gif/check.gif)
  
  ☲ Url,Xml,string x-ref...

  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/gif/mainfest.gif)
  
  ☳ Variable trace
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/gif/dataflow_return.gif)
  
  ☴ Color theme
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/GDA%20Color%20theme/white_black.png)
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/GDA%20Color%20theme/white_black1.png)
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/GDA%20Color%20theme/white_red.png)
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/GDA%20Color%20theme/black_black.png)
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/GDA%20Color%20theme/black_blue.png)
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/GDA%20Color%20theme/black_green.png)
  
