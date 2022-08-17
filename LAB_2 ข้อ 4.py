num = input("Enter Your List : ")

num = num.split()

numlist = []

intnum = [int(a) for a in num]

if len(num) <= 2 :

    print("Array Input Length Must More Than 2")

    exit(0)

for i in range(len(intnum)) :

    for j in range(i + 1 , len(intnum)) :

        for k in range(j + 1 , len(intnum)):

            if intnum[i] + intnum[j] + intnum[k] == 5:

                if sorted([intnum[i] , intnum[j] , intnum[k]]) not in numlist :

                    numlist.append(sorted([intnum[i] , intnum[j] , intnum[k]]))

print(numlist)
 

       

                


        


