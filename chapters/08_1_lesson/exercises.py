
##### Template for Chapter 8 Exercises 1 - 5 ######

print("********** Ch 8 Exercise 1 **********")

# Do your work for Excercise 1 here.  

print("Ch 8 Exercise 1: Not implemented") # Delete this line when you write your code!


print("********** Ch 8 Exercise 2 **********")

# Do your work for Excercise 2 here.

print("Ch 8 Exercise 2: Not implemented") # Delete this line when you write your code!



print("********** Ch 8 Exercise 3 **********")

# Do your work for Excercise 3 here.

print("Ch 8 Exercise 3: Not implemented") # Delete this line when you write your code!



print("********** Ch 8 Exercise 4 **********")

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print('''''')




print("********** Ch 8 Exercise 5 **********")

print

text = input("Enter message")
shift = 9

result = ""

for letter in text:
    if letter == " ":
        result = result + " "
    else:
        number = ord(letter) - ord("a") 
        new_number = (number + shift) % 26
        new_letter = chr(new_number + ord("a"))
        result = result + new_letter
print("Encrypted:", result)