import GdaImport
#gjden
#example of dumping data
def GDA_MAIN(gda_obj):
    gda=gda_obj
    Dex0=gda.DexList[0]
    head=Dex0.DexHeader
    out="the string Ids off:\n\n"
    #dump hex data
    out+=gda.DumpHexData(head.stringIdsOff,128,128,0)
    gda.log(out)
    #dump bin to file
    #gda.DumpBin("bin.data",head.stringIdsOff,128)
    #modify the dex file
    #bytes = b'\xe4\xba\xba'
    #gda.WriteBinaryToDex(0,bytes,len(bytes))
    return 0
