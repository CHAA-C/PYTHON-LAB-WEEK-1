print("*** New Range ***")

num = input("Enter Input : ")

num = num.split()

if len(num) == 1:

    d = float(num[0])

    numlist = []

    numlist.append( str(0.0) )

    while float(numlist[-1]) < d - 1 :

        a = float(numlist[-1]) + 1

        numlist.append(str(a))

    print('(' + ', '.join(numlist) + ')')

elif len(num) == 2:

    d,f = float(num[0]),float(num[1])

    numlist = list()

    numlist.append(str(d))

    while float(numlist[-1]) < f - 1 :

        a = float(numlist[-1]) + 1
        
        numlist.append(str(a))

    print('(' + ', '.join(numlist) + ')')

elif len(num) == 3:

    d,f,g = float(num[0]),float(num[1]),float(num[2])

    dp = str(d+f+g).split(".")

    dpp = len(dp[1])

    numlist = list()

    numlist.append(str(d))

    while float(numlist[-1]) < f-g :

        a = round(float(numlist[-1])+g,dpp)

        numlist.append(str(a))

    if float(numlist[-1]) >= f:

        numlist.pop(-1) 

    print('(' + ', '.join(numlist) + ')')





