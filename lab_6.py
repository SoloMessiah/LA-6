"""
We will create a random number between one and twenty and based on the results of the random
number, we will check to see if the number falls within certain ranges.
If the number is greater than 15, the result will be "Cherries".
If the number is greater than 10, the result will be "Orange".
If the number is greater than 5, the result will be "Plum".
If the number is greater than 2, the result will be "Melon".
If the number is greater than 1, the result will be "Bell".
If the number is not any of the above, than the result will be "Bar".

We loop three times and print the results to the user.
"""


"""
 import random module
num = generated random number

If num > than 15, 
    the result will be "Cherries".
If num > 10,
     the result will be "Orange".
If num is > 5,
    the result will be "Plum".
If num > 2, 
    the result will be "Melon".
If num >  1, 
    the result will be "Bell".
Else
    the result will be "Bar".

loop three times
    print the output(fruit)
"""




import random

def main():
    for i in range(0, 3):
        spin()

def spin():
    rand_num = random.randint(1, 20)
    output = ""

    if(rand_num > 15):
        output = "Cherries"
    elif(rand_num > 10):
        output = "Orange"
    elif(rand_num > 5):
        output = "Plum"
    elif(rand_num > 2):
        output = "Melon"
    elif(rand_num > 1):
        output = "Bell"
    else:
        output = "Bar"

    print(output, end=" ")

main()
