from math import ceil
test_h = int(input("Enter the Height of the wall: "))
test_w = int(input("Enter the Width of the wall: "))
coverage = 5

def paint_cal(height, width, cover):
    total_cans = ceil((height * width) / cover)
    print(f"Total number of cans needed is {total_cans}")
    
paint_cal(height = test_h, width = test_w, cover = coverage)
