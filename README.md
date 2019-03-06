# GDA-android-reversing（New Daviki Decompiler）

GDA is a new decompiler writen by myself with c++ ,so it does not rely on the Java platform.

It provides many useful sub-tools, such as check shell(protection software), ODEX to DEX, Oat to DEX, XML binary parser, algorithm tool, Android device memory dump and so on. In the interactive analysis, provides a string, method, and domain cross references query, function query, the caller query, comments, and analysis results saving, and so on. I rewritten all Decompiler code basing on Decompiling theory for GDA3, And the disassembly engine, data flow analysis, interlingua optimization, structured analysis and so on,they have all made significant changes.And I also optimized the DEX parsing engine, malicious behavior detection engine, checking shell engine, compared with GDA1 and GDA2, The speed, stability and experience of the analysis are all great improvement and upgrading.

more detail:https://github.com/charles2gan/GDA-android-reversing-Tool/wiki
