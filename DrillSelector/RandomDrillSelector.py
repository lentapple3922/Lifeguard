import MainFunctions
from MainFunctions import*
print('Are we open sundays?')
sundays = input()
if sundays == 'Yes':
    sundays = 1
elif sundays == 'No':
    sundays = 0
i = 1
while i < 3:
    print(RandomPersonSelector(RandomShiftSelector(RandomDaySelector(sundays))))
    i = i + 1
