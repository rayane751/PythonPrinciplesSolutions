
def capital_indexes(string):
    indexes = []
    for i, char in enumerate(string):
        if char.isupper():
            indexes.append(i)
    return indexes

        
        
string = ("HeLlO")
result = capital_indexes(string)
print(result)
