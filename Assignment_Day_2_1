# Q1 Create a function to return a frequency distribution of a given sequence of values
# f = frequency( 2,2,9,1,2,2,1,4,2,2,3,1) print(f) # {2:6,1:3, 9:1,4:1,3:1}

def freq_dist(numbers):
    
    # create empty dictionary at first
    freq = {}
    for x in numbers:
        """if(x in freq):
            freq[x] += 1
        else:
            freq[x] = 1"""
        
        # more readable but same performance
        freq[x] = freq.get(x, 0) + 1
    return freq


freq_dist([2,2,9,1,2,2,1,4,2,2,3,1])
