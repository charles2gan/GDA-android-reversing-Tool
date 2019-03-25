# GDA(GJoy Dex Analysizer)


![](https://github.com/charles2gan/GDA-android-reversing-Tool/blob/master/GDA_PIC/3_entry_x-ref.png)

GDA is a new decompiler written entirely in c++. so it does not rely on the Java platform, which is succinct, portable and fast, and supports APK, DEX, ODEX, oat files.
```
Interactive operation:
  	1.X-references for strings, methods and field;
  	2.searching for strings, methods and field;
  	3.comments for java code;
  	4.modification the name of methods,field and class;
  	5.saving the analysis results in gda db file.
 	...
  
Practical Tools for Assisted Analysis:
 	1.extracting DEX from ODEX;
 	2.extracting DEX from OAT;
	3.XML Decoder;
	4.algorithm tool;
	5.device memory dump;
	...
    
New features:
	1.Brand new daviki decompiler in c++ with friendly GUI;
	2.Suport python script
	3.packers Recognition;
	4.Multi-DEX supporting;
	5.making and loading signature of method 
	6.Malicious Behavior Scanning by API chains;
	7.taint anlysis to preview the behavior of variables;
	8.taint anlysis to trace the path of varibales;
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
  
  
  
  
  
  
