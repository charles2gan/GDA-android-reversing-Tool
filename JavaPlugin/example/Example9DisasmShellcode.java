package example;
import com.gda.api.GDAInterface;
//import javax.xml.bind.annotation.adapters.HexBinaryAdapter;
//import javax.xml.bind.DatatypeConverter;
//gjden
//example of dumping the code of method or class
class Example9DisasmShellcode {
	public static byte[] HexStringToByteArray(String s) {
		byte data[] = new byte[s.length()/2];
		for(int i=0;i < s.length();i+=2) {
			data[i/2] = (Integer.decode("0x"+s.charAt(i)+s.charAt(i+1))).byteValue();
		}
		return data;
	}
	public int GDA_MAIN(GDAInterface gda) throws Exception{
		try{
			String data="3223224332435354325f32257547488568458625";
			byte[] bytes = HexStringToByteArray(data);
			String disastr=gda.DisasmBinData(bytes);
			gda.log(disastr);
		}catch(Exception e)
		{
			gda.log("exception");
		}
		
		return 0;
	}
}