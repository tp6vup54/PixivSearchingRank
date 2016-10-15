loaded = false
loading = false
loadScript("static/modalLoading.js", function(){loaded = true});
var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function() {
    socket.emit('test', {data: 'I\'m connected!'});
});

socket.on("update-progress", function(msg) {
    j = JSON.parse(msg)
});

socket.on("search", function(msg) {
    j = JSON.parse(msg)
    deploy_result(j.images, 3)
});

socket.on("sort", function(msg) {
    j = JSON.parse(msg)
    deploy_result(j.images, j.mode)
});

function deploy_result(images, mode) {
    document.getElementById("image-frame").innerHTML = images;
    var radios = document.querySelectorAll("input[name='sort']");
    for (i = 0; i < radios.length; i++) {
        if(radios[i].value == mode) {
            radios[i].checked = true
            break
        }
    }
    if(loading) {
        // Remove loading
        load = document.getElementById("openModalLoading")
        load.parentNode.removeChild(load);
        loading = false
    }
}

document.getElementById("search").addEventListener("click", function() {
    var keyword = document.getElementById("search-text").value;
    if(keyword === "") {
        return;
    }
    var favorite = document.querySelector('input[name="favorite"]:checked').value;
    if(loaded) {
        modalLoading.init(true);
        loading = true
    }
    socket.emit("search", {key: keyword, favor: favorite})
});

// On press enter on textbox.
document.getElementById("search-text").addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode == 13) {
        document.getElementById("search").click();
    }
});

function onChangeSortMode(target) {
    var sort = document.querySelector('input[name="sort"]:checked').value;
    if(loaded) {
        modalLoading.init(true);
        loading = true
    }
    socket.emit("sort", {data: sort})
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