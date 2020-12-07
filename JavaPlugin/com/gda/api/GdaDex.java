package com.gda.api;
import java.util.HashMap;
import java.util.ArrayList;
public class GdaDex{
	public DexHeader dexHeader;
	public HashMap<String, MethodInfo> MethodTable;
	public HashMap<String, ClassInfo> ClassTable;
	public ArrayList<MethodInfo> MethodList;
	public ArrayList<ClassInfo> ClassList;
	public GdaDex(){
		super();
	}
}