# Assignemnt Day #3
# print the calendar vertically like below
# Sun         4    11    18    25
# Mon         5    12    19    26
# Tue         6    13    20    27
# Wed         7    14    21    28
# Thu    1    8    15    22    29    
# Fri    2    9    16    23    30
# Sat    3    10   17    24    31

def print_dates_in_week_day(start_date, days):
    
    # print the consecutive dates in a week day (like sunday or monday)
    
    # use for loop
    
    for i in range(4):
        print(start_date + (7 * i), end = '\t')
    
    ## print(start_date,  (start_date + 7), (start_date + 14), (start_date + 21),sep="\t", end = '\t')
            
    if((start_date + 28) <= days):
        print( (start_date + 28), end = '')
    print()

def print_calendar_vertically(month, year):
    
    # to print week days, create a list of all days in week
    week_days = ["Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    
    # get the starting day position of the given month
    start_day_pos = date_to_week_day(1, month, year)
    
    # get the total days in the given month
    days = days_in_month(month, year)
    
    # for loop's gonna run for the 7 times as there are 7 days in a week
    for i in range(7):
        
        print(week_days[i], end='\t')
        
        
        if(i < start_day_pos):
            
            # since month hasn't started with this day yet give tab space initially
            print('\t', end = '')
            
            start_date_in_row = (7 - start_day_pos) + i + 1
            
        else:
            
            start_date_in_row = (i - start_day_pos) + 1
        
        print_dates_in_week_day(start_date_in_row, days)
        print("\n")
        
  print_calendar_vertically(1, 1948)
