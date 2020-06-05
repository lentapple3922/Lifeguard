import random, sys
def RandomListPick(List):   #This is a simple fuction to take the length of a list and return it
    return random.randint(0, (len(List) - 1))


def RandomDaySelector(Sundays):#This is to select a random day of the week,
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







