---
categories:
- blog
date: '2022-10-31'
tag:
- Knowledge-Management
title: How I Use Embedded Queries In Obsidian To Simplify My Note Management
width: wide
---

Today I'm going to share with you how I use embedded queries inside of Obsidian. 

I'll explain what they are, how they work, and give you some examples of how I use them to retrieve lists of notes inside my personal Obsidian vault.

## What Is An Embedded Query?

In Obsidian, an embedded query is functionality that lets you insert a search query into a note. You'll then see the results of the query display from directly within the note.

Think of it like a saved search that you don't have to type into the search bar every time you need it.

This is useful if you'd like to retrieve lists of specific notes on a regular basis.

This is core Obsidian functionality which means you don't have to install any community plugins to make it work.

## How Can I Set Up An Embedded Query?

To set up an [embedded query](https://help.obsidian.md/Plugins/Search#Embed+search+results+in+a+note) in a note you'll need to:
1. Create a [code block](https://help.obsidian.md/How+to/Format+your+notes#Code+blocks) which is three opening and three closing backticks. 
2. After the first three backticks, you add the term query to denote this is a search query.
3. Enter a search term into the code block. You can build a search term using the search bar and copy the search in here.
4. If all is working correctly you should see a list of notes that match the search term you entered! (See the code snippet below as an example).

````
```query
file:("Daily Note")
```
````

## Pros And Cons Of Embedded Queries

I realize this approach may not be for everyone so I wanted to highlight some of the pros and cons of using embedded queries over using something like Dataview.

### Pros:
- Much simpler to use than a plugin like Dataview. 
- You can build a search query using the search bar and simply copy it into the query code block.
- If you know how to search inside of Obsidian you don't need to learn anything new to make embedded queries work.
- This might be my crazy designer brain here but I prefer how embedded query results look to Dataview query results. Especially with the stunningly beautiful default theme that ships with Obsidian V1.0.

### Cons:
- As it's simpler than Dataview you're missing a lot of the functionality of something as powerful as Dataview. For instance you can only retrieve lists not tables.
- As I write this, [Obsidian Publish doesn't support embedded search results](https://help.obsidian.md/Plugins/Search#Embed+search+results+in+a+note).

## Power User Tip: How To Extend The Functionality Of Embedded Queries With Query Control

This is the reason I find embedded queries so perfect for my use case: [the Query Control plugin](https://github.com/nothingislost/obsidian-query-control).

With it enabled, I can add search controls to the embedded query. It adds a bit more control to how I setup my queries without being overly complicated. 

Here's what that looks like (taken from the plugin source page):

![Query Control In Action](https://user-images.githubusercontent.com/89109712/154376835-08c1d3ab-b67c-4ca6-8261-abf41c38d7c1.gif)


As of the time of writing this plugin still appears to be in beta so to install it is a little bit more involved than finding it in the community plugins page and hitting install.

You'll either need to manually install it or install the BRAT community plugin ([details on how to do each is outlined here on the plugin page](https://github.com/nothingislost/obsidian-query-control#installing-via-brat)).

## Examples Of How I Use Embedded Queries

Let's take a look at some of the ways I've incorporated embedded queries into my Obsidian vault.

### 1 - Content Processing Inbox
My Inbox note is where I process the bulk of my notes. These are made up of old unprocessed random notes and highlights synced from my read-it-later tool [Matter](https://hq.getmatter.com/).

It's basically just a list of every note tagged with #inbox.

Here's the query:

![Inbox Query](/assets/images/2022/MXA22020/inbox-query.png)

And here's what that produces:

![Inbox Result](/assets/images/2022/MXA22020/inbox-results.png)

Note: "-path:99-templates" is used to exclude anything that lives in the "99-templates" directory.

To process my notes I simply open this note, click on a note that seems interesting to me and start processing. 

Note: I'd love to be able to return a random ordering of these results but it's something I'm still working on. If you know of a way to return a random ordering of results I'd love to hear from you!

### 2 - Content Creation Hub

This note contains a list of articles I want to/am writing. As you can see from the screenshot below, it's broken out into In Progress, Up Next, and Backlog.

![Content Creation Hub Note](/assets/images/2022/MXA22020/content-creation-hub.png)

If you need some help using the Obsidian search operators, I made a helpful cheat sheet you can view and download over on Twitter:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Now that I&#39;m using embedded search queries a lot more in <a href="https://twitter.com/obsdmd?ref_src=twsrc%5Etfw">@obsdmd</a> I needed to get to grips with the search operators so I made a handy cheat sheet to help me out.<br><br>Including it here incase it helps anyone else out 👇<br><br>Of course there&#39;s a light and dark mode option 😅 <a href="https://t.co/0ERnkPOxBx">pic.twitter.com/0ERnkPOxBx</a></p>&mdash; Michelle Mac (@heymichellemac) <a href="https://twitter.com/heymichellemac/status/1585980871248867328?ref_src=twsrc%5Etfw">October 28, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Or you can download and modify [the Figma file here](https://www.figma.com/community/file/1168867974967146879).

### 3 - List of Articles To Include In My Weekly Newsletter

I publish a newsletter called [Design Insight](https://designinsight.substack.com/) which is a weekly newsletter for creatives with a focus on design.

Each week I share 2-3 articles I found helpful and want to share with my readers. Previously this was all managed in Notion but I recently switched to doing it in Obsidian.

Articles I read that I'd like to include in my newsletter are tagged with #DesignInsight. Then all these notes are retrieved in my newsletter draft template each week. 

This quickly and easily lets me pick which articles to include in that week's newsletter edition which saves me lots of time and effort.

![Design Insight Articles List](/assets/images/2022/MXA22020/design-insight-query.png)


### 4 - In my Yearly, Quarterly, Weekly, Daily notes

Full disclosure I haven't fully overhauled my time-based notes yet to make use of embedded queries but I've tried it with a few that previously relied on Dataview and everything works perfectly.

Let's look at my yearly note. You can see below I have a section to retrieve all the Quarterly notes in the current year.

Here's the query:

![Yearly Note Query](/assets/images/2022/MXA22020/years-query.png)

And here's the result:

![Yearly Note Result](/assets/images/2022/MXA22020/years-results.png)

Simple!


## To Wrap Up

So far, I've found that anywhere I have used Dataview previously I can replace it with an embedded query. This has forced me to simplify the way I retrieve data and has dramatically simplified how I think about the information stored in my Obsidian vault.

This approach may not be for everyone but I wanted to share it in the hopes that other people will find it helpful 😄

P.S. If you need some help using the Obsidian search operators, I made a helpful cheat sheet you can view and download [over on Twitter](https://twitter.com/heymichellemac/status/1585980871248867328).

Or you can download and modify [the Figma file here](https://www.figma.com/community/file/1168867974967146879).