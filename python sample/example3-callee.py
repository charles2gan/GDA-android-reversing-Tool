import GdaImport
#gjden
#example of dumping all the callors of a method
def GDA_MAIN(gda_obj):
    gda=gda_obj
    Dex0=gda.DexList[0]
    try:
        calleeStr=""
        for method in Dex0.MethodList:
            if len(method.refMethodIdxList)>5:
                calleeStr="the [%d] callees of the method: %s\n\n" % (len(method.refMethodIdxList),method.methodFullName)
                #gda.log(calleeStr)
                for calleeidx in method.refMethodIdxList:
                    index=str(calleeidx)
                    if index in Dex0.MethodTable:
                        obj=Dex0.MethodTable[index]
                        calleeStr+=obj.methodFullName+obj.MethodSignature
                    else:
                        calleeStr+=gda.GetMethodNameById(calleeidx)
                    calleeStr+="\n"
                break;
        gda.log(calleeStr)
    except Exception as e:
        gda.log(str(e))
    return 0