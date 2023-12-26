---
title: Untitled Submarine Game (devlog 2)
description:
---

A few more additions to the prototype since the first week! It's slowly starting to resemble something playable.

### Week 2

Now that I had a chair I could sit in, I decided to create a simple model for the control panel and some nicer controls for the submarine. I added a lever to control the thrust, and added a bit more information the SONAR display.

<video width="100%" controls>
    <source src="/blog/assets/video/a850uOhlfu.mp4" type="video/mp4">
</video>

At this point, I decided to change the way you interacted with objects. I wanted to keep a crosshair that you could interact with, instead of switcing to a mouse pointer when you sit down. This made things a bit more difficult, but I eventually got it working.

The most difficult part was probably the lever. I couldn't figure out how to make it move nicely until I stumbled across this [random reddit post](https://www.reddit.com/r/Unity3D/comments/ogagbj/draggable_lever_with_mouse_cursor/) with the same issue.

The final set up has this funny collision shape and moves based on where a raycast lands on that collider. It was surprisingly simpler than I originally made it out to be, but it works excellently.

<figure>
    <img src="/blog/assets/img/lever.jpg" alt="">
    <figcaption>The lever with a semi-circular collision shape.</figcaption>
</figure>

This also meant that I could add an indicator on the crosshair about what interactable objects do. This took quite a while for me to get a system working well, but now it's general enough that I can add whatever I want.

The crosshair icons are placeholder assets stolen from SOMA currently since I really like the way it works in that game.

<video width="100%" controls>
    <source src="/blog/assets/video/zNdlhPpH6G.mp4" type="video/mp4">
</video>

I also added a simple physics item which you can drag around. I would like to eventually let the player find some random items which they can place around the ship as decorations.

<video width="100%" controls>
    <source src="/blog/assets/video/NnpsGiR1Yy.mp4" type="video/mp4">
</video>

Here's a silly bug due to collisions between the physics item and the player.

<video width="100%" controls>
    <source src="/blog/assets/video/KgIfFpsbrv.mp4" type="video/mp4">
</video>

I found a [CRT shader](https://godotshaders.com/shader/crt-shader-2/) which added a bit of visual interest to the SONAR display, and makes it look much nicer. I also added latitude and longitude coordinates to the display. I would like to use these in gameplay eventually.

The coordinates are just based on the player's X and Z coordinates in meters but converted to latitude and longitude, and offset by a ((random)) amount.

<video width="100%" controls>
    <source src="/blog/assets/video/ijCR6XAYvU.mp4" type="video/mp4">
</video>

I also started working on a basic proximity sensor to let you discern how far away you are from nearby terrain as the display can be confusing at times. It will beep faster and faster until you are about 10 meters away and then become static.

<video width="100%" controls>
    <source src="/blog/assets/video/4D33UT9n3g.mp4" type="video/mp4">
</video>

That's all I did in week 2. Thanks for checking it out so far! Look out for more updates in the future.