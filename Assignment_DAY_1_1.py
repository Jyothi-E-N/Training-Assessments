# Q1 Write a program to take "n" numbers from user and find the largest¶

no_of_inputs = int(input("Enter the number of inputs: "))

lar = 0

for i in range(no_of_inputs):
    num = int(input("Enter the number: "))
    if(lar == 0 or lar<num): lar = num

print("Largest  is: ", lar)
