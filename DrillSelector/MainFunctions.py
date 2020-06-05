import random, sys
def RandomListPick(List):   #This is a simple fuction to take the length of a list and return it
    return random.randint(0, (len(List) - 1))

#def indexNumber #make a function to replace the take index number to return its value from the list repetitive part in the functions.

def RandomDaySelector(Sundays):#This is to select a random day of the week
    if Sundays == 0:  #If we are not open sundays
        OperatingDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    elif Sundays == 1:  #If we are open sundays
        OperatingDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    else:
        print('Invald selection')
        sys.exit()
    indexNumber = RandomListPick(OperatingDays) #randomly selects a index number from the lenght of the list
    return OperatingDays[indexNumber] #returns the value in the list that is randomly selected

def RandomShiftSelector(Weekday):
    Monday = ['6:00 - 9:30', '9:30 - 1:00', '1:00 - 4:30', '4:30 - 7:30']
    Tuesday = ['6:00 - 9:30', '9:30 - 1:00', '1:00 - 4:30', '4:30 - 7:30']
    Wednesday = ['6:00 - 9:30', '9:30 - 1:00', '1:00 - 4:30', '4:30 - 7:30']
    Thursday = ['6:00 - 9:30', '9:30 - 1:00', '1:00 - 4:30', '4:30 - 7:30']
    Friday = ['6:00 - 9:30', '9:30 - 1:00', '1:00 - 4:30', '4:30 - 7:30']
    Saturday = ['6:45 - 10:00', '10:00 - 1:30']
    Sunday = ['closed']
    print('Are there Sundays? Type 0 or 1')
    SundaysValid = input()
    Day = RandomDaySelector(SundaysValid)
    if Day == 'Monday':
        indexNumber = RandomListPick(Monday)
    elif Day == 'Tuesday':
        indexNumber = RandomListPick(Tuesday)
    elif Day == 'Wednesday':
        indexNumber = RandomListPick(Wednesday)
    elif Day == 'Thursday':
        indexNumber = RandomListPick(Thursday)
    elif Day == 'Friday':
        indexNumber = RandomListPick(Friday)
    elif Day == 'Saturday':
        indexNumber = RandomListPick(Saturday)
    elif Day == 'Sunday':
        indexNumber = RandomListPick(Sunday)
    else:
        print('Not a valid day')
        sys.exit()











