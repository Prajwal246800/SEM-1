import datetime

events = []
while True:
    print()
    '''This loop is to take multiple inputs'''
    event ={}
    while True:
        '''To check whether name is empty if empty ask again
        '''
        event['name'] = input("Enter the name of the event:")
        if len(event['name'])==0:
            print('Name of event cannot be empty')
        else:
            event['name']=event['name'].capitalize()
            break
    event['detail'] = input("Enter details about the event:")        
    while True:
        '''this loop is used to input date
            and check whether the date is valid or not
            if not valid asking to re-enter and if valid proceed
        '''       
        while True:            
            try:
                eventdate =(input("Enter the date of the event (YYYY-MM-DD): "))
                event['date']=eventdate
                year,month,day =event['date'].split("-")
                break               
            except ValueError:
                print("Enter sufficient date")
                pass
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            print("Enter valid date")
            '''this if is used to check whether the date entered
                is all digits or any characters
                if characters present it returns not valid and
                ask to re-enter and if it is correct proceed
            '''            
        else:
            year,month,day = int(year),int(month),int(day)          
            if month not in range(1,13):
                print("Enter valid date")
                '''this is to check whether the
                    month is valid or not
                '''             
            elif day not in range(1,32):
                print("Enter valid date")
                '''this is to check whether the
                    day is valid or not
                '''              
            elif (month == 2) and ((year%4==0 and day>29) or (year%4!=0 and day>28)):
                print("Enter valid date")
                '''this is check whether the
                    year is leap year or not 
                    if yes check for date entered and 
                    if month is February check date is valid or not
                '''              
            else:
                '''this is to check whether the date
                    entered is after today's date or not
                '''
                date_obj=datetime.datetime(year,month,day)                
                if date_obj>datetime.datetime.now():
                    break                  
                else:
                    a=(input("The date entered is already over would you like to continue (y/n)"))                   
                    if a[0]=='y' or a[0]=='Y':
                        break
                    else:
                        pass
    event['people'] = input("Enter the names of the people attending the event, separated by a comma: ").split(',')
    event['people']=[a.capitalize() for a in event['people']]
    events.append(event) #append dictionary to a list  
    a=input("Will you enter another event (y/n)")
    if a[0]=='n' or a[0]=='N':
        break
print('\n'*2)
events=[list(d.values()) for d in events]    #converting list of dictionary to list of list
events.sort(key=lambda x:x[2])    #sorting according to date
print()

for i in events:
    print('Name of Event    : ',i[0])
    print('Details of Event :  ',end='')
    if len(i[1])==0:
        print('No Details given')
    else:
        print(i[1])
    print('Date of Event    : ',i[2])
    print('People Attending : ',','.join(i[3]))
    print()
print(' '*5,end='')
print('Thank You for Giving Such a Wonderful mini Project\n',' '*8,'It Made us understand more about PYTHON\n',' '*13,'We Enjoyed a Lot')
print()
print(' '*5,'Program By Team of UNITY',"👬👬")
print('Team Leader\n','Ankith Gowda B S \n''Team Members\n','Chetan Subash\n','D Vidya Sagar')