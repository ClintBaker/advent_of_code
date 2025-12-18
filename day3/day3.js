// batteries are labeled with their joltage rating
// value from 1 to 9
// input is joltage rating
// batteries are arranged into banks
// each line of digits in input corresponds to a single bank of batteries
// within each bank, you need to turn on exactly two batteries
// the joltage that the bank produces
// turn on two of the bank, and the first + second = jolts

// find the largest possible joltage each bank can produce
// total output joltage is the sum of the max joltage from each bank

// return the total max output joltage
import { readFileSync } from 'fs'
import { fileURLToPath } from 'url'
import path from 'path'

const injestBanks = () => {
  const __filename = fileURLToPath(import.meta.url)
  const __dirname = path.dirname(__filename)
  return readFileSync(path.join(__dirname, 'day3.txt'), 'utf-8')
    .trim()
    .split(/\r?\n/)
    .map((line) => line.split(''))
}

const pickMax = (bank, count) => {
  const digits = bank.map(Number) // map chars to numbers
  let drop = digits.length - count // calculate the number of digits to drop
  const stack = [] // hold the best digits in order

  // scan left to right
  for (const d of digits) {
    // while there are digits to drop, digits in stack, and the last item in the stack < current digit
    while (drop > 0 && stack.length && stack[stack.length - 1] < d) {
      stack.pop() // drop smaller previous digits to make space
      drop-- // adjust our drop count (we just dropped a number)
    }
    stack.push(d) // keep current digit at the given place in the stack
  }

  return Number(stack.slice(0, count).join('')) // take the first count digits as a number
}

const main = () => {
  const banks = injestBanks()
  // reduce to aggregate into sum (we are picking max for each bank)
  let totalJoltage = banks.reduce((sum, b) => sum + pickMax(b, 12), 0)
  console.log(totalJoltage)
}

main()

// legacy
const maxJoltage = (bank) => {
  // loop and find biggest num
  // as long as biggest isn't last char in array
  let biggestI = 0
  for (let i = 0; i < bank.length - 1; i++) {
    if (bank[i] > bank[biggestI]) biggestI = i
  }
  // loop and find second biggest
  let secondBiggestI = biggestI + 1
  for (let i = biggestI + 1; i < bank.length; i++) {
    if (bank[i] > bank[secondBiggestI]) secondBiggestI = i
  }
  // build our num
  let joltage = bank[biggestI] + bank[secondBiggestI]
  console.log(joltage)
  return Number(joltage)
}
