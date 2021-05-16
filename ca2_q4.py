# date : 14/05/2021
# Author : Renato Gusani
# Student no. : x19411076
# Question - Q4 - Insertion sort 

# * * * * * * * * * * question 4) * * * * * * * * * *


user_input = input("Enter a sentence: ") # takes user input and stores it in user_input
useranswer = user_input.split() # takes user_input splits it and stores in useranswer

# based on my student number i was to do the insertion sort to sort the split words alphabethically
def insertionSort():
    for number in range(1,len(useranswer)):
        key=useranswer[number]
        split=number-1
        while split>=0 and key<useranswer[split]:
            useranswer[split+1]=useranswer[split]
            split=split-1
        useranswer[split+1]=key
    print(useranswer)

# printing the split words from user input alphabetically
insertionSort()