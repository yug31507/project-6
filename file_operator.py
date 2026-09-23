import datetime
class JManager:
    def __init__(self):
        self.filename="journal.txt"

        try:
            file = open(self.filename, "x")
            file.close()
        except FileExistsError:
             print("File already exists")
             
        except PermissionError:
            print("Permission denied while creating the journal file.")

    def new_entry(self):
        entry= input("Enter your journal entry:\n")
        try:
            with open(self.filename,"a") as file:
                    t = datetime.datetime.now()
                    formatted_date = t.strftime("%Y-%m-%d %H:%M:%S")
                    file.write("["+formatted_date+"]\n")
                    file.write(entry + "\n\n") 
            print("\nEntry added successfully")
        except PermissionError:
             print("Permission denied. Unable to add the entry.")


    def view_entries(self):
        try:
                with open(self.filename,"r") as file:
                    print("Your Journal Entries :")
                    print("__________________________")
                    print()
                    data=file.read()
                    print(data)
        except FileNotFoundError:
                print("No journal entries found. Start by adding a new entry!")
        except PermissionError:
             print("Permission denied. Unable to read the journal.")
             

    def search_entries(self):
        a=input("Enter a Keyword or date to search :")
        try:
                with open(self.filename,"r") as file:
                    matching_word=file.read()
                    mword=matching_word.split("\n\n")
                    check=False
                    for i in mword:
                        if( a in i):
                            print("Matching Entries :")
                            print("-----------------")
                            print(i)

                            check=True
                    
                  
                    if(check==False):
                        print( "No entries were found for the keyword: "
                                 , a, ".")

        except FileNotFoundError:
                print("No journal entries found. Start by adding a new entry!")
        except PermissionError:
             print(" Unable to serach the entry.")

    def delete_entries(self):
        user=input("Are you sure you want to delete all entries? (yes/no):")
        if(user =="yes"):
              try:
                with open(self.filename, "w") as file:
                    file.write("")

                print("All journal entries have been deleted.")
              except PermissionError:
                   print("Unable to delete the entries")
        else:
              print("entries deletion cancelled.")

J=JManager()   

print("Welcome to Personal Journal Manager!")
print("Please select an option:")

while(True):
    print()
    print("1.Add a New Entry")
    print("2.View All Entries")
    print("3.Search for an Entry")
    print("4.Delete All Entries")
    print("5.Exit")
    
    option=int(input("User Input: "))

    match option:
            case 1:
                J.new_entry()
    
            case 2:
                J.view_entries()
                
            case 3:
                J.search_entries()

            case 4:
                J.delete_entries()

            case 5:
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break
            case _:
                print("Invalid option.Please select a valid option from the menu")
