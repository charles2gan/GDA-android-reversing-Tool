package example;
import com.gda.api.GDAInterface;
import com.gda.api.GdaDex;
import com.gda.api.DexHeader;
//gjden
//example of dumping data
class Example2Dumpdata {
	public int GDA_MAIN(GDAInterface gda)
	{
		GdaDex Dex0=gda.DexList.get(0);
		DexHeader head=Dex0.dexHeader;
		String out="the string Ids off:\n\n";
		//dump hex data
		out+=gda.DumpHexData(head.stringIdsOff,128,128,0);
		gda.log(out);
		//dump bin to file
		//gda.DumpBinData("bin.data",head.stringIdsOff,128);
		//modify the dex file
		//byte []bytes = "\xe4\xba\xba";
		//gda.WriteBinaryToDex(0,bytes,len(bytes));
		return 0;
	}
}