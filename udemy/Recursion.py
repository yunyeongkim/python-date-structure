#Function tha that calls it self,,, until It doesn't
"""
### The process of opening each new box is the same
### Each time we open a box, we make the problem smaller

Below two option is needed to prevent stack over flow.
### ** Base Case
### ** Return statement  
def open_gift_box():
    ## This is base case. 
    if ball:
        return ball   <- This part should be here.
    ## This is recursion
    open_gift_box()

"""

# def funcThree():
#     print("Three")

# def funcTwo():
#     funcThree()
#     print("Two")

# def funcOne():
#     funcTwo()
#     print('One')
# funcOne()



def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))