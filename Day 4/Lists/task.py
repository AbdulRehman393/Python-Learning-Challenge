# A list in Python is an ordered, mutable collection of elements that can hold items of any data type.
# Key points:
# Ordered → items keep their position/index.
# Mutable → you can change, add, or remove elements after creation.
# Heterogeneous → can store different data types in one list.
my_list = [1,"Hello",3.1415,True]
print(my_list)
print(my_list[1])
print(my_list[-1])
my_list[1]="Hi"
print(my_list)

my_list.append("How are you?")   #Append will add item at the end of the list
my_list.remove(1)                #Remove will remove item from the list
print(my_list)

my_list.extend(["Bilal",True])   #extend will add another list at the end of
                                 # the list
print(my_list)


