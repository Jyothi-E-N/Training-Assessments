# Assignemnt 4.2
# rewrite histogram function to add follwoing customization

# we can change the design of the bar which defaults to '==='
#   2 | +++++ ++++++ ++++++ +++++ 4
#   9 | +++++ 1
#   11 | +++++ 

# we may want to hide the extact freq value which shoukd be
# 2 | +++++ ++++++ ++++++ +++++ 
# 9 | +++++ 
# 11 | +++++ 
# we may want to align the frequency value (default false)

# 2 | +++++ ++++++ ++++++ +++++ 4
# 9 | +++++                     1
# 11 | +++++ 

def print_histogram(freq_dict, design = '===', show = True, align = False):
    max_freq = max(freq_dict.values())
    
    for ind  in freq_dict:
        print(ind, end = ' | ')
        print(design * freq_dict[ind], end = ' ')
        
        if(align): 
            print((max_freq - freq_dict[ind]) * ((' '*len(design))), end = '')
        if(show): 
            print(freq_dict[ind])
        else:
            print()

print_histogram({2:6,1:3, 9:2,4:3,3:1}, align=True, show=True, design=':::::')
