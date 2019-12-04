import GdaImport
#gjden
#example of dumping the code of method or class
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
    callorHex='0000'
    callorTable={}
    strIdxTable={}
    for idx in clist:
        sidx=str(idx)
        if callorTable.has_key(sidx):
            continue
        callorTable[sidx]=idx
        callor=Dex0.MethodTable[sidx]
        callorHex=gda.DumpHexData(callor.offset+0x10,callor.size-0x10,callor.size-0x10,0)
        callorHex=callorHex[0:-2]
        #gda.log(callorHex)
        start=8
        end=len(callorHex)      
        while True:
            pos=callorHex.find('c94f',start,end-1)
            if pos<0:
                break;
            start=pos+1
            if callorHex[pos-4:pos-2]=='71':
                strIdx1=callorHex[pos-6:pos-4]
                strIdx2=callorHex[pos-8:pos-6]
                strIdx=strIdx1+strIdx2
                if strIdxTable.has_key(strIdx):
                    continue    
                strIdxTable[strIdx]=strIdx
                dstr=decodeString(gda,int(strIdx,16))
                #gda.SetStringById(int(strIdx,16),dstr)
                destr+="[string@"
                destr+=strIdx
                destr+="] "
                destr+=dstr
                destr+='\n'
    gda.log(destr)
    return 0
