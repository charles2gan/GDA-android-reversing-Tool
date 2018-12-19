# this file is just used for GDA python, cannot be modified, or some erro will occur
# author:gjden
# 2018.9.10
import ctypes
#define the Interface type 
CALLFUNC_P = ctypes.CFUNCTYPE(ctypes.c_char_p)
CALLFUNC_IP = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_char_p)
CALLFUNC_PI = ctypes.CFUNCTYPE(ctypes.c_char_p,ctypes.c_int)
CALLFUNC_IPI = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_char_p,ctypes.c_int)
CALLFUNC_PII = ctypes.CFUNCTYPE(ctypes.c_char_p,ctypes.c_int,ctypes.c_int)
CALLFUNC_IIP = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)
CALLFUNC_IIPI = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_char_p,ctypes.c_int)
CALLFUNC_PIIII = ctypes.CFUNCTYPE(ctypes.c_char_p,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int)
CALLFUNC_IIPI = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_char_p,ctypes.c_int)
CALLFUNC_IIPII = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_char_p,ctypes.c_int)
CALLFUNC_IPIII = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_char_p,ctypes.c_int,ctypes.c_int,ctypes.c_int)
# Dex File Header
class DexHeader:
    def __init__(self):
        #dex header
        self.magic= []
        self.checksum= 0
        self.signature= []
        self.DexSize= 0
        self.headerSize= 0
        self.endianTag= 0
        self.linkSize= 0
        self.linkOff= 0
        self.mapOff= 0
        self.stringIdsSize= 0
        self.stringIdsOff= 0
        self.typeIdsSize= 0
        self.typeIdsOff= 0
        self.protoIdsSize= 0
        self.protoIdsOff= 0
        self.fieldIdsSize= 0
        self.fieldIdsOff= 0
        self.methodIdsSize= 0
        self.methodIdsOff= 0
        self.classDefsSize= 0
        self.classDefsOff= 0
        self.dataSize= 0
        self.dataOff= 0
# android-method infomation Class  
class MethodInfo:
    def __init__(self):
        idx  = 0                    #index to a method_id_item
        methodName = ""             #method name like OnCreate
        modifiedMethodName = ""     #the modified method name like OnCreate_
        methodFullName = ""         #method full name like com.gda.MyActivity.OnCreate
        methodPackage = ""          #package eg:com.gda.MyActivity
        MethodSignature = ""        #method signature eg:(IILandroid/sys/network;)I
        offset  = 0                 #the method binary code offset which is equal to codeOff of DexMehtod
        size = 0                    #the size of DexCode(the members and binary instruction data)
        regSize  = 0                #the register size
        permission = ""             #method execute permisson
        methodSmaliCode = ""        #smail code text
        methodJavaCode = ""         #java code text
        callorIdxList = []          #the callor list of the method
        refMethodIdxList = []       #the callee list of the method
        refStringIdxList  = []      #the string list that is used of method
#        refClassIdxList  = []
#        refFieldIdxList  = []
#  
# android-class infomation class
class ClassInfo:
    def __init__(self):
        idx  = 0
        className = ""
        modifiedClassName = ""
        classFullName = ""
        sourceFileIdx  = 0          #the source file string index
        superclassIdx = 0           #the parent class index
        classCode = ""              #class code without method code
        subClassList = []           #subClass List
#  Gda-Dex interface Class
#          
class GdaDex:
    def __init__(self):
        self.DexHeader = 0          #Class DexHeader instance 
        self.MethodTable = {}       #Methods Hash Table (dictionary<idx,MethodInfo>)
        self.ClassTable = {}        #Classes Hash Table (dictionary<idx,ClassInfo>)
        self.ClassList = []
        self.MethodList = []
        
class GDAInterface:
    def initInterface(self, InterfaceDic):
        self.pInstance= 0 #Class instance,will be setup by GDA
        
        #interface
        self.InterfaceDic_= InterfaceDic
        self.GetAppString_ = CALLFUNC_PI(InterfaceDic['GetAppString'])
        self.log_ = CALLFUNC_IP(InterfaceDic['gprint'])
        self.GetPermission_ = CALLFUNC_P(InterfaceDic['GetPermission'])
        self.GetCert_ = CALLFUNC_P(InterfaceDic['GetCert'])
        self.GetSupicous_ = CALLFUNC_PI(InterfaceDic['GetSupicous'])
        self.GetStringById_ = CALLFUNC_PII(InterfaceDic['GetStringById'])
        self.SetMethodName_ = CALLFUNC_IIPI(InterfaceDic['SetMethodName'])
        self.SetClassName_ = CALLFUNC_IIPI(InterfaceDic['SetClassName'])
        self.GetClassCodeById_ = CALLFUNC_PII(InterfaceDic['GetClassCodeById'])
        self.GetSmaliCodeById_ = CALLFUNC_PII(InterfaceDic['GetSmaliCodeById'])
        self.GetJavaCodeById_ = CALLFUNC_PII(InterfaceDic['GetJavaCodeById'])
        self.GetUrlString_ = CALLFUNC_PI(InterfaceDic['GetUrlString'])
        self.FindClassId_ = CALLFUNC_IPI(InterfaceDic['FindClassId'])
        self.GetMethodNameById_ = CALLFUNC_PII(InterfaceDic['GetMethodNameById'])
        self.GetStringByTypeId_ = CALLFUNC_PII(InterfaceDic['GetStringByTypeId'])
        self.DumpData_= CALLFUNC_PIIII(InterfaceDic['DumpData'])
        self.WriteBinaryToDex_= CALLFUNC_IIPII(InterfaceDic['WriteBinaryToDex'])
        self.DumpBin_= CALLFUNC_IPIII(InterfaceDic['DumpBin']) 
        self.GetMethodDeclare_= CALLFUNC_PII(InterfaceDic['GetMethodDeclare']) 
        self.DexList=[]    # GdaDex List,for supporting multi-Dex,will be setup by GDA       
        
    # return the strings used by all methods, dexId is the index of GdaDex,
    # default value is 0, most of apk only contains one Dex    
    def GetAppString(self,dexId=0):
        return self.GetAppString_(dexId)
    # GDA print, the string will be output in GDA tool    
    def log(self,str):
        return self.log_(ctypes.c_char_p(str))
    # return all Permissions string of apk file   
    def GetPermission(self):
        return self.GetPermission_()
    # return the certificate      
    def GetCert(self):
        return self.GetCert_()
    # return the Suspicious behavior    
    def GetSupicous(self,dexId=0):
        return self.GetSupicous_(dexId)
    # getting string by string index    
    def GetStringById(self,idx,dexId=0):
        return self.GetStringById_(idx,dexId)
    # getting method name by method index    
    def GetMethodNameById(self,idx,dexId=0):
        return self.GetMethodNameById_(idx,dexId)
    # updating the class name    
    def SetClassName(self,idx,name,dexId=0):
        return self.SetClassName_(idx,ctypes.c_char_p(name),dexId)
    # updating the method name    
    def SetMethodName(self,idx,name,dexId=0):
        return self.SetMethodName_(idx,ctypes.c_char_p(name),dexId)   
    # getting the chass code by class index    
    def GetClassCodeById(self,idx,dexId=0):
        return self.GetClassCodeById_(idx,dexId)
    # getting the smali code by method index    
    def GetSmaliCodeById(self,idx,dexId=0):
        return self.GetSmaliCodeById_(idx,dexId)
    # getting the java code by method index    
    def GetJavaCodeById(self,idx,dexId=0):
        return self.GetJavaCodeById_(idx,dexId)
    # getting the all the strings like url    
    def GetUrlString(self,dexId=0):
        return self.GetUrlString_(dexId)
    # getting class idx by the class descriptor    
    def FindClassId(self,descriptor,dexId=0):
        return self.FindClassId_(ctypes.c_char_p(descriptor),dexId)
    # getting type string by type index    
    def GetStringByTypeId(self,idx,dexId=0):
        return self.GetStringByTypeId_(idx,dexId) 
    # getting method by index, etc:setValue(Activity myActivity)   
    def GetMethodDeclare(self,idx,dexId=0):
        return self.GetMethodDeclare_(idx,dexId) 
    # dump the binary data of dex file into file     
    def DumpBin(self,fileName,offset,size,dexId=0):
        return self.DumpBin_(ctypes.c_char_p(fileName),offset,size,dexId)
    # getting the binary data of dex file by hex formation   
    # width is the bytes of a line,eg:16
    def DumpData(self,offset,size,width=16,dexId=0):
        return self.DumpData_(offset,size,width,dexId)  
    # write binary data into dex file, note:probaly damage the Dex File     
    def WriteBinaryToDex(self,offset,bytes,buffLen,dexId=0):
        return self.WriteBinaryToDex_(offset,ctypes.c_char_p(bytes),buffLen,dexId)         
        
        
        
        