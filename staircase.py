def staircase(n):

    for i in range(n):
        y = i+1
        x = n-y
        list = []
        string = ""
        for i in range(x):
            list.append(" ")
        for i in range(y):
            list.append("#")
        for i in list:
            string = string + i
        print(string)

n = input("Provide a number: ")
staircase(int(n))