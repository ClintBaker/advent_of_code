# largest area of a rectangle
# we use two given coordinates as opposite corners
# fill in the gaps for rectangle

from pathlib import Path

def ingest_data(filename = 'sample.txt'):
    path = Path(__file__).with_name(filename)
    data = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data.append([int(field.strip()) for field in line.split(",")])
    return data

def find_area_between_coords(a, b):
    x = abs(a[0] - b[0]) + 1
    y = abs(a[1] - b[1]) + 1

    return x * y


def find_rectangle_areas(coordinates):
    areas = [] # [[area, index1, index2]]

    for i in range(len(coordinates)):
        for j in range(i, len(coordinates)):
            area = find_area_between_coords(coordinates[i], coordinates[j])
            areas.append([area, i, j])
    
    return areas

def find_perimeter(coordinates):
    x_values_by_row = {}
    length = len(coordinates)
    # example: {'row_num': ['x1', 'x2', 'x3']}

    # we are either moving left, right, up or down
    # define the bounds for each row
    for i in range(length):
        a = coordinates[i]
        b = []
        # define b based on special cases
        if i == (length - 1): # last coord special case
            b = coordinates[0]
        else:
            b = coordinates[i + 1]
        
        # connect to the next coord
        if a[1] == b[1]: # horizontal connection
            if a[1] not in x_values_by_row:
                x_values_by_row[a[1]] = []
            x_values_by_row[a[1]].append(a[0])
            x_values_by_row[a[1]].append(b[0])
        else: # vertical connection
            # push x value to every row in between cur_row and target_row
            direction = a[1] - b[1] # [7,1] -> [12,1] -> negative = moving down. positive = moving up
            cur_row = 0
            target_row = 0
            if direction > -1: # moving up
                cur_row = b[1]
                target_row = a[1]
            else: # moving down
                cur_row = a[1]
                target_row = b[1]
            while (cur_row != target_row):
                if cur_row not in x_values_by_row:
                    x_values_by_row[cur_row] = []
                x_values_by_row[cur_row].append(a[0])
                cur_row+=1
    # take x_values_by_row -> only keep largest and smallest for each row ->
    for row_index, x_values in x_values_by_row.items():
        x_values_by_row[row_index] = [min(x_values), max(x_values)]
    
    return x_values_by_row

def is_inbounds(coord1, coord2, x_values_by_row):
    # [11,1] [2,5]  -> the one with the bigger y value is the bottom
    a = 0
    b = 0
    if coord1[1] < coord2[1]:
        a = coord1[1]
        b = coord2[1]
    else:
        a = coord2[1]
        b = coord1[1]
    
    # we are going from a -> b where the greater x value is our right bound, and the lesser is left bound
    rb = 0
    lb = 0
    if coord1[0] < coord2[0]:
        rb = coord2[0]
        lb = coord1[0]
    else: 
        rb = coord1[0]
        lb = coord2[0]
    cur_row = a
    # iterate across each row until we reach b, or we are out of bounds
    while cur_row != b:
        # check x_values_by_row at this row and make sure we're in bounds
        if rb > x_values_by_row[cur_row][1] or lb < x_values_by_row[cur_row][0]:
            return False
        cur_row+=1
    

    return True
        

def find_largest_inbounds(areas, coords, perimeter):
    """
    we have a list of areas, a perimeter, and coords that coorespond to the given ids in the area lists area[1], area[2]
    we need to check the space between the coords of each area and confirm that the area is in bounds

    areas = [[area_calculation, index1, index2], [50,1,5]]
    coords = [[x_value, y_value], [7,1], [11,1] [11,7]]
    perimeter (x_values_by_row) = {'row_index': [left_limit, right_limit], 1: [7,11], 2: [7,11], 3: [2,11]}
    """

    for area in areas:
        if is_inbounds(coords[area[1]], coords[area[2]], perimeter):
            return area[0]

    return 0 # zero fallback



def main():
    input = ingest_data("input.txt") # ingest input (we now have a list of coords) :  [[7, 1], [11, 1], [11, 7], [9, 7], [9, 5], [2, 5], [2, 3], [7, 3]]

    perimeter = find_perimeter(input) # define the perimeter as a dictionary x_values_by_row = {'row_num': [left_limit, right_limit]}
    
    all_areas = find_rectangle_areas(input) # get the area of all possible rectangles
    all_areas.sort(key=lambda e: e[0], reverse=True) # sort all_areas from greatest to least
    
    largest_inbounds = find_largest_inbounds(all_areas, input, perimeter) # iterate over all areas until we find one inbounds, first in bounds found return and print
    print(largest_inbounds)

main()