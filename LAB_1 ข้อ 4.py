print("*** Fun with Drawing ***")

n = int(input("Enter input : "))

for i in range( 0 , 3 * n - 2 ) :

    s = ""

    if i == 0 :

        s += "." * ( n - i - 1 ) + "*" + "." * ( 2 * n - 3 ) + "*" + "." * ( n - i - 1 )

    elif i < n :

        if 2 * n - 3 - 2 * i < 0 :

            s += "." * ( n - i - 1 ) + "*" + "+" * ( 2 * i - 1 ) + "*" + "+" * ( 2 * i - 1 ) + "*" + "." * ( n - i - 1 )

        else :

            s += "." * ( n - i - 1 ) + "*" + "+" * ( 2 * i - 1 ) + "*" + "." * ( 2 * n - 3 - 2 * i ) + "*" + "+" * ( 2 * i - 1 ) + "*" + "." * ( n - i - 1 )

    else :

        dull = i - n

        if i == 3 * n - 3 :

            s += "." * ( 2 * n - 2 ) + "*" + "." * ( 2 * n - 2 )

        else :

            s += "." * ( dull + 1 ) + "*" + "+" *( 4 * n - 3 - 2 * ( dull + 2 ) ) + "*" + "." * ( dull + 1 )
            
    print(s)