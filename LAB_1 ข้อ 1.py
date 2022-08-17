print("*** Rabbit & Turtle ***")

d , Vr , Vt , Vf = input('Enter Input : ').split()

if int(d) >= 5000 :

    print("Input Must Not Greater Than 5000")
    SystemExit

elif int(Vr) >= 5000 :

    print("Input Must Not Greater Than 5000")
    SystemExit

elif int(Vt) >= 5000 :

    print("Input Must Not Greater Than 5000")
    SystemExit

elif int(Vf) >= 5000 :

    print("Input Must Not Greater Than 5000")
    SystemExit

elif int(Vr) >= int(Vt) :

    print("Vt Must Greater Than Vr")
    SystemExit

elif int(Vr) & int(Vt) > int(Vf) :

    print("Vf Must Greater Than Vr and Vt")
    SystemExit

print("{0:.2f}".format(int(d)/(int(Vt)-int(Vr))*int(Vf)))











