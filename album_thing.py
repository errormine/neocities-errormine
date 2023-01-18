
while (True):
    image_id = input("IMAGE ID: ")
    artist = input("ARTIST: ")
    song = input("SONG: ")
    song_id = (artist.lower() + "-" + song.lower()).replace(" ", "-")
    album = input("ALBUM: ")

    html = f'''            <figure class="album">
                    <img src="/jukebox/img/covers/{image_id}.jpg" alt="" id="{song_id}" class="album-cover">
                    <figcaption>
                        <h4><i>{album}</i></h4>
                        <p>{artist}</p>
                    </figcaption>
                </figure>'''

    print(html)