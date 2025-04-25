class chatbook:
    def __init__(self):
        self.__username='Default user'
        self.passsword=''
        self.loggedin=False
        # self.menu()
        # self.signup()


    def menu(self):
        user_input=input("""Welcome to chatbook!! How would you like to proceed
                         1. Press 1 to signup
                         2. Press 2 to signin
                         3. Press to 3 to Write a post
                         4. Press 4 to message a friend 
                         5. Press any other to exit
                         
                         """)
        if user_input == "1":
            self.signup()                        
        elif user_input == "2":
            self.signin()                         
        elif user_input == "3":
            self.myPost()                      
        elif user_input == "4":
            self.sending()                         
        else:
            exit()

    def signup(self):
        email=input("Enter your mail ->")
        pwd=input("Enter your pass->")
        self.username= email
        self.password=pwd
        print("You had succesfulyy signed up on chat book")
        print("\n")
        self.menu()



    def signin(self):
        if self.username =='' and self.password =='':
            print("Please signup by presssing 1 in menu")
        else:
            uname=input("ENter user name here->")
            pwd=input("ENter password name here->")
            if self.username==uname and self.passsword==pwd:
                print("You successfully signed in")
                print("\n")
                self.loggedin= True
            else:
                print("Enter correct credintial")
        self.menu()
            
    
    def myPost(self):
        if self.loggedin==True :
            txt=input("Enter you message post here")
            print(f"Follwing content will be posted{txt}")
        else:
            print("You need to sign in first")
            print("\n")
        self.menu()

    def sending(self):
        if self.loggedin==True:
            txt =input("Enter your message->")
            frnd =input("whom to send message->")
            print(f"Your messag esent to {frnd}")
        else:
            print("You need to sign in first")
        print("\n")
        self.menu()
    













user1=chatbook()                  
        