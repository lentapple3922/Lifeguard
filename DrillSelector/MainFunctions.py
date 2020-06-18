import random, sys
def RandomListPick(List):   #This is a simple fuction to take the length of a list and return it
    return random.randint(0, (len(List) - 1))  #this returns a random number from the length of the list

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
        return 'Monday', Monday[indexNumber]
    elif Weekday == 'Tuesday':
        indexNumber = RandomListPick(Tuesday)
        return 'Tuesday', Tuesday[indexNumber]
    elif Weekday == 'Wednesday':
        indexNumber = RandomListPick(Wednesday)
        return 'Wednesday', Wednesday[indexNumber]
    elif Weekday == 'Thursday':
        indexNumber = RandomListPick(Thursday)
        return 'Thursday', Thursday[indexNumber]
    elif Weekday == 'Friday':
        indexNumber = RandomListPick(Friday)
        return 'Friday', Friday[indexNumber]
    elif Weekday == 'Saturday':
        indexNumber = RandomListPick(Saturday)
        return 'Saturday', Saturday[indexNumber]
    elif Weekday == 'Sunday':
        indexNumber = RandomListPick(Sunday)
        return 'Sunday', Sunday[indexNumber]
    else:  #I see no way this could be used in the actuall program but it exits the program if there is a value not stored, more for redundency
        print('Not a valid day')
        sys.exit()


def RandomPersonSelector(dayAndShift):  #This is to take the day picked and shift picked and then choose a person that is working
    print('How many people are working on' + str(dayAndShift) +'?' )
    numberOfEmployees = int(input())
    #print('Who is working on ' + str(dayAndShift) + ' ? Type one person at a time')
    employees = []
    #print('Any more?')
    #answer = str(input())
    l = 0
    while l < numberOfEmployees:
        print('Type there name')
        employee2 = str(input())
        employees.append(employee2)
        l = l + 1
    luckyPerson = RandomListPick(employees)
    return employees[luckyPerson]




print(RandomPersonSelector(RandomShiftSelector(RandomDaySelector(1))))


