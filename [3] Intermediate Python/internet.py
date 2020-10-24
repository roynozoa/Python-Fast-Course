# Intermediate Programming in python
# handling with internet

# import library
from urllib import request

# requesting url
req_url = request.urlopen("http://www.youtube.com")
print(req_url.getcode())
# print(req.read())  # read web data (very long html)
