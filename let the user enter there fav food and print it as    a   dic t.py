dict = {}
a1 = input("what is your favorite food farhan\n")
a2 = input("what is your favorite food aadil\n")
a3 = input("what is your favorite food ehtesam\n")
a4 = input("what is your favorite food rashmi\n")

dict["farhan"] = a1
dict["aadil"] = a2
dict["ehtesam"] = a3
dict["rashmi"] = a4

for key,value in dict.items():
    print( key + " likes " + value)
    