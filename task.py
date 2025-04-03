# "String Functions"

'''
a="Hi This is Nikhilesh"
print(type(a))
#length
print(f"Length of the string : {len(a)}")

#count method
c=a.count("h")
print(f"The count of the letter h in the given string {c}")

#find method
f=a.find("e")
print(f"To find the index of the letter which comes first {f}")

#replace Method
print("Replacing of words",a.replace("This is","I am"))

#uppercase
print("Changing all letter to uppercase",a.upper())

#lower case
print("Changing all letter to lowercase",a.lower())

#Capitalize
print("Capitalize in string",a.capitalize())

#conditions
print("Checks if the string is upper",a.isupper())
print("Checks if the string is lower",a.islower())
print("Checks the string is alpha",a.isalpha())
print("Checks if the string is digit",a.isdigit())
print("Checks if the digit is alpha num",a.isalnum())
print("Checks weather the given letter starts with",a.startswith("H"))
print("Checks weather the given ends with letter",a.endswith("h"))

#split()
print("Splits the given string\n",a.split())

#join
print("Joins the given list as a string with the given space or words","*".join(a))

#strip
k="   Ram krishna"
print("Removes spaces from the left side",k.lstrip())
l="Ram Krishna   "
print("Removes spaces from the right side",l.rstrip())

'''


#"List Methods"
'''
li=["python","SQL","Java","C"]
print(type(li))

li.append("Flask")
print("Append used to to add an element to the list",li)

li.pop()
print(li)

del li[1]
print(li)

li.extend(["SQL","Flask"])
print(li)

li.insert(1,"HTML")
print(li)

li.reverse()
print(li)

li.sort()
print(li)

print(len(li))
'''


#Tuple Methods
'''
tu=("Ram",1,2+4j,True)
print(type(tu))

print(len(tu))

print(tu.index("Ram"))

'''

#Grading Marks
'''
m=int(input("Enter Marks 0 to 100: "))
if m<100:
    if 90<m and m<=100:
        print("Grade A")
    if 70<m and m<=89:
        print("Grade B")
    if 60<=m and m<=69:
        print("Grade C")
    else:
        print("Fail")
else:
    print("Please Enter Correct Marks")
'''
# Palindrome

'''a=input("Enter a string :")
l=len(a)
str=""
for i in range(l):
    str+=a[-(i+1)]
if str==a:
    print("Palindrome")
else:
    ("Not A Palindrome")'''

'''a=input("Enter a string: ")
rev=a[::-1]
if rev==a:
    print("Palindrome")
else:
    print("Not a Palindrome")'''

#Prime Number
'''num=int(input("Enter a Number: "))
if num>1:
    for i in range(2,num//2):
        if num%i==0:
            print("Its not Prime")
            break
    else:
        print("Its prime")
else:
    print("Its not a prime number")'''

'''num=int(input())
for i in range(2,num+1):
    c=0
    for j in range(2,i+1):
        if i%j==0:
            c=c+1
        else:
            pass
    if c==1:
        print(i)
    else:
        pass'''

#Fibbanoci series(0,1,1,2,3,5,8,13)
'''
num=int(input("Enter a Number: "))
a,b=0,1
for i in range(num):
    print(a,end=",")
    a,b=b,a+b'''
'''
n=int(input())
fs=[0,1]
for i in range(2,n):
    fn=fs[i-1]+fs[i-2]
    fs.append(fn)
    print(fs)'''
    
#Retrieve the keys from the dictionary based on the key display the value
'''dic={"name":"Ram","age":22,"city":"Vijayawada","state":"Andhra Pradesh","Country":"India"}
k=dic.keys()
for i in k:
    print(i)
    print(dic[i])'''
    
#1-100 even number change to @
'''for i in range(1,101):
    if i%2==0:
        print("@")
    else:
        print(i)'''
        
#Collection iterate each element and square it
k=[2,3,4,5,6,7,8,9]
'''for i in k:
    k=i**2
    print(k)'''
    
'''l=[i**2 for i in k]
print(l)'''

#Get the details from the user,function is to display the values whatever we get from the user
'''
def details():
    name=input("Name")
    city=input("City")
    gender=input("gender")
    print(name)
    print(city)
    print(gender)
details()'''

#Calaculator

'''
def cal(a,b):
    k=input("Select an operator +, - , * , / ")
    if k=="+":
        return a+b
    elif k=='-':
        return a-b
    elif k=="*":
        return a*b
    elif k=="/":
        return a/b
a=int(input("a value: "))
b=int(input("b value: "))
print(cal(a,b))

'''




