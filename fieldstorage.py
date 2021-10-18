#! /usr/bin/python37all

import cgi
import cgitb
cgitb.enable()

print("Content-type: text/html\n\n")

data = cgi.Fieldstorage()