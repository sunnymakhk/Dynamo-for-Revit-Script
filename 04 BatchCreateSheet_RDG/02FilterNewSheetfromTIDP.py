import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

#The inputs to this node will be stored as a list in the IN variable.
dataEnteringNode = IN

excelSheetNumber = IN[0]
excelSheetName = IN[1]
projectSheetNumber = IN[2]
projectSheetName = IN[3]

#compare excel sheets to project sheets and pass only new sheets

newNumber, newName = [], []
for i, j in zip(excelSheetNumber, excelSheetName):
    if "".join(i.split()) in projectSheetNum:
        continue
    else:
        newNumber.append(i)
        newName.append(j)

#Assign your output to the OUT variable
OUT = [newNumber, newName]