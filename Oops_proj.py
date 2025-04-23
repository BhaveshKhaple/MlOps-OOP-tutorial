class chatbook:
    def __init__(self):
        self.username=''
        self.passsword=''
        self.loggedin=False
        self.menu()
        # self.signup()


    def menu(self):
        user_input=input("""Welcome to chatbook!! How would you like to proceed
                         1. Press 1 to signup
                         2. Press 2 to signin
                         3. Press to 3 tp Write a post
                         4. Press 4 to message a friend 
                         5. Press any other to exit""")
        if user_input == "1":
            self.signup()                        
        elif user_input == "2":
            pass                         
        elif user_input == "3":
            pass                         
        elif user_input == "4":
            pass                         
        else:
            exit()

    def signup(self):
        email=input("Enter your mail ->")
        password=input("Enter your pass->")
        self.username= email
        self.password=password
        print("You had succesfulyy signed up on chat book")
        print("\n")
        self.menu()







obj1=chatbook()                  
        