import random #Importing random module to generate random numbers 

def random_number(): #Start of the function
    number = random.randrange(1,101) # We create a variable where we store the random number in a range between 1 and 101 to have 100 numbers
    return number # We return the value of the variable which is the randomly generated number
