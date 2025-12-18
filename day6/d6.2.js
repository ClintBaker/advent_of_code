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

const findOperatorIndices = (row) => {
  let operatorIndices = []
  for (let i = 0; i < row.length; i++) {
    if (row[i] === '*' || row[i] === '+') {
      operatorIndices.push(i)
    }
  }
  return operatorIndices
}

const consolidatedOperatorList = (row) => {
  return row.trim().split(/\s+/)
}

const performMathPartTwo = (data) => {
  // find operator indices and create operator stack to identify when to move on to next eq group
  const operatorIndices = findOperatorIndices(data[data.length - 1])
  const operatorStack = operatorIndices.reverse()
  operatorStack.pop()
  let stopGap = operatorStack.pop()

  const operators = consolidatedOperatorList(data[data.length - 1])

  let equations = []
  let index = 0
  let group = []
  // for each col
  for (let c = 0; c < data[0].length; c++) {
    let num = ''
    // for each row
    for (let r = 0; r < data.length - 1; r++) {
      if (data[r][c]) num += data[r][c]
    }
    // organize our numbers
    if (c == stopGap) {
      stopGap = operatorStack.pop()
      index = 0
      equations.push(group)
      group = []
    }
    if (Number(num)) {
      group.push(Number(num))
      index++
    }

    if (c == data[0].length - 1) {
      equations.push(group)
    }
  }
  console.log(equations)

  // loop over our equations / operators, perform math, tabulate
  let total = 0

  // for each equation -> add innerTotal to total
  for (let i = 0; i < equations.length; i++) {
    let innerTotal = equations[i][0]
    if (operators[i] === '*') {
      // multiply
      for (let j = 1; j < equations[i].length; j++) {
        innerTotal *= equations[i][j]
      }
    } else {
      // sum
      for (let j = 1; j < equations[i].length; j++) {
        innerTotal += equations[i][j]
      }
    }
    total += innerTotal
  }

  return total
}

const main = () => {
  // part two
  const testData = ingestData('input.txt')
  const partTwoSolution = performMathPartTwo(testData)
  console.log(partTwoSolution)
}

main()
