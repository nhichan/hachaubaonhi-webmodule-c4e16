from models.service import Service
import mlab

mlab.connect()

#all_services = Service.objects()

#print(all_services[10].name)

id_to_find = "5ac0946cf03a9d054485c451"

#tim  ID:
#Dua = Service.objects(id=id_to_find)[0] #Lay thang dau tien vi day hien ra kq la 1 list

#Dua = Service.objects.get(id=id_to_find)

service = Service.objects.with_id(id_to_find)
#phai check truoc khi in ra
if service is None:
    print('service not found')
else:
    service.update(set__yob=1995)
    service.reload()
    print(service.yob)
    #print(Dua.to_mongo())
#lay het tat ca du lieu do ra
#để xóa:
#Dua.delete()
