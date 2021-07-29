
def reverse(rev):
    return rev[::-1]

def big(up):
      return up.upper()

def small(low):
    return low.lower()

def word(word):
    listt = word.split()
    return len(listt)

def char(ch):
    return len(ch)

menu = '''
1: Reverse Text
2: Write all words in uppercase
3: Write all words in lowercase
4: Word counter
5: Number of characters with spaces
q: Sign Out
'''

while True:
    print("\n\n"+menu)
    choice = input("Please select the action you want to do: ")
    
    if choice == "1":
        text = input("Enter the text you want to see reversed:\n>> ")
        print("\n\nYour reversed text is:\n>> " + reverse(text))
        
    elif choice == "2":
        text = input("Enter Text:\n>> ")
        print("\n\nCapitalization use of your text:\n>> " + big(text))
        
    elif choice == "3":
        text = input("Enter Text:\n>> ")
        print("\n\nLowercase use of your text:\n>> " + small(text))
    
    elif choice == "4":
        text = input("Enter Text:\n>> ")
        print("\n\nWords Count:\n>> " , word(text))

    elif choice == "5":
        text = input("Enter Text:\n>> ")
        print("\n\nCharacters Count:\n>> " , char(text))
        
    elif choice == "q":
        print("\n***Logged Out***")
        break
    else:
        print("\n  !!!Please make a choice!!! ")




























