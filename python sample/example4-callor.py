import GdaImport
#gjden
#example of dumping all the callors of a method
def GDA_MAIN(gda_obj):
    
    gda=gda_obj
    Dex0=gda.DexList[0]
    callorStr=""
    for method in Dex0.MethodList:
        if len(method.callorIdxList)>5:
            callorStr="the [%d] callors of the method: %s\n\n" % (len(method.callorIdxList),method.methodFullName)
            for calloridx in method.callorIdxList:
                index=str(calloridx)
                if index in Dex0.MethodTable:
                    obj=Dex0.MethodTable[index]
                    callorStr+=obj.methodFullName+obj.MethodSignature
                    callorStr+="\n"
            break;
    gda.log(callorStr)
    return 0
