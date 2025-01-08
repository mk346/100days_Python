# 😬 ◻
row1 = ["◻","◻","◻"] #index 0
row2 = ["◻","◻","◻"] #index 1
row3 = ["◻","◻","◻"] #index 2
map = [row1, row2, row3]

#print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

#12 column 1 row 2
digits = [int(digit) for digit in str(position)]
#print(digits[1])
column = digits[0]
row = digits[1]

#print(type(column), type(row))

# input_map = map.append(di)
#32
map[row-1][column-1] = "x"

#map = [[1], [2], [3]
print(f"{row1}\n{row2}\n{row3}")


