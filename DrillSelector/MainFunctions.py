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

def RandomShiftSelector(Weekday):  #This is a function to randomly select the shift for the day selected
    Monday = ['6:00 - 9:30', '9:30 - 1:00', '1:00 - 4:30', '4:30 - 7:30']  #Lists of all the shifts for each day
    Tuesday = ['6:00 - 9:30', '9:30 - 1:00', '1:00 - 4:30', '4:30 - 7:30']
    Wednesday = ['6:00 - 9:30', '9:30 - 1:00', '1:00 - 4:30', '4:30 - 7:30']
    Thursday = ['6:00 - 9:30', '9:30 - 1:00', '1:00 - 4:30', '4:30 - 7:30']
    Friday = ['6:00 - 9:30', '9:30 - 1:00', '1:00 - 4:30', '4:30 - 7:30']
    Saturday = ['6:45 - 10:00', '10:00 - 1:30']
    Sunday = ['closed']
    if Weekday == 'Monday':  #selects a weekday variable from the return string from RandomDaySelector
        indexNumber = RandomListPick(Monday)
        return Monday [indexNumber], "Monday"
    elif Weekday == 'Tuesday':
        indexNumber = RandomListPick(Tuesday)
        return Tuesday [indexNumber], "Tuesday"
    elif Weekday == 'Wednesday':
        indexNumber = RandomListPick(Wednesday)
        return Wednesday [indexNumber], "Wednesday"
    elif Weekday == 'Thursday':
        indexNumber = RandomListPick(Thursday)
        return Thursday [indexNumber], "Thurday"
    elif Weekday == 'Friday':
        indexNumber = RandomListPick(Friday)
        return Friday [indexNumber], "Friday"
    elif Weekday == 'Saturday':
        indexNumber = RandomListPick(Saturday)
        return Saturday [indexNumber], "Saturday"
    elif Weekday == 'Sunday':
        indexNumber = RandomListPick(Sunday)
        return Sunday [indexNumber], "Sunday"
    else:  #I see no way this could be used in the actuall program but it exits the program if there is a value not stored, more for redundency
        print('Not a valid day')
        sys.exit()


def RandomPersonSelector(dayAndShift):  #This is to take the day picked and shift picked and then choose a person that is working
    print('How many people are working on ' + str(dayAndShift) + ' ?')
    employees = [str(input())]  #Need to make a plan on how to convert user input into a list not just one string
    return employees


print(RandomPersonSelector(RandomShiftSelector(RandomDaySelector(1))))





