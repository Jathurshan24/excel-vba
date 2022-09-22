wordDictionary = {
    "bat" :"red",
    "ball":"blue",
    "apple":"green",
    "test":"paper",
    "box":"cyan",
    "tree":"brown"
}

def getString(dictonary):
    list =[]
    for key in dictonary.keys():
        if len(key) == 4:
            list.append(key)

    for val in dictonary.values():
        if len(val) == 4:
            list.append(val)
    return list

print(len(getString(wordDictionary)))
