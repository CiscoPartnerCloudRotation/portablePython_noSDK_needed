import xml.etree.ElementTree as ET
import f
import sys
head = []
#head.append(["User-Agent","myown"])


org = "org-root"

fl = open(sys.argv[1],"r")




text = fl.read()
ActionList = []
lines = text.split("\n")


for line in lines:
	if line.startswith("$"):
		varbs = line.split(" = ")
	
		for i in range(len(lines)):
			if lines[i].startswith("$")==False:
				oldline = lines[i]
				lines[i] = varbs[1].join(lines[i].split(varbs[0]))
				if oldline != lines[i]:		
					if len(varbs)>2:
					 vlen = len(varbs[1])
					 varbs[1] = str(int(varbs[1])+int(varbs[2]))
					 varbs[1] = "0"*(vlen-len(varbs[1]))+varbs[1]

for line in lines:
	words = line.split(" ")
	if len(words)>1:
		if words[0] == "UCSM":
			ucsmIP = words[1] #assign IP address from text file
			ucsmUser = words[2]
			ucsmPass = words[3]
		elif words[0].startswith("$"):
			#print words, "@"
			1+1
		else:
			ActionList.append(words) #get objects from text file
			
			
			

aaaLogin = ET.Element("aaaLogin")
aaaLogin.set("inName",ucsmUser)
aaaLogin.set("inPassword",ucsmPass)
ucsmBody =   ET.tostring(aaaLogin)



#ret = f.API_call("http://"+ucsmIP+"/nuova",ucsmBody,head)
#retXML = ET.fromstring(ret)

#outCookie =  retXML.get("outCookie")
outCookie = "1471028430/3267b149-ab6a-435c-a7c3-1303effef903"
#print outCookie

for line in ActionList: 
	print line
	ucsmBody = ""
	if line[0]=="VLAN":
		ucsmBody = f.makeUCS_XML(outCookie,"fabricVlan","fabric/lan/net-vlan"+line[2],{"id":line[2],"name":"vlan"+line[2],"status":line[1]})
		
	if line[0]=="MACPOOL":
		ucsmBody = f.makeUCS_XML(outCookie,"macpoolPool",org+"/mac-pool-"+line[2],{"name":line[2],"status":line[1]})
		
	if line[0]=="MACPOOLBLOCK":
		ucsmBody = f.makeUCS_XML(outCookie,"macpoolBlock",org+"/mac-pool-"+line[2]+"/block-"+line[3]+"-"+line[4],{"from":line[3], "to":line[4],"status":line[1]})
	
	if line[0]=="UUIDPOOL":
		ucsmBody = f.makeUCS_XML(outCookie,"uuidpoolPool",org+"/uuid-pool-"+line[2],{"name":line[2],"status":line[1]})
	
	if line[0]=="UUIDPOOLBLOCK":
		ucsmBody = f.makeUCS_XML(outCookie,"uuidpoolBlock",org+"/uuid-pool-"+line[2]+"/block-"+line[3]+"-"+line[4],{"from":line[3], "to":line[4],"status":line[1]})
	if line[0]=="SERVER":
		ucsmBody = f.makeUCS_XML(outCookie,"lsServer",org+"/ls-"+line[2],{"name":line[2],"status":line[1],"identPoolName":line[3]})
	if line[0]=="ADDNIC":
		ucsmBody = f.makeUCS_XML(outCookie,"vnicEther",org+"/ls-"+line[2]+"/ether-"+line[3],{"name":line[3],"status":line[1],"identPoolName":line[4]})
	
	if line[0]=="ADDVLAN":
		ucsmBody = f.makeUCS_XML(outCookie,"vnicEtherIf",org+"/ls-"+line[2]+"/ether-"+line[3]+"/if-vlan"+line[4],{"name":"vlan"+line[4],"status":line[1],"defaultNet":line[5]})
	



	if ucsmBody != "":
		ret = f.API_call("http://"+ucsmIP+"/nuova",ucsmBody,head)
		retXML = ET.fromstring(ret)
		#print ret
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
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
