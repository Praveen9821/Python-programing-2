Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#The float funtion converts a strings into a floating-point numbers.
float('10.23')
10.23
float('3.124')
3.124
float('9.99')
9.99
2,45*6
(2, 270)
5.55*10
55.5
3.7e1
37.0
#A complex numbers is a number that can be expressed in the form a+bj,where a and b are real numbers amd j is an imgaginary unit.
2+4j
(2+4j)
type(2+4j)
<class 'complex'>
9j
9j
67y
SyntaxError: invalid decimal literal
9a
SyntaxError: invalid decimal literal
#only j can be written
7j
7j
type(9j)
<class 'complex'>
type(7j)
<class 'complex'>

#The Boolean data type is represented in python as type bool.It is a primitive data type havinng one of the two values,viz.True or False.Internally, the True value is represented as 1 and False as 0.
5=5
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
5==5
True
5==4
False
4<6
True
7<5
False
6<3
False
7>5
True
4>7
False

# A string literal or string in python can be created using single,double and triple quotes.
A='Hello World'
A
'Hello World'
B='Bye'
B
'Bye'

# The str function is uesd to convert a number into a string.
12.5
12.5
type(34.6)
<class 'float'>
str(12.5)
'12.5'
str(6.7)
'6.7'

"Praveen" + "kumar"
'Praveenkumar'
"abc" + "def "
'abcdef '
"abc" + "def ghi"
'abcdef ghi'
print('Hello welcome to Python Programing')
Hello welcome to Python Programing
# The task of print function is to display the contents on the screen.
print('Hello') # ('') inverted comma before and after every string type.
Hello
print(' Hello' ,end=' ')
 Hello 
# Multiple assignments
P=20
Q=30
Temp=P
P=Q
Q=Temp
P
30
Q
20
P, Q = Q, P
P
20
Q
30
P=10
Q=20
P, Q = Q, P
P
20
Q
10
x=10
print(type(x))
<class 'int'>
2/3
0.6666666666666666
2.0/3
0.6666666666666666
2.0/3.0
0.6666666666666666
2//3
0
2//3.0
0.0
2.0//3.0
0.0
Fun*3
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    Fun*3
NameError: name 'Fun' is not defined
"Fun"*3
'FunFunFun'
