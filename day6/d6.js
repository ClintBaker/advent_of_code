import { readFileSync } from 'fs'
import { fileURLToPath } from 'url'
import path from 'path'

const ingestData = (filename = 'input.txt') => {
  const __filename = fileURLToPath(import.meta.url)
  const __dirname = path.dirname(__filename)
  const str = readFileSync(path.join(__dirname, filename), 'utf-8')
  const lineStrs = str.split(/\r?\n/) // split by lines
  const lines = lineStrs.map((lineStr) => lineStr.trim().split(/\s+/)) // only chars no whitespace
  return lines
}

const performMathPartOne = (data) => {
  let total = 0
  const len = data[0].length

  // adjust for numbers on first 4
  for (let i = 0; i < 4; i++) {
    data[i] = data[i].map((char) => Number(char))
  }

  for (let i = 0; i < len; i++) {
    if (data[4][i] === '*') {
      total += data[0][i] * data[1][i] * data[2][i] * data[3][i]
    } else {
      total += data[0][i] + data[1][i] + data[2][i] + data[3][i]
    }
  }

  return total
}

const performInnerMath = (nums, operator) => {
  let lengths = nums.map((innerDigit) => innerDigit.length) // get length of each digit str
  let len = Math.max(...lengths) // get max len

  let values = []
  // outer loop over each digit
  for (let i = 0; i < len; i++) {
    let innerDigits = ''
    // inner loop within to determine how many i chars we are combining
    for (let j = 0; j < nums.length; j++) {
      if (nums[j][i]) innerDigits += nums[j][i]
    }
    // convert innerDigits to Number and add to values
    values.push(Number(innerDigits))
  }
  console.log(values)

  return 0
}

const performMathPartTwo = (data) => {
  let total = 0
  const len = data[0].length
  const colLen = data.length

  // for each row
  for (let i = 0; i < len; i++) {
    // for each column
    const digits = []
    const operator = data[colLen - 1][i]
    for (let j = 0; j < colLen - 1; j++) {
      digits.push(data[j][i].toString())
    }
    const innerMath = performInnerMath(digits, operator)
    total += innerMath
  }

  return total
}

const main = () => {
  // PART ONE
  const data = ingestData()
  const part1 = performMathPartOne(data)

  // part two
  const testData = ingestData('control.txt')
  const partTwoSolution = performMathPartTwo(testData)

  console.log(partTwoSolution)
}

main()
