# """ user = []
# user.append("hello")
# user.append("world")
# print(user)
# print(user[0] + " " + user[1])
#  """

# # user = [ "salom", 123456, 745285, True]
# # user.append('odam')
# # print(user)  #0
# # # user.insert(2,"HHH")
# # print(user)

# # user.remove("odam")
# # print(user)
# # user.pop(0)
# # print(user)

# # print(user.index(745285))
# # user.clear( )
# # print(user)







# persons = {
#     "name": "Sulton",
#     "age": 123456,
#     "is_active": False   
# }

# print(persons["is_active"])

# persons["tarmoq"] = 'facebook'
# # print(persons["name"])
# persons.update({ "hayvoni": 'pikachu', "mahalla" : 'jilvon' , "age" : '30'})
# print(persons.keys())
# print(persons.values())
# print(persons.items())
# print(persons)

# # for value in persons.values():
# #     print(value)


# # lugat = {"janob":"Effendi", "sogʻinch": "Hodisalar", "ishq": "Sevgi"}
# # for kalit, qiymat in lugat.items():
# #     print(kalit, qiymat)










# # odamlar = [
# #     { "name" : "Abdulla" , "age" : 12, "faolmi": True},
# #     { "name" : "paloncha" , "age" : 12, "faolmi": True },
# #     { "name" : "pistoncha" , "age" : 12 , "faolmi": True}
# # ]
















# # for items in persons.items():
# #     print(items)


# # for value in persons.values():
# #     print(value)


from turtle import *
import colorsys
tracer(5)
bgcolor("black")
pensize(2)
h=0.3
for i in range(9000):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    fd(i)
    rt(50)
    rt(40)
    fd(50)
    rt(120)
done()

print (goto)