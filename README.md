# GDA(GJoy Dex Analysizer)

Here, a new Dalvik bytecode decompiler, GDA（this project started in 2013 and released its first version 1.0 in 2015 at www.gda.wiki:9090) , is proposed and implemented in C++ to provide more sophisticated, fast and convenient decompilation support. GDA is completely self-independent and very stable. It supports APK, DEX, ODEX, oat files, and run without installation and Java VM support. GDA only takes up 2M of your disk space, and you can use it in any newly installed windows system and virtual machine system without additional configuration. In addition, GDA has more excellent features as follows:



![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/GDA_PIC/3_entry_x-ref.png)


```
Interactive operation:
    1.Cross-references for strings, classes, methods and fields;
    2.Searching for strings, classes methods and fields;
    3.Comments for java code;
    4.Rename methods,fields and classes;
    5.Save the analysis results in gda db file.
    ...
  
Utilities for Assisted Analysis:
    1.Extracting DEX from ODEX;
    2.Extracting DEX from OAT;
    3.XML Decoder (Component filter);
    4.Algorithm tool(Support rolling encryption and almost all popular encryption algorithms);
    5.Device memory dump(Dump so, odex, dex, oat file);
    ...
    
New features:
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
    ...
```  


`GDA shortcut key`

|shortcut    |description|
|:-|:-|
|F5   |Switch java to smali, pressing it again for back to java|
|F    |Trace the args and return-value by dataflow analysis|
|X    |Cross-referencing, locating callers (of strings, classes, methods, field)|
|Esc/<-/Backspace    |Back to the last visit|
|->    |Forward to the next visit|
|G    |Jump to somewhere by you inputting offset |
|N    |Rename the variable/method/class name|
|S    |Search for all the elements by the given string|
|C    |Comments. Only supports the Java code|
|DoubleClick    |The cursor's placed at the method/str/field/class, and double-click to access objects|
|M    |The cursor's placed at the Smali line and pressing the key 'M' to edit the instruction|
|UP\bigtriangleup   |Press 'up' key to access the up-method in the tree control|
|Down\bigtriangledown   |Press 'down' key to access the down-method in the tree control|
|D    |Dump the binary data of methods, only supports the Smali window|
|Enter     |The modification of edit boxes take effect|
|H    |Show data in Hex|
|Ctr+H    |Pop searching history window|
|Ctr+A    |Select all|
|Ctr+C    |Copy|
|Ctr+V    |Paste, only for editable boxes|
|Ctr+X    |Cut|
|Ctr+F    |Find out the string of the current window|
|Ctr+S    |Save the modifications into the GDA database file|


# Installing
  Not yet, just double-click the bin and you can enjoy it.

# Supported platforms
  Only for windows

# Usage:

  Brief guide: https://github.com/charles2gan/GDA-android-reversing-Tool/wiki
  
  Python script:https://github.com/charles2gan/GDA-android-reversing-Tool/wiki/GDA-Python-scripts
  
# Shows:
  
  File loading and decompiling:
  
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/gif/load.gif)
  
  MalScan, API search, x-ref...
  
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/gif/check.gif)
  
  Url,Xml,string x-ref...

  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/gif/mainfest.gif)
  
  Variable trace
  ![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/gif/dataflow_return.gif)
