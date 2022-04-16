function generateHTML(artist, albumName, songName) {
    return `
    <li>
        <img id='${songName.toLowerCase().replaceAll(' ', '-')}' class='album-cover' src='/jukebox/img/covers/${artist.toLowerCase().replaceAll(' ', '-')-albumName.toLowerCase().replaceAll(' ', '-')}.jpg' alt=''>
        <h5>${albumName}</h5>
        <p>${artist}</p>
        <a href=''>View on Discogs</a>
    </li>`
}