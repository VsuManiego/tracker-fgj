import sys


TOOL_DATE = []
TOOL_NAME = []
TOOL_DESCRIPTION = []
TOOL_COUNT = []
TOOL_SUPPLIER_NAME = []
TOOL_SUPPLIER_COMPANY_NAME = []
TOOL_SERIAL_NUMBER = []


InformationFile = open('Information.txt', 'a')
def ADD_TOOL_INFORMATION():
    addLoop = True
    while addLoop == True:

        print("ADDING TOOL INFORMATION : \n")        
        DATE = input("ENTER DATE (MM/DD/YY) :")
        TOOL_DATE.append(DATE)       
     
        NAME = input("ENTER TOOL NAME :").upper()
        TOOL_NAME.append(NAME)      
    
        DESCRIPTION = input("ENTER TOOL DESCRIPTION :").upper()
        TOOL_DESCRIPTION.append(DESCRIPTION)
        
        COUNT = int(input("ENTER TOOL COUNT :"))
        TOOL_COUNT.append(COUNT)
      
        SUPPLIER_NAME = input("ENTER TOOL SUPPLIER NAME :").upper()
        TOOL_SUPPLIER_NAME.append(SUPPLIER_NAME)
        
        SUPPLIER_COMPANY_NAME = input("ENTER TOOL SUPPLIER COMPANY NAME :").upper()
        TOOL_SUPPLIER_COMPANY_NAME.append(SUPPLIER_COMPANY_NAME)
       
        
        SERIAL_NUMBER = int(input("ENTER TOOL SERIAL NUMBER :"))
        TOOL_SERIAL_NUMBER.append(SERIAL_NUMBER)
        print(NAME + ' WAS ADDED SUCCESSFULLY.')
        print("\n")  
        
        addExit = input("Enter q to add again or any to go back to main menu")
        print(addExit)
        if addExit != 'q':
            addLoop = False        
        
        InformationFile.write(NAME + '\n')
        InformationFile.write(DATE + '\n')
        InformationFile.write(DESCRIPTION + '\n')
        InformationFile.write(str(COUNT))
        InformationFile.write(SUPPLIER_NAME + '\n')
        InformationFile.write(SUPPLIER_COMPANY_NAME + '\n')
        InformationFile.write(str(SERIAL_NUMBER))
        InformationFile.close()
        

TOOL_BORROWER = []
TOOL_DATE = []
TOOL_TIME = []
TOOL_NAME = []
TOOL_DESCRIPTION = []
TOOL_COUNT = []
TOOL_RETURNED = []



def BORROW_TOOL_INFORMATION():
    addLoop = True
    while addLoop == True:
        print("BORROWING TOOL INFORMATION : \n")
        BORROWER = input("ENTER YOUR NAME :")
        TOOL_BORROWER.append(BORROWER)
              
        DATE = input("ENTER DATE (MM/DD/YY) :")
        TOOL_DATE.append(DATE)
              
        TIME = int(input("ENTER TIME [H]:[M]:[S] :"))
        TOOL_COUNT.append(TIME)
               
        NAME = input("ENTER TOOL NAME :").upper()
        TOOL_NAME.append(NAME)
       
        DESCRIPTION = input("ENTER TOOL USAGE :").upper()
        TOOL_DESCRIPTION.append(DESCRIPTION)
       
        COUNT = int(input("ENTER TOOL COUNT :"))
        TOOL_TIME.append(COUNT)
               
        RETURNED = int(input("ENTER APPROXIMATE TIME RETURNED :"))
        TOOL_RETURNED.append(RETURNED)
        print (BORROWER + ' BORROWED A TOOL.')
        
        addExit = input("Enter q to add again or any to go back to main menu")
        print(addExit)
        if addExit != 'q':
            addLoop = False
 
def DELETE_TOOL_INFORMATION():
    addLoop = True
    while addLoop == True:
        print("DELETING STUDENT INFORMATION : \n")      
        tool = input("FROM WHICH INFORMATIONS YOU WANT TO DELETE: ADD/BORROW ").upper()        
        if len(TOOL_SERIAL_NUMBER) == 0:
            print("\n")
            print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY")
            print("\n")
        else:           
            SERIAL_NUMBER = int(input("ENTER SERIAL NUMBER :"))
            NAME = input("ENTER TOOL NAME :").upper()
            LOC = TOOL_SERIAL_NUMBER.index(SERIAL_NUMBER)

            TOOL_SERIAL_NUMBER.remove(TOOL_SERIAL_NUMBER[LOC])
            TOOL_NAME.remove(TOOL_NAME[LOC])
            TOOL_DATE.remove(TOOL_DATE[LOC])
            TOOL_DESCRIPTION.remove(TOOL_DESCRIPTION[LOC])
            TOOL_COUNT.remove(TOOL_COUNT[LOC])
            TOOL_SUPPLIER_NAME.remove(TOOL_SUPPLIER_NAME[LOC])
            TOOL_SUPPLIER_COMPANY_NAME.remove(TOOL_SUPPLIER_COMPANY_NAME[LOC])

            print("\n")
            print(NAME + " TOOL INFORMATION DELETED SUCCESSFULLY.")
            print("\n")
            
            addExit = input("Enter q to add again or any to go back to main menu")
            print(addExit)
            if addExit != 'q':
                addLoop = False
        
        if len(TOOL_BORROWER) == 0:
            print("\n")
            print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY")
            print("\n")
        else:
            BORROWER = (input("ENTER NAME OF BORROWER :"))
            LOC = TOOL_BORROWER.index(BORROWER)

            TOOL_BORROWER.remove(TOOL_BORROWER[LOC])
            TOOL_DATE.remove(TOOL_DATE[LOC])
            TOOL_TIME.remove(TOOL_TIME[LOC])
            TOOL_NAME.remove(TOOL_NAME[LOC])
            TOOL_DESCRIPTION.remove(TOOL_DESCRIPTION[LOC])
            TOOL_COUNT.remove(TOOL_COUNT[LOC])
            TOOL_RETURNED.remove(TOOL_RETURNED[LOC])
            print("\n")
            print(BORROWER + "'s BORROW INFORMATION DELETED SUCCESSFULLY.")
            print("\n")
	        
            addExit = input("Enter q to add again or any to go back to main menu")
            print(addExit)
            if addExit != 'q':
                addLoop = False
def UPDATE_TOOL_INFORMATION():
    addLoop = True
    while addLoop == True:
        print("UPDATING TOOL INFORMATION : \n")      
        tool = input("FROM WHICH INFORMATIONS YOU WANT TO UPDATE: ADD/BORROW ").upper()   
        
        if tool == " ADD ":
            if tool != 'ADD': 
                tool = False
        elif len(TOOL_SERIAL_NUMBER) == 0:
            print("\n")
            print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY")
            print("\n")
        else:
            print("LIKE NAME, DATE, DESCRIPTION, COUNT, SUPPLIER NAME, SUPPLIER COMPANY NAME, SERIAL NUMBER.")
            ATTRIBUTE = input("ENTER TOOL ATTRIBUTE YOU WANT TO UPDATE :").upper()  
            if ATTRIBUTE == 'DATE':
                OLD_DATE = input("ENTER 'OLD DATE' :")
                LOC_DATE = TOOL_DATE.index(OLD_DATE)
                
                NEW_ROLL = input("ENTER 'DATE UPDATED' :")
                TOOL_DATE[LOC_DATE] = NEW_DATE
                print("\t DATE UPDATED SUCCESSFULLY.")
                print("\n")  

            elif ATTRIBUTE == 'NAME':
                OLD_NAME = input("ENTER OLD NAME :").upper()
                LOC_NAME = TOOL_NAME.index(OLD_NAME)

                NEW_NAME = input("ENTER NEW NAME :")
                TOOL_NAME[LOC_NAME] = NEW_NAME
                print("\t NAME UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'DESCRIPTION':             
                OLD_DESCRIPTION = input("ENTER 'OLD DESCRIPTION' :")
                LOC_DESCRIPTION = TOOL_DESCRIPTION.index(OLD_DESCRIPTION)

                NEW_DESCRIPTION = input("ENTER 'NEW DESCRIPTION' :")
                TOOL_DESCRIPTION[LOC_DESCRIPTION] = NEW_DESCRIPTION
                print("\t DESCRIPTION UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'COUNT':
                OLD_COUNT = int(input("ENTER 'OLD COUNT' :"))
                LOC_ROLL = TOOL_COUNT.index(OLD_COUNT)

                NEW_COUNT = int(input("ENTER 'NEW COUNT' :"))
                TOOL_COUNT[LOC_ROLL] = NEW_COUNT
                print("\t COUNT UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'SUPPLIER NAME':
                OLD_SUPPLIER_NAME = input("ENTER 'OLD SUPPLIER NAME' :")
                LOC_SUPPLIER_NAME = TOOL_SUPPLIER_NAME.index(OLD_SUPPLIER_NAME)

                NEW_SUPPLIER_NAME = input("ENTER 'NEW SUPPLIER NAME' :")
                TOOL_SUPPLIER_NAME[LOC_SUPPLIER_NAME] = NEW_SUPPLIER_NAME
                print("\t SUPPLIER NAME UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'SUPPLIER COMPANY NAME':
                print("ENTER 'OLD SUPPLIER COMPANY NAME' :", end=" ")
                OLD_SUPPLIER_COMPANY_NAME = input()
                LOC_SUPPLIER_COMPANY_NAME = TOOL_SUPPLIER_COMPANY_NAME.index(OLD_SUPPLIER_COMPANY_NAME)

                NEW_SUPPLIER_COMPANY_NAME = input("ENTER 'NEW SUPPLIER COMPANY NAME' :")
                TOOL_SUPPLIER_COMPANY_NAME[LOC_SUPPLIER_COMPANY_NAME] = NEW_SUPPLIER_COMPANY_NAME
                print("\t SUPPLIER COMPANY NAME' UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'SERIAL NUMBER':
                OLD_SERIAL_NUMBER = int(input("ENTER 'OLD SERIAL NUMBER' :"))
                LOC_ROLL = TOOL_SERIAL_NUMBER.index(OLD_SERIAL_NUMBER)

                NEW_SERIAL_NUMBER = int(input("ENTER 'NEW SERIAL NUMBER' :"))
                TOOL_SERIAL_NUMBER[LOC_ROLL] = NEW_SERIAL_NUMBER
                print("\t SERIAL NUMBER UPDATED SUCCESSFULLY.")
                print("\n")
        addExit = input("Enter q to add again or any to go back to main menu")
        print(addExit)
        if addExit != 'q':
            addLoop = False       
        
        if tool == " BORROW ":
            if tool != 'BORROW': 
                tool = False
        elif len(TOOL_COUNT) == 0:
            print("\n")
            print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY")
            print("\n")
    
        else:
            print("LIKE BORROWER, DATE, TIME, COUNT, NAME, DESCRIPTION, RETURNED.")
            ATTRIBUTE = input("ENTER TOOL ATTRIBUTE YOU WANT TO UPDATE :").upper()  
            if ATTRIBUTE == 'BORROWER':
                OLD_BORROWER = input("ENTER 'OLD BORROWER' :")
                LOC_BORROWER = TOOL_BORROWER.index(OLD_BORROWER)
                
                NEW_BORROWER = input("ENTER 'NEW BORROWER' :")
                TOOL_BORROWER[LOC_BORROWER] = NEW_BORROWER
                print("\t BORROWER UPDATED SUCCESSFULLY.")
                print("\n") 
            elif ATTRIBUTE == 'DATE':
                OLD_DATE = input("ENTER 'OLD DATE' :")
                LOC_DATE = TOOL_DATE.index(OLD_DATE)
                
                NEW_ROLL = input("ENTER 'DATE UPDATED' :")
                TOOL_DATE[LOC_DATE] = NEW_DATE
                print("\t DATE UPDATED SUCCESSFULLY.")
                print("\n")    
                    
            elif ATTRIBUTE == 'TIME':
                OLD_TIME = int(input("ENTER 'OLD TIME' :"))
                LOC_ROLL = TOOL_TIME.index(OLD_TIME)

                NEW_TIME = int(input("ENTER 'NEW TIME' :"))
                TOOL_TIME[LOC_ROLL] = NEW_TIME
                print("\t TIME UPDATED SUCCESSFULLY.")
                print("\n")
                    
            elif ATTRIBUTE == 'NAME':
                OLD_NAME = input("ENTER OLD NAME :").upper()
                LOC_NAME = TOOL_NAME.index(OLD_NAME)

                NEW_NAME = input("ENTER NEW NAME :")
                TOOL_NAME[LOC_NAME] = NEW_NAME
                print("\t NAME UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'DESCRIPTION':             
                OLD_DESCRIPTION = input("ENTER 'OLD USAGE' :")
                LOC_DESCRIPTION = TOOL_DESCRIPTION.index(OLD_DESCRIPTION)

                NEW_DESCRIPTION = input("ENTER 'NEW USAGE' :")
                TOOL_DESCRIPTION[LOC_DESCRIPTION] = NEW_DESCRIPTION
                print("\t DESCRIPTION UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'COUNT':
                OLD_COUNT = int(input("ENTER 'OLD COUNT' :"))
                LOC_ROLL = TOOL_COUNT.index(OLD_COUNT)

                NEW_COUNT = int(input("ENTER 'NEW COUNT' :"))
                TOOL_COUNT[LOC_ROLL] = NEW_COUNT
                print("\t COUNT UPDATED SUCCESSFULLY.")
                print("\n")
                    
            elif ATTRIBUTE == 'RETURNED':
                OLD_RETURNED = int(input("ENTER 'OLD APPROXIMATE TIME RETURNED' :"))
                LOC_ROLL = TOOL_RETURNED.index(OLD_RETURNED)

                NEW_RETURNED = int(input("ENTER 'NEW TIME RETURNED' :"))
                TOOL_RETURNED[LOC_ROLL] = NEW_RETURNED
                print("\t TIME RETURNED UPDATED SUCCESSFULLY.")
                print("\n")
            
        addExit = input("Enter q to add again or any to go back to main menu")
        print(addExit)
        if addExit != 'q':
            addLoop = False       

def PRINT_TOOL_INFORMATION():
        print("DISPLAYING TOOLS INFORMATION : \n")

        if len(TOOL_DATE) == 0 and len(TOOL_NAME) == 0 and len(TOOL_DESCRIPTION) == 0 and len(
                TOOL_COUNT) == 0 and len(TOOL_SUPPLIER_NAMER) == 0 and len(TOOL_SUPPLIER_COMPANY_NAME) == 0 and len(
                TOOL_SERIAL_NUMBER) == 0:
            print("\n")
            print("\t\t\t 'OOPS ! NOTHING TO DISPLAY, BECAUSE NO DATA IS THERE.")
            print("\n")
        else:
            print("DATE ON : ", end="\n")

            for x in TOOL_DATE:
                print(x)
            print()

            print(end="\n")

            print("NAME OF TOOL :", end="\n")

            for y in TOOL_NAME:
                print(y)
            print()

            print(end="\n")

            print("DESCRIPTION :", end="\n")

            for z in TOOL_DESCRIPTION:
                print(z)
            print()

            print(end="\n")

            print("NUMBER OF TOOL :", end="\n")

            for x in TOOL_COUNT:
                print(x)
            print()

            print(end="\n")

            print("SUPPLIER'S NAME :", end="\n")

            for y in TOOL_SUPPLIER_NAME:
                print(y)
            print()

            print(end="\n")

            print("SUPPLIERS COMPANY NAME :", end="\n")

            for z in TOOL_SUPPLIER_COMPANY_NAME:
                print(z)
            print()

            print(end="\n")

            print("TOOL SERIAL NUMBER :", end="\n")

            for x in TOOL_SERIAL_NUMBER:
                print(x)
            print()

            print(end="\n")            
    
    
                    
if __name__ == '__main__':
    print("\n")
    print("\t\t\t\t              WELCOME TO TOOL USAGE TRACKER SYSTEM               \n")
    run = True

    while run:
        print("PRESS FROM THE FOLLOWING OPTION : \n")

        print("PRESS 1 : ADD")
        print("PRESS 2 : BORROW")
        print("PRESS 3 : DELETE")
        print("PRESS 4 : UPDATE")
        print("PRESS 5 : PRINT")
        print("PRESS 6 : EXIT")

        OPTION = int(input("ENTER YOUR OPTION : "))
        print("\n")
        print(end="\n")

        if OPTION == 1:
            ADD_TOOL_INFORMATION()
        elif OPTION == 2:
            BORROW_TOOL_INFORMATION()
        elif OPTION == 3:
           DELETE_TOOL_INFORMATION()
        elif OPTION == 4:
           UPDATE_TOOL_INFORMATION()
        elif OPTION == 5:
            PRINT_TOOL_INFORMATION()
        elif OPTION == 6:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
        else:
            print("PLEASE CHOOSE CORRECT OPTION FROM THE FOLLOWING.")
            print("\n")



