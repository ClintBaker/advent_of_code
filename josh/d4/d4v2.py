from pathlib import Path

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]

def load_grid(filename: str = "dayFourTestData.txt"):
    """Return the grid as a list of lists, treating the file next to this script as the source."""
    file_path = Path(__file__).with_name(filename)
    return [list(line.rstrip("\n")) for line in file_path.read_text().splitlines() if line]

def adjacent_rolls(r: int, c: int, grid) -> int:
    """Count adjacent @ cells around (r, c)."""
    count = 0
    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]):
            if grid[nr][nc] == "@":
                count += 1
    return count

def find_accessible(grid):
    """Return coordinates of rolls with fewer than four adjacent @ neighbors."""
    coords = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == "@" and adjacent_rolls(r, c, grid) < 4:
                coords.append((r, c))
    return coords

def remove_accessible(grid, coords):
    for r, c in coords:
        grid[r][c] = "x"

def count_accessible_rolls(grid):
    total = 0
    while True:
        coords = find_accessible(grid)
        if not coords:
            break
        total += len(coords)
        remove_accessible(grid, coords)
    return total

def main():
    grid = load_grid()
    total = count_accessible_rolls(grid)
    print(total)

if __name__ == "__main__":
    main()
