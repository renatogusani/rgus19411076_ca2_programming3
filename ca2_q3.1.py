# date : 21/05/2021
# Author : Renato Gusani
# Student no. : x19411076
# Question - Q3.1 + Q3.2

# * * * * * * * * * * question 3.1) * * * * * * * * * *


import matplotlib.pyplot as plt # plot package

Number = [] # empty list


dup_list = [1, 2, 2, 3, 4, 5, 5] # list with duplicates
dup_list = list(dict.fromkeys(dup_list))
Number.append(dup_list)
print(Number)

for iteration_count in range(len(Number)):
    # counter
    for random in range(0,len(Number)-1):
        # swaps each element for each iteration
        if (Number[random]>Number[random+1]):
            Number[random],Number[random+1] = Number[random+1],Number[random]
        
# plot 
plt.plot(dup_list)
plt.xlabel("Size of input")
plt.ylabel("Time Complexity")
plt.show()

# * * * * * * * * * * question 3.1) * * * * * * * * * *

'''
My algorithm:
1. empty list (number)
2. list with dups removed (dup-list)
3. empty list gets updated (number)
4. plot

Now that I identified my operations 
i calculate the Big O for each of them. 
In this algorithm, we’re dealing with pretty simple 
operations — each of which has a time complexity of O(n).

Algorithms or activities that make some linear time
complexity can be distinguished by the way that the
quantity of tasks increments straightly with the size
of the info. 

That implies if an activity needs to run multiple 
times for a rundown that is 100 things in length, 
at that point it has linear time complexity.
'''