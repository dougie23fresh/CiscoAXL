# FreshCiscoAXL
Python Class for CUCM AXL API

Update coming soon
=========================

pip install the following
requests
xmltodict


from axl_requests import axl
c = axl(username, password, server_ip, server_ver, tls_verify, timeout)

r = c._post('getUser', {'userid': user})
r = c.get_user(user)

c.last_exception
