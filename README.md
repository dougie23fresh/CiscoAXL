# FreshCiscoAXL

Python Class for CUCM AXL API

pip install the following
requests
xmltodict

from axl_requests import axl
c = AXL(host, username, password, version=11.5, tls_verify=False)

r = c.get_phone('SEP0029C2949E7A')
r = c.get_user('user')
