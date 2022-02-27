from pprint import pprint
#from sys import api_version
from Google import Create_Service
USER_SECRET_FILE = "USER_SECRET_FILE.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
service = Create_Service(USER_SECRET_FILE, API_NAME, API_VERSION , SCOPES)

print(dir(service))