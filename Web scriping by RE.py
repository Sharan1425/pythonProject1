import re,urllib
import urllib.request
site = urllib.request.urlopen("https://www.maxfashion.in/in/en/contactus")
data = site.read() # Here the data will be in binary format and we have to convert it into string format
contacts = re.findall("[ +0-9]{3,4}[ ][0-9]{7,8}",str(data))
print("The Apsrtc Contact numbers: ")
for num in contacts:
    print(num)