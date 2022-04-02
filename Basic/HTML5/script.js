window.onload = () => {
    const reset = document.querySelector("#reset")

    reset.addEventListener("click", () => {
        console.log("Reset")
        document.querySelector(".block2").style.display = "block"
    })

    document.querySelector(".toggle").addEventListener("click", () => {
        console.log("toggle Click event.")
        document.querySelector(".block2").style.display = "none"
    })

}



