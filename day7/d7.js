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

const splitCoords = []

const recursiveLower = (row, col, data) => {
  let timesSplit = 0
  // go down a row until you hit a ^ -> then split and continue going down
  while (true) {
    if (row + 1 >= data.length) break // you made it home
    row++

    // check next row
    if (data[row][col] == '^') {
      let innerSplitBool = false
      // we hit a ^, time to split
      // split
      // account for overlap
      if (col - 1 >= 0) {
        const exists = splitCoords.some(([r, c]) => r === row && c === col - 1)
        if (!exists) {
          splitCoords.push([row, col - 1])
          innerSplitBool = true
          timesSplit += recursiveLower(row, col - 1, data)
        }
      }
      if (col + 1 < data[row].length) {
        const exists = splitCoords.some(([r, c]) => r === row && c === col + 1)
        if (!exists) {
          innerSplitBool = true
          splitCoords.push([row, col + 1])
          timesSplit += recursiveLower(row, col + 1, data)
        }
      }
      if (innerSplitBool) timesSplit++
      break
    }
  }
  // while loop ends
  return timesSplit
}

const partOne = () => {
  const data = ingestData('input.txt') // ingest data
  const startingPoint = data[0].indexOf('S') // identify starting point
  // begin loop
  const timesSplit = recursiveLower(0, startingPoint, data)
  console.log(timesSplit)
}

partOne()
