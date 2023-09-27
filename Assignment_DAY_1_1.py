# Q1 Write a program to take "n" numbers from user and find the largest¶

inp_string = str(input("Enter the n numbers separated by spaces: "))
num_list = inp_string.split(" ")

largest = int(num_list[0])
for x in num_list:
    if(largest<int(x)):
        largest = int(x)
print("Largest of all is :", x)
