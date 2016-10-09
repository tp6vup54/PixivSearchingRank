function LargeImageModalOn(target) {
    modal = document.querySelector(".illust_modal")
    modal.style.zIndex = "10001"
    modal.style.display = "block"
    large_image = document.querySelector(".original-image")
    large_image.src = target.dataset.largeimg
    document.body.style.overflow = "hidden"
}

function LargeImageModalOff(target) {
    modal = document.querySelector(".illust_modal")
    modal.style.zIndex = "10000"
    modal.style.display = "none"
    document.body.style.overflow = "visible"
}