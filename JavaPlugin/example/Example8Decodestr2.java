package example;
import com.gda.api.*;
import java.util.HashMap;
//gjden
//example of decrypting strings

class Example8Decodestr2 {
	//copy from Request.ALLATORIxDEMO decompiled by GDA
	static public String Request_ALLATORIxDEMO(String arg0)	//method@4fc9
	{
		 int v3;
		 int v0 = arg0.length();
		 char[] v2 = new char[v0];
		 v0--;
		 int v1 = v0;
		 while ((v0 >= 0)) {	
			 v3 = v1-1;
			 v2[v1]=(char)(arg0.charAt(v1)^0x27);
			 if (v3 < 0) {	
				 return new String(v2);
			 }	
			 v0 = v3-1;
			 v2[v3]=(char)(arg0.charAt(v3)^0x65);
			 v1 = v0;
		 }	
		 return new String(v2);
	}

	public int GDA_MAIN(GDAInterface gda)//GDA main function which is the entry of executing code
	{
		GdaDex Dex0=gda.DexList.get(0);//first Dex(classes.dex file),most of apks have multi-dex.
		int mindex=Integer.parseInt("4fc9", 16);
		String midx=""+mindex;
		MethodInfo method=Dex0.MethodTable.get(midx);//get the decryption method by method index which noted as some strings like "method@"
		HashMap<String, Integer> callorTable=new HashMap<String, Integer>();
		HashMap<String, Integer> strIdxTable=new HashMap<String, Integer>();
		String callorHex="";
		String destr="";
		destr=""+method.callorIdxList.length;
		
		for (int idx:method.callorIdxList){//callorIdxList is byte[] which handles all callor's method index.
			if(callorTable.get(""+idx)!=null)
				continue;
			callorTable.put(""+idx,idx);
			MethodInfo callor=Dex0.MethodTable.get(""+idx);//get callor
			//dump the hex string,where the real method bytecode begin with offset 0x10.
			callorHex=gda.DumpHexData(callor.offset+0x10,callor.size-0x10,callor.size-0x10,0);
			int size=callorHex.length();
			callorHex=callorHex.substring(0,size-2);
			int start=8;
			while(true){
				int pos=callorHex.indexOf("c94f",start);
				if(pos<0)
					break;
				start=pos+1;
				String invoke=callorHex.substring(pos-4,pos-2)+"";
				if(invoke.equals("71")){
					gda.log(invoke+"\n");
					String strIdx1=callorHex.substring(pos-6,pos-4);
					String strIdx2=callorHex.substring(pos-8,pos-6);
					String sidx=strIdx1+strIdx2;
					if(strIdxTable.get(sidx)!=null)
						continue;
					int index=Integer.parseInt(sidx, 16);
					strIdxTable.put(sidx,index);
					String rawstr=gda.GetStringById(index);
					String decodeStr=Request_ALLATORIxDEMO(rawstr);
					gda.SetStringById(index,decodeStr);//write decode string back
					
					//print decoded string
					destr+="[string@";
                    destr+=sidx;
                    destr+="] ";
                    destr+=decodeStr;
                    destr+='\n';
				}
			}
		}
		gda.log(destr);
		return 0;
	}
}

