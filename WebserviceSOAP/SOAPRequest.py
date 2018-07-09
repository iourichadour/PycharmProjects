from zeep import Client

client = Client('https://graphical.weather.gov/xml/DWMLgen/wsdl/ndfdXML.wsdl')
result = client.service.LatLonListZipCode('20910')

print(result)

wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
client = Client(wsdl=wsdl)
print(client.service.Method1('Zeep', 'is cool'))