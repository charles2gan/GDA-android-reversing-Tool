import GdaImport
#gjden
#example of deob
def GDA_MAIN(gda_obj):
    gda=gda_obj
    Dex0=gda.DexList[0]
    str1="the update name:len "
    str1+=str(len(Dex0.ClassList))
    str1+="\n"
    for classi in Dex0.ClassList:
        sourceFileName=gda.GetStringById(classi.sourceFileIdx)
        newName=sourceFileName[:-5]
        oldName=classi.className
        if len(oldName)<=2 and not(newName==oldName):
            str1+=newName+"-"
            str1+=oldName
            str1+="\n"
            gda.SetClassName(classi.idx,newName)
    gda.log(str1)
    return 0
