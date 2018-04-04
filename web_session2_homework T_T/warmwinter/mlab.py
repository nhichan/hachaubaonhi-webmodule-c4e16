import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds121588.mlab.com:21588/mua_dong_khong_lanh

host = "ds121588.mlab.com"
port = 21588
db_name = "mua_dong_khong_lanh"
user_name = "johnprice"
password = "johnprice"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
