import arabic_reshaper 
from classes import user1

#____________________________________________________Arabic___________________________________________
def resh (par1):
    reshaped_text = arabic_reshaper.reshape(par1)
    correct_text = ""
    for i in reshaped_text[::-1]:
        correct_text+= i
    
    return correct_text

def log_in_ar ():
    while True:
        try:
            print("\n")
            print (resh("ادخل اسمك بالانجليزية"))
            name_input_ar = input()
            user1.name[name_input_ar]  
        except KeyError:
            print(resh("الاسم المدخل غير صحيح"))
        else:
            break

    while True:
        try:
            print("\n")
            print(resh("ادخل كلمة المرور"))
            passwprd_input_ar = int(input())
            user1.get_password()[passwprd_input_ar]
        except KeyError:
            print(resh(f"كلمة المرور غير صحيحة")) 
        else:
            print(resh("مرحبا بعودتك"))
            name_input_ar =list(filter(lambda x:user1.name[x] == 'name',user1.name ))[0]
            print(f"{name_input_ar}")
            break  

    return 

################################################################
def add_progress_ar():                                         #
    file_ar = open("my_track_ar.txt","a",encoding="utf-8")     #
    file_ar.write("\n"+input(resh("مالذي تريد اضافته ؟")))    #
    file_ar.close()                                            #
    return                                                     #

def progress_check_ar():                                       #
    file_ar = open("my_track_ar.txt","r",encoding="utf-8")     #
    cont_ar = file_ar.readlines()                              #
    for i in cont_ar:                                          #
        print(resh(str(i)))                                    #
    file_ar.close()                                            #
    return                                                     #
################################################################

################################################################
def add_absent_ar():                                           #
    file_ar = open("absents_ar.txt","a",encoding="utf-8")      #
    file_ar.write("\n"+input(resh("مالذي تريد اضافته ؟")))    #
    file_ar.close()                                            #
    return                                                     #

def absents_check_ar():                                        #
    file_ar = open("absents_ar.txt","r",encoding="utf-8")      # 
    cont_ar = file_ar.readlines()                              #
    for i in cont_ar:                                          #
        print(resh(str(i)))                                    #
    file_ar.close()                                            #
    return                                                     #
################################################################

def progress_options_ar():
    while True:
        print("\n\n")
        print(resh('للاضافة في تقدمك في اللاب اضغط "ت" لرؤية تقدمك في اللاب اضغط "ر" وللخروج اضغط "خ"'))
        user_inp2_ar = input()
        if user_inp2_ar == 'ت':
            add_progress_ar()
        elif user_inp2_ar == 'ر':
            progress_check_ar()
        elif user_inp2_ar == 'خ':
            print("\n")
            print(resh("تم الخروج من خيارات التقدم"))
            break
            
    return " "

def absents_options_ar():
    while True:
        print("\n\n")
        print(resh('للاضافة في الغياب اضغط "غ" لرؤية الغياب اضغط "ر" وللخروج اضغط "خ"'))
        user_inp3_ar = input()
        if user_inp3_ar == 'غ':
            add_absent_ar()
        elif user_inp3_ar == 'ر':
            absents_check_ar()
        elif user_inp3_ar == 'خ':
            print("\n")
            print(resh("تم الخروج من خيارات الغياب"))
            break
    return " "


#______________________________________________English________________________________________________________________


def log_in ():
    while True:
        try:
            print("\n")
            print (("Enter your name"))
            name_input = input()
            user1.name[name_input]  
        except KeyError:
            print(("The name is incorrect"))
        else:
            break

    while True:
        try:
            print("\n")
            print(("Enter your password"))
            passwprd_input_ar = int(input())
            user1.get_password()[passwprd_input_ar]
        except KeyError:
            print("The password is incorrect") 
        else:
            for i in user1.name.items():
                if name_input == i:
                    return name_input
            print(f"Welcome back {name_input}")
            break       
    return 

############################################################
def add_progress():                                        #
    file = open("my_track.txt","a",encoding="utf-8")       #
    file.write("\n"+input("What do you want to add?"))     #
    file.close()                                           #
    return                                                 #

def progress_check():                                      #
    file = open("my_track.txt","r",encoding="utf-8")       #
    cont = file.read()                                     #
    print(cont)                                            #
    file.close()                                           #
    return                                                 #
############################################################

###########################################################
def add_absent():                                         #
    file = open("absents.txt","a",encoding="utf-8")       #
    file.write("\n"+input("What do you want to add?"))    #
    file.close()                                          #
    return                                                #

def absents_check():                                      #
    file = open("absents.txt","r",encoding="utf-8")       #
    cont = file.read()                                    #
    print(cont)                                           #
    file.close()                                          #
    return                                                #
###########################################################

def progress_options():
    while True:
        user_inp2:str.lower = input("\n\nto add to your lab progress press 'a'\nto see your lab progress press 'p'\nto exit press 'e': ")
        if user_inp2 == 'a':
            add_progress()
        elif user_inp2 == 'p':
            progress_check()
        elif user_inp2 == 'e':
            print("Leaving progress options")
            break
        
    return " "

def absents_options ():
    while True:
        user_inp3:str.lower = input("\n\nto add to your absents press 'a'\nto see your absents press 'p'\nto exite press 'e': ")
        if user_inp3 == 'a':
            add_absent()
        elif user_inp3 == 'p':
            absents_check()
        elif user_inp3 == 'e':
            print("Leaving absent options")
            break
    return " "