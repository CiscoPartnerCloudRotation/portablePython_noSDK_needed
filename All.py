import xml.etree.ElementTree as ET
import f
head = []
#head.append(["User-Agent","myown"])



fl = open("in.txt","r")

text = fl.read()
ActionList = []
lines = text.split("\n")
for line in lines:
	words = line.split(" ")
	if len(words)>1:
		if words[0] == "UCSM":
			ucsmIP = words[1] #assign IP address from text file
			ucsmUser = words[2]
			ucsmPass = words[3]
			print ucsmIP
		else:
			ActionList.append(words) #get objects from text file
			
			
			

aaaLogin = ET.Element("aaaLogin")
aaaLogin.set("inName",ucsmUser)
aaaLogin.set("inPassword",ucsmPass)
ucsmBody =   ET.tostring(aaaLogin)

ucsmIP = "10.0.254.12"


#ret = f.API_call("http://"+ucsmIP+"/nuova",ucsmBody,head)
#retXML = ET.fromstring(ret)

#outCookie =  retXML.get("outCookie")
outCookie = "1471015912/e622ff26-6362-4aed-a1c7-a43d7ef0d4ed"
#print outCookie

for line in ActionList: 
	print line
	ucsmBody = ""
	if line[0]=="VLAN":
		ucsmBody = f.makeUCS_XML(outCookie,"fabricVlan","fabric/lan/net-VLAN"+line[2],{"id":line[2],"name":"VLAN"+line[2],"status":line[1]})
	ret = f.API_call("http://"+ucsmIP+"/nuova",ucsmBody,head)
	#retXML = ET.fromstring(ret)
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
'''
Example of creating multiple vlans using makeUCS_XML to generate XML file from
for  v in range(20,31):

	ucsmBody = f.makeUCS_XML(outCookie,"fabricVlan","fabric/lan/net-vlan"+str(v),{"id":str(v),"name":"vlan"+str(v),"status":"deleted"})
	ret = f.API_call("http://"+ucsmIP+"/nuova",ucsmBody,head)
	#retXML = ET.fromstring(ret)


'''
"""
ucsmBody = f.makeUCS_XML(outCookie,"macpoolPool","org-root/mac-pool-mac_pool_one1",{"name":"mac_pool_one1","status":"created"})
ret = f.API_call("http://"+ucsmIP+"/nuova",ucsmBody,head)

retXML = ET.fromstring(ret)
print ret
"""
"""
ucsmBody = f.makeUCS_XML(outCookie,"macpoolBlock","org-root/mac-pool-mac_pool_one/block-00:25:C5:00:00:00-00:25:C5:00:00:7F",{"from":"00:25:C5:00:00:00","to":"00:25:C5:00:00:7f","status":"created"})
ret = f.API_call("http://"+ucsmIP+"/nuova",ucsmBody,head)

retXML = ET.fromstring(ret)
print ret
"""
