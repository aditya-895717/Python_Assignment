# How do we concatenate two strings in python ?
str1="hello"
str2="python developer"
print(str1+' ' +str2)

#What is the difference between the + operator and the join() method for concatening string?
# the + operator can concatenate two or more string together, while the join operator can be use to concatenate a iterable of string
strlist=["hello","python"]
print(''.join(strlist))
# here strlist is a iterable of string

# How do we access individual character in a string ?
str="hello"
for i in str:
    print(i) #use of indexing
print(str[0])

#what method is used to find the length of a string ?
a="hello"
print(len(a))

#how can you convert a string to uppercase or lowercase in python ?
b="hello"
print(b.upper())
print(b.lower())

#which method is used to replace a substring with string ?
c="hello_dev"
print(c.replace("dev","developer"))

#How can you check a string starts with a particular string ?
d="hello python developer"
print(d.startswith("hello")) #true

#how cann we split a string into a list of substring based on delimeter?
e="hello_python_developer"
print(e.split('_'))

#How can you check if a string ends with a particular substrin g?
f="hell0 python "
print(f.endswith("python")) #true

#how can you remove leading and trailing whitespace from a string ?
g="hello Baba"
print(g.strip()) # no leading and trailing whitespace 

#method to find the index of first occurence of a substring within a string
h='hello python developer'
print(h.index('l')) #2 index

#how can you format string with placeholder for variABLE VALUES?
name="baba"
age=22
print(f"my name is {name}and my age is {age}")

#how do you access a substring of sstring using slicing?
s="hello python developer"
print(s[0:5]) #hello
print(s[-1:-8]) #repovt

#how can you remove sspecific character from a string in python ?
t="hello$ python developer"
print(t.replace('$','')) #remove $ character
 # translate both are correct

#reverse a string in  python ?
u='hello'
print(u[-1:])
print(u[::-1]) #both are correct 

#checking if a string contain alphabets or numbers only ?
v="hello 123"
print(v.isalnum())

w="hello buddy "
print(w.isalpha())

x="12345"
print(x.isdigit())

#how can we find a string is a palindrome or not ?
y="madam"
if y==y[::-1]:
    print("palindrome")

z='hello world is program' 
# we have to replace all e all o at one time 
print(z.translate(str.maketrans({'e':'','o':''})))



