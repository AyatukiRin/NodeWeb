const { readFileSync } = require("fs")


const testJson = readFileSync("test.json",{
    encoding: "utf8",
    flag: 'r'
})

console.log(JSON.parse(testJson) )
