#Project Cakken "Average Data"

amount_data = int(input("Input Amount Of Data : "))

mark = []

for i in range(amount_data) :
    n = int(input(f"Input Mark of-{i+1}: "))
    mark.append(n)


average = sum(mark) / (amount_data)
print("\nAmount Data :", (mark))
print("Sum Mark  :", sum(mark))
print("Average   :", average)

if(average) >= 80 :
    print("Pass Satidfied")
elif(average) >= 70:
    print("Pass")
else :
    print("Not Pass")
