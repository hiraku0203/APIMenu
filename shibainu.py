import requests

url='http://shibe.online/api/shibes?count=[1-100]&urls=[true/false]&httpsUrls=[true/false]'
get_result = requests.get(url).json()
result = ["https://cdn.shibe.online/shibes/"+get_result[0]+".jpg"]
print(result)