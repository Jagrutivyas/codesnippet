from collections import Counter
d = {}
list1=[]
str1 = ""
with open("library.txt") as f:
  for line in f:
    (val1,val2,val3) = line.split()
    str1 =str1 + val3 + ","
    print(str1)
(value) = str1.split(",")
list1= list1 + value
print (list1)
c=Counter(list1)
print(c)

""""
src = [ 'one', 'two', 'three', 'two', 'three', 'three' ]
result_dict = dict( [ (i, src.count(i)) for i in set(src) ] )
print(result_dict)
"""