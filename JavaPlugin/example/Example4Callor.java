package example;
import com.gda.api.GDAInterface;
import com.gda.api.GdaDex;
import com.gda.api.MethodInfo;
import com.gda.api.DexHeader;
//gjden
//example of dumping all the callors of a method
class Example4Callor {
	public int GDA_MAIN(GDAInterface gda)
	{
		String callorStr="";
		GdaDex Dex0=gda.DexList.get(0);
		for (MethodInfo method:Dex0.MethodList){
			if(method!=null&&method.callorIdxList.length>5){
				callorStr=String.format("the [%d] callors of the method: %s\n\n",method.callorIdxList.length,method.methodFullName);
				for (int calloridx:method.callorIdxList){
					String index=""+calloridx;
					if (Dex0.MethodTable.containsKey(index)){
						MethodInfo obj=Dex0.MethodTable.get(index);
                        callorStr+=obj.methodFullName;
						callorStr+=obj.MethodSignature;
						callorStr+="\n";
					}
				}
				break;
			}
		}
		gda.log(callorStr);
		return 0;
	}
}