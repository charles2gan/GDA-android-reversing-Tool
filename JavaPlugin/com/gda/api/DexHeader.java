package com.gda.api;
public class DexHeader{
	public byte[] magic= new byte[8];
	public int checksum= 0 ;
	public byte[] signature= new byte[20];
	public int DexSize= 0 ;
    public int headerSize= 0 ;
    public int endianTag= 0 ;
    public int linkSize= 0 ;
    public int linkOff= 0 ;
    public int mapOff= 0 ;
    public int stringIdsSize= 0 ;
    public int stringIdsOff= 0 ;
    public int typeIdsSize= 0 ;
    public int typeIdsOff= 0 ;
    public int protoIdsSize= 0 ;
    public int protoIdsOff= 0 ;
    public int fieldIdsSize= 0 ;
    public int fieldIdsOff= 0 ;
    public int methodIdsSize= 0 ;
    public int methodIdsOff= 0 ;
    public int classDefsSize= 0 ;
    public int classDefsOff= 0 ;
    public int dataSize= 0 ;
    public int dataOff= 0 ;
	public DexHeader(){super();}
}