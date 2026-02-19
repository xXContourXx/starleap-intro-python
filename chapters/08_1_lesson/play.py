fruit = 'Banana'
print(fruit)
letter = fruit[0]
print(letter)
print('len',len(fruit))
last = len(fruit)
print(fruit[last -1])

print()
index = 0
while index <len(fruit):
    letter = fruit[index]
    print(letter)
    index +=1

for letter in fruit:
    print('1=', letter)

prefixes = 'JKLMNOP'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)

s = "MontyPython"
print(s[0:5])
print(s[5:11])

for i in range(len(s)):
    print(i, s[i])

greeting = 'hello world'
greeting = 'J'+greeting[1:]
print(greeting)

def find_first(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index +=1
    return -1

print('found at', find_first('bob', 'o'))

def count_letters(word, letter):
    count = 0
    for l in word:
        if l == letter:
            count +=1
    return count

print('count: ', count_letters('bob', 'b'))

name = 'Brodie'
print(name.title())
print(name.find('i'))

n1 = 'Kurt'
n2 = 'Dave'
n1c = n1.casefold()
n2c = n2.casefold()
if n1c == n2c:
    print('same')
elif n1c < n2c:
    print('less than')
elif n1c > n2c:
    print('greater than')


def is_reverse(word1, word2):
    flip1 = ''
    index = len(word) - 1
    while index >=0:
        l = word[index]
        flip1 = flip1 +l
        index -=1
    print('flip1', flip1)
    return flip1 == word2

print(is_reverse('kurt', ''))

