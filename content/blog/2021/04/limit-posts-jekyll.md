---
categories:
- blog
date: '2021-04-07'
tag:
- Coding
title: Jekyll - How To Limit Posts During The Build Process
width: wide
---

As your Jekyll blog grows in size over time, you might find that the build process takes longer to run.

This can be frustrating if you just want to test out a small UI change.

Luckily, the workaround for this is to limit the number of posts during the build process.

Here's the command:

```
bundle exec jekyll serve --limit_posts 10
```

This will limit the build to 10 posts but you can change the number to be whatever you need.

Try this out the next time you're looking to test out a small change on your website locally and you'll find this has a big impact on your build times.