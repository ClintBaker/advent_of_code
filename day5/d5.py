from input import realData
from input import testData
from input import print_in_rows

def get_data ():
    input_data = realData
    input = input_data.strip().split("\n")
    inputLen = len(input)

    data = []

    for i in range(inputLen):
        rangeNums = input[i].split('-')
        start = int(rangeNums[0])
        end = int(rangeNums[1])
        data.append([start, end])
    
    sorted_data = sorted(data)
    return sorted_data

# we have a sorted list of ranges
# return all the numbers between the ranges (NO OVERLAP)
# how many numbers between each range, total, return

def calculate_range_values(data):
    total = 0
    for r_list in data:
        total += (r_list[1] -r_list[0]+1)
    return total

def merge_data(data):
    merged = []
    for start, end in sorted(data):  # already sorted, but we can sort again yall
        if not merged or start > merged[-1][1] + 1:  # no overlap/adjacent -> append that hoe
            merged.append([start, end])
        else:  # overlaps or touches
            merged[-1][1] = max(merged[-1][1], end)
    return merged


def main () : 
    data = get_data() # ingest data
    merged_data = merge_data(data) # merge data to accomodate gaps
    print(calculate_range_values(merged_data)) # calculate fresh produce

main()