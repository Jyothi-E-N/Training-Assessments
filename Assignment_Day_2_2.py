# Q2 Create a Historgram for a given frequency table
# we are NOT using any external or builtin libraries plot_historgram({2:6,1:3, 9:2,4:3,3:1})
# 2 | ================== 6
# 1 | ========= 3
# 9 | ====== 2
# 4 | ========= 3
# 3 | === 1

def print_histogram(freq_dict):
    
    for ind  in freq_dict:
        print(ind, end = ' | ')
        print("===" * freq_dict[ind], end = ' ')
        print(freq_dict[ind])

print_histogram({2:6,1:3, 9:2,4:3,3:1})
