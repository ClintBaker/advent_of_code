import { readFileSync } from 'fs'
import { fileURLToPath } from 'url'
import path from 'path'

// identify paper that is removable
// remove (replace @ w/ x)
// repeat - loop until no more rolls of paper are accessible

const directions = [
  [0, 1],
  [0, -1],
  [-1, 0],
  [1, 0],
  [-1, -1],
  [-1, 1],
  [1, -1],
  [1, 1],
]

// g is for GIRTH
const ingestGrid = () => {
  const __filename = fileURLToPath(import.meta.url)
  const __dirname = path.dirname(__filename)
  return readFileSync(path.join(__dirname, 'grid.txt'), 'utf-8')
    .trim()
    .split(/\r?\n/)
    .map((line) => line.split(''))
}

const isAccessible = (r, c, grid) => {
  let adjacent = 0
  for (const [dr, dc] of directions) {
    const nr = r + dr
    const nc = c + dc
    if (nr >= 0 && nr < grid.length && nc >= 0 && nc < grid[r].length) {
      if (grid[nr][nc] === '@') adjacent++
    }
  }
  return adjacent < 4 // true if less than 4, false if more than 4
}

const identifyAccessible = (grid) => {
  let accessible = []
  let totalAcc = 0
  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[r].length; c++) {
      if (grid[r][c] === '@' && isAccessible(r, c, grid)) {
        totalAcc++
        accessible.push([r, c])
      }
    }
  }
  return { totalAcc, accessible }
}

const updateGrid = (grid, accessible) => {
  // update the coordinates in accessible with x
  accessible.forEach((coords) => {
    grid[coords[0]][coords[1]] = 'x'
  })
  return grid
}

const main = () => {
  let total = 0
  let grid = ingestGrid()

  while (true) {
    const { totalAcc, accessible } = identifyAccessible(grid)
    total += totalAcc // increment our total from this individual round check

    if (totalAcc <= 0) break // if no more rolls are accessible, break while loop
    grid = updateGrid(grid, accessible) // update grid and loop again
  }

  console.log(total)
}

const main2 = () => {
  let grid = ingestGrid()

  const { totalAcc, accessible } = identifyAccessible(grid)
  console.log(totalAcc)
}

main2()
