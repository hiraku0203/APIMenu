import requests

#url='https://dog.ceo/api/breeds/image/random'
url = 'https://random.dog/doggos/image/random'
get_result = requests.get(url).json()
result = [get_result]
print(result)