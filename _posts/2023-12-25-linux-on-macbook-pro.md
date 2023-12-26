---
title: The Apple Experience
description: My experience trying to install an SSD in a MacBook Pro.
---

My cheap shit Asus laptop which I purchased a couple years ago is falling apart at the hinges, and any repair shops I talked to said it's beyond screwed. So for the past 4 months I've been living with the screen held together with electrical tape and my hopes and dreams. I decided to forget about trying to fix it and get myself a nicer used laptop which is hopefully better build quality and won't fall apart within a couple years.

I eventually found a nice 2015 13" MacBook Pro which was in excellent condition and would be perfectly serviceable for any school work / general productivity that I need. It was only $320 on sale and came with a brand spanking new ($80) MagSafe<sup>&trade;</sup> charger for FREE!

<figure class="medium-large">
    <img class="pixel colorize" src="/blog/assets/img/macbook.png">
    <figcaption>This is what a MacBook looks like if you weren't aware</figcaption>
</figure>

Now today I'm finally trying to get Linux Mint installed and I wanted to share the trials and tribulations of getting it working. It can't be that hard, right?

First of all, I've got a Samsung 980 EVO in my previous laptop, and my plan is to backup what I need and scoop it out of there to use in this laptop. Not a problem, the Asus is simple to open and easy to retrieve the SSD from. Now I'll plonk it into the MacBook and be ready to install whatever I want on it! WRONG!!!!!

Apple uses a [proprietary connector](https://beetstech.com/blog/apple-proprietary-ssd-ultimate-guide-to-specs-and-upgrades#hdr-5) which is incompatible with M.2 and you need some shitty adapter inside the thing too... thankfully I did a bit of research before attempting this and was able to pick one up at Microcenter. You can also find them easily online.

<figure class="small-medium">
    <img class="pixel colorize" src="/blog/assets/img/sintech-adapter.png">
    <figcaption><a href="https://www.eshop.sintech.cn/index.php?route=product/product&product_id=50">Sintech M.2 adapter</a></figcaption>
</figure>

I first plugged it in with an external SSD adapter thing, and it showed up no problem. I was able to even install Linux Mint on it, but when I took it out and installed it inside the laptop... Nothing. 

Okay... I start searching for what the issue might be, and I get a few results suggesting that it needs to be formatted as APFS which the Linux Mint installation didn't do, of course. So, I take it out, put the original SSD back in, plug in the Samsung SSD with the external adapter, load up Disk Utility, and format as APFS. Install it in the MacBook again, and lo and behold... NOTHING!

At this point I'm scratching my head confused, and a bit worried I borked something while trying to install it. The MacBook is simple enough to open and install the SSD, but it's a possibility I screwed something up given that I am an idiot. Well I take it back out, plug it in with the external adapter and it shows up once again. What is going on???

<img class="pixel colorize" src="/blog/assets/img/clueless.png" alt="cat playing a guitar with the caption 'it has no idea what it is doing lol'">

I start searching again, and it seems only MacOS versions 10.13 (possibly 10.15, I'm not entirely sure) and higher have support for NVMe drives. Wonderful, this model is quite old, and I have no clue what version of MacOS I'm on! Luckily I hadn't deleted any MacOS installation and it was already updated when I purchased the thing so I didn't have to manually do that. It's still not working, though.

After messing around for a while and trying a few other random ideas, I realize maybe I should try installing MacOS to it and see if that makes it show up for some reason. I go through the whole dance to get into Disk Utility again, format it to APFS again, and install MacOS Catalina. Once it's done, I plop it back into the MacBook itself and thank heavens it shows up and boots.

Success! I'm finally able to install Linux Mint on the new SSD, and customize to my hearts content. I'm not quite sure why that was necessary ultimately, but I'm just glad it works. Time to get used to my new (8 year old) laptop! Thanks for reading, and happy holidays for I have overcome Apple's nonsense this time.