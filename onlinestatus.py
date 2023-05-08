#Dictionary we will use
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    }

#Initialisation of the function 
def online_count (statuses):
    nb_pers = 0  #variable where we store the number of occurences 
    for occurence,number in statuses.items(): #for each element of the dictionary, we store each key in occurence and the value of the key in number
        if number == "online": #we check if the value in number is "online" 
            nb_pers+=1 #we add 1 to the last value of this variable in order to count
            
    return nb_pers  #and return the number of users online
