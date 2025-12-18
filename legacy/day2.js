// few product ID ranges (my puzzle input)

// you are given a bunch of ranges -> the ids must fall within those ranges -> ranges are separated by commas

// each range gives its first ID and last ID separated by a dash

// sequence of digits twice is invalid (55, 6464, 123123) -> first half same as second half...

// none of the IDs have leading 0s (0101).

// 1. Find all invalid IDs that appear in the given ranges
// 2. Add up the value of all of the invalid ids and return

// Invalid IDs:
// - isPalindrome = True = invalid
// - leading 0 = invalid

import fs from 'fs'

const readInput = (path = 'day2.txt') => {
  const data = fs.readFileSync(path, 'utf-8')
  const values = data.split(',').map((s) => s.trim())
  return values
}

// OLD ISINVALID
// const isInvalid = (n) => {
//   const s = String(n)
//   if (s.length % 2 !== 0) return false // false if not even

//   const mid = s.length / 2
//   return s.slice(0, mid) === s.slice(mid) // check if the first half and second half are the same
// }

const isInvalid = (n) => {
  const s = String(n)
  const len = s.length

  // iterate over each sequence of digits up to half the total integer
  // check if the length of str is divisible by k (length of chunk)
  // - if not continue (must be clean division)
  // slice up to k (now we have a chunk)
  // rebuild the full string by duplicating the chunk len/k times and compare to og string (implicit bool return)

  for (let k = 1; k <= len / 2; k++) {
    if (len % k !== 0) continue // length must be cleanly divisible by len of chunk

    const chunk = s.slice(0, k) // we now have a chunk
    //rebuild string w/ chunk
    if (chunk.repeat(len / k) === s) return true
  }
  return false // no chunk worked → valid
}

const aggregateInvalidIds = (rangeStr) => {
  const [start, end] = rangeStr.split('-').map(Number)
  const invalids = [] // array of invalid ids

  for (let n = start; n <= end; n++) {
    if (isInvalid(n)) invalids.push(n)
  }

  return invalids
}

const main = () => {
  const ranges = readInput() // we now have strings of ranges
  const invalids = [] // aggregate invalid ids here
  // for each range -> check each value in the range for isInvalid
  ranges.forEach((range) => {
    const innerInvalids = aggregateInvalidIds(range)
    invalids.push(...innerInvalids)
  })

  // sum
  const sum = invalids.reduce((total, id) => total + id, 0)
  console.log('The sum of all the invalid ids is:')
  console.log(sum)
}

main()
