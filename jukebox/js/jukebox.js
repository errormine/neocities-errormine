// Check if Winamp is supported in this browser
if(!Webamp.browserIsSupported()) {
    alert("Oh no! Webamp is not supported; you will not be able to listen to any songs.")
    throw new Error("What's the point of anything?")
}

const webamp = new Webamp({
    initialTracks: [{
        metaData: {
            artist: "Harold Budd / Brian Eno",
            title: "A Stream With Bright Fish",
        },
        url: "https://cdn.discordapp.com/attachments/763823389483073586/962130929629929572/harold-budd-a-stream-with-bright-fish.mp3"
    }]
});

// Render after the skin has loaded.
webamp.renderWhenReady(document.querySelector("#winamp-container"));