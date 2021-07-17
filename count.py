from collections import Counter

dict ={
    "d1" :{
    "book id" : "1",
    "author" : "Jagruti",
    "type" : ["Kids","adult","teens","Kids","teens"]
    },
    "d2":{
     "book id" : "2",
    "author" : "Rahul",
    "type" : ["Kids","teens"]
    },
     "d3":{
     "book id" : "2",
    "author" : "Rahul",
    "type" : ["Kids","teens"]
    }
}

list1=[]
for keys in dict:
    tempdict = dict[keys]
    for tempkeys in tempdict:
        if tempkeys == "type":
          x =tempdict[tempkeys]
          list1= list1 + x
print(list1)
c=Counter(list1)
print(c)