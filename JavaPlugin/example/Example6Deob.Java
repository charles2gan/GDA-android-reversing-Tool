package example;
import com.gda.api.*;
//gjden
//example of deob
class Example6Deob {
	public int GDA_MAIN(GDAInterface gda)
	{
		GdaDex Dex0=gda.DexList.get(0);
		String code="";
		String str1="the update name:len ";
		str1+=Dex0.ClassList.size();
		str1+="\n";
		String sourceFileName="";
		for (ClassInfo classi:Dex0.ClassList){
			sourceFileName=gda.GetStringById(classi.sourceFileIdx);//gda.GetSmaliCodeById(method.idx)
			String newName=sourceFileName.substring(0,sourceFileName.length()-5);
			String oldName=classi.className;
			if (oldName.length()<=2&& newName!=oldName){
				str1+=newName+"-";
				str1+=oldName;
				str1+="\n";
				gda.SetClassName(classi.idx,newName);
			}
		}
		
		gda.log(str1);
		return 0;
	}
}