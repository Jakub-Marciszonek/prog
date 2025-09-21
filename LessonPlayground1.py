# Teacher = {
#     "name":"Teacher",
#     "age": 47,
#     "city":"Lahti"
# }
# for key in Teacher:
#     print(key)
#     print(Teacher[key])

# Students = [
#     {"name":"Mikko", "age":25, "city":"Tampere"},
#     {"name":"Majia", "age":30, "city":"Espoo"},
#     {"name":"Ville", "age":35, "city":"Helsinki"}
# ]
# # print(Students)
# # print(Students[0])

# for key in Students:
#     print(key)
    
# Order = {
#     "starter":{1:"Salad",2:"Soup"},
#     "main":{1:["Burger","Fries"], 2:["Steak"]},
#     "dessert":{1:["ice Cream"], 2:[]},
# }

# #### instruction are readed respectivly first dictionary main tag then 1 tag 
# ### and then component of list with

# print(Order["main"][1][0])

Courses = {
    "Python basics":{
        "content":[
            "conditions", "loops", "functions", "data types"
        ],
    },
    "html":{
        "content":[
            "cos", "tak", "dupa"
    ]
    }
}

        
#### first attempt
# for i in Courses["Python basics"]["content"]:
#     print(i)
# for i in Courses["html"]["content"]:
#     print(i)

#### noah idea/most efficient/attapeted
# for i in Courses:
#     for k in Courses[i]["content"]:
#         print(k)

### universal method
# for i in Courses:
#     for k in Courses[i]:
#         for z in Courses[i][k]:
#             print(z)

# import random

# StudentsAge = []
# n=range(10)
# for i in n:
#     StudentsAge.append(random.randint(18,60))
# print(StudentsAge)

# for i  in range(1,10):
#     print(i)

# for i in range(1,10):
#     print(i,end=' ')

# for i in range(1,10,3):
#     print(i)

# Total = 0 
# for i in range(1, 101):
#     Total += i
# print(Total)

# Given = int(input("Give nr "))

# for i in range(2 , Given, 2):
#     print(i, end=" ")


###it skips 3###
# for i in range(9): 
#     if i == 3:
#         continue
#     print(i)


# i = 0
# while i <= 10:
#     print(f"The interation is: {i}")
#     i+=1

# ContinueLoop = True
# while ContinueLoop == True:
#     if input("Do you want to contine?") !="yes":
#         ContinueLoop = False
