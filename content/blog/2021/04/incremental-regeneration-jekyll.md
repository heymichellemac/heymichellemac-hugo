---
categories:
- blog
date: '2021-04-21'
tags:
- coding
title: Jekyll - How To Enable Incremental Regeneration To Speed Up Build Times
width: wide
---

A great tip for speeding up the build time of your Jekyll blog is to make use of the incremental regeneration feature.

This process will only generate the pages that were updated since the last build as opposed to re-generating all pages with each build.

## A Word Of Caution

While this sounds like a fix-all solution in theory, in practice a word of caution is advised when using this feature.

As described on the [Jekyll website](https://jekyllrb.com/docs/configuration/incremental-regeneration/), incremental regeneration is an experimental feature at the time of writing this. 

Don't expect it to work flawlessly every time.

For example, I noted that my homepage never updated even though it shows my latest posts. 

As the actual code of the homepage was rarely updated, it wasn't updated to include the latest posts.

The workaround was to manually update the homepage, save, then rebuild. 

Something like this can become tedious over time so just be aware this feature has some limitations. 

---

## Ways To Use Incremental Regeneration

Anyway, with all of that out of the way, let's look at how to implement incremental regeneration to speed up build times.

There are 2 ways to do this:

1. Include the incremental flag in your build command
2. Set incremental: true in your config file.

### #1 --incremental flag

Here's the command:

```
bundle exec jekyll serve --incremental
```

### #2 incremental: true

Add this line to your _config.yml file:

```
incremental: true
```