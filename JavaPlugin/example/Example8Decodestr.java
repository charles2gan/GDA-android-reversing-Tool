package example;
import com.gda.api.*;
import java.util.HashMap;
//gjden
//example of dumping the code of method or class

class Example8Decodestr {
	//copy from Request.ALLATORIxDEMO decompiled by GDA
	static public String Request_ALLATORIxDEMO2(String arg0)	//method@4fc9
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
	static public String ha_ALLATORIxDEMO(String arg0)	//method@5095
	{
		 int v3;
		 int v0 = arg0.length();
		 char[] v2 = new char[v0];
		 v0--;
		 int v1 = v0;
		 while ((v0 >= 0)) {	
			 v3 = v1-1;
			 v2[v1]=(char)(arg0.charAt(v1)^0x1f);
			 if (v3 < 0) {	
				 return new String(v2);
			 }	
			 v0 = v3-1;
			 v2[v3]=(char)(arg0.charAt(v3)^0x14);
			 v1 = v0;
		 }	
		return new String(v2);
	}

	public int GDA_MAIN(GDAInterface gda)
	{
		GdaDex Dex0=gda.DexList.get(0);
		int mindex=Integer.parseInt("5059", 16);
		String midx=""+mindex;
		MethodInfo method=Dex0.MethodTable.get(midx);
		HashMap<String, Integer> callorTable=new HashMap<String, Integer>();
		HashMap<String, Integer> strIdxTable=new HashMap<String, Integer>();
		String smalicode="";
		String destr="";
		destr=""+method.callorIdxList.length;
		for (int idx:method.callorIdxList){
			if(callorTable.get(""+idx)!=null)
				continue;
			callorTable.put(""+idx,idx);
			smalicode=gda.GetSmaliCodeById(idx);
			String[] splitstr = smalicode.split("\n");
			for(int i=0;i<splitstr.length;i++){
				String line=splitstr[i];
				if(line.contains("@5059")){
					String lastLine=splitstr[i-1];
					int pos=lastLine.indexOf("ing@");//find string@
					if(pos<0)
						continue;
					String sidx=lastLine.substring(pos+4,pos+4+4);//get string idx
					int index=Integer.parseInt(sidx, 16);
					if(strIdxTable.get(sidx)!=null)
						continue;
					strIdxTable.put(sidx,index);
					String rawstr=gda.GetStringById(index);
					String decodeStr=ha_ALLATORIxDEMO(rawstr);
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
