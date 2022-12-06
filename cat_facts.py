import requests

url='https://cat-fact.herokuapp.com/facts'
get_result = requests.get(url).json()
result = [get_result]
print(result)