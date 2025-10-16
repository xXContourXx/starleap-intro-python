
##### Template for Chapter 5.14, Exercises 1 - 4 ######


def time_since_epoch():
    import time
    T= time.time()
    print(T)
    days =int (T // 86400)
    print(days)
#time_since_epoch()





#print("********** Ch 5 Exercise 2 **********")

# Do your work for Excercise 2 here.

#print("Ch 5 Exercise 2: Not implemented") # Delete this line when you write your code!



##print("********** Ch 5 Exercise 3 **********")

def is_triangle(a, b, c):
    print('is triangle()', a, b, c)
    if a>=b + c:
        print('Not a triangle')
    elif b>= a + c:
        print('Not a triangle')
    elif c>= a + b:
        print('Not a triangle')
    else:
        print('Is a triangle')
    
a = float(input('how long is side a?'))
print('a is', a, type(a))

b = float(input('how long is side b?'))
print('b is', b, type(b))

c = float(input('how long is side c?'))
print('c is', c, type(c))

is_triangle(a, b, c)

#print("********** Ch 5 Exercise 4 **********")

# Do your work for Exercise 4 here.

#print("Ch 5 Exercise 4: Not implemented") # Delete this line when you write your code!
