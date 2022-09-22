import xml.etree.ElementTree as ET

tree = ET.parse(IN[0]) #IN[0]
exchange = tree.getroot()

clashname = []
clashdistance = []
clashx = []
clashy = []
clashz = []
gridlocation = []
obj1ID = []
obj2ID = []
info1 = []
info2 = []

batchtest = exchange.find('batchtest')
clashtests = batchtest.find('clashtests')
clashtest = clashtests.find('clashtest')
clashresults = clashtest.find('clashresults')
for clashresult in clashresults:
    clashname.append(clashresult.get('name'))
    clashdistance.append(clashresult.get('distance'))

    crchildren = clashresult.getchildren()
    clashpoint = crchildren[2].getchildren()
    clashx.append(clashpoint[0].get('x'))
    clashy.append(clashpoint[0].get('y'))
    clashz.append(clashpoint[0].get('z'))

    gridlocation.append(crchildren[3].text)

    clashobjects = crchildren[5]

    clashobject = clashobjects.getchildren()

    objectattribute0 = clashobject[0].getchildren()
    objattr = objectattribute0[0].getchildren()
    obj1ID.append(objattr[1].text)
    smarttag1 = objectattribute0[2].getchildren()
    info1.append(smarttag1[0][1].text)


    objectattribute1 = clashobject[1].getchildren()
    objattr = objectattribute1[0].getchildren()
    obj2ID.append(objattr[1].text)
    smarttag2 = objectattribute1[2].getchildren()
    info2.append(smarttag2[0][1].text)
#Preparing output to Dynamo
OUT = [clashname, clashdistance, clashx, clashy, clashz, gridlocation, obj1ID, obj2ID, info1, info2]