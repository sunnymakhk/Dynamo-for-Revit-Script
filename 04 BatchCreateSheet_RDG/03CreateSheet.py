# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN
newNumber = IN[0]
newName = IN[1]
titleblock = IN[2]

#split and transpose newNumber into splitNumT
splitNum = [i.split('-') for i in newNumber]
splitNumT = [[j[i] for j in splitNum] for i in range(len(splitNum[0]))]

newpinfonumber = splitNumT[0] #projectinfopara + builtIN
newRDG_Originator = splitNumT[1] #projectinfopara
newRDG_SheetFunction = splitNumT[2] #sheetpara
newRDG_SheetSpatial = splitNumT[3] #sheetpara
newRDG_SheetForm = splitNumT[4] #sheetpara
newRDG_SheetDiscipline = splitNumT[5] #projectinfopara
newSheetNumber = splitNumT[6] #sheetpara + builtIN

# "Start" the transaction
TransactionManager.Instance.EnsureInTransaction(doc)

sheets = []
for i, j, k, l, m in zip(newName, newRDG_SheetFunction, newRDG_SheetSpatial, newRDG_SheetForm, newSheetNumber):
	#create new sheet
	newSheet = ViewSheet.Create(doc, titleBlockTypeId[0])
	#set sheet name param
	bipName = BuiltInParameter.SHEET_NAME
	sheetName = newSheet.get_Parameter(bipName)
	sheetName.Set(i)
	#set sheet number param
	bipNumber = BuiltInParameter.SHEET_NUMBER
	sheetNumber = newSheet.get_Parameter(bipNumber)
	sheetNumber.Set(m)
	
	try:
	   sheetpara_RDG_SheetFunction = sheet.LookupParameter("RDG_SheetFunction")
	   sheetpara_RDG_SheetSpatial = sheet.LookupParameter("RDG_SheetSpatial")
	   sheetpara_RDG_SheetForm = sheet.LookupParameter("RDG_SheetForm")
	   
	   sheetpara_RDG_SheetFunction.set(j)
	   sheetpara_RDG_SheetSpatial.set(k)
	   sheetpara_RDG_SheetForm.set(l)
	except:
	   pass
	   
	sheets.append(newSheet)

# "End" the transaction
TransactionManager.Instance.TransactionTaskDone()

#Assign your output to the OUT variable
OUT = sheets