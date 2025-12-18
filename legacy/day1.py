def read_input(filename="input.txt"):
    """Read rotations from a file and return a list of strings like 'L68'."""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    return [line for line in lines if line]


def count_end_hits(rotations, start=50):
    """Count times the dial points at 0 at the end of a rotation (Part 1)."""
    pos = start
    count = 0
    for item in rotations:
        dir = item[0]
        dist = int(item[1:])
        if dir == 'R':
            pos = (pos + dist) % 100
        else:
            pos = (pos - dist) % 100
        if pos == 0:
            count += 1
    return count


def count_during_hits(rotations, start=50):
    """Count times the dial points at 0 during any click of rotations (Part 2).

    For each rotation starting at s with direction dir (1 for R, -1 for L)
    and distance d, we need the number of integers t in [1..d] such that
    (s + dir * t) % 100 == 0. Solve for the first t0 (1..100) then count
    occurrences every 100 steps: 0 if t0> d else 1 + (d - t0)//100.
    """
    pos = start
    total = 0
    for item in rotations:
        dir = 1 if item[0] == 'R' else -1 # direction
        dist = int(item[1:]) # distance
        s = pos # postion at start of rotation
        # compute first t >=1 such that (s + dir*t) % 100 == 0
        if dir == 1:
            t0 = (100 - s) if s != 0 else 100
        else:
            t0 = s if s != 0 else 100
        if t0 <= dist:
            total += 1 + (dist - t0) // 100
        # update pos to rotation end
        pos = (pos + dir * dist) % 100
    return total


def main(argv=None):
    import sys
    argv = argv if argv is not None else sys.argv
    path = argv[1] if len(argv) > 1 and not argv[1].startswith('part') else 'test_input.txt'
    rotations = read_input(path)
    part1 = count_end_hits(rotations)
    part2 = count_during_hits(rotations)
    print(part1)
    print(part2)


if __name__ == '__main__':
    main()