from itertools import cycle
from datetime import timedelta
from datetime import date

shifts = ['Morning', 'Night', 'Rest1', 'Rest2']
shiftNames = ['A','C','B','D']
refShifts = zip(shiftNames, shifts)
refDate = date(2018,12,17)

def getShift(date1, shiftofDay1, date2):
    '''
date1 --->> This is the day which I know what shift it is.
shiftofDay1 --->> This is ths shift belongs to date1, its value belongs to [shifts] list.
date2 --->> This is the day which I want to know which shift it is.
'''
    
    global shifts
    
    shiftsCycle = cycle(iter(shifts))    
    #Setting position of shiftsCycle at the starting point which is the associated shift shiftofDay1.
    initShift = next(shiftsCycle)
    while initShift != shiftofDay1 :
        initShift = next(shiftsCycle)
    #================================================================================================
        
    deltadays = date2 - date1
    for i in range(deltadays.days):
        shiftOfDay2 = next(shiftsCycle)

    return(shiftOfDay2)


def shiftsMap(xdate):
    '''
xdate --->> What will be the shifts schedule at this date?
'''
    global refShifts
    global refDate    

    for each in refShifts:
        print(each[0], '-->> ', getShift(refDate, each[1], xdate))

    #Resetting iterables.
    global shiftNames
    global shifts
    refShifts = zip(shiftNames, shifts)
   


  

    

    
    
    
