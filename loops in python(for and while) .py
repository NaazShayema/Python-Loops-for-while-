#!/usr/bin/env python
# coding: utf-8

# # for loop 
# Used to iterate over a sequence or an iterable object(such as list,tuple,string)
# 
# Used to repeatedly execute the code block while iterating over a sequence or an iterable object such as list,tuple,dict,sets

# # 1. Print the first 10 natural numbers using for loop

# In[5]:


print("The first 10 natural numbers are : ")

for i in range (1,11):
    print(i)


# # 2. Python program to print all the even numbers within the given range

# In[4]:


# 0 is considered an even number as 0%2==0


# In[5]:


n=int(input("Enter the range : "))

print(f"The even numbers within the range {n} are: ")

for i in range(n):     # range(0,n)---------> 0<=i<n
    if i%2==0:
        print(i)


# # 3. Python program to calculate the sum of all numbers from 1 to a given number

# In[14]:


n=int(input("Enter the number : "))

print(f"The sum of all numbers from 1 to {n} is : {sum} ")

for i in range(1,n+1):
    sum=(n*(n+1))/2
    


# # 4. Python program to calculate the sum of all odd numbers within the given range

# In[19]:


1+3+5+7+9


# In[34]:


num=int(input("Enter the range : "))

sum=0

for i in range(num):
    if i%2!=0:
        sum+=i
        
print(f"The sum of all odd numbers within the given range {num} is : {sum}")


# # 5. Python program to print a multiplication table to a given number

# In[39]:


n=int(input("Enter a number : "))

print(f"The multiplication table of {n} is : ")

for i in range(1,11):
    n*i
    print(f"{n}*{i}={n*i}")


# # 6. Python program to display numbers from a list using a for loop

# In[41]:


List=[1,24,56,90,23,0]

for i in List:
    print(i)


# In[46]:


# converting numbers to a list 

List=[1,24,56,90,23,0]
L=[]

for i in List:
    print(i)
    L.append(i)
    
print(L)


# # 7. Python program to count the total number of digits in a number

# In[57]:


number=int(input("Enter a number : "))

number=str(number)

count=0

for i in number:
    count+=1
    
print(f"The total number of digits in {number} is {count}")


# # 8. Python program to check if the given string is a palindrome

# In[3]:


# a palindrome string is a sequence of characters that reads the same backward as forword.
# example; "radar"-------->"radar"


# In[30]:


string='shayema'
n=len(string)
n


# In[34]:


string='shayema'
string[2]


# In[11]:


string='shayema'
n=len(string)

# creating reverse string 
reverse_string=""
for i in range(n-1,-1,-1):
    print(string[i])
    reverse_string=reverse_string+string[i]
reverse_string

# main code
if string==reverse_string:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not palindrome")


# In[16]:


string=str(input("Enter a string: "))
n=len(string)

# creating reverse string 
reverse_string=""
for i in range(n-1,-1,-1):
    reverse_string=reverse_string+string[i]

# main code
if string==reverse_string:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not palindrome")


# # 9. Python program that accepts a word from the user and reverses it 

# In[19]:


string=str(input("Enter a string: "))
n=len(string)

# creating reverse string 
reverse_string=""
for i in range(n-1,-1,-1):
    reverse_string=reverse_string+string[i]
reverse_string    


# # 10. Python program to check if a given number is an armstrong number

# In[20]:


# 153= 1**3 + 5**3 + 3**3 = 1+125+27


# In[49]:


# Examples;0,1,153,370,371,407,.........

# -ve are not armstrong numbers


# In[50]:


(153%1000)//100


# In[51]:


(153%100)//10


# In[52]:


(153%10)//1


# In[54]:


num=int(input("Enter a number : "))
power=len(str(num))
power
    


# In[55]:


num=153
power=3

(num%(10**power))//(10**(power-1))


# In[56]:


num=153
power=3

for i in range(1,power+1):
    x=(num%(10**i))//(10**(i-1))
    print(x)


# In[57]:


num=153
power=3

for i in range(1,power+1):
    x=((num%(10**i))//(10**(i-1)))**power
    print(x)


# In[63]:


num=int(input("Enter a number : "))
power=len(str(num))

sum=0

for i in range(1,power+1):
    x=((num%(10**i))//(10**(i-1)))**power
    sum=sum+x


if num==sum:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")


# # 11. Python program to count the number of even and odd numbers from a series of numbers

# In[71]:


# 0 is an even number 
# because odd numbers are integers that are not divisible by 2, meaning they leave a remainder of 1 when divided by 2
# since 0%2==0 , it is even


# In[73]:


num_list=[2,52,45,10,69,3,71,0]
even=[]
odd=[]

for i in num_list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
print(f"The number of even numbers is {len(even)} and odd numbers is {len(odd)}")


# # 12. Python program to display all numbers within a range except the prime numbers

# In[2]:


# 2,3,5,7,11,13,17,19,23,29,31,..............


# In[3]:


# prime numbers have factors 1 and itself only:


# In[9]:


n=int(input("Enter a range : "))

for i in range(n):
    print(i)


# In[24]:


n=int(input("Enter a range : "))


for i in range(n):
    if i==0 or i==1:    # 0 and 1 are not prime numbers
        continue
    if i%2==0:
        j+=1
        continue
    print(i)


# In[3]:


n=int(input("Enter a range : "))

for i in range(2,):
    


# In[5]:


import math
int(math.sqrt(10))+1


# In[6]:


for i in range(2,10):
    print(i)


# In[36]:


n=int(input("Enter a range : "))

for i in range(2,n):
    print(i)


# In[28]:


for j in range(2,n):
    print(j)


# In[32]:


1%2


# In[33]:


2%2


# In[34]:


3%2


# In[35]:


0%2


# # 13. Python program to get the Fibonacci series between 0 to 50

# In[1]:


# Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones,usually starting with 0 and 1


# In[3]:


# 0,1,1,2,3,5,8,13,21,.........


# In[17]:


# 0, 1, 1(=0+1), 2(=1+1), 3(=1+2), 5(=2+3), 8(=3+5),.....................


# In[19]:


def fibonaaci(n):
    fib_series=[]
    a,b=0,1
    for i in range(n):
        if a>50:
            break
        else:
            fib_series.append(a)
            a,b=b,a+b
    return fib_series

fibonaaci(50)


# # 14. Python program to find the factorial of a given number.

# In[ ]:


# fact of 4 = 4*3*2*1


# In[24]:


n=6

for i in range(1,n+1):
    print(i)
    


# In[25]:


# fact of 0 = 1


# In[29]:


n=9
for i in range(n,0,-1):
    print(i)


# In[47]:


n=int(input("Enter a number: "))
fact=1

for i in range(n,0,-1):
    fact=fact*i
fact


# In[45]:


import math
math.factorial(5)


# # 15. Python program that accepts a string and calculates the number of digits and letters

# In[48]:


string=str(input("Enter a string: "))

for i in string:
    print(i)


# In[51]:


string=str(input("Enter a string: "))

letters=0
digits=0

for i in string:
    if i.isdigit(): 
        digits+=1
    elif i.isalpha():
        letters+=1
        
print(f"{string} has {digits} no.of digits and {letters} no.of letters")


# # 16. Write a Python program that iterates the integers from 1 to 25

# In[52]:


for i in range(1,26):
    print(i)


# # 17. Python program to check the validity of password input by users

# In[53]:


# It should be a minimum of 8 characters
# It should contain a mix of uppercase letters,lowercase letters,numbers, and special characters(such as !,@,#,$,etc)
# It shouldn't contain any spaces 


# In[5]:


password=input("Enter a password: ")

has_valid_length=False 
has_lower_case=False 
has_upper_case=False 
has_digits=False 
has_special_characters=False

if (len(password)>=8) and (len(password)<=16):
    has_valid_length=True  
    for i in password:
        if i.isupper():
            has_upper_case=True    
        if i.islower():
            has_lower_case=True
        if i.isdigit():
            has_digits=True
        if(i=="!" or i=="@" or i=="#" or i=="$" or i=="^" or i=="&" or i=="*"):
            has_special_characters=True

            
if (has_valid_length==True and has_upper_case==True and has_lower_case==True and has_digits==True and has_special_characters==True):
    print("Valid password")
else:
    print("Invalid password")


# # 18. Python program to convert the month name to a number of days

# In[7]:


month=["January","April","December","Moye"]

for i in month:
    if i=="February":
        print(f"{i} has 28/29 days")
    elif i in ("January","March","May","July","August","October","December"):
        print(f"{i} has 31 days")
    elif i in ("April","June","September","November"): 
        print(f"{i} has 30 days")
    else:
        print(f"{i} is incorrect name of month")
                    
            


# # while loop
# 
# 
# It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop is executed.
# 
# 
# 
# while expression:
# 
#     statement(s)
#     
#     
#     
#     
# while loop falls under the category of indefinite iteration. Indefinite iteration means that the number of times the loop is executed isn't specified explicitly in advance.
# 
# 

# # Difference between for loop and while loop
# 
# The main difference is that for loop is usually used when the number of iterations is known, whereas while loop is used when the number of iterations is unknown

# # Applications of loop:
#     
# 1.Iterating over data: Loops are used to traverse through lists,arrays,or other data structures to perform operations on each item
#     
# 2.Input validation: They can be used to validate user input until valid data is provided
#     
# 3.Automation: Loops are essential in automation tasks, like processing a large number of files or performing repetitive tasks
#     
# 4.Calculations: They help in performing calculations iteratively, such as summing a series of numbers or generating a sequence
#     
# 5.Game development: Loops are crucial for game development to update game states, handle user input, and simulate game worlds
#     
# 6.Control flow: Loops are used for control flow, such as executing a set of instructions until a specific condition is met or processing elements until reaching the end of a sequence
# 
# 7.User interfaces: They are used in graphical user interfaces(GUIs) to handle events and update interface elements based on user actions
# 
# 8.Simulation and modeling: Loops are used extensively in simulations and modeling to iterate through time steps and update simulation state

# In[1]:


# Real life application of loops:
    
# Whenever we go to any application then the format of displaying products is 'loops'


# # 1. Take 10 integers from user using loop and print their average value

# In[2]:


i=1

while i<11:     # when this condition becomes False , the loop ends
    print(i)
    i+=1        # This is necessary to write , otherwise the loop becomes infinite


# In[6]:


i=1
sum=0

while i<11:    
    print(i)
    i+=1
    sum=(sum+i)
print(f"The average is {sum/10}")

# 2. Print the following patterns using loop:

a.
*
**
***
****

b.
  *
 ***
*****
 ***
  *

c.
1010101
 10101
  101
   1
# In[5]:


# a.

i=1

while i<5:
    print('*'*i,end='')
    i+=1
    print()    


# In[10]:


# b.

num=3

row=0
i=1
while row<num: 
    spaces=(num-row-1)
    while spaces>0:
        print(' ',end='')
        spaces-=1
    star=(row+i)
    while star>0:
        print('*',end='')
        star-=1
    i+=1
    row+=1
    print()


# In[12]:


num=3

row=0
i=0
while row<num: 
    spaces=row
    while spaces>0:
        print(' ',end='')
        spaces-=1
    star=(num-row-i)
    while star>0:
        print('*',end='')
        star-=1
    i+=1
    row+=1
    print()


# In[14]:


num=3

row=0
i=1
while row<num: 
    spaces=(num-row-1)
    while spaces>0:
        print(' ',end='')
        spaces-=1
    star=(row+i)
    while star>0:
        print('*',end='')
        star-=1
    i+=1
    row+=1
    print()
    
row=0
i=0
while row<num: 
    spaces=row+1
    while spaces>0:
        print(' ',end='')
        spaces-=1
    star=(num-row-i)
    while star>0:
        print('*',end='')
        star-=1
    i+=1
    row+=1
    print()


# In[18]:


# c.

num=7

row=0
i=0
while row<num: 
    spaces=row
    while spaces>0:
        print(' ',end='')
        spaces-=1
    star=(num-row-i)
    j=0
    while star>0:
        if j%2==0:  
            print('1',end='')
        else:
            print('0',end='')
        star-=1
        j+=1
    i+=1
    row+=1
    print()


# # 3. Print multiplication table of 24, 50 and 29 using loop.

# In[25]:


num=int(input("Enter a number : "))
i=1

while i<=10:
    result=num*i
    print(f'{num} * {i} = {result}')
    i+=1


# In[26]:


num=int(input("Enter a number : "))
i=1

while i<=10:
    result=num*i
    print(f'{num} * {i} = {result}')
    i+=1


# In[27]:


num=int(input("Enter a number : "))
i=1

while i<=10:
    result=num*i
    print(f'{num} * {i} = {result}')
    i+=1


# # 4. Write an infinite loop.
# A infinite loop never ends. Condition is always true.
# 
# Answer:
# 
# while True:
# 
#     print("Infinte")

# # 5.Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. 
# E.g.-
# 
# 4! = 1*2*3*4 = 24
# 
# 3! = 3*2*1 = 6
# 
# 2! = 2*1 = 2
# 
# Also,
# 
# 1! = 1
# 
# 0! = 1
# 
# Write a program to calculate factorial of a number.

# In[4]:


num=int(input("Enter a number : "))
fact=1

while num>=1:
    fact=fact*num
    num-=1
print(fact)


# # 6. Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
# 
# Example;
# 
# a=48 , b=18
# 
# First iteration; a=18, b=48%18=12
# 
# Second iteration; a=12, b=18%12=6
# 
# Third iteration; a=6, b=12%6=0
# 
# The loop exits and the GCD is a = 6

# In[9]:


x=int(input("Enter first number : "))
y=int(input("Enter second number : "))

def gcd(x,y):    
    while y!=0:
        x,y=y,x%y
    return x

print(f"The HCF/GCD of {x} and {y} is {gcd(x,y)}")


# # 7. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

# In[4]:


def main():
    numbers=[]
    product=1
    
    while True:
        user_input=input("Enter any integer and enter 'q' to 'quit' : ")
        if user_input.lower()=='q':
            break
        try:
            num=int(user_input)
            numbers.append(num)
            product=product*num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
        if numbers:
            average=sum(numbers)/len(numbers)
            print(f"The average of {numbers} is {average}")
            print(f"The product of {numbers} is {product}")
        else:
            print("No numbers were entered")
            
if __name__=="__main__":
    main() 


# # 8. Calculate the sum of digits of a number given by user. E.g.-
# 
# INUPT : 123        OUPUT : 6
#         
# INUPT : 12345        OUPUT : 15
# 

# In[14]:


num=int(input("Enter a number : "))
power=len(str(num))
power    


# In[15]:


(153%1000)//100


# In[16]:


(153%100)//10


# In[17]:


(153%10)//1


# In[18]:


num=153
power=3

for i in range(1,power+1):
    x=(num%(10**i))//(10**(i-1))
    print(x)


# In[27]:


num=int(input("Enter any number : "))
power=len(str(num))

i=1

while i<=power:
    x=((num%(10**i))//(10**(i-1)))
    print(x)
    i+=1    


# In[30]:


num=int(input("Enter any number : "))
power=len(str(num))
sum=0
i=1

while i<=power:
    x=((num%(10**i))//(10**(i-1)))
    sum=sum+x
    i+=1 
print(sum)


# # 9. A three digit number is called Armstrong number if sum of cube of its digit is equal to number itself.
# 
# E.g.- 153 is an Armstrong number because (13)+(53)+(33) = 153.
# 
# Write all Armstrong numbers between 100 to 500

# In[31]:


num=int(input("Enter any number : "))
power=len(str(num))

i=1

while i<=power:
    x=((num%(10**i))//(10**(i-1)))
    print(x)
    i+=1  


# In[32]:


num=int(input("Enter any number : "))
power=len(str(num))

i=1

while i<=power:
    x=((num%(10**i))//(10**(i-1)))**power
    print(x)
    i+=1  


# In[37]:


num=int(input("Enter any number : "))
power=len(str(num))
sum=0
i=1

while i<=power:
    x=((num%(10**i))//(10**(i-1)))**power
    sum=sum+x
    i+=1
print(sum)


# In[36]:


num=int(input("Enter any number : "))
power=len(str(num))
sum=0
i=1

while i<=power:
    x=((num%(10**i))//(10**(i-1)))**power
    sum=sum+x
    i+=1
    
if sum==num:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")


# # 10. Write a program to print a number given by user but digits reversed. E.g.-
# 
# INPUT : 123        OUTPUT : 321
#         
# INPUT : 12345        OUTPUT : 54321

# In[38]:


num=int(input("Enter any number : "))
power=len(str(num))

i=1

while i<=power:
    x=((num%(10**i))//(10**(i-1)))
    print(x)
    i+=1  


# In[3]:


num=int(input("Enter any number : "))
power=len(str(num))
reverse=[]
i=1

while i<=power:
    x=((num%(10**i))//(10**(i-1)))
    reverse.append(x)
    i+=1
print(reverse)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Solve any star pattern question in Python ( Using for loop ) 

# In[2]:


# putting together nested loops

n=5
print('*'*n)      # for printing n no.of stars


# In[3]:


n=5

for j in range(n):
    print('*')


# In[5]:


# but we wan't this in same line, not in newline

n=5
for j in range(n):
    print('*',end=' ')


# In[6]:


# Now we want this row , 5 times , to get a square pattern


# In[7]:


n=5

for i in range(n):
    for j in range(n):
        print('*',end='')


# In[8]:


n=5

for i in range(n):
    for j in range(n):
        print('*')


# In[10]:


n=5

for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()


# In[12]:


# Increasing triangle pattern
# i=0   *           -------> 0+1 = i+1
# i=1   * *         -------> 1+1 = i+1
# i=2   * * *       -------> 2+1 = i+1
# i=3   * * * *     -------> 3+1 = i+1
# i=4   * * * * *    ------> 4+1 = i+1


# In[16]:


# So the code is quite correct

n=5
for i in range(n):             # ---------> row number
    for j in range(i+1):       # ---------> column number
        print('*',end=' ')
    print()


# In[18]:


# Decreasing triangle pattern

# (0 to 5) * * * * *
# (1 to 5) * * * *
# (2 to 5) * * *
# (3 to 5) * *
# (4 to 5) *


# In[19]:


n=5
for i in range(n):             # ---------> row number
    for j in range(i,n):       # ---------> column number
        print('*',end=' ')
    print()


# In[25]:


# Right sided triangle (increasing)
#            *
#          * *
#        * * *
#      * * * *
#    * * * * *

# 1. decreasing space
# 2. increasing star


# In[50]:


n=5

for i in range(n):    
    for j in range(i,n):
        print(' ',end='')    
    for j in range(i+1):
        print('*',end='')   
    print()


# In[52]:


# Right sided triangle (decreasing)

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# 1. increasing space
# 2. decreasing star


# In[53]:


n=5

for i in range(n):
    
    for j in range(i+1):
        print(' ',end='')
        
    for j in range(i,n):
        print('*',end='')
        
    print()


# In[54]:


# Hill pattern

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# 1. decreasing space 
# 2. increasing star
# 3. increasing star


# In[58]:


n=5

for i in range(n):
    
    for j in range(i,n):
        print(' ',end='')
    
    for j in range(i):
        print('*',end='')
    
    for j in range(i+1):
        print('*',end='')
    
    print()


# In[59]:


# Reverse Hill pattern

# * * * * * * * * *
#  * * * * * * *
#    * * * * *
#      * * *
#        *

# 1. Increasing space
# 2. Decreasing star
# 3. Decreasing star 


# In[64]:


n=5

for i in range(n):
    
    for j in range(i):
        print(' ',end='')
        
    for j in range(i,n-1):
        print('*',end='')
        
    for j in range(i,n):
        print('*',end='')
        
    print()


# In[65]:


# Diamond pattern


# In[71]:


n=5

for i in range(n):
    
    for j in range(i,n):
        print(' ',end='')
    
    for j in range(i):
        print('*',end='')
    
    for j in range(i+1):
        print('*',end='')
    print()
        
for i in range(n):
    
    for j in range(i+1):
        print(' ',end='')
        
    for j in range(i,n-1):
        print('*',end='')
        
    for j in range(i,n):
        print('*',end='')
        
    print()
    


# In[72]:


n=5

for i in range(n-1):    # change this
    
    for j in range(i,n):
        print(' ',end='')
    
    for j in range(i):
        print('*',end='')
    
    for j in range(i+1):
        print('*',end='')
    print()
        
for i in range(n):
    
    for j in range(i+1):
        print(' ',end='')
        
    for j in range(i,n-1):
        print('*',end='')
        
    for j in range(i,n):
        print('*',end='')
        
    print()
    


# In[1]:


# Double hill


# In[38]:


n=5

for i in range(n):
    
    for j in range(i,n-1):
        print(' ',end='')
        
    for j in range(i-1):
        print('*',end='')
          
    for j in range(i):
        print('*',end='')
    
    print()
    


# In[44]:


n=5

for i in range(n):
    
    for j in range(i,n):
        print(' ',end='')
        
    for j in range(i):
        print('*',end='')
          
    for j in range(i+1):
        print('*',end='')
   
    for j in range(i,n-1):
        print(' ',end='')
        
    for j in range(i,n-1):
        print(' ',end='')
        
    for j in range(i+1):
        print('*',end='')
        
    for j in range(i):
        print('*',end='')
    
    print()


# In[46]:


# Butterfly


# In[19]:


def butterfly_pattern(rows):
    
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print('*',end='')
        for j in range(1,(2*rows-2*i)+1):
            print(" ",end='')
        for j in range(1,i+1):
            print('*',end='')
        print()
        
butterfly_pattern(5)                                                                                                                                                                     


# In[25]:


def butterfly_pattern(rows):
    
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print('*',end='')
        for j in range(1,(2*rows-2*i)+1):
            print(" ",end='')
        for j in range(1,i+1):
            print('*',end='')
        print()
        
        
    for i in range(rows-1,0,-1):
        for j in range(1,i+1):
            print('*',end='')
        for j in range(1,(2*rows-2*i)+1):
            print(' ',end='')
        for j in range(1,i+1):
            print('*',end='')
        print()
        
butterfly_pattern(5) 


# In[12]:


# sandglass


# In[23]:


n=5

for i in range(n):
    
    for j in range(i):
        print(' ',end='')
        
    for j in range(i,n-1):
        print('*',end='')
        
    for j in range(i,n):
        print('*',end='')
        
    print()


# In[24]:


n=5

for i in range(n):
    
    for j in range(i,n):
        print(' ',end='')
    
    for j in range(i):
        print('*',end='')
    
    for j in range(i+1):
        print('*',end='')
    
    print()


# In[41]:


n=5

for i in range(n-1):  # 
    
    for j in range(i):
        print(' ',end='')
        
    for j in range(i,n-1):
        print('*',end='')
        
    for j in range(i,n):
        print('*',end='')
        
    print()
    
for i in range(n):
    
    for j in range(i,n-1):  #
        print(' ',end='')
    
    for j in range(i):
        print('*',end='')
    
    for j in range(i+1):
        print('*',end='')
    
    print()


# In[42]:


# Left pascal's triangle


# In[47]:


n=5

for i in range(n):
    for j in range(i):
        print('*',end='')
    print()                   # increasing triangle


# In[51]:


n=5

for i in range(n):
    for j in range(i,n):
        print('*',end='')
    print()                   # decreasing triangle


# In[53]:


n=5

for i in range(n):
    for j in range(i):
        print('*',end='')
    print()                   # increasing triangle
    
for i in range(n):
    for j in range(i,n):
        print('*',end='')
    print()                   # decreasing triangle
    
# combining increasing and decreasing triangle we get Left pascal's triangle


# In[54]:


# Right pascal's triangle


# In[55]:


n=5

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()                   # right sided triangle(increasing)


# In[58]:


n=5

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    print()                   # right sided triangle(decreasing)
    


# In[60]:


n=5

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()
    
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    print()
# combining right sided triangle(increasing) and right sided triangle(decreasing) we get Right pascal's triangle    


# # Solve any number pattern program in Python ( Using for loop )

# In[2]:


# Do not mix code for number and pattern 
# Pattern + Number


# In[7]:


# <1>


# In[8]:


n=5

for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()


# In[9]:


n=5

for i in range(n):
    for j in range(i+1):
        print('1',end='')
    print()


# In[11]:


# <2>

# Increasing triangle
# Incrementing rows


# In[12]:


n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end='')
    p+=1
    print()


# In[13]:


# <2>

# Increasing triangle
# Decrementing rows


# In[14]:


n=5
p=5
for i in range(n):
    for j in range(i+1):
        print(p,end='')
    p-=1
    print()


# In[15]:


# <3>

# Increasing triangle
# Incrementing rows by 2


# In[16]:


n=5
p=0
for i in range(n):
    for j in range(i+1):
        print(p,end='')
    p+=2
    print()


# In[17]:


# <4>


# In[18]:


n=5

for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print('1',end='')
        else:
            print('2',end='')
    print()


# In[19]:


# <5>

# Diamond pattern
# Incrementing rows


# In[26]:


n=5

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()


# In[27]:


n=5

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()


# In[29]:


n=5

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    print()


# In[35]:


n=5

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    for j in range(i+1,n):
        print('*',end='')
    print()


# In[42]:


n=5

for i in range(n-1):   #
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()
    
for i in range(n):
    for j in range(i+1):   # 
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    for j in range(i+1,n):
        print('*',end='')
    print()


# In[50]:


n=5
p=1
for i in range(n-1):    #
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(p,end='')
    for j in range(i+1):
        print(p,end='')
    p+=1
    print()
    
for i in range(n):
    for j in range(i+1):       # 
        print(' ',end='')
    for j in range(i,n):
        print(p,end='')
    for j in range(i+1,n):
        print(p,end='')
    p+=1
    print()


# In[51]:


# <6>


# In[52]:


n=5
p=1

for i in range(n-1):          #
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(p,end='')
    for j in range(i+1):
        print(p,end='')
    p+=1
    print()
    
for i in range(n):
    for j in range(i+1):       # 
        print(' ',end='')
    for j in range(i,n):
        print(p,end='')
    for j in range(i+1,n):
        print(p,end='')
    p-=1
    print()                


# In[57]:


# <7>
# Pattern : Increasing triangle
# Number : Incrementing columns

# Pattern : change in column numbers


# In[58]:


n=5

for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()


# In[61]:


n=5

for i in range(n):      # ----------> rows
    p=1
    for j in range(i+1):    # ------------> columns
        print(p,end='')
        p+=1
    print()


# In[1]:


# <8>

# Pattern: Decreasing triangle 
# Number : Decrementing columns


# In[3]:


n=5

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    print()


# In[10]:


n=5

for i in range(n):           # ----------> rows
    p=1
    for j in range(i):       # ------------> columns
        print(' ',end='')
    for j in range(i,n):
        print(p,end='')
        p+=1
    print()


# In[11]:


# <9>

# Pattern: Hill triangle
# number: incrementing columns


# In[14]:


n=5

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()


# In[21]:


n=5

for i in range(n):
    p=1
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(p,end='')
        p+=1
    for j in range(i+1):
        print(p,end='')
        p+=1
    print()


# In[27]:


# <10>

# Pattern: Increasing triangle
# Number : Decrementing columns


# In[28]:


n=5

for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()


# In[30]:


n=5


for i in range(n):           # ----------> rows
    p=5
    for j in range(i+1):     # ------------> columns
        print(p,end='')
        p-=1
    print()


# In[31]:


# <11>

# Pattern: Decrementing triangle
# Number: Decrementing columns


# In[32]:


n=5

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    print()


# In[33]:


n=5

for i in range(n):
    p=5
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print(p,end='')
        p-=1
    print()


# In[34]:


# <12>

# Pattern: Hill triangle
# Number: Increasing and decreasing columns


# In[42]:


n=5

for i in range(n):      
    p=1
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(p,end='')
        p+=1
    for j in range(i+1):
        print('*',end='')
    print()


# In[43]:


n=5

for i in range(n):             # ----------> rows
    p=1
    for j in range(i,n):       # ------------> columns
        print(' ',end='')
    for j in range(i):
        print(p,end='')
        p+=1
    for j in range(i+1):
        print(p,end='')
        p-=1
    print()


# In[44]:


# <13>

# Floyd triangle

# Pattern: Increasing triangle
# Number : Increasing number


# In[46]:


n=5

for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()


# In[49]:


n=5
p=1
for i in range(n):             # ----------> rows
    for j in range(i):         # ------------> columns
        print(p,end='')
        p+=1
    print()


# In[50]:


# <14>

# Diamond 🔹 pattern


# In[58]:


n=5

for i in range(n-1):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()


# In[57]:


n=5

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i+1,n):
        print('*',end='')
    for j in range(i,n):
        print('*',end='')
    print()


# In[60]:


n=5

for i in range(n-1):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()
    
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i+1,n):
        print('*',end='')
    for j in range(i,n):
        print('*',end='')
    print()


# In[63]:


n=5

for i in range(n-1):
    p=1
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(p,end='')
        p+=1
    for j in range(i+1):
        print('*',end='')
    print()
    
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i+1,n):
        print('*',end='')
    for j in range(i,n):
        print('*',end='')
    print()


# In[62]:


n=5

for i in range(n-1):
    p=1
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(p,end='')
        p+=1
    for j in range(i+1):
        print(p,end='')
        p+=1
    print()
    
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i+1,n):
        print('*',end='')
    for j in range(i,n):
        print('*',end='')
    print()


# In[65]:


n=5

for i in range(n-1):
    p=1
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(p,end='')
        p+=1
    for j in range(i+1):
        print(p,end='')
        p+=1
    print()
    
for i in range(n):
    p=1
    for j in range(i+1):
        print(' ',end='')
    for j in range(i+1,n):
        print(p,end='')
        p+=1
    for j in range(i,n):
        print(p,end='')
        p+=1
    print()


# In[67]:


# <15>

# Butterfly  


# In[6]:


rows=5

for i in range(1,rows+1):
        for j in range(1,i+1):
            print('*',end='')
        for j in range(1,(2*rows-2*i)+1):
            print(" ",end='')
        for j in range(1,i+1):
            print('*',end='')
        print()
        
        
for i in range(rows-1,0,-1):
    for j in range(1,i+1):
        print('*',end='')
    for j in range(1,(2*rows-2*i)+1):
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end='')
    print()
        


# In[13]:


rows=5

for i in range(1,rows+1):
    p=1
    for j in range(1,i+1):
        print(p,end='')
        p+=1
        
    for j in range(1,(2*rows-2*i)+1):
        print(" ",end='')
        
    p=1
    for j in range(1,i+1):
        print(p,end='')
        p+=1
    print()
        
        
for i in range(rows-1,0,-1):
    p=1
    for j in range(1,i+1):
        print(p,end='')
        p+=1
    for j in range(1,(2*rows-2*i)+1):
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end='')
    print()


# In[15]:


rows=5

for i in range(1,rows+1):
    p=1
    for j in range(1,i+1):
        print(p,end='')
        p+=1
        
    for j in range(1,(2*rows-2*i)+1):
        print(" ",end='')
        
    p=1
    for j in range(1,i+1):
        print(p,end='')
        p+=1
    print()
        
        
for i in range(rows-1,0,-1):
    p=1
    for j in range(1,i+1):
        print(p,end='')
        p+=1
        
    for j in range(1,(2*rows-2*i)+1):
        print(' ',end='')
        
    p=1
    for j in range(1,i+1):
        print(p,end='')
        p+=1
    print()


# In[16]:


# <16>

# pattern: Decreasing triangle
# number: Decrementing columns


# n=5   54321
# n-1    4321
# n-2     321
# n-3      21
# n-4       1


# In[17]:


n=5

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    print()


# In[19]:


n=5

for i in range(n):
    for j in range(i):
        print(' ',end='')
    p=5
    for j in range(i,n):
        print(p,end='')
        p-=1
    print()


# In[20]:


n=5
k=5

for i in range(n):       # ---------> rows
    p=k
    for j in range(i):   # ----------> columns
        print(' ',end='')
    for j in range(i,n):
        print(p,end='')
        p-=1
    k-=1
    print()


# In[21]:


# <17>

# pattern: Hill triangle
# number: increasing and decreasing column


# In[23]:


n=5

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()


# In[26]:


n=5

for i in range(n):
    
    for j in range(i,n):
        print(' ',end='')
        
    p=1
    for j in range(i):
        print(p,end='')
        p+=1
    
    
    for j in range(i+1):
        print(p,end='')
        p-=1
    print()


# # Solve any character pattern in Python ( Using for loop )

# In[3]:


# <1> 

# Pattern: Increasing triangle
# Character: A's


# In[4]:


n=5

for i in range(n):
    
    for j in range(i+1):
        print('A',end='')
    print()


# In[5]:


# <2>

# Pattern: Increasing triangle
# Character: Incrementing rows


# In[8]:


n=5
p=65                       # asci value for 'A'

for i in range(n):
    for j in range(i+1):
        print(chr(p),end='')
    p+=1
    print()


# In[1]:


# <3>

# pattern: Left traingle 
# character: Incrementing rows


# In[7]:


n=5
p=65

for i in range(n):   # ------> rows
    for j in range(i):     # ------>columns 
        print(' ',end='')
    for j in range(i,n):
        print(chr(p),end='')
    p+=1
    print()    


# In[9]:


# <4>

# pattern: Hill pattern
# character: Incrementing rows


# In[11]:


n=5
p=65

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(chr(p),end='')
    for j in range(i+1):
        print(chr(p),end='')
    p+=1
    print()


# In[12]:


# <5>

# pattern: Reverse Hill pattern
# character: Incrementing rows


# In[16]:


n=5
p=65

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print(chr(p),end='')
    for j in range(i,n-1):
        print(chr(p),end='')
    p+=1
    print()


# In[1]:


# <6>

# pattern: Increasing triangle
# character: Decrementing rows


# In[2]:


n=5
p=69

for i in range(n):
    for j in range(i+1):
        print(chr(p),end='')
    p-=1
    print()
        


# In[3]:


# <7>

# pattern: Left triangle
# character: Decrementing rows


# In[5]:


n=5
p=69

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print(chr(p),end='')
    p-=1
    print()
        


# In[6]:


# <8>

# pattern: Hill pattern
# character: Decrementing rows


# In[8]:


n=5
p=69

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(chr(p),end='')
    for j in range(i+1):
        print(chr(p),end='')
    p-=1
    print()


# In[9]:


# <9>

# pattern:Reverse Hill pattern
# character: Decrementing rows


# In[11]:


n=5
p=69

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print(chr(p),end='')
    for j in range(i,n-1):
        print(chr(p),end='')
    p-=1
    print()


# In[12]:


# <10>

# pattern:Increasing triangle
# character: Rows incrementing by 2


# In[15]:


n=5
p=65

for i in range(n):
    for j in range(i+1):
        print(chr(p),end='')
    p+=2
    print()


# In[16]:


# <11>

# pattern:Right triangle
# character: Rows odd = A and Even= B


# In[17]:


n=5

for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print('A',end='')
        else:
            print('B',end='')
    print()


# In[1]:


# <12>

# pattern: Left triangle
# character: Rows odd = Z and Even = 0


# In[2]:


n=5

for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n):
        if i%2==0:
            print('Z',end='')
        else:
            print('0',end='')
    print()


# In[3]:


# <13>

# pattern: Hill pattern
# character: Rows odd = A and Even = #


# In[5]:


n=5

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        if i%2==0: 
            print('A',end='')
        else:
            print('#',end='')
    for j in range(i+1):
        if i%2==0:   
            print('A',end='')
        else:
            print('#',end='')
    print()


# In[6]:


# <14>

# pattern:Reverse Hill pattern
# character: Rows odd = Z and Even = 0


# In[8]:


n=5

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        if i%2==0:
            print('Z',end='')
        else:
            print('0',end='')
    for j in range(i,n-1):
        if i%2==0:    
            print('Z',end='')
        else:
            print('0',end='')
    print()


# In[9]:


# <15>

# pattern: Diamond
# character: incrementing rows


# In[10]:


n=5
p=65

for i in range(n-1):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(chr(p),end='')
    for j in range(i+1):
        print(chr(p),end='')
    p+=1
    print()
    
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i+1,n):
        print(chr(p),end='')
    for j in range(i,n):
        print(chr(p),end='')
    p+=1
    print()


# In[11]:


# <16>

# pattern: Butterfly
# character: incrementing rows


# In[12]:


rows=5
p=65

for i in range(1,rows+1):
        for j in range(1,i+1):
            print(chr(p),end='')
        for j in range(1,(2*rows-2*i)+1):
            print(" ",end='')
        for j in range(1,i+1):
            print(chr(p),end='')
        p+=1
        print()
        
        
for i in range(rows-1,0,-1):
    for j in range(1,i+1):
        print(chr(p),end='')
    for j in range(1,(2*rows-2*i)+1):
        print(' ',end='')
    for j in range(1,i+1):
        print(chr(p),end='')
    p+=1
    print()
        


# In[13]:


# <17>

# pattern: Diamond
# character: incrementing rows and decrementing rows


# In[14]:


n=5
p=65

for i in range(n-1):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(chr(p),end='')
    for j in range(i+1):
        print(chr(p),end='')
    p+=1
    print()
    
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i+1,n):
        print(chr(p),end='')
    for j in range(i,n):
        print(chr(p),end='')
    p-=1
    print()


# In[15]:


# <18>

# pattern: Right triangle
# character: change in column characters


# In[5]:


n=5


for i in range(n):              # --------> rows
    p=65
    for j in range(i+1):        # --------> columns
        print(chr(p),end='')
        p+=1
    
    print()


# In[6]:


# <19>

# pattern:Left triangle 
# character:change in column characters


# In[8]:


n=5

for i in range(n):
    p=65
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print(chr(p),end='')
        p+=1
    print()


# In[1]:


# <20>

# pattern: Hill pattern
# character: Incrementing columns


# In[3]:


n=5

for i in range(n):              # rows
    p=65
    for j in range(i,n):        # columns
        print(' ',end='')
    for j in range(i):
        print(chr(p),end='')
        p+=1
    for j in range(i+1):
        print(chr(p),end='')
        p+=1
    print()


# In[4]:


# <21>

# pattern: Diamond
# character: Incrementing columns


# In[6]:


n=5

for i in range(n-1):
    p=65
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(chr(p),end='')
        p+=1
    for j in range(i+1):
        print(chr(p),end='')
        p+=1
    print()
    
for i in range(n):
    p=65
    for j in range(i+1):
        print(' ',end='')
    for j in range(i+1,n):
        print(chr(p),end='')
        p+=1
    for j in range(i,n):
        print(chr(p),end='')
        p+=1
    print()


# In[7]:


# <22>       

# pattern: Butterfly
# character: Incrementing columns


# In[15]:


rows=5     ######
    
for i in range(1,rows+1):
    p=65
    for j in range(1,i+1):
        print(chr(p),end='')
        p+=1
    for j in range(1,(2*rows-2*i)+1):
        print(" ",end='')
    for j in range(1,i+1):
        print(chr(p),end='')
        p+=1
    print()
        
        
for i in range(rows-1,0,-1):
    p=65
    for j in range(1,i+1):
        print(chr(p),end='')
        p+=1
    for j in range(1,(2*rows-2*i)+1):
        print(' ',end='')
    for j in range(1,i+1):
        print(chr(p),end='')
        p+=1
    print()


# In[16]:


# <23>

# pattern:  Right triangle
# character: Starting character is same


# In[18]:


n=5

for i in range(n):
    p=69
    for j in range(i+1):
        print(chr(p),end='')
        p-=1
    print()


# In[19]:


# <24>

# pattern: Left triangle
# character:Ending character is same 


# In[27]:


n=5
k=69

for i in range(n):
    p=k
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print(chr(p),end='')
        p-=1
    k-=1
    print()


# In[28]:


# <25>

# pattern: Hill pattern
# character:Ending character is same 


# In[43]:


n=5

for i in range(n):
    p=65
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(chr(p),end='')
        p+=1
    for j in range(i+1):
        print(chr(p),end='')
        p-=1
    
    print()


# In[44]:


# <26>

# pattern: Right triangle
# character: Form a pattern with specific word CODER 


# In[1]:


s="CODER"
n=len(s)
p=0

for i in range(n):
    for j in range(i+1):
        print(s[p],end='')
    p+=1
    print()


# In[2]:


# <27>

# pattern: Left triangle
# character: Form a pattern with specific word CODER


# In[3]:


s="CODER"
n=len(s)
p=0

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print(s[p],end='')
    p+=1
    print()


# In[4]:


# <28>

# pattern: Hill pattern
# character: Form a pattern with specific word CODER


# In[5]:


s="CODER"
n=len(s)
p=0

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(s[p],end='')
    for j in range(i+1):
        print(s[p],end='')
    p+=1
    print()


# In[6]:


# <29>

# pattern: Right triangle
# character: Form a pattern with specific word CODER 


# In[8]:


s="CODER"
n=len(s)
p=n-1

for i in range(n):
    for j in range(i+1):
        print(s[p],end='')
    p-=1
    print()


# In[9]:


# <30>

# pattern: Left triangle
# character: Form a pattern with specific word CODER


# In[10]:


s="CODER"
n=len(s)
p=n-1

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print(s[p],end='')
    p-=1
    print()


# In[11]:


# <31>

# pattern: Hill pattern
# character: Form a pattern with specific word CODER


# In[13]:


s="CODER"
n=len(s)
p=n-1

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(s[p],end='')
    for j in range(i+1):
        print(s[p],end='')
    p-=1
    print()


# In[14]:


# <32>

# pattern: Right triangle
# character: Form a pattern with specific word CODER 


# In[17]:


s="CODER"
n=len(s)

for i in range(n):                 # rows
    p=0
    for j in range(i+1):           # columns
        print(s[p],end='')
        p+=1
    print()


# In[18]:


# <33>

# pattern: Left triangle
# character: Form a pattern with specific word CODER


# In[19]:


s="CODER"
n=len(s)

for i in range(n):
    p=0
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print(s[p],end='')
        p+=1
    print()


# In[20]:


# <34>

# pattern: Right triangle
# character: Form a pattern with specific word CODER (Starting character is same)


# In[21]:


s="CODER"
n=len(s)

for i in range(n):                 # rows
    p=n-1
    for j in range(i+1):           # columns
        print(s[p],end='')
        p-=1
    print()


# In[22]:


# <35>

# pattern: Left triangle
# character: Form a pattern with specific word CODER (Ending character is same)


# In[7]:


s="CODER"
n=len(s)
k=n-1

for i in range(n):             # rows
    p=k
    for j in range(i):         # columns
        print(' ',end='')
    for j in range(i,n):
        print(s[p],end='')
        p-=1
    k-=1
    print()


# # Star pattern program ( Using while loop )

# In[2]:


num=int(input("Enter a number : "))

row=0

while row<num:
    spaces=num-row-1
    while spaces>0:
        print(' ',end='')
        spaces-=1
    star=row+1
    while star>0:
        print('*',end=' ')
        star-=1
    row+=1
    print()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              


# In[ ]:




