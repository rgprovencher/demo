#!/usr/bin/python37all

import cgi
import cgitb
cgitb.enable()
import json

# # takes in data passed by html page

data = cgi.FieldStorage()

settings = {"LED":data.getvalue("LED"), "Brightness":data.getvalue("Brightness")
}



with open('led-settings.txt', 'w') as f:
  # writes user-selected settings into a csv text file

  # Old code, still works for troubleshooting, but using json formatting instead
  # f.write("{},{}".format( data.getvalue('LED'),  data.getvalue('Brightness')  ))

  json.dump(settings, f)


print("""Content-type: text/html\n\n

<html>
<form action =" /cgi-bin/demo/lab4.py" method="POST">
  <input type = "radio" name = "LED" value = "0" checked > Red <br>
  <input type = "radio" name = "LED" value = "1" > Green <br>
  <input type = "radio" name = "LED" value = "2" > Blue <br>
  <br>
  <br>
  <input type = "range" name = "Brightness" min = "0" max = "100" value ="50"/>
    <input type = "submit" value = "Set LED Brightness">
</form>
</html>


""")