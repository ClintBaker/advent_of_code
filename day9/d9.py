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
    if a[0] == b[0]:
        return 0
    
    x = abs(a[0] - b[0]) + 1
    y = abs(a[1] - b[1]) + 1

    return x * y


def find_largest_rectangle(coordinates):
    largest_rectangle = [0,0,0]

    for i in range(len(coordinates)):
        for j in range(i, len(coordinates)):
            area = find_area_between_coords(coordinates[i], coordinates[j])
            if area > largest_rectangle[0]:
                largest_rectangle = [area, i, j]
    
    return largest_rectangle


def main():
    # ingest input (we now have a list of coords)
    # [[7, 1], [11, 1], [11, 7], [9, 7], [9, 5], [2, 5], [2, 3], [7, 3]]
    input = ingest_data('input.txt')

    # iterate through each coordinate, identify all rectanlges that can be formed, and keep a 'largest_rectangle' with [area, index1, index2]
    # overwrite largest rectangle every time the area exceeds the previous largest
    largest_rectangle = find_largest_rectangle(input)

    # print the biggest rectangle's area
    print(largest_rectangle[0])

main()