package com.gda.api;
// android-method infomation Class  
public class MethodInfo{
	public int idx=0;
    public String methodName="";
    public String modifiedMethodName="";
    public String methodFullName="";
    public String methodPackage="";
    public String MethodSignature="";
    public int offset=0 ;
    public int size=0;
    public int regSize=0 ;
    public String permission="";
    public String methodSmaliCode="";
    public String methodJavaCode="";
    public int[] callorIdxList;
    public int[] refMethodIdxList;
    public int[] refStringIdxList; 
	public MethodInfo(){
			super();
	}
}
