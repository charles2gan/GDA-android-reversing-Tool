import GdaImport
#gjden
#example of dumping the code of method or class
def GDA_MAIN(gda_obj):
    gda=gda_obj
    Dex0=gda.DexList[0]
    code=""     
    for classCode in Dex0.ClassList:
        code=gda.GetClassCodeById_Ex(classCode.idx)
        if len(code)>1000:# only dump a class code whoes length is bigger than 1000 bytes 
            gda.log(code)
            javaFileName=classCode.className;
            javaFileName+='.java'
            tofile = open(javaFileName,'w')
            tofile.write(code)
            tofile.close()
            break;
    return 0
