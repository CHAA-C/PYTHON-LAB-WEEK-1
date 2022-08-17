def deciToRoman(x):

    num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']

    i = 12
    romannum = ""

    while x != 0 :
        if num[i] <= x:
            romannum += roman[i]
            x = x - num[i]

        else :

            i -= 1

    return romannum

numbers = int(input("Enter number to translate : "))

print(deciToRoman(numbers))
print(int(numbers))


