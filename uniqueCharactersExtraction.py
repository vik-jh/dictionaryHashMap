def uniqueChar(s):
    new_string = ""  # making a new string empty for storing the unique character
    for i in range(len(s)):
        if s[i] not in new_string:  #if the individual character is not in string
            						#when there are characters appearing more no of times
                					#why to print them as it won't be unique
            new_string += s[i]
    return new_string


# Main 
s=input() 
print(uniqueChar(s))