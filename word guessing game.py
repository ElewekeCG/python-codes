#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random 
name = input("What is your name? ") 
print("Good Luck ! ", name) 
words =  ['bring', 'gather', 'redeem', 'rewind', 'oracle', 'thinks', 'apples', 'buckle', 'fish', 'brand', 
         'works', 'dilute']
word = random.choice(words)
print("Guess the characters")
print("you have 8 turns")
guesses = ''
turns = 8
while turns > 0:
    failed = 0
    
    for char in word:
         
        if char in guesses:
            print(char)
             
        else:
            print("_")
             
            failed += 1
 
    if failed == 0:
        
        print("You Win")
         
        print("The word is: ", word)
        break
     
    guess = input("guess a character:")
     
    guesses += guess
     
    if guess not in word:
         
        turns -= 1
         
        print("Wrong")
         
        print("You have", + turns, 'more guesses')
         
        if turns == 0:
            print("You Loose")


# In[ ]:




