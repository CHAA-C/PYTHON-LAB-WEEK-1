from collections import OrderedDict


class funString():

    def __init__(self,string = ""):

        self.string = string

    def size(self) :

        count = 0
        
        for char in str1:

            count += 1

        return count

    def replace(self) :

        return str1.swapcase()

    def reverse(self) :

        str = ""

        for i in str1:
            
            str = i + str

        return str

    def delete(self) :

        return "".join(OrderedDict.fromkeys(str1))

str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :   
    
    print(res.size())

elif str2 == "2" :

    print(res.replace())

elif str2 == "3" :

    print(res.reverse())

elif str2 == "4" :

    print(res.delete())

