from zeep import Client

client = Client('https://graphical.weather.gov/xml/DWMLgen/wsdl/ndfdXML.wsdl')
result = client.service.LatLonListZipCode('20910')

print(result)
