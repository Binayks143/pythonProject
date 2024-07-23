class PhoneBook:
    d={}

    def add_contact(self,name,phnum):
        if name in self.d:
            # Ensure the value is a list before appending
            if isinstance(self.d[name],list):
                self.d[name].append(phnum)
                print(f"Contact number appended with name {name} and number {phnum}")
            else:
                self.d[name]=[self.d[name],phnum]
                print(f"Contact added with name {name} and number {phnum}")
        else:
            self.d[name]=phnum
            print(f"Contact added with name {name} and number {phnum}")

        return self.d


    def view_contact(self,userChoice,userInput=None):
        if userChoice==1:
            return self.d

        elif userChoice==2:
            if userInput in self.d:
                return self.d[userInput]
            else:
                key=None
                for k,v in self.d.items():
                    if v==userInput:
                        key=k
                        break
                return key


    def delete_contact(self,delRequest):
        key_to_delete=[]

        for k,v in self.d.items():
            if k==delRequest or v==delRequest:
                key_to_delete.append(k)

        for i in key_to_delete:
            del self.d[i]
            print(f"contact details deleted with entered {delRequest}")

        if not key_to_delete:
            print(f"enter {delRequest} is not available in phonebook")
        return self.d

    def modify_contact(self,update,e1,e2):
        if update==1:
            if e1 in self.d:
                if e2 in self.d:
                    print(f"{e2} is already exits in phone book can not be updated")
                else:
                    self.d[e2]=self.d.pop(e1)
                    print(f"{e1} has benn updated with {e2}")
                    print("new phone book is",self.d)
            else:
                print(f"{e1} is not available in phone book")

        elif update==2:
            key=[]
            for k,v in self.d.items():
                if v==e1:
                    key.append(k)
            for i in key:
                self.d[i]=e2
                print(f"Phone number {e1} updated successfully with {e2}")
                print("new phone book is", self.d)

            if not key:
                print(f"{e1} is not available in phonebook")
        return self.d


def main():
    p1=PhoneBook()

    while True:
        n = int(input("Enter the key for operation \n 1. For add Contact \n 2. View Contact "
                      "\n 3. Delete Contact \n 4. Format PhoneBook \n 5. Modify Contact \n "
                      "6. Exit \nYour Input="))

        # For add Contact
        if n==1:
            name=input("Enter the name: ")
            phNum=input("Enter the Ph Number: ")
            print("added contact in phonebook: ",p1.add_contact(name,phNum))


        #View Contact
        elif n==2:
            user_input=int(input("1. for all contact\n2. Enter name or phnumber for specific contact \n"
                                 "your input: "))
            if user_input==1:
                print("Phone Book contact is : \n", p1.view_contact(user_input))

            elif user_input==2:
                UNorphnum=input("Enter the name or phone number : ")
                print(f"Person details for {UNorphnum} is : ",p1.view_contact(user_input,UNorphnum))
            else:
                print("Invalid input")


        elif n==3:
            del1=input("Enter the name or number to delete: ")
            o1=p1.delete_contact(del1)
            print("Updated Phone book: ",o1)

        elif n==4:
            PhoneBook.d.clear()
            print("All contacts deleted from phonebook")
            print("Updated phonebook is: ", PhoneBook.d)

        elif n==5:
            print("1. Want to update Name?")
            print("2. Want to update Ph Number?")
            update=int(input("Enter the choice: "))
            if update==1:
                e1=input("Enter the existing name to modify: ")
                e2=input("enter the New Name: ")
                o1=p1.modify_contact(update,e1,e2)
            elif update==2:
                e1=input("Enter the Existing Ph number to modify: ")
                e2=input("Enter the new phone number: ")
                o1=p1.modify_contact(update,e1,e2)

            else:
                print("Invalid input")

        elif n==6:
            print("Exiting the phonebook")
            break

        else:
            print("Invalid Input")

if __name__=="__main__":
    main()