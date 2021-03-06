#Loops

Loops

-While Loops
-for Loops

Condition is true, while loop execute a set of statements

x = 1
while x < 7:
	print(x)
	x += 1



while loop require variable ready

x = 1
while x < 7:
	print(x)
	if x == 5:
		break
	x += 1

>>> x = 1
>>> while x < 7:
...     print(x)
...     x += 1
...
1
2
3
4
5
6

>>> x = 1
>>> while x < 7:
...     print(x)
...     if x == 5:
...             break
...     x+= 1
...
1
2
3
4
5

For Loops

#for loops is iterating over a sequence

fruits = ["apple","banana","orange","pineapple","coconut","cucumber"]
for x in fruits:
	print(x)

#Looping in a String

for x in "pineapple":
	print(x)

#the break statement

#stop after condition

fruits = ["apple","banana","orange","pineapple","coconut","cucumber"]
for x in fruits:
	print(x)
	if x == pineapple:
		break


----
#stop before condition

fruits = ["apple","banana","orange","pineapple","coconut","cucumber"]
for x in fruits:
	if x == "pineapple":
		break
	print(x)

#The range() Function - a set of code a specified number of times 

for x in range(10):
	print(x)


for x in range (10, 100):
	print(x)


for x in range (10, 100, 5):
	print(x)


#Nested loops

NumberA = [1,2,3,4,5]
NumberB = [1,2,3,4,5]

for x in numberA:
	for y in NumberB:
		print (x,y)

#Pass 

for x in [1,2,3,4,5]:
	if x == 3:
		pass
	print(x)

-----------------------

words = ['cat','window','defenestrate']
for x in words:
	print(w, len(w))



------------------------

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x , '*', n//x)
			break
	else:
		#loop fell through without finding a factor
		print(n, 'is a prime number')

2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
------------------------

for num in range (2, 10):
	if num % 2 == 0:
		print('Found an even number' , num)
			continue
		print("Number is", num +10)
	print("Found a number", num)

Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9

-------------------------

 for num in range(2, 10):
...     if num % 2 == 0:
...             print("Found an even number" , num)
...             continue
...             print("Number is", num + 10)
...     print("Found a number", num)

