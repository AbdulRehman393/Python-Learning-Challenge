You can create a simple collection of ordered items using a Python list. e.g.

`fruits = ["Cherry", "Apple", "Pear"]`

or

`states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]`

### Accessing Items in Lists

You can provide the name of the list then a square bracket and then the item index that you want. e.g.

`states_of_america[0]`

will give you "Delaware".

Remember that everything computer related, the first number we count with is 0 and never 1. 0, 1, 2, 3 instead of 1, 2, 3 4.

### Negative Indices

You can access items in the list counting from the end of the list by using negative whole numbers. e.g.
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] #this will be "Pear"
```

### Modifying Items
You can use the same syntax to get hold of items in a List to modify it. e.g.
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
# fruits will now become ["Orange", "Apple", "Pear"]
```

### Adding Items
You can add items to the end of a List using the `append()` function. e.g.
```
fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# fruits will now become ["Cherry", "Apple", "Pear", "Orange"]
```

### Lists Documentation
You can find the documentation for Python Lists and other List related functions here: https://docs.python.org/3/tutorial/datastructures.html