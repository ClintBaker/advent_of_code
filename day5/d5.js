import { readFileSync } from 'fs'
import { fileURLToPath } from 'url'
import path from 'path'

const ingestData = () => {
  const __filename = fileURLToPath(import.meta.url)
  const __dirname = path.dirname(__filename)
  return readFileSync(path.join(__dirname, 'josh.txt'), 'utf-8')
}

const parseRangeString = (str) => {
  const [start, end] = str.split('-').map((part) => Number(part.trim()))
  return { start, end }
}

const parseIdString = (str) => {
  return Number(str.trim())
}

const sortData = (input) => {
  // split by lines
  const lines = input.split(/\r?\n/)
  // organize the raw text data into two usable arrays
  let ranges = []
  let ids = []
  let checkRanges = true

  lines.forEach((line) => {
    // if line is just whitespace (indicating we're moving on to ids)
    if (checkRanges) {
      if (line.trim().length <= 0) {
        checkRanges = false
      } else {
        // add the range to the list
        ranges.push(parseRangeString(line))
      }
    } else {
      // add the id to the list
      if (line.trim().length > 0) ids.push(parseIdString(line))
    }
  })

  return { ranges, ids }
}

const checkIds = (ranges, ids) => {
  let numFresh = 0

  for (let i = 0; i < ids.length; i++) {
    // for each id loop ranges until you fit in one then break
    let j = 0
    while (j < ranges.length) {
      if (ids[i] >= ranges[j].start && ids[i] <= ranges[j].end) {
        numFresh++
        break
      }
      j++
    }
  }

  return numFresh
}

// const main = () => {
//   // 1. ingest data -> get ranges and ids to check
//   const input = ingestData()
//   // 2. organize input
//   const { ranges, ids } = sortData(input)
//   // 3. check each id against ranges
//   const numFresh = checkIds(ranges, ids)
//   // 4. return num fresh
//   console.log(`Number of Fresh Ingredients: ${numFresh}`)
// }

const mergeRanges = (ranges) => {
  // sort by start so we can sweep once and merge overlaps/adjacent ranges
  const sorted = [...ranges].sort((a, b) => a.start - b.start)
  const merged = []

  for (const range of sorted) {
    const last = merged[merged.length - 1]
    if (!last || range.start > last.end + 1) {
      merged.push({ ...range })
    } else {
      last.end = Math.max(last.end, range.end)
    }
  }

  return merged
}

const calculateNumFreshFromRanges = (ranges) => {
  // merge overlaps so each id is counted once
  const merged = mergeRanges(ranges)

  return merged.reduce((total, { start, end }) => {
    return total + (end - start + 1) // +1 because ranges are inclusive
  }, 0)
}

// pt 2
const partTwo = () => {
  // 1. ingest data
  const input = ingestData()
  // 2. organize input
  const { ranges, ids } = sortData(input)
  // 3. check ranges for num ids (beware of overlap)
  const numFresh = calculateNumFreshFromRanges(ranges)
  // 4. return num fresh
  console.log(numFresh)
}

partTwo()
