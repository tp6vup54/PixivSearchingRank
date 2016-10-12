var request = new XMLHttpRequest();
loaded = false
loadScript("http://www.cssscript.com/demo/minimalist-loading-overlay-javascript-library-modalloading/modalLoading.js", function(){loaded = true});

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
            if(loaded) {
                // Remove loading
                loading = document.getElementById("openModalLoading")
                loading.parentNode.removeChild(loading);
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
    if(loaded) {
        modalLoading.init(true);
    }
    request.send();
});

function onChangeSortMode(target) {
    var sort = document.querySelector('input[name="Sort"]:checked').value;
    var params = "Sort-mode=" + sort
    request.open("Get", "/sort?" + params);
    if(loaded) {
        modalLoading.init(true);
    }
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

function loadScript(url, callback)
{
    // Adding the script tag to the head as suggested before
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;

    // Then bind the event to the callback function.
    // There are several events for cross browser compatibility.
    script.onreadystatechange = callback;
    script.onload = callback;

    // Fire the loading
    head.appendChild(script);
}