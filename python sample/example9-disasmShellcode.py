import GdaImport
#gjden
#example of disasmbling bin data
def GDA_MAIN(gda):
    data='3223224332435354325f32257547488568458625'
    ret=data.decode('hex')
    destr=gda.DisasmBinData(ret,len(ret))
    gda.log(destr)
    return 0
