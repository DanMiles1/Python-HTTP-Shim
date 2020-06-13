#!/usr/bin/python3
import cgi, cgitb
import requests
cgitb.enable()
print("Content-Type: text/html\n\n")
print("""
<html>
    <head>
        <title>Sensor Shim</title>
    </head>
    <body>
        <form method="post" action="temp.py">
<table>
<tr>
<td>Temprature:</td>
<td><input type="text" name="temp"/></td>
</tr>
<tr>
<td>Humidity:</td>
<td><input type="text" name="humidity"/></td>
</tr>
<tr>
<td>Pressure:</td>
<td><input type="text" name="pressure"/></td>
</tr>
<tr>
<td><input type="submit" value="Submit"/></td>
        </form>
</tr>
</table>
""")
form = cgi.FieldStorage()
if "temp" in form:
    temp = form["temp"].value
if "humidity" in form:
    humidity = form["humidity"].value
if "pressure" in form:
    pressure = form["pressure"].value

url = "https://endpoint"
myobj = {'Temp': temp,'Humidity': humidity,'Pressure': pressure}

x = requests.post(url, data = myobj)

print(x.text)
print("</body></html")
