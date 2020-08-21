#RelationShipGame !
import sys
def Menu_Page():
    print("\t\t\t\tWelcome to Love Calculator Program! V1.0")
    print("Things to know")
    print("1.This Program Is Built To Check Your RelationShip Status With Another Person")
    print("Your Relationship Can Be Love/Marriage/Friends/etc")
    print("Note, That This Program Doesn't Uses Random Function\nSo, You Won't Get Different Results\n"
          "Like in other stupid love calculator programs!")
    print("However The Change In Your Name or Other Person Will Differ The Result")
    print("Rules!")
    print("Only Type The Information That Is Asked !")
    print("Don't use fake names use only your real name and other persons real name!")
    print("Choose any one from the options!")
    print("1.Start The Program")
    print("2.How to use the program?")
    print("3.Information About the program")
    print("4.Exit")
    choice = input("Enter your choice 1/2/3/4: ")
    if choice == "1":
        start_program()
    elif choice == "2":
        how_to_use()
    elif choice == "3":
        Information()
    elif choice == "4":
        exit()
def start_program():
    import os
    os.system('cls')
    import os
    user_first_name = input("Enter your first name: ")
    user_last_name = input("Enter your surname: ")
    user2_first_name = input("Enter another person's first name: ")
    user2_last_name = input("Enter another person's last name: ")
    string = user_first_name + user_last_name
    string2 = user2_first_name + user2_last_name
    common_string = "" # Common_String Collector string
    common_string2 = "" # Common_String Collector for string2
    string_len = len(string) # Finding out the length of string
    string2_len = len(string2) # Finding out the length of string2
    if string_len >= string2_len: # Condition
        for x in string: # Looping to go- through every string presented in string
            for y in string2: # Looping to go- through every string presented in string2
                if x in y: # Condition for common_String
                    common_string = common_string + x
                    string = string.replace(x,'')
                    string2 = string2.replace(y,'')
    elif string2_len > string_len: # Another Condition
        for x in string: # Again Looping through every string presented
            for y in string2: # Again Looping through every string
                if y in x: # Condition for Common_String
                    common_string2 = common_string2 + y
                    string = string.replace(x,'')
                    string2 = string2.replace(y,'')
    if string_len >= string2_len:
        final_value = len(string) + len(string2)
        x = "flames"
        print(final_value)
        magical_letter = x[final_value%len(x)-1]
        print(magical_letter)
    if string2_len > string_len:
            final_value = len(string) + len(string2)
            x = "flames"
            magical_letter = x[final_value%len(x)-1]
    if magical_letter == "f":
        print("congratulations you both are friends :)")
        print(""" _________________##_________##
              _ ______________###*_______*###
              __________ _.*#####_________#####*.
              __________*######__________######*
              ________*#######____ _______#######*
              _______*########.______ ____.########*
              ______*#########.__________.#########*
              ______*######@###*_______* ###@######*
              _____*#########*###____###*#########*
              ____*##########*__*####*__*### #######*
              __*###########_____*_*______###########*
              _############_______________## ##########
              *##*#########____FRIENDS____#########*##*
              _____########______________ __########
              _______#######_____ _________#######
               ________*######________ ____######*
              _________*#####*__________*#####*
             ___________*####*________*####*
             _ ____________*####______####*
             ___________ ____*##*____*##*
              _________________*##__# #*
              __________________*####*
              ___________ ______.######.
               _______________.#########""")
        input("Press enter to close!")

    elif magical_letter == "l":
        print("congratulations you both are in love :)")
        print("""    LoveLoveLov                eLoveLoveLo
                  veLoveLoveLoveLove          LoveLoveLoveLoveLo
               veLoveLoveLoveLoveLoveL      oveLoveLoveLoveLoveLove
              LoveLoveLoveLoveLoveLoveL    oveLoveLoveLoveLoveLoveLo
             veLoveLoveLoveLoveLoveLoveL  oveLoveLoveLoveLoveLoveLove
             LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
             LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
              LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo
              veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
                LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo
                 veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
                    LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo
                      veLoveLoveLoveLoveLoveLoveLoveLoveLove
                        LoveLoveLoveLoveLoveLoveLoveLoveLo
                        veLoveLoveLoveLoveLoveLoveLove
                            LoveLoveLoveLoveLoveLoveLo
                             veLoveLoveLoveLoveLo
                                   veLoveLoveLo
                                        ve""")
        input("Press enter to close !")  

    elif magical_letter == "a":
        print("congratulation you both have Affection for eachother :)")
        print("""              __        __        __        __ 
              .*.        /~ .~\    /~  ~\    /~ .~\    /~  ~\ 
              ***       '      `\/'      *  '      `\/'      *
               V       (                .*)(               . *)
             /\|/\      \            . *./  \            . *./
               |         `\ .      . .*/'    `\ .      . .*/'       .*.
               |           `\ * .*. */' _    _ `\ * .*. */'         ***
                             `\ * */'  ( `\/'*)  `\ * */'          /\V
                               `\/'     \   */'    `\/'              |/\ 
                                         `\/'                        |
                                       Affection                      """) 
        input("Press enter to close!")                                      

    elif magical_letter == "m":
        print("Are you married ? with the other person ? if No don't worry soon you will be married :)")
        print(""".::\)`:`, 
    	       .:;\/~`\``;)                    ,.~-----,
    	       ;;==`_  ~:;(                ,,~{*}\~~--,.`.
    	      ;:==  6   6;;)             ,(((((({*});~~. .\ 
    	      ;;C      } )'             (('`)))~({*}) . \ .\ 
    	      :;`    `--';               >6  6`({*}))) . \~~
    	        |  `____/                ( {    ))())) . .`,
    	  ____._|      |_____.            `--' (((()))  .  |
    	 /    \  \__  _| |    \            `--  )))))) .  .|
    	|      )  \/\/\_{@}    |           ,-| (((((((  .  |
    	|       \_ \ \  | /    |          / | / )))))))   .|
    	|    |\   : \ |/ |  Y  |         (/*@@*( '   ` ) . |
    	\     \    \_\/_/   |  |         /  */  \ \'/ /.   |
    	 \     \     |o     |  |         \.  \   |'@'|    .|
    	  \     \    |      ; ,'--,.,.,.,  \     ~*@*~.  . |
    	   \     \_________._--`((,:{@}.:))_\    |~@~|  .  |
    	    \    '         |   ((,{@}:{@}.))-----'   ;/\   (,
    	     \._____________`-__((;,{@},:))_________/|{ | . ;
    	     |       |     |      `';{@},)   /`-----'\  |.  |
    	     |    .__/\__  |       `{@};,;  / / | \ \ \/   .|
    	     |   /   :;  \ |        `(@))\ /           \. . |
    	     |  /!   |    \|         ';; ))_/`-'/`_`.,  \.  |
    	     | | !   |     |          ';((   |   |  ! `_ \ .|
    	     | | !   |     |             ))  |   |  ! |.\_| |
    	     |/  !   |     |            (/   |   |  ! |  .  |
    	      |  !   |     |                 |   |  ! |~~~~'
    	      |  !   |     |                 |   |  ! |
    	      |  !   |     |                 |   |  ! |
    	      |  !  `|    `|                 |'  |' ! |
    	      |  !  -|    -|                 |`  |` ! |
    	      |  !   |     |                 |   |  ! |
    	      |  !   |     |                 |   |  ! |
    	      |  !   |     |                 |   |  ! |
    	      |  !   |     |                 |   |  ! |
    	      |  !   |     |                 |   |  ! |
    	      |  !   |     |                 |   |  ! |
    	      |  !   |     |                 |   |  ! |
    	      |  !   |     |                 ~~~~|~~~~~
    	      |======|=====|                 /__//__/|
    	       |     \___  \___            _/) _/)  _J
    	       L_--______)-____)          (___(____/ Y  """)

        input("Press enter to close!")       
    elif magical_letter == "e":
        print("Sorry, to say but you both are enemy")
        print("""            ,       ,
    	           /(       )`
    	           \ \__   / |
    	           /- _ `-/  '
    	          (/\/ \ \   /\ 
    	          / /   | `    \ 
     	          O O   )      |
    	          `-^--'`<     '
    	         (_.)  _ )    /
    	          `.___/`    /
    	            `-----' /
    	<----.     __ / __   \ 
    	<----|====O)))==) \) /=============
    	<----'    `--' `.__,' \ 
    	            |         |
    	             \       /
    	         ____( (_   / \______
    	       ,'  ,----'   |        \ 
    	       `--{__________)       \/""")
        input("Press enter to close!")       
    elif magical_letter == "s":
        print("you are siblings")
        print("""    .===.                 
                    / _/\ \ 
                    \/6.6\/
                    (  _  )         .===.
                    _)---(_        / ,,, \ 
                   /  `~`  \      ( /6.6\ )
                  /\/     \/\     )(  _  )(
                  \ |     | /    (_/;---;\_)
                   \|_____|/      / `"*"` \ 
                    |  L  |      ( (_.@._) )
                    |__|__|      /'._\|/_.'\ 
                     | | |      /. . . . . .\ 
                     |_|_|      `"`"|"|"|"`"`
                    _|_|_|_        _|_|_|_
                   (___|___)      (___|___) """)
        input("Press enter to close!")
def how_to_use():
    import os
    os.system('cls')
    print("This program is simple to use")
    print("just provide your first name while the program ask you to enter your first name")
    print("But, keep in mind that you should only provide your first name in the section not your last name as well")
    print("Then program will ask you to provide your last name, Provide the program with your last name only!")
    print("Then program will ask you to enter another person first name, provide the program with another person's first name only!")
    print("Then program will ask you to enter another person last name, provide the program with another person last name only!")
    print("After this your are done the program will automatically, tell you your results!")
    print("your result can be like friends,love,marriage, etc")
    print("Have fun ;)")
    input("Press enter to close!")
def Information():
    #information
    import os
    import sys
    os.system('cls')
    print("Welcome to information page:")
    print("This program was created using python programming language!")
    print("Coded using visual studio code IDE")
    print("python version: {}".format(sys.version))
    print("Works fine on windows 10, haven't tested on other opearting system platform.")
    input("Press enter to close!")
def exit():
    #exit
    import time
    import sys
    import os
    os.system('cls')
    print("Exiting...............")
    time.sleep(2.5)
    sys.exit()
Menu_Page()