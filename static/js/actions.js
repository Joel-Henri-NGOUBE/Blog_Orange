document.querySelector(".links :last-child").addEventListener("click", () => {
    document.querySelector(".switch-language").style.display = "flex"
})

document.querySelector(".modal :first-child").addEventListener("click", () => {
    document.querySelector(".switch-language").style.display = "none"
})