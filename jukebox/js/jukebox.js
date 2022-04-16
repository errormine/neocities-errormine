// Check if Winamp is supported in this browser
if(!Webamp.browserIsSupported()) {
    alert("Oh no! Webamp is not supported; you will not be able to listen to any songs.")
    throw new Error("What's the point of anything?")
}

const webamp = new Webamp({
    initialTracks: [{
        url: "https://raw.githubusercontent.com/prycaustic/neocities-errormine/main/jukebox/audio/songs/harold-budd-a-stream-with-bright-fish.mp3"
    }]
});

// Render after the skin has loaded.
webamp.renderWhenReady(document.querySelector("#winamp-container"));

const albumCovers = document.querySelectorAll(".album-cover");
for (var i = 0; i < albumCovers.length; i++) {
    albumCovers[i].addEventListener("click", handleAlbumClick)
}

function handleAlbumClick(event) {
    var parent = event.target.parentElement;
    var listItems = document.querySelectorAll("li");

    for (var i = 0; i < listItems.length; i++) {
        if (listItems[i].classList.length > 0 && listItems[i] != parent) {
            listItems[i].classList.remove("playing");
        }
    }

    if (parent.classList.contains("playing")) {
        webamp.pause();
    } else {
        parent.classList.add("playing");
        webamp.setTracksToPlay([{url: "https://raw.githubusercontent.com/prycaustic/neocities-errormine/main/jukebox/audio/songs/" + event.target.id + ".mp3"}]);
    }
}