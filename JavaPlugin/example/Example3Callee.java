package example;
import com.gda.api.GDAInterface;
import com.gda.api.GdaDex;
import com.gda.api.MethodInfo;
import com.gda.api.DexHeader;
//gjden
//example of dumping all the callors of a method
class Example3Callee {
	public int GDA_MAIN(GDAInterface gda)
	{
		GdaDex Dex0=gda.DexList.get(0);
		String calleeStr="";
		//String leng="MethodList"+Dex0.MethodList+"\n\n";
		//leng+="ClassList"+Dex0.ClassList+"\n\n";
		//leng+="MethodTable"+Dex0.MethodTable+"\n\n";
		//leng+="ClassTable"+Dex0.ClassTable+"\n\n";
		//gda.log(leng);
		
        for(MethodInfo method:Dex0.MethodList){
            if (method!=null&&method.refMethodIdxList.length>5){
                calleeStr+=String.format("the [%d] callees of the method: %s\n\n",method.refMethodIdxList.length,method.methodFullName);
                for(int calleeidx:method.refMethodIdxList)
				{
                    String index=""+calleeidx;
                    if (Dex0.MethodTable.containsKey(index))
					{
                        MethodInfo obj=Dex0.MethodTable.get(index);
                        calleeStr+=obj.methodFullName+obj.MethodSignature+"\r\n";
					}else
					{
                        calleeStr+=gda.GetMethodNameById(calleeidx)+"\r\n";
					}
					
				}
				gda.log(calleeStr);
                break;
			}
		}
        
		return 0;
	}
}