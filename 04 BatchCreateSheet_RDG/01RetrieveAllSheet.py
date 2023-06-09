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

#FEC for sheets catgories
sheets = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets)

#get RDG_ parameters from ProjectInformation and output as dictionary
projectinfopara = doc.ProjectInformation.ParametersMap
projectinfoparaguid = []
projectinfoparaname = []
for i in projectinfopara:
    try:
        projectinfoparaguid.append(i.GUID) #non shared parameters are filtered out by try-except as only shared para got GUID
        projectinfoparaname.append(i.Definition.Name)
    except:
        pass        
projectinfoparadict = {}
for i,j in zip(projectinfoparaname, projectinfoparaguid):
    projectinfoparadict[i] = doc.ProjectInformation.get_Parameter(j).AsString()
    
projectinfoRDG_Originator = projectinfoparadict["RDG_Originator"]
#projectinfoRDG_ProjectNumber = projectinfoparadict["RDG_ProjectNumber"] #what is the purpose of this parameter???
projectinfoRDG_Discipline = projectinfoparadict["RDG_Discipline"]
projectinfoNumber = doc.ProjectInformation.Number

projectsheetnumber = [projectinfoNumber + '-' + projectinfoRDG_Originator + '-' + sheet.LookupParameter("RDG_SheetFunction").AsValueString() + '-' + sheet.LookupParameter("RDG_SheetSpatial").AsValueString() + '-' + sheet.LookupParameter("RDG_SheetForm").AsValueString() + '-' + projectinfoRDG_Discipline + '-' + "".join(sheet.get_Parameter(BuiltInParameter.SHEET_NUMBER).AsString().split()) for sheet in sheets]
projectsheetname = []
for sheet in sheets:
    name1 = sheet.get_Parameter(BuiltInParameter.SHEET_NAME).AsString()
    name2 = sheet.LookupParameter("RDG_SheetName02").AsValueString()
    name3 = sheet.LookupParameter("RDG_SheetName03").AsValueString()
    if name3 is None or name3 == "":
        try:
            temp = name1 + '-' + name2 if name2 != "" else name1
        except:
            temp = name1
    else:
        temp = name1 + '-' + name2 + '-' + name3
    projectsheetname.append(temp)

projectsheetid = [sheet.Id for sheet in sheets]

#Assign your output to the OUT variable
OUT = [projectsheetid, projectsheetnumber, projectsheetname]