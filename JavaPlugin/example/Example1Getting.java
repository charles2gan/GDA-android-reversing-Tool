//   getting example
//   gjden
package example;
import com.gda.api.GDAInterface;
class Example1Getting {
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