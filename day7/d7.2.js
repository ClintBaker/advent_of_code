import { readFileSync } from 'fs'
import { fileURLToPath } from 'url'
import path from 'path'

const ingestData = (filename = 'input.txt') => {
  const __filename = fileURLToPath(import.meta.url)
  const __dirname = path.dirname(__filename)
  const str = readFileSync(path.join(__dirname, filename), 'utf-8')
  const lineStrs = str.split(/\r?\n/) // split by lines
  return lineStrs
}

// quantum -> how many alternate realities are there?  how many possible combos

// cache of solutions (starting at this point how many timelines hit the bottom)
let cache = {}

const recursiveLower = (row, col, data) => {
  // check cache first
  // must convert coords into string
  let coordStr = `${row}${col}`
  if (cache[coordStr]) return cache[coordStr]
  // if it's not cached, keep working (once)
  while (true) {
    if (row + 1 >= data.length) {
      cache[coordStr] = 1 // update cache
      return 1 // we made it to the bottom -> answer is one
    }
    row++

    // we hit a splitter -> return left answer + right answer
    if (data[row][col] == '^') {
      let total = 0
      if (col - 1 >= 0) {
        total += recursiveLower(row, col - 1, data)
      }
      if (col + 1 < data[row].length) {
        total += recursiveLower(row, col + 1, data)
      }
      cache[coordStr] = total // update str
      return total // return total
    }
  }
}

const partOne = () => {
  const data = ingestData('input.txt') // ingest data
  const startingPoint = data[0].indexOf('S') // identify starting point
  // begin loop
  const timesSplit = recursiveLower(0, startingPoint, data)
  console.log(timesSplit)
}

partOne()
