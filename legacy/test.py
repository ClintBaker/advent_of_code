text = open("day2.txt").read()
ranges = text.split(",")

print(ranges)

invalids = []
for r in ranges:
    start, end = map(int, r.strip().split("-"))

    for i in range(start, end + 1):
        s = str(i)
        l = len(s)

        half = l // 2 # first half index
        first_haf = s[:half]
        second_half = s[half:]

        if first_haf == second_half:
            print(f"invalid: {s}")
            invalids.append(i)

sum = 0
for value in invalids:
    sum += value
print(f"sum of invalids: {sum}")
