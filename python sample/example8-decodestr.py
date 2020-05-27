import GdaImport
#gjden
#example of decoding strings which is located by smali code
def printStringHex(stri): 
    ret=''
    for ch in stri:
        ret+="%02x " % (ord(ch))
    return ret
def decodeString(gda,idx):
    rawstr=gda.GetStringById(idx)
    if rawstr==None:
        return ''
    stri=rawstr
    ret=list(stri)
    i=len(stri)-1
    xx=''
    while i>= 0:
        ret[i]=chr(ord(stri[i])^39)
        if i <= 0:
            break
        i=i-1
        ret[i]=chr(ord(stri[i])^101)
        i=i-1
    xx = ''.join(ret)   
    return xx

def GDA_MAIN(gda_obj):
    gda=gda_obj
    Dex0=gda.DexList[0]
    midx=0x4fc9
    method=Dex0.MethodTable[str(midx)]
    clist=method.callorIdxList
    destr=''
    callorTable={}
    strIdxTable={}
    for idx in clist:
        if callorTable.has_key(str(idx)):
            continue
        #dump smali code of callors
        smalicode=gda.GetSmaliCodeById(idx)
        splitstr=smalicode.split('\r\n')
        i=0
        for sstr in splitstr:
            if '@4fc9' in sstr:
                line=splitstr[i-1]
                if 'string@' in line:
                    pos=line.find('ing@')+4
                    strIdx=line[pos:pos+4]
                    if strIdxTable.has_key(strIdx):
                        i=i+1
                        continue
                    strIdxTable[strIdx]=strIdx
                    dstr=decodeString(gda,int(strIdx,16))
                    gda.SetStringById(int(strIdx,16),dstr)
                    destr+="[string@"
                    destr+=strIdx
                    destr+="] "
                    destr+=dstr
                    destr+='\n' 
            i=i+1           
    gda.log(destr)
    return 0
