import xml.etree.ElementTree as ET
import f
head = []
#head.append(["User-Agent","myown"])



aaaLogin = ET.Element("aaaLogin")
aaaLogin.set("inName","admin")
aaaLogin.set("inPassword","")
ucsmBody =   ET.tostring(aaaLogin)

ucsmIP = "10.0.254.12"


#ret = f.API_call("http://"+ucsmIP+"/nuova",ucsmBody,head)
#retXML = ET.fromstring(ret)

#outCookie =  retXML.get("outCookie")
outCookie = "1470339685/20ecf369-4ac8-441f-8b86-bfaa6228c381"
#print outCookie


'''
Example of creating multiple vlans using makeUCS_XML to generate XML file from
for  v in range(20,31):

	ucsmBody = f.makeUCS_XML(outCookie,"fabricVlan","fabric/lan/net-vlan"+str(v),{"id":str(v),"name":"vlan"+str(v),"status":"deleted"})
	ret = f.API_call("http://"+ucsmIP+"/nuova",ucsmBody,head)
	#retXML = ET.fromstring(ret)


'''
ucsmBody = f.makeUCS_XML(outCookie,"macpoolPool","org-root/mac-pool-mac_pool_one1",{"name":"mac_pool_one1","status":"created"})
ret = f.API_call("http://"+ucsmIP+"/nuova",ucsmBody,head)

retXML = ET.fromstring(ret)
print ret
"""
ucsmBody = f.makeUCS_XML(outCookie,"macpoolBlock","org-root/mac-pool-mac_pool_one/block-00:25:C5:00:00:00-00:25:C5:00:00:7F",{"from":"00:25:C5:00:00:00","to":"00:25:C5:00:00:7f","status":"created"})
ret = f.API_call("http://"+ucsmIP+"/nuova",ucsmBody,head)

retXML = ET.fromstring(ret)
print ret
"""
