import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('ryan', 'password')
r = requests.post(url="http://pythinscraping.com/pages/auth/login.php", auth=auth)
print(r.text)
