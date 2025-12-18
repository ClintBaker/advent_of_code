const fs = require('fs')
const path = require('path')

const readData = (filePath) => {
  const text = fs.readFileSync(path.resolve(__dirname, filePath), 'utf8')
  // Normalize on windows
  return text
    .replace(/\r/g, '')
    .split('\n')
    .map((s) => s.trim())
    .filter(Boolean)
}

const main = () => {
  const path = 'test_input.txt'
  // get rotations from file
  const rotations = readData(path)
  // loop over each rotation and find out how many times we cross 0
  let pos = 0
  let total = 0
  rotations.forEach((item) => {
    const dir = item[0] === 'R' ? 1 : -1 // direction
    let distance = parseInt(item.slice(1), 10)
    while (distance > 0) {
      if (dir === 1) {
        if (pos == 99) {
          total += 1
          pos = 0
        } else {
          pos++
        }
      } else {
        if (pos == 0) {
          total += 1
          pos = 99
        } else {
          pos--
        }
      }
      distance--
    }
  })

  console.log('Total crossings:', total)
}

main()
