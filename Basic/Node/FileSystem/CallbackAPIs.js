const { mkdir } = require("fs")

console.log("Script Executing...")  // 1

setTimeout(()=> {
    console.log("setTimeout.....")
}, 0)   // 3


mkdir("./TestDirectory", {recursive: true}, (err => {
    console.log(err)    // 4
}))

console.log("Script Executed done.")// 2
