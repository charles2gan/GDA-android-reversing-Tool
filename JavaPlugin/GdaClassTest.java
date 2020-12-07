//±àÒëE:\javatest>D:\JavaAndroid\jdk1.8.0_131\bin\javac.exe -source 1.6 -target 1.6 Test.java

//https://www.codota.com/code/java/methods/com.sun.jna.Function/getFunction
//https://java-native-access.github.io/jna/4.2.1/com/sun/jna/Function.html

import com.gda.api.GDAInterface;
class GdaClassTest {
	public int GDA_MAIN(GDAInterface gda)
	{
		String	per="the apk permission:\n";
		//per+=gda.GetAppString();
		//per+=gda.GetCert();
		//per+=gda.GetUrlString();
		per+=gda.GetPermission();
		gda.log(per);
		return 0;
	}
}