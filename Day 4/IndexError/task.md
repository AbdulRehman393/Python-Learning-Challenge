### Length of List
You can get the length of a list (number of items in the list) or the length of a string (number characters in the string) by using the `len()` function. https://docs.python.org/3/library/functions.html#len

### IndexError
When you try to access an item that is not in the range of the List, you will get an IndexError. e.g.

```
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3]) #This will be an IndexError
```

### Nested Lists
You can put Lists inside other Lists, this becomes something called a "Nested List" or a "2D List". e.g.

```
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
```
You could also represent the list in 2D format like this:
```
["Cherry", "Apple", "Pear"]
["Cucumber", "Kale", "Spinnach"]
```
