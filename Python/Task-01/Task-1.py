#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Problem 1 – Gaming Tournament
scores = [520, 780, 430]
players = ["Player1", "Player2", "Player3"]

if len(set(scores)) != len(scores):
    print("Tie Detected")
else:
    temp_scores = scores[:]
    temp_players = players[:]

    for i in range(len(temp_scores)):
        max_index = i
        for j in range(i + 1, len(temp_scores)):
            if temp_scores[j] > temp_scores[max_index]:
                max_index = j
        temp_scores[i], temp_scores[max_index] = temp_scores[max_index], temp_scores[i]
        temp_players[i], temp_players[max_index] = temp_players[max_index], temp_players[i]

    print("First Rank :", temp_players[0], temp_scores[0])
    print("Second Rank:", temp_players[1], temp_scores[1])
    print("Third Rank :", temp_players[2], temp_scores[2])


# In[2]:


# Problem 2 – Pizza Party
orders = ["Veg","Paneer","Veg","Cheese","Paneer","Veg"]
unique = set(orders)
print(unique)
print("Unique pizzas:", len(unique))


# In[3]:


# Problem 3 – ATM Machine
balance = 15000
withdraw = 7000

if withdraw < 0:
    print("Invalid Amount")
elif withdraw <= balance:
    balance -= withdraw
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")


# In[4]:


# Problem 4 – Scholarship Selection
marks = [96,81,55,74,67,92]
for mark in marks:
    if mark >= 90:
        print(mark, "Full Scholarship")
    elif mark >= 75:
        print(mark, "Half Scholarship")
    elif mark >= 60:
        print(mark, "Training Program")
    else:
        print(mark, "Better Luck Next Time")


# In[5]:


# Problem 5 – Traffic Signal
signal = "Green"

if signal == "Red":
    print("STOP")
elif signal == "Yellow":
    print("READY")
elif signal == "Green":
    print("GO")
else:
    print("Signal Error")


# In[6]:


# Problem 6 – Shopping Cart
prices = [250,180,450,120,600]
total = 0
highest = prices[0]
lowest = prices[0]
for p in prices:
    total += p
    if p > highest:
        highest = p
    if p < lowest:
        lowest = p

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)


# In[8]:


# Problem 7 – Movie Ticket Checker

cases = [(16, True),(20, False),(22, True)]
for age, ticket in cases:
    
    if age >= 18 and ticket:
        print("Entry Allowed")
    else:
        print("Entry Denied")


# In[9]:


# Problem 8 – Library System
books = ["Python","Java","Python","C","C++","Java"]
unique_books = set(books)
print(unique_books)
print("Unique Books:", len(unique_books))
if "Python" in books:
    print("Python Exists")
else:
    print("Python Not Found")


# In[1]:


# Problem 9 – Race Elimination
players = ["Ajay","Ravi","Ali","Kiran","John"]
for player in players:
    if player == "Ali":
        continue
    print(player)


# In[2]:


# Problem 10 – Bus Capacity
passengers = []

for i in range(1, 60):
    passengers.append(i)
    if len(passengers) == 40:
        print("Bus Full")
        break


# In[3]:


# Problem 11 – Lucky Number Hunt

numbers = [12,8,21,15,9,18,27]

for n in numbers:
    if n % 3 == 0 and n % 7 == 0:
        print("Lucky Number:", n)
        break


# In[4]:


# Problem 12 – Fruit Market

fruits = ["Apple","Banana","Mango","Orange","Apple","Mango"]

if "Mango" in fruits:
    print("Available")
else:
    print("Out of Stock")

print(set(fruits))


# In[5]:


# Problem 13 – Secret Number
secret = 25
guesses = [10,14,25,31,42]

for g in guesses:
    if g == secret:
        print("Correct Guess")
        break


# In[6]:


# Problem 14 – Hospital Queue
patients = ["Rahul","Emergency","Sita","Ramesh","Akash"]
for patient in patients:
    if patient == "Emergency":
        print("Treat Immediately")
        break
    print(patient)


# In[7]:


# Problem 15 – Sports Academy
scores = [45,82,61,93,55,78]

count = 0

for score in scores:
    if score >= 60:
        print(score, "Qualified")
        count += 1
    else:
        print(score, "Not Qualified")

print("Qualified Students:", count)


# In[8]:


# Problem 16 – Mobile Password
password = 1234
entered = 1111

if entered == password:
    print("Phone Unlocked")
else:
    print("Wrong Password")


# In[9]:


# Problem 17 – Cab Booking
fare = 850

if fare > 1000:
    fare -= fare * 20 / 100
elif fare > 500:
    fare -= fare * 10 / 100

print("Final Fare:", fare)


# In[10]:


# Problem 18 – School Attendance

attendance = ["Present","Absent","Present","Present","Absent"]

present = 0
absent = 0

for a in attendance:
    if a == "Present":
        present += 1
    else:
        absent += 1

print("Present:", present)
print("Absent:", absent)



# In[11]:


# problem 19- international conference
countries = [
    "India",
    "USA",
    "India",
    "Japan",
    "Germany",
    "USA",
    "France"
]

# Remove duplicates
unique_countries = set(countries)

# Print all unique countries
print("Unique Countries:")
for country in unique_countries:
    print(country)

# Count participating countries
print("Total participating countries:", len(unique_countries))


# In[12]:


# problem 20 -space mission control
systems = (
    "Engine",
    "Fuel",
    "Navigation",
    "Communication",
    "Cooling"
)

status = [
    "OK",
    "OK",
    "FAIL",
    "OK",
    "OK"
]

for i in range(len(systems)):
    if status[i] == "FAIL":
        print("Failed System:", systems[i])
        print("Launch Aborted!")
        break
else:
    print("Ready for Launch")


# In[ ]:




