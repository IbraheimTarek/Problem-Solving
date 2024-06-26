def main():
    testcases =int(input())
    for i in range(0,testcases):
        string1, string2 = input().split()
        temp1 = string2[0] + string1[1:]
        temp2 = string1[0] + string2[1:]
        print(temp1," ", temp2)

main()
