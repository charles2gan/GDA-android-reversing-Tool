package example;
import com.gda.api.GDAInterface;
import com.gda.api.GdaDex;
import com.gda.api.MethodInfo;
import com.gda.api.DexHeader;
import com.gda.api.ClassInfo;
//gjden
//example of dumping the code of method or class
class Example5Code {
	public int GDA_MAIN(GDAInterface gda)
	{
		GdaDex Dex0=gda.DexList.get(0);
		String code="";
		for (MethodInfo method:Dex0.MethodList){
			code=gda.GetJavaCodeById(method.idx);//gda.GetSmaliCodeById(method.idx)
			if(code.length()>500){
				gda.log(code);
				break;//just one method code for test
			}
		}
		code="";
		for (ClassInfo classi:Dex0.ClassList){
			code=gda.GetClassCodeById(classi.idx);//gda.GetSmaliCodeById(method.idx)
			if(code.length()>500){
				gda.log(code);
				break;//just one method code for test
			}
		}
		return 0;
	}
}