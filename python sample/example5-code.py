import GdaImport
#gjden
#example of dumping the code of method or class
def GDA_MAIN(gda_obj):
    gda=gda_obj
    Dex0=gda.DexList[0]
    code=""
    for method in Dex0.MethodList:
        code=gda.GetJavaCodeById(method.idx)#gda.GetSmaliCodeById(method.idx)
        if len(code)>500: # only dump the method code whoes code length is bigger than 500 bytes   
            gda.log(code)
            break;#just one method code for test
    code=""        
    for classCode in Dex0.ClassList:
        code=gda.GetClassCodeById(classCode.idx)
        if len(code)>500:
            gda.log(code)
            break;
    return 0
