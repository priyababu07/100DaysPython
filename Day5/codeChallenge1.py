heights = input("Student heights: ")
height_list = heights.split()

sum_height = 0
for height in height_list:
    sum_height += int(height)

average_height = round(sum_height / len(height_list))
print("Average height:", average_height)


