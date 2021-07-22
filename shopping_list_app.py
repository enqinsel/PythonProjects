mylist = set()

while True:
    user = input("Add to the list: ")
    mylist.add(user)
    if user == "del":
        mylist.remove("del")
    elif user == "0":
        mylist.remove("0")
        print("\nProcess Completed...")
        print("\n Final Version Of Your List: " , (mylist))
        break
    print("Your List: " , (mylist))
    print("\n   Note: If there is something you want to delete, type the \t command 'del' followed by the item you want to delete.")
    if user == "del":
        delete = input("Enter the item you want to delete: ")
        mylist.remove(delete)
        print("\nFinal Version Of Your List: " , (mylist))
        print("\nContinue>>>")
        continue
    print("\n   Press '0' to finish")