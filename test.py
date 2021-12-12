#replace 0 with 1 and 1 with 0
string = [0,1]
length = len(string)
i = 0
while i < length:
    if string[i] == 0:
        string.insert(i+1, 1)
        length += 1
        i += 1
    else:
        string.insert(i+1, 0)
        length += 1
        i += 1
    i += 1
    # if i + 1 == length and string[i] == 0 :
    #     string.append(1)

print (string)
