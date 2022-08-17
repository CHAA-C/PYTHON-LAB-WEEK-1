from cgitb import text


def replace(text,highlight) :

    s = text
    s2 = s.replace(highlight,'['+ highlight+']')
    print(s2)

print("*** Reading E-Book ***")

a , b = input('Text , Highlight : ').split(',')
replace(a,b)