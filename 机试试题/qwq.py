def add(a):
    a += 2
    if a > 100:
        return a
    else: 
        return add(a)

print(add(1))
str_1 = "qwq"
str_1[0]
print(str_1[0])


arr_1 = (1, 2, 3 ,4)  #List
#        0  1  2  3
arr_2 = (1, 2 ,3 ,4)  #tuple

arr_3 = arr_1 + arr_2
print(arr_2 + arr_1)
set_1 = {1, 2 ,3 ,4, 2, 5, 1}  #object
arr_1[1]
set_1.add(1)  #引用对象中的方法
print (set_1)
def qwq() -> None:
    print("Hello World!")

y = 0

print(not y)

dict_1 = {
    #键Key : 值Value  键值对
    'yaoyifeng' : arr_1[0],
    'shutianyu' : arr_1[1]
}        

print (dict_1)
