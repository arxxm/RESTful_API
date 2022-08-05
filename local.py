import requests

res = requests.put('http://127.0.0.1:3000/api/courses/3', json={'name': 'Swift', 'videos': 8})
# res = requests.post('http://127.0.0.1:3000/api/courses/3', json={'name': 'PHP', 'videos': 15})
print(res.json())