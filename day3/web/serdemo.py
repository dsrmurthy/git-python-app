import requests,json

url ="https://jsonplaceholder.typicode.com/users"
response=requests.get(url)
users=json.loads(response.text)
#print(users)
data=json.dumps(users,indent=2)  #memory 
#print(data)

#file level serialization
with open('users.json','w')  as fw:
    json.dump(data,fw)
    print("file created")
# deserialisation
with open("users.json",'r') as fr:
    data=json.load(fr)
    print(data)
