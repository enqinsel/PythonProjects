def reverse(rev):
    return rev[::-1]

def big(up):
     return up.upper()

def small(low):
    return low.lower()


menu = '''
1: Reverse Text
2: Write all words in uppercase
3: Write all words in lowercase
q: Sign Out
'''

while True:
    print("\n\n"+menu)
    choice = input("Please select the action you want to do: ")
    
    if choice == "1":
        text = input("Enter the text you want to see reversed:\n>> ")
        print("\n\nYour reversed text is:\n>> " + reverse(text))
        
    elif choice == "2":
        user = input("Enter Text:\n>> ")
        print("\n\nCapitalization use of your text:\n>> " + big(user))
        
    elif choice == "3":
        user2 = input("Enter Text:\n>> ")
        print("\n\nLowercase use of your text:\n>> " + small(user2))
        
    elif choice == "q":
        print("\n***Logged Out***")
        break
    else:
        print("\n  !!!Please make a choice!!! ")
        



