### Nested conditionals
You can put if/else statements inside other if/else statements. This is known as nesting.
e.g.

```
if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
if english_score >= 90:
    print("You're good at english)
```

In this case only when a student has over 90 on maths and english, do they get "You are good at everything".

Note: You can also have if statements that don't have a paired else statement.
