def checkSubsequence(s, t):
    # Write your plan below
    # loop over the second string
    # whenever you find a letter in the first one continue to the second one
    # 
    #

    # Write your code below
    if s =="" and t == "":
        return True
    
    if len(s) > len(t) or s =="":
        return False
    j = 0
    for i in range(len(t)):
        if s[j] == t[i]:
            j +=1
    
    if j == len(s):
        return True
    else:
        return False
    
s = "ghghf";t = ""
print(checkSubsequence(s,t))