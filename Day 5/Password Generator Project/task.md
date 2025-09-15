The program will ask:
```
How many letters would you like in your password?
How many symbols would you like?
How many numbers would you like?
```
The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

### Demo
https://appbrewery.github.io/python-day5-demo/

### Easy Version
Generate the password in sequence. Letters, then symbols, then numbers. If the user wants

4 letters
2 symbols and
3 numbers
then the password might look like this:

`fgdx$*924`

You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

<div class="hint">
  Remember you can use the random.choice() function to get a random item from a List! But you need to import the random module first.
</div>


### Hard Version
When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:

`x$d24g*f9`

And every time you generate a password, the positions of the symbols, numbers, and letters are different. This will make the password more difficult for hackers to crack.

The essential skill of a good programmer is using Google to find what you need. Your brain is for thinking, not memorising functions! You will need to Google to solve this project on the hard level. If you get stuck, check the hint below for what to Google.

<div class="hint">
  Try googling: "How to shuffle items in a List in Python"
</div>
