Title: App.net Sidebar
Date: 2013-05-08 14:03
Slug: app-net-sidebar
Tags: Nerdery, Software

“Surely,” I thought, “there already exists an App.net sidebar for Octopress.”

[**Edit:** Well, there is, [officially](https://github.com/octopress/adn-timeline).]

<strike>Well, there is, sorta.</strike> [But She’s a
Girl](http://www.rousette.org.uk/blog/archives/app-dot-net-widget/) posted
about her work at getting it integrated with her site, but its artifacts are
mostly bound up in the commit messages for her blog. Additionally, there’s no
longer a real need to offload the fetching of your App.net content to cron, you
can get perfectly serviceable JSON directly from App.net’s API. So, I opted to
tweak it, the results of which you can see in my sidebar.  

<!-- more -->

I reached out to the Octopress folks and learned that a future update will
include better ways to bundle new functionality and templates together, but for
now, I've uploaded my start at
[an App.net sidebar for Octopress](https://github.com/urbanape/octopress-appnet-sidebar/).

[**Edit 1/14/2014**: Since I’ve migrated the blog to
[Pelican](http://getplican.com), and no longer use the App.net sidebar, I’ve
removed the previous code snippets, but the repo still exists on Github.]
