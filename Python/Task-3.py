#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''1 secret diary
• Ask the user to enter today's memory.
• Append it to diary.txt.
• Read the entire file and display all saved memories.
'''
with open('diary.txt','a+') as file:
    today_memory=input("\n")
    file.write(today_memory+"\n")
    file.seek(0)
    context=file.read()
print(context)


# In[2]:


'''2 class attendance
• Read the file.
• Count how many students attended the class.
• Display the total attendance.
'''
with open('attendance.txt','r') as file:
    count=0
    for line in file:
        count+=1
print("total attendance:",count)


# In[3]:


'''3 shopping history
• Read all the items from the file.
• Display each item.
• Count and display the total number of orders placed.
'''
with open('orders.txt','a+') as file:
    count=0
    item=input("")
    file.write(item+"\n")
    file.seek(0)
    context=file.readlines()
    for line in context:
        print(line)
        count+=1
print("total no of orders:",count)


# In[4]:


'''4 password inspector
• Count the number of uppercase letters.
• Count the number of lowercase letters.
• Count the number of digits.
•Display whether the password is Strong
(at least 8 characters and contains uppercase, lowercase, and digits) or Weak.
'''
pwd=input("")
u=l=d=0
for ch in pwd:
    if ch.isupper():
        u+=1
    elif ch.islower():
        l+=1
    elif ch.isdigit():
        d+=1
print("no of uppercase letters:",u)
print("no of lowercase letters:",l)
print("no of digits :",d)
if len(pwd)>=8 and u>=1 and l>=1 and d>=1:
    print("strong")
else:
    print("weak")


# In[5]:


'''5 chat message analyzer
• Count how many times the word Python appears.
• Convert the message to uppercase.
• Replace Powerful with Amazing.
• Display the modified message.
'''
msg=input("")
print(msg.count("Python"))
print(msg.upper())
print(msg.replace("Powerful","Amazing"))


# In[6]:


'''6 flight ticket
• Convert it to title case.
• Remove any extra spaces.
• Display the cleaned city name.
'''
city=input("")
city=city.strip()
city=city.title()
print(city)


# In[7]:


'''7 atm withdrawal
• Check whether sufficient balance is available.
• Return the remaining balance after withdrawal.
• If the balance is insufficient, return an appropriate message.
'''
def withdraw(balance,amount):
    if balance>=amount:
        return balance-amount
    else:
        print("Insufficient balance")
withdraw(1000,1500)


# In[9]:


#8 grade calculator
#Create a function named:
#calculate_grade(mark)
#Grade Rules
#•90+ → A
#•75–89 → B
#•60–74 → C
#•Below 60 → F

def calculate_grade(marks):
    if marks>=90:
        print("A")
    elif 89<=marks or marks>=75:
        print("B")
    elif 74<=marks or marks>=60:
        print("C")
    else:
        print("F")
calculate_grade(61)


# In[10]:


'''9 bill calculator
Create a function:
calculate_bill(price, quantity)
The function should:
• Calculate the total amount.
• Return the final bill.
• Display the result in a user-friendly format.
'''
def calculate_bill(price,quantity):
    total=0
    total+=price*quantity
    print(f"The total amount of each price {price} of quantity {quantity} is {total}")
calculate_bill(20,2)


# In[11]:


#10 discount calculator
#Create a lambda function that calculates 10% discount on a product price.
price=lambda a:(a)*(0.9)
print(int(price(1500)))


# In[12]:


#11 rectangle area
#Create a lambda function to calculate the area of a rectangle.
area=lambda l,b:l*b
print(area(10,5))


# In[13]:


'''12 speed checker
Create a lambda function that returns:
•
"Overspeed" if speed is greater than 80.
•
"Normal Speed" otherwise.
'''
speed=lambda x: "Overspeed" if x>80 else "Normal speed" 
print(speed(90))


# In[ ]:




