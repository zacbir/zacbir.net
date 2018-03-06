Title: Self Control
Date: 2015-01-19 08:44
Slug: self-control
Tags: Hardware, Hacking, Keyboards, Software

In response to my recent keyboard posts, Alpha Chen posed a really good question:

<blockquote class="twitter-tweet" lang="en"><p><a href="https://twitter.com/zacbir">@zacbir</a> Re: <a
href="http://t.co/AmXWBktHHe">http://t.co/AmXWBktHHe</a> Why not remap caps lock to control directly in the
firmware instead of doing it in OS X?</p>&mdash; Alpha Chen (@kejadlen) <a
href="https://twitter.com/kejadlen/status/556682394372427776">January 18, 2015</a></blockquote> <script async
src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

The answer to which is: \*headslap\* Of course!

I’ve modified my firmware again to map the key to LCTL, and now the keyboard converter will always send Control
when that key is pressed, regardless of OS settings. In fact, it’ll send Control regardless of OS.

Thanks for the dose of obvious, Alpha Chen!

Current keymap file:

{% include_code keymap_zbir_2015-01-19.c lang:c %}
