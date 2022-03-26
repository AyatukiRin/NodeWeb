const {mkdir} = require("fs/promises")

console.log("Script Executing...")  // 1

setTimeout(() => {
    console.log("setTimeout.....")
}, 0);   // 4

(async () => {
    console.log("async function executing...")  // 2
    await mkdir("./TestDirectory", {recursive: true})
        .then(resolve => {
            console.log(`resolve: ${resolve}`)  //  5
        })
        .catch(err => {
            console.log(err)    // 5
        })
    console.log("async function executed done.")    // 6
})()

console.log("Script Executed done.")// 3
