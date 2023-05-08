statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    }
   
def online_count (statuses):
    nb_pers = 0   
    for occurence,number in statuses.items():
        if number == "online":
            nb_pers+=1
            
    return nb_pers  
