---
categories:
- blog
date: '2021-11-22'
tags:
- coding
title: How To Add A Table Of Contents To Jekyll Blog Posts
width: wide
---

A table of contents is a helpful component to include in longer blog posts that have lots of detail. It gives readers an easy way to navigate through your blog post to find exactly what they're looking for.

I use a table of contents for most of the blog posts on this Jekyll blog and it was very easy to add.

In this post, I'll walk you through the process of setting up and adding a table of contents to blog posts in Jekyll.

---

## Anatomy Of Table Of Contents

You've likely seen a table of contents before at the start of a blog post. 

They essentially pull all the headings used throughout the blog post and put them in one place to:

1. Give you a sense of the overall structure and content of the blog post
2. Allow you to navigate to different sections of the blog post.

Here's an example of the table of contents for my previous blog post: [The 7 Step Process I Used To Build A Landing Page To Promote My Book](/book-landing-page)

![Table Of Contents Component](/assets/images/2021/table-of-contents.png)

---

## Configuring Table Of Contents In Jekyll

There are two parts to this walkthrough: configuring the table of contents functionality and then actually adding a table of contents to relevant posts. Let's look at the first part in this section.

The easiest way I found to achieve this functionality is by adding a plugin, namely: [jekyll-toc](https://github.com/toshimaru/jekyll-toc)

To add this plugin to your Jekyll project add the following to your **Gemfile**:

```
gem 'jekyll-toc'
```

Next, to the **_config.yml** file add:

```
plugins:
	- jekyll-toc
	
# TOC Settings
toc:
 min_level: 1
 max_level: 3
 list_class: toc
 list_class: toc__list
 sublist_class: toc__sublist
```

You can read more about the TOC settings in the [readme file in the jekyll-toc repo](https://github.com/toshimaru/jekyll-toc) but this is the configuration I use.

Once you've added these lines of code, run  ```bundle install``` which will add the necessary dependencies to the project.	

For actually styling the table of contents, here's what I added to my styles.css:

```css
.toc__list:before {
 content: "Table Of Contents";
 font-weight: bold;
 font-size: 1.5rem;
}

.toc__list {
 border: 2px solid #eee;
 border-radius: 4px;
 line-height: 1.8rem;
 padding: 1rem 1.5rem;
 font-weight: 600;
}

.toc__sublist li {
 padding-left: 1.25rem;
}

.toc-h2:first-child {
 margin-top: 1rem;
}  

#toc a {
 color: #BE185D;
 text-decoration: underline;
}

#toc a:hover {
 color: #9D174D;
}
```

You're mileage may vary here so feel free to style this how you like. In the config file you'll see I made use of 'list_class' and 'sublist_class' to add CSS classes into the table of contents code. 

This allowed me to target those elements specifically to style them.

---

## Adding A Table Of Contents To A Blog Post

OK, if you've been following along the Table Of Contents plugin should now be configured.

It's time to actually add a table of contents to blog posts.

The first step here is to add the liquid tag for table of contents to where you want it to appear. 

In my case, I have a file: **_layouts/article.html** which is the layout I use for my blog posts. This is where I place the following code:

```
{% raw %}
{% toc %}
{% endraw %}
```

The next step is to tell the plugin which posts we want to display a table of contents in. That is done in the front matter of each blog post.

Here's what you need to include in the front matter:

```
---
toc: true
---
```

This will display a table of contents for that blog post.

Everything should be setup and ready to go so simply start up your Jekyll project and see how things work. You should see a table of contents has been added to the blog posts you've specified.

You can of course tweak the toc configuration in config.yml and the CSS styling to suit your needs but this implementation works very well for me.

---

## Wrap Up

I hope this walkthrough helped you to add a table of contents to your Jekyll website. If you have any questions or comments, let me know! I also have a number of other Jekyll related blog posts you can read down below 👇