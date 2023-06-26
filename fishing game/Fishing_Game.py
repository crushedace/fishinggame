import csv
import hashlib
from ctypes.wintypes import BOOLEAN
from tkinter import *

import Fish_Dict
from Die import Die

main=Tk()

main.title('Login Page')
main.geometry("400x100")

#Create a Login Frame
window =Frame(main)
window.grid()
global feedback
feedback = StringVar()


def savereg(ID,hash_password):
    
    fieldnames = ['Username', 'Password','Score']
    data = [{'Username': ID, 'Password': hash_password }]
    filename = "User_info"
    try:
       
        with open(filename + '.csv', 'x', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for data in data:
                writer.writerow(data)
    except FileExistsError:
        with open(filename + '.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for data in data:
                writer.writerow(data)

            return True
            
# Register Function
def register():
    
    ID = username.get()
    PW = password.get()
    hash_password = hashlib.sha256(PW.encode()).hexdigest()
    answer = savereg(ID,hash_password)

    if answer:
        feedback.set("User Created, Please Login")
    else:
        feedback.set("try register again")



# Clear Function
def clear_frame():
    for widgets in window.winfo_children():
        widgets.destroy()

# Login 
def login():
    with open("C:\\fishing game\\User_Info.csv", 'r') as file:
        global new
        new = BOOLEAN(True)
        #data_arr =[]
        global ID
        ID = username.get()
        global pwd
        pwd = password.get()
        hash_password = hashlib.sha256(pwd.encode()).hexdigest()
        csv_file = csv.DictReader(file)
        for row in csv_file:
            #data_arr.append(dict(row))  
            NewID = row['Username']
            key2 = row['Password']

            if ID == NewID:
                if hash_password == key2:
                    feedback.set("Login Success")
                    clear_frame()
                    FishGame()
                    break
                else:
                    continue
            elif ID == NewID:
                continue
        feedback.set("Please Enter \n Valid Username or Password")

    



#Login Page Items
def LoginPage():
    #Labels
    #Username Label
    userlbl=Label(window, text = "Username")
    #Password Label
    passlbl=Label(window, text = "Password")
    #User Feedback
    feedlbl=Label(window, textvariable=feedback)

    global username
    global password
    username = StringVar()
    password = StringVar()
 
    #Entry Boxes
    #Username Entry Box
    userEnt= Entry(window, textvariable=username)
    #Password Entry Box
    passEnt= Entry(window, textvariable=password, show="*")


    #Buttons
    #Quit Button
    quitBtn=Button(window, text="Quit", fg='black', command=quit)
    #Register Button
    regBtn=Button(window, text="Register", fg='black', command=register)
    #Login Button
    logBtn=Button(window, text="Login", fg='black', command=login)

    #Widget Positioning

    userlbl.grid(row = 0, column =0, sticky = W, pady = 2)
    passlbl.grid(row = 1, column =0, sticky = W, pady = 2)
    feedlbl.grid(row = 1, column =3, sticky = W, pady = 2)

    userEnt.grid(row = 0, column =1, pady = 2)
    passEnt.grid(row = 1, column =1, pady = 2)

    regBtn.grid(row = 2, column =0, sticky = W, pady = 2)
    logBtn.grid(row = 2, column =1, sticky = W, pady = 2)
    quitBtn.grid(row = 2, column =2, sticky = W, pady = 2)







    main.mainloop()



    
#Fishing Game Main Screen
def FishGame():
    global Score
    Score = int()
    Score = Score
    global Caught
    Caught =BooleanVar()
    Caught = False

    def Reset():
        global new
        for widgets in window.winfo_children():
            widgets.destroy()
        new = True
        FishGame()

    def Fish():
        global new
        if new == True:
            global Caught
            if Caught == False:
                global Score
                Caught = True
                global FishType
                FishType =StringVar()
                global Kept
                Kept =int()
                global Release
                Release =int()
                DiceRoll = 0
                # create die with 6 sides
                create_die = Die(6)
                # die roll
                DiceRoll = create_die.roll_die()
            

                #Get Single Point Value
                points = Fish_Dict.GetFish(DiceRoll)
                #print(points)
                FishType = points[0]
                Kept = points[1]
                Release = points[2]
                species['text'] = FishType
            
                if FishType == "Lost Bait":
                    Caught = False
                    Score = Score + int(Kept)
                finlbl['text'] = "Total Score " + str(Score)
            elif Caught == True:
                species['text'] = FishType + "\n" + "Release or Keep?"
        elif new == False:
            species['text'] = "Please Start A Fishing Session"
    
    def Keep():
        global Caught
        global Score
        global FishType
        if Caught == True:
            listbox.insert(0, FishType)
            #print("You Have Kept The Fish")
            Caught = False
            FishType = ""
            species['text'] = "You Have Kept The Fish"
            Score = Score + int(Kept)
            finlbl['text'] = "Total Score " + str(Score)
            #print(Score)
        elif Caught == False:
            #print("Please Go Fishing")
            species['text'] = "Please Go Fishing"
    
    def ReleaseFish():
        global Caught
        global Score
        global FishType
        if Caught == True:
            #print("You Have Released The Fish")
            Caught = False
            FishType = ""
            species['text'] = "You Have Released The Fish"
            Score = Score + int(Release)
            finlbl['text'] = "Total Score " + str(Score)
            #print(Score)
        elif Caught == False:
            #print("Please Go Fishing")
            species['text'] = "Please Go Fishing"
    
    def Final():
        finBtn.grid_forget()
        startbtn.grid()
        global new
        new = False
        global Score
        message = str()
        int(Score)
        species['text'] = "Thank You For Playing"
        while int(Score) >= 100 <=200:
            message = "You've Done Ok"
            break
        while int(Score)  >= 200 < 500:
            message = "Well Done \n cap'n "
            break
        while int(Score) <100:
            message = "Try Harder \n Next Time"
            break
        str(Score)
        finlbl['text'] = "Total Score " + str(Score)+ "\n" + str(message)
        #print(Score)
        with open("C:\\fishing game\\User_Info.csv", 'r') as file:
            data_arr =[]
            global ID
            global pwd
            csv_file = csv.DictReader(file)
            for row in csv_file:
                data_arr.append(dict(row))  
                Name2 = row['Username']
                Pass2 = row['Password']
                Score = row['Score']
                fieldnames = ['Username','Password','Score']

                if ID == Name2:
                    if pwd == Pass2:
                        with open("C:\\fishing game\\Highscore.csv", mode="a", newline='') as csv_file:
                            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                            #write to file
                            writer.writerow({'Username': ID,'Score': Score})
                            csv_file.close()
                            break
                    else:
                        continue
                elif ID == Name2:
                    continue
        startbtn.grid(row = 4, rowspan = 1, column=1, columnspan=2, sticky = W, pady = 2)
        
    main.title('Fishing Game')
    main.geometry("470x280")
    #Labels
    #Title Label
    titlelbl=Label(window, text = "Fishing Game")
    #Name of Fish Caught Label
    species=Label(window, text= "yarrgh Capt'n \n the sea is calling", width=20)
    #Total Score Label
    totlbl=Label(window, text = "ye Caugh a ")
    #Final Message Label
    finlbl=Label(window, text = "Total Score " + str(Score))

    #Listbox
    listbox = Listbox(window)


    global username
    global password
    username = StringVar()
    password = StringVar()

    #Buttons
    #Finish Fishing Button
    startbtn=Button(window, text="Start New Session", fg='white', bg='blue', command=Reset)
    #set Sail Button
    Sailbtn=Button(window, text="set sail", fg='white', bg='green', command=Reset)
    #Go Fishing Button
    finBtn=Button(window, text="Finish Fishing", fg='white', bg='blue', command=Final)
    #Reset Button
    fishBtn=Button(window, text="Cast Line", fg='blue', activebackground='blue', activeforeground='white', command=Fish)
    #Keep Button
    keepBtn=Button(window, text="Keep", fg='blue', command=Keep)
    #Release Button
    relBtn=Button(window, text="Release", fg='blue', command=ReleaseFish)
    #Quit Button
    quitBtn=Button(window, text="Quit", fg='white', bg='red', command=quit)

    #Widget Positioning

    listbox.grid(row=1, column=5, sticky = W, pady = 4, padx= 10)

    titlelbl.grid(row = 0, column =1, sticky = N, pady = 2)
    species.grid(row = 1, column=1, sticky = W, pady = 2,)
    totlbl.grid(row = 0, column=5, sticky = W, pady = 2)
    finlbl.grid(row = 1, column=7, sticky = W, pady = 2)

    Sailbtn.grid(row = 1, column=2, columnspan=2, sticky = W, pady = 2)
    fishBtn.grid(row = 1, column=2, columnspan=2, sticky = NW, pady = 2)
    
    keepBtn.grid(row = 2, column=5, sticky = NW, pady = 2)
    relBtn.grid(row = 2, column=5, sticky = NE, pady = 2)
    finBtn.grid(row = 4, rowspan = 1, column=1, columnspan=2, sticky = W, pady = 2)
    quitBtn.grid(row = 7, rowspan = 1, column=1, columnspan=2, sticky = W, pady = 2)
    main.mainloop()


#if __name__=="Fishing_Game":
LoginPage()