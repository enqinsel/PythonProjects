# Add Customers or Staff in alphabetical order

mylist = []
while True:
    user = input("Add data, press 0 when done: ")
    mylist.append(user)
    mylist.sort()
    if user == "0":
        mylist.remove("0")
        print("Your list sorted: " , mylist)
        break