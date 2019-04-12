import requests

f = open('helloworld.txt','w')
f.write('hello world')
f.close()

while True: 
    res = requests.get('https://appputh2.herokuapp.com/')
