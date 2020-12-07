package com.gda.api;
import com.sun.jna.Function;
import com.sun.jna.Pointer;
import java.util.HashMap;
import java.util.ArrayList;
public class GDAInterface{
	public ArrayList<GdaDex> DexList;
	Function GetAppString_;
	Function log_;
	Function GetPermission_;
	Function GetCert_;
	Function GetSupicous_;
	Function GetStringById_;
	Function SetStringById_;
	Function SetMethodName_;
	Function SetClassName_;
	Function GetClassCodeById_;
	Function GetSmaliCodeById_;
	Function GetJavaCodeById_;
	Function GetUrlString_;
	Function FindClassId_;
	Function GetMethodNameById_;
	Function GetStringByTypeId_;
	Function DumpHexData_;
	Function WriteBinaryToDex_;
	Function DumpBin_;
	Function GetMethodDeclare_;
	Function GetClassCodeById_Ex_;
	Function DisasmBinData_;

	public GDAInterface(){
		super();
	}
	public Function GetFunction(HashMap<String, Integer> interfaceMap,String func){
		Integer ints=interfaceMap.get(func);
		Pointer p=Pointer.createConstant(ints);
		return Function.getFunction(p, Function.ALT_CONVENTION);
	}
	public byte[] getBytes(String str,String encoding)
	{	
		try{
			byte[] bbuff=str.getBytes("UTF-8");
			byte[] newbuff = new byte[bbuff.length+1];
			System.arraycopy(bbuff, 0, newbuff, 0, bbuff.length);
			newbuff[bbuff.length]=0;
			return newbuff;
		}catch(Exception e)
		{
			log("getBytes function exception");
			return null;
		}
	}
	public void initInterface(HashMap<String, Integer> interfaceMap){
		try{
			GetAppString_ = GetFunction(interfaceMap,"GetAppString");
			log_ = GetFunction(interfaceMap,"gprint");
			GetPermission_ = GetFunction(interfaceMap,"GetPermission");
			GetCert_ = GetFunction(interfaceMap,"GetCert");
			GetSupicous_ = GetFunction(interfaceMap,"GetSupicous");
			GetStringById_ = GetFunction(interfaceMap,"GetStringById");
			SetStringById_ = GetFunction(interfaceMap,"SetStringById");
			SetMethodName_ = GetFunction(interfaceMap,"SetMethodName");
			SetClassName_ = GetFunction(interfaceMap,"SetClassName");
			GetClassCodeById_ = GetFunction(interfaceMap,"GetClassCodeById");
			GetSmaliCodeById_ = GetFunction(interfaceMap,"GetSmaliCodeById");
			GetJavaCodeById_ = GetFunction(interfaceMap,"GetJavaCodeById");
			GetUrlString_ = GetFunction(interfaceMap,"GetUrlString");
			FindClassId_ = GetFunction(interfaceMap,"FindClassId");
			GetMethodNameById_ = GetFunction(interfaceMap,"GetMethodNameById");
			GetStringByTypeId_ = GetFunction(interfaceMap,"GetStringByTypeId");
			DumpHexData_ = GetFunction(interfaceMap,"DumpHexData");
			WriteBinaryToDex_ = GetFunction(interfaceMap,"WriteBinaryToDex");
			DumpBin_ = GetFunction(interfaceMap,"DumpBin");
			GetMethodDeclare_ = GetFunction(interfaceMap,"GetMethodDeclare");
			GetClassCodeById_Ex_ = GetFunction(interfaceMap,"GetClassCodeById_Ex");
			DisasmBinData_ = GetFunction(interfaceMap,"DisasmBinData");
		}catch (Exception e){
			System.out.println("erro:\n\t" + e);
		}
    }
	
	public Object CallFunction(Class returnType,Function func,Object...args){
		return func.invoke(returnType,args);
	}
	public String GetAppString(int dexId){
		return (String)CallFunction(String.class,GetAppString_,dexId);
	}
	public int log(String str){
		return (Integer)CallFunction(Integer.class,log_,getBytes(str,"UTF-8"));
	}
	public String GetPermission(){	
		return (String)CallFunction(String.class,GetPermission_);
	}
	public String GetCert(){
		return (String)CallFunction(String.class,GetCert_);
	}
	public String GetSupicous(int dexId){
		return (String)CallFunction(String.class,GetSupicous_,dexId);
	}
	public String GetSupicous(){
		return (String)CallFunction(String.class,GetSupicous_);
	}
	public String GetStringById(int idx,int dexId){
		return (String)CallFunction(String.class,GetStringById_,idx,dexId);
	}
	public int SetStringById(int idx,String str,int dexId){
		return (Integer)CallFunction(Integer.class,SetStringById_,idx,getBytes(str,"UTF-8"),dexId);
	}
	public int SetMethodName(int idx,String str,int dexId){
		return (Integer)CallFunction(Integer.class,SetMethodName_,idx,getBytes(str,"UTF-8"),dexId);
	}
	public int SetClassName(int idx,String str,int dexId){
		return (Integer)CallFunction(Integer.class,SetClassName_,idx,getBytes(str,"UTF-8"),dexId);
	}
	public String GetClassCodeById(int idx,int dexId){
		return (String)CallFunction(String.class,GetClassCodeById_,idx,dexId);
	}
	public String GetSmaliCodeById(int idx,int dexId){
		return (String)CallFunction(String.class,GetAppString_,idx,dexId);
	}
	public String GetJavaCodeById(int idx,int dexId){
		return (String)CallFunction(String.class,GetSmaliCodeById_,idx,dexId);
	}
	public String GetUrlString(int dexId){
		return (String)CallFunction(String.class,GetUrlString_,dexId);
	}
	public int FindClassId(String descriptor,int dexId){
		return (Integer)CallFunction(int.class,FindClassId_,descriptor,dexId);
	}
	public String GetMethodNameById(int idx,int dexId){
		return (String)CallFunction(String.class,GetMethodNameById_,idx,dexId);
	}
	public String GetStringByTypeId(int idx,int dexId){
		return (String)CallFunction(String.class,GetStringByTypeId_,idx,dexId);
	}
	public String DumpHexData(int offset,int size,int width,int mode,int dexId){
		return (String)CallFunction(String.class,DumpHexData_,offset,size,width,mode,dexId);
	}
	public int WriteBinaryToDex(int offset,byte[] bytes,int dexId){
		return (Integer)CallFunction(Integer.class,WriteBinaryToDex_,offset,bytes,dexId);
	}
	public int DumpBin(String fileName,int offset,int size,int dexId){
		return (Integer)CallFunction(Integer.class,DumpBin_,fileName,offset,size,dexId);
	}
	public String GetMethodDeclare(int idx,int dexId){
		return (String)CallFunction(String.class,GetMethodDeclare_,idx,dexId);
	}
	public String GetClassCodeById_Ex(int idx,int dexId){
		return (String)CallFunction(String.class,GetClassCodeById_Ex_,idx,dexId);
	}
	public String DisasmBinData(byte[] bytes,int dexId){
		return (String)CallFunction(String.class,DisasmBinData_,bytes,bytes.length,dexId);
	}
	//the follow is a case that  above api
	public String GetAppString(){	
		return (String)CallFunction(String.class,GetAppString_,0);
	}
	public String GetStringById(int idx){
		return (String)CallFunction(String.class,GetStringById_,idx,0);
	}
	public int SetStringById(int idx,String str){
		return (Integer)CallFunction(Integer.class,SetStringById_,idx,getBytes(str,"UTF-8"),0);
	}
	public int SetMethodName(int idx,String str){
		return (Integer)CallFunction(Integer.class,SetMethodName_,idx,getBytes(str,"UTF-8"),0);
	}
	public int SetClassName(int idx,String str){
		return (Integer)CallFunction(int.class,SetClassName_,idx,getBytes(str,"UTF-8"),0);
	}
	public String GetClassCodeById(int idx){
		return (String)CallFunction(String.class,GetClassCodeById_,idx,0);
	}
	public String GetSmaliCodeById(int idx){
		return (String)CallFunction(String.class,GetSmaliCodeById_,idx,0);
	}
	public String GetJavaCodeById(int idx){
		return (String)CallFunction(String.class,GetJavaCodeById_,idx,0);
	}
	public String GetUrlString(){
		return (String)CallFunction(String.class,GetUrlString_,0);
	}
	public int FindClassId(String descriptor){
		return (Integer)CallFunction(Integer.class,FindClassId_,descriptor,0);
	}
	public String GetMethodNameById(int idx){
		return (String)CallFunction(String.class,GetMethodNameById_,idx,0);
	}
	public String GetStringByTypeId(int idx){
		return (String)CallFunction(String.class,GetStringByTypeId_,idx,0);
	}
	public String DumpHexData(int offset,int size,int width,int mode){
		return (String)CallFunction(String.class,DumpHexData_,offset,size,width,mode,0);
	}
	public int WriteBinaryToDex(int offset,byte[] bytes){
		return (Integer)CallFunction(Integer.class,WriteBinaryToDex_,offset,bytes,0);
	}
	public int DumpBin(String fileName,int offset,int size){
		return (Integer)CallFunction(Integer.class,DumpBin_,getBytes(fileName,"UTF-8"),offset,size,0);
	}
	public String GetMethodDeclare(int idx){
		return (String)CallFunction(String.class,GetMethodDeclare_,idx,0);
	}
	public String GetClassCodeById_Ex(int idx){
		return (String)CallFunction(String.class,GetClassCodeById_Ex_,idx,0);
	}
	public String DisasmBinData(byte[] bytes){
		return (String)CallFunction(String.class,DisasmBinData_,bytes,bytes.length,0);
	}
	
}