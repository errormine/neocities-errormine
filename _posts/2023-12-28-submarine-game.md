---
title: Submarine Game (devlog 1)
description:
---

Around half way through the fall semester of 2023, I had an idea to make a game where you have to control a submarine and navigate using only a very limited amount of information about your surroundings. I thought it might be an interesting concept and make for some unique game mechanics and controls. After looking around I found there were a couple existing submarine games, but they didn't really do what I had in mind. So I thought I might as well try and make my own prototype. 

This is an oultine of around one month of my progress so far. I've learned a great deal since I started this, and hope to continue working on it throughout the rest of next year.

### Week 1

To begin, I got the submarine itself moving around with keyboard controls so that it's easy to test and fix things quickly at this stage. Eventually, I will refine the controls and make it closer to what I originally imagined.

<video width="100%" controls>
    <source src="/blog/assets/video/ioBhpTxyCP.mp4" type="video/mp4">
</video>

After I had the submarine moving, I created some basic buttons which you could click and it would adjust the different controls of the submarine. At first I had just buoyancy, thrust, and rotation.

I created a very simple SONAR display using some control nodes and a viewport texture attached to a plane. At this point, all it shows are nearby objects and it updates every 3 seconds. I also added a couple sound effects for fun.

<video width="100%" controls>
    <source src="/blog/assets/video/JSJVfU31kq.mp4" type="video/mp4">
</video>

I wanted to have some kind of control panel that you sit down at and have a set of controls so I created a chair for you to sit in. I was very proud of making the sit down work on my first try.

Typically, I would struggle with something like this, but I feel over a couple years I've gotten comfortable enough with Godot that I can make what I want fairly quickly. It's nice to know I've improved from my very first prototypes.

<video width="100%" controls>
    <source src="/blog/assets/video/KxVFFZ7N0e.mp4" type="video/mp4">
</video>

And that's all for the first week. I was busy with school, and other projects so this is all I got. I would say it's a decent start! Hopefully I can start getting all the mechanics together and creating some levels soon... right?