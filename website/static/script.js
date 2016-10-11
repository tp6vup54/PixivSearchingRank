var request = new XMLHttpRequest();

request.onreadystatechange = function() {
    if(request.readyState === 4) {
        if(request.status === 200) {
            document.getElementById("image-frame").innerHTML = request.responseText;
            mode = document.querySelector(".sort-radio").dataset.mode;
            if(mode) {
                var radios = document.querySelectorAll("input[name='Sort']");
                for (i = 0; i < radios.length; i++) {
                    if(radios[i].value === mode) {
                        radios[i].checked = true
                        break
                    }
                }
            }else{
                document.querySelector("input[name='Sort'][value='3']").checked = true
            }
        }
    }
}

document.getElementById("Search").addEventListener("click", function() {
    var keyword = document.getElementById("search-text").value;
    if(keyword === "") {
        return;
    }
    var favorite = document.querySelector('input[name="Favorite"]:checked').value;
    var params = "Search-text=" + keyword + "&" + "Favorite=" + favorite
    request.open("Get", "/search?" + params);
    request.send();
});

function onChangeSortMode(target) {
    var sort = document.querySelector('input[name="Sort"]:checked').value;
    var params = "Sort-mode=" + sort
    request.open("Get", "/sort?" + params);
    request.send();
}

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

function onSubmitEmpty() {
    var x;
    x = document.querySelector("#search-text").value;
    if (x == "") {
        return false;
    };
}