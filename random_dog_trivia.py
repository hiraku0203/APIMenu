import requests

url='https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number1'
get_result = requests.get(url).json()
#result = ["https://cdn.shibe.online/shibes/"+get_result[0]+".jpg"]
print(get_result)