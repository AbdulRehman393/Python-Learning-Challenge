### Flooring a Number
You can floor a number or remove all decimal places using the `int()` function which converts a floating point number (with decimal places) into an integer (whole number).

`int(3.738492) # Becomes 3` 

### Rounding a Number
However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python `round()` function.

`round(3.738492) # Becomes 4`

`round(3.14159) # Becomes 3`

`round(3.14159, 2) # Becomes 3.14`

### Assignment Operators
Assignment operators such as the addition assignment operator `+=` will add the number on the right to the original value of the variable on the left and assign the new value to the variable.

`+=`

`-=`

`*=`

`/=`

### f-Strings
In Python, we can use f-strings to insert a variable or an expression into a string.

`age = 12`

`print(f"I am {age} years old")`

`# Will output I am 12 years old.`