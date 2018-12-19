#import ctypes
#import GdaImport
#import matplotlib.pyplot as plt
#   getting example
#   gjden

def GDA_MAIN(gda_obj):
    
    per='the apk permission:\n'
    #  per+=gda_obj.GetAppString()
    #  per+=gda_obj.GetCert()
    #  per+=gda_obj.GetUrlString()
    #  
    per+=gda_obj.GetPermission()
    gda_obj.log(per)
    tofile = open('out.txt','w')
    tofile.write(per)
    tofile.close()
    return 0
    