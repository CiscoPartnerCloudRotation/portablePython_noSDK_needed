import urllib2
import xml.etree.ElementTree as ET

def API_call(url,data,headers=[]):
	
	req = urllib2.Request(url)
	if data:
		req.data = data
	if headers:
		for hd in headers:
			print "has headers"
			req.add_header(hd[0],hd[1]);
			print (hd)

	ret = urllib2.urlopen(req)
	return ret.read()


def makeUCS_XML(outCookie,name,dn,obj):
	configConfMos = ET.Element("configConfMos")
	configConfMos.set("cookie",outCookie)
	configConfMos.set("inHierarchical","false")

	inConfigs = ET.Element("inConfigs")

	pair = ET.Element("pair")
	pair.set("key",dn)
	

	elem = ET.Element(name)
	elem.set("dn",dn)
	for el in obj:
		elem.set(el,obj[el])



	pair.append(elem)
	inConfigs.append(pair)
	configConfMos.append(inConfigs)


	return   ET.tostring(configConfMos)


