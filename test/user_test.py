import requests

URL = "http://127.0.0.1:5000/"

# GET test
id=1
res = requests.get(URL+"user?id={}".format(id))
assert res.status_code == 200

# POST test
data = {
    "users" :[
        {
            "name" : "前田四郎"
        },
        {
            "name" : "水野五郎"
        }
    ]
}
res = requests.post(URL+"user?id={}".format(id), json=data )
assert res.status_code == 204

# PUT test
data = {
   "id":1,
   "name":"変更花子"
}
res = requests.put(URL+"user?id={}".format(id), json=data )
assert res.status_code == 204 


# DELETE test
del_id=2
res = requests.delete(URL+"user?id={}".format(del_id) )
assert res.status_code == 204
