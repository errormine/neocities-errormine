// Check if Winamp is supported in this browser
if(!Webamp.browserIsSupported()) {
    alert("Oh no! Webamp is not supported; you will not be able to listen to any songs.")
    throw new Error("What's the point of anything?")
}

const webamp = new Webamp();

// Render after the skin has loaded.
webamp.renderWhenReady(document.getElementById("winamp-container"));

const albumCovers = document.querySelectorAll(".album-cover");
for (var i = 0; i < albumCovers.length; i++) {
    albumCovers[i].addEventListener("click", handleAlbumClick);
}

function handleAlbumClick(event) {
    document.getElementById("webamp").style.position = "fixed"; // fudge to get the fixed position to work...
    var parent = event.target.parentElement;
    var albums = document.querySelectorAll(".album");

    for (var i = 0; i < albums.length; i++) {
        if (albums[i].classList.length > 0 && albums[i] != parent) {
            albums[i].classList.remove("playing");
        }
    }

    if (parent.classList.contains("playing")) {
        webamp.pause();
    } else {
        parent.classList.add("playing");
        webamp.setTracksToPlay([{url: "/jukebox/audio/" + event.target.id + ".mp3"}]);
    }
}

//ffmpeg -i input.flac -ab 192k -map_metadata 0 -id3v2_version 3 output.mp3