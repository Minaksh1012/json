# Q8.Tumhare pass four employes ki details hai list mai:-

# pass four employes ki details hai list mai:-

# [“neelam”,”programer”,”24”,”2400”,]
# [“komal”,”trainer”,”24”,”20000”]
# [“anuradha”,”HR”,”25”,”40000”]
# [“Abhishek”,”manager”,”29”,”63000”]  

# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4. har ek employee ka dictionary main name,designation,age and salary honi chahiye. aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.

# Output:-

#  { 
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#          }

#     "emp2":
#       { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         }

 
#     "emp3":
#        { "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000",
#          }


#     "emp4":
#        { "name":"Abhishek",
#          "Designation":"Manager",
#          "Age":"29",
#        }
#  }



import json
list1=["neelam","programer","24","2400"]
key1=["name","destination","age","salary"]
emp1={}
for keys in key1:
    for values in list1:
        emp1[keys]=values
        list1.remove(values)
        break

list2=["komal","trainer","24","20000"]
key1=["name","destination","age","salary"]
emp2={}
for keys in key1:
    for values in list2:
        emp2[keys]=values
        list2.remove(values)
        break
    

list3=["komal","trainer","24","20000"]
key1=["name","destination","age","salary"]
emp3={}
for keys in key1:
    for values in list3:
        emp3[keys]=values
        list3.remove(values)
        break

list4=["komal","trainer","24","20000"]
key1=["name","destination","age","salary"]
emp4={}
for keys in key1:
    for values in list4:
        emp4[keys]=values
        list4.remove(values)
        break
dict1={}
dict1.update({"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4})
print(dict1)    
with open("salary.json","w")as json_file:
    json.dump(dict1,json_file,indent=2)