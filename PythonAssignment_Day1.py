#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1) After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')

bacon = 22

bacon + 1

Ans : 23


# In[ ]:


get_ipython().set_next_input('2) What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')

'spam' + 'spamspam'

'spam' * 3

Ans : 'spamspamspam' (if we excute above 2 stmts o/p is same)


# In[ ]:


get_ipython().set_next_input('3) How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

Ans:
    break :
        It eliminates the execution of remaining iteration of loop.
        The ‘break ‘stop the continuation of the loop.
    
    continue:
        It will terminate only the current iteration of loop.
        The ‘continue’ does not stop the continuation of loop and it stops the current.
        


# In[ ]:


4) In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Ans: it will be the same output above 3 stmts,in range function default step value is 1
    1.1st stmt we are not menction start range just we are mectioned stop range(10-1=9)
    2. 2nd stmt we are menctioned start range and stop range (start from 0 and end with 10-1=9)
    3. 3rd stmt we menctioned start ,stop and step value, step value means start value + next incremnt value 
        ex: step value 1 =0+1=1(step)
            step value 2 = 0+2 =2,
            
    for i in range(10):
        print(i)
    O/p : 0,1,2,3,4,5,6,7,8,9
    for i in range(0,10):
        print(i)
    o/p :0,1,2,3,4,5,6,7,8,9
    for i in range(0,10,1):
        print(i)
    o/p : 0,1,2,3,4,5,6,7,8,9
    


# In[ ]:


5) Using a for loop, write a short programme that prints the numbers 1 to 10 Then, 
using a while loop, create an identical programme that prints the numbers 1 to 10.


# In[ ]:


for a in range(1,11):
    print(a)


# In[ ]:


i=1
while(i<=10):
    print(i)
    i+=1


# In[ ]:


6) Given a number x, determine whether the given number is Armstrong number or not.

Input : 153

Output : Yes

153 is an Armstrong number.

1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3 = 153


# In[ ]:


number = int(input("Input: "))
noofdigits = len(str(number))
sum = 0
temp = number
while temp > 0:
   reminder = temp % 10
   sum += reminder ** noofdigits
   temp //= 10
if number == sum:
    print("Yes")
    print(num,"is an Armstrong number")
else:
    print("No")
    print(num,"is not an Armstrong number")


# In[ ]:


7) Program to find Sum of squares of first n natural numbers.


# In[ ]:


number = int(input("Enter a number: "))
sum = 0
for i in range(1, number+1):
    sum += (i*i)

print("Sum of squares = ", sum)


# In[ ]:


8) Program to Reverse words in a given String in Python.


# In[ ]:


string = input("Enter any string: ")
splitstring = string.split()
splitstring.reverse()
print(' '.join(splitstring))


# In[ ]:


9) Given a list of numbers, write a Python program to find the sum of all the elements in the list.

Input: [10,12,13]

Output: 35


# In[ ]:


l = [10,12,12]
sum = 0
for x in l:
    sum = sum + x
print(sum)


# In[ ]:


10) Write a Python program to print all even numbers between 10-1000.


# In[ ]:


for num in range(10,1000):
    if num%2==0:
        print (num)

