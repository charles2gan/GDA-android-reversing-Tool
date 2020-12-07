package example;
import com.gda.api.*;
//gjden
//example of dumping the code of class to java file
class Example7DumpJava {
	public int GDA_MAIN(GDAInterface gda)
	{
		GdaDex Dex0=gda.DexList.get(0);
		String code="";
		for (ClassInfo classi:Dex0.ClassList){
			code=gda.GetClassCodeById_Ex(classi.idx);
			if(code.length()>1000){// only dump a class code whoes length is bigger than 1000 bytes 
				gda.log(code);
				break;//just one method code for test
			}
		}
		return 0;
	}
}