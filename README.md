# GDA(GJoy Dex Analysizer)



Most reverse engineers mainly use Java decompiler, commercial dalvik decompiler Jeb and smali2java to do decompilation analysis. Java decompiler is based on Java bytecode, including JD, JD-GUI, jadx, and others. smali2java is a decompiler based on Smali code. They have their own shortcomings, for example, Java decompiler needs to use dex2jar to convert first. For complex, obfuscated or packed apks, there will be conversion failure; while smali2java needs to convert APK into Smali code with apktool, and then decompile, which increases the difficulty and error rate, and decreases the speed of manual analysis. In addition, the interaction between these two types of decompilers is poor, which increases the difficulty of manual analysis. Although the commercial Jeb has better interactivity, it is easy to death when analyzing large-sized APP with the multidex-based APP, and it is very expensive... Here, a new decompiler based on Dalvik bytecode, GDA, is proposed and implemented in C++ language to provide more sophisticated, fast and convenient decompilation support. GDA is completely self-independent. It supports APK, DEX, ODEX, oat files, and run without installation and Java VM support. GDA only takes up 2M of your disk space, and you can use it in any newly installed windows system and virtual machine system. In addition, GDA has more features as follows:


![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/GDA_PIC/3_entry_x-ref.png)

```
Interactive operation:
    1.cross-references for strings, classes, methods and fields;
    2.searching for strings,classes methods and fields;
    3.comments for java code;
    4.rename for methods,fields and classes;
    5.save the analysis results in gda db file.
    ...
  
Practical Tools for Assisted Analysis:
    1.extracting DEX from ODEX;
    2.extracting DEX from OAT;
    3.XML Decoder;
    4.algorithm tool;
    5.device memory dump;
    ...
    
New features:
    1.Brand new dalvik decompiler in c++ with friendly GUI;
    2.Support python script
    3.packers Recognition;
    4.Multi-DEX supporting;
    5.making and loading signature of the method 
    6.Malicious Behavior Scanning by API chains;
    7.taint analysis to preview the behavior of variables;
    8.taint analysis to trace the path of variables;
    9.de-obfuscate;
    10.API view with x-ref;
    11.Association of permissions with modules;
    ...
```  

`GDA shortcut key`

|shortcut    |description|
|:-|:-|
|X    |Cross-referencing, locating callers (of strings, classes, methods, field)|
|Esc/<-/Backspace    |Back to the last visit|
|->    |Go to the next accessed View|
|G    |Jump to the specified offset address|
|N    |The cursor's placed at the variable/method/class name, and which can be modified|
|S    |Global Searching for all the elements|
|C    |Comments，only supports the Java code|
|DoubleClick    |The cursor's placed at the method/str/field/class, double-click to access objects|
|M    |the cursor's placed at the Smali line and pressing M, and edit the instruction|
|UP    |Press “up” key to access the previous method in the tree control|
|Down    |Press “down” key to access the next method in the tree control|
|D    |Dump the binary data of methods, only supports the Smali window|
|Enter     |The modification of edit boxes will take effect|
|H    |Show data in Hex|
|Ctr+H    |pop searching history|
|Ctr+A    |Select all|
|Ctr+C    |copy|
|Ctr+V    |Paste, only for editable boxes|
|Ctr+X    |cut|
|Ctr+F    |locating the string of the current window|
|Ctr+S    |Save the current modification into the GDA database file|


# Installing
  not yet, just double-click the bin and you can enjoy it.

# Supported platforms
  Only for windows

# Usage:

  brief guide: https://github.com/charles2gan/GDA-android-reversing-Tool/wiki
  
  python script:https://github.com/charles2gan/GDA-android-reversing-Tool/wiki/GDA-Python-scripts
  
  
  
  
  
  
