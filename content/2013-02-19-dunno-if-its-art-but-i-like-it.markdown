Title: Dunno if It’s Art, but I Like It
Date: 2013-02-19 13:06
Slug: dunno-if-its-art-but-i-like-it
Tags: Art, Python

## The Itch

It started innocuously enough. It started with a tweet:

<blockquote class="twitter-tweet"><p>Since some of you have asked, I love these wallpapers: <a href="http://t.co/TrsZykfq"
title="http://simoncpage.co.uk/blog/">simoncpage.co.uk/blog/</a></p>&mdash; Craig Hockenberry (@chockenberry) <a href="https://twitter.com/chockenberry/status/302180625870364672">February 14,
2013</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

I followed the link and Simon’s art made an immediate impression on me. In an
instant, I knew how I might go about riffing on his designs. A long time ago,
there was an app called [NodeBox](http://nodebox.net/) (and before that was
DrawBot), which was made for generating programmatic art. I set about creating
a simple NodeBox script to start making circles, hexagons, lines, and filling
them in with various colors.

<!-- more -->

{% img /images/ugly_circles.jpeg 'Ugly Circles' %}

My first attempts were beyond ugly. Random colors do not a palette make. So, I
started browsing Adobe’s [Kuler](http://kuler.adobe.com/) for some thoughtfully
composed palettes. 

{% img /images/pretty_circles.jpeg 'Pretty Circles' %}

I also played with creating more lines connecting the various circle centers,
varying the thickness of all the strokes, parameterizing the size of the
circles, and seeding the image with larger blobs of color. Around this time, I
also cleaned up the maths that situated the circles and the lines connecting
them. Amazingly, the first attempts were produced via trial-and-error, and were
within a few pixels of what they should have been (sad Zac forgot a lot of math
since high school).

{% img /images/more_lines.jpeg 'More Lines' %}

Finally, as nice and complementary as the colors were, there was a richness and
depth that was missing. So I applied a few Snapseed filters to give them a bit
more toothsomeness.

{% img /images/toothsome_depth.jpeg 'Toothsome Depth' %}

Since playing with the hexacircles, I’ve also taken a quick stab at doing
something with triangles, and lollipops, inspired by several of the pieces in
Simon’s
[Futurism set](http://www.flickr.com/photos/simoncpage/sets/72157623099901702/with/4296226201/).

[{% img /images/triangles.jpeg 'Triangles' %}](http://www.flickr.com/photos/urbanape/8485895127/in/set-72157632795310221)

[{% img /images/lollipops.jpeg 'Lollipops' %}](http://www.flickr.com/photos/urbanape/8488761549/in/set-72157632795310221)

[{% img /images/hexacircles.jpeg 'Hexacircles' %}](http://www.flickr.com/photos/urbanape/8487004774/in/set-72157632795310221)

## The Tools

### [Pythonista](https://itunes.apple.com/app/id528579881)

This Universal iOS app is a brilliant little self-contained Python environment,
complete with network access APIs for pulling in content (like the Adobe Kuler
RSS feeds), and canvas and scene libraries for making drawing (and
interactivity) easy. Highly recommended.

### [NodeBox 1](http://nodebox.net/code/index.php/Home)

For the desktop, I use NodeBox 1. For the work I’ve done to date, it’s more
than adequate. There are some discrepancies in the APIs between Pythonista and
NodeBox, and I’m currently writing a bridge library to make it easier to use
the same scripts in both environments.

### [Snapseed](https://itunes.apple.com/us/app/snapseed/id439438619?mt=8)

For image filtering and processing, you can hardly go wrong with this app.
There is a counterpart Mac app, but I haven’t used it yet. I understand it’s
still awaiting a Retina update. For my images, I typically give them an Auto
Correct, a Drama with Saturation bumped up to about 65%, and a Grunge with
Saturation kept at 65%, Texture Strength at 25%, and the others tweaked until
it looks good.

## The Code

I’ve begun uploading the [suite](http://github.com/urbanape/pythonista/) of
scripts that generate the base images. Pull requests welcome.

## The Results

And I’ve uploaded the standouts to my
[Flickr set](http://www.flickr.com/photos/urbanape/sets/72157632795310221/).

I hope you enjoy, and I’d love to hear how folks riff off my pretty pictures.
