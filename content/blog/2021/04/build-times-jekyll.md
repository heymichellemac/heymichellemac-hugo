---
categories:
- blog
date: '2021-04-14'
tag:
- Coding
title: Jekyll - How To Determine Build Times
---

If you're looking to optimize the build time of your Jekyll blog, it's useful to know just how long each part of the build process takes.

By using the profile flag at the end of your build command, you'll be given an output of the build process summary and the site render stats.

Here's the command:

```
bundle exec jekyll build --profile
```

Here's an example of the build process summary:

```
| PHASE      |   TIME |
+------------+--------+
| RESET      | 0.0001 |
| READ       | 2.3622 |
| GENERATE   | 0.0096 |
| RENDER     | 1.9764 |
| CLEANUP    | 0.0127 |
| WRITE      | 0.5394 |
+------------+--------+
| TOTAL TIME | 4.9004 |
```

And here's an example of the site render stats:

```
| Filename                      | Count |    Bytes |  Time |
+-------------------------------+-------+----------+-------+
| _layouts/defaultsidebar.html  |    54 | 1346.50K | 0.335 |
| _layouts/article.html         |    32 |  596.41K | 0.333 |
| _includes/header.html         |    62 |  329.12K | 0.310 |
| _layouts/book-note.html       |    12 |  242.36K | 0.113 |
| _layouts/pagewsidebar.html    |     6 |   76.17K | 0.018 |
| _layouts/default.html         |     2 |   23.05K | 0.005 |
| _includes/sidebar.html        |    60 |   91.23K | 0.004 |
| _layouts/article-archive.html |     3 |   32.34K | 0.002 |
| _layouts/homepage.html        |     1 |   10.51K | 0.001 |
| _includes/footer.html         |    62 |   80.65K | 0.001 |
| 404.html                      |     1 |    0.49K | 0.000 |
| tag/Creation.html     |     1 |    3.93K | 0.000 |
| tag/Design.html         |     1 |    5.65K | 0.000 |
| projects.html                 |     1 |    0.89K | 0.000 |
+-------------------------------+-------+----------+-------+
| TOTAL (for 19 files)          |   303 | 2860.80K | 1.130 |

                    done in 4.965 seconds.
```

This is useful for identifying the bottlenecks i.e. the pages that take the longest to render.

Generally speaking, excessive use of Liquid is often the cause of slow build times. 

With this in mind, you can target specific pages that are taking longer to load and make steps to reduce the complexity of those pages.

If you're looking for more on this, you can find a list of build command options on the Jekyll website: [Jekyll Build Command Options.](https://jekyllrb.com/docs/configuration/options/)