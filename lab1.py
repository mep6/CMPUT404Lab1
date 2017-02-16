#!/usr/bin/env python
import requests

print requests.__version__

response = requests.get("https://raw.githubusercontent.com/mep6/CMPUT404Lab1/master/lab1.py")


print response.text
print response.status_code
