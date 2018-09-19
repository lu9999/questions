# 1  0  1  1  0
# 1  0  0  0  1
# 0  1  1  1  0
# 0  0  0  1  0
# 1  1  0  1  0
# 
# a n*n metrics as 2D array, give distance r, get a integral image as below
# r=1
# 2  3  2  3  2
# 3  5  5  5  3
# .....
#

# 1 normal way
import copy

input_array = [[1,0,1,1,0],[1,0,0,0,1],[0,1,1,1,0],[0,0,0,1,0],[1,1,0,1,0]]
r = 1

def get_integral_loop_one_by_one(input_array, r):
    final_image = []
    for row in range(0, len(input_array)):
        x_l = row - r if (row - r) > 0 else 0
        x_h = row + r if (row + r) < len(input_array) - 1 else len(input_array) - 1
        current_row = []
        for col in range(0, len(input_array[row])):
            y_l = col - r if (col - r) > 0 else 0
            y_h = col + r if (col + r) < len(input_array[row]) - 1 else len(input_array[row]) - 1

            current_item = 0

            # for x in range(x_l, x_h+1):
            #     for y in range(y_l, y_h+1):
            #         current_item += input_array[x][y]
            
            current_item = sum([input_array[x][y] for x in range(x_l, x_h+1) for y in range(y_l, y_h+1)])
            current_row.append(current_item)
        final_image.append(current_row)
    return final_image

def get_integral_loop_one_by_one_add_back(input_array, r):
    output_array = copy.deepcopy(input_array)
    for x in range(0, len(input_array)):
        for y in range(0, len(input_array[x])):
            current_value = input_array[x][y]
            if current_value > 0:
                x_l = x-r if (x-r) > 0 else 0
                x_h = x+r if x+r < len(input_array)-1 else len(input_array)-1
                y_l = y-r if (y-r) > 0 else 0
                y_h = y+r if y+r < len(input_array[x])-1 else len(input_array[x])-1 
                
                for n in range(x_l, x_h+1):
                    for m in range(y_l, y_h+1):
                        if n!=x or m!=y:
                            output_array[n][m] += current_value
    return output_array

# TODO ref_array correct, rest wrong, too complex
def get_integral_intergral_image_way(input_array, r):
    output_array = copy.deepcopy(input_array)

    ref_array = copy.deepcopy(input_array)
    for x in range(0, len(input_array)):
        for y in range(0, len(input_array[x])):
            if x==0 and y==0:
                pass
            elif x==0:
                ref_array[0][y] += ref_array[0][y-1]
            elif y==0:
                ref_array[x][0] += ref_array[x-1][0]
            else:
                ref_array[x][y] += ref_array[x-1][y] + ref_array[x][y-1] - ref_array[x-1][y-1]
    print ref_array

    for x in range(1, len(input_array)):
        for y in range(1, len(input_array[x])):
            x1 = x+r if x+r < len(input_array)-1 else len(input_array)-1
            y1 = y+r if y+r <len(input_array[x])-1 else len(input_array[x])-1
            x2 = x-r if x-r > 0 else 0
            y2 = y-r if y-r > 0 else 0
            output_array[x][y] = ref_array[x1][y1] - ref_array[x2][y2] - ref_array[x2][y1] - ref_array[x1][y2]
    return output_array

def get_integral_slide_window(input_array, r):
    output_array = copy.deepcopy(input_array)
    for row in range(0,len(input_array)):
        win_list = []

        up = row-r if row-r > 0 else 0
        down = row+r if row+r < len(input_array[row])-1 else len(input_array[row])-1
        print up, " ", down

        for col in range(0, len(input_array[row])):
            win_list.append(sum([input_array[z][col] for z in range(up,down+1)]))
        print win_list

        start = sum([win_list[z] for z in range(0,r)])
        print start
        for col in range(0, len(input_array[row])):
            output_array[row][col] = start
            if col-r > 0:
                output_array[row][col] -= win_list[col-r-1]
            if col+r < len(input_array[row])-1:
                output_array[row][col] += win_list[col+r]
    return output_array


print get_integral_loop_one_by_one(input_array, 1)
print get_integral_loop_one_by_one_add_back(input_array, 1)
print get_integral_slide_window(input_array, 1)


            