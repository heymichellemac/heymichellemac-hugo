---
categories:
- blog
date: '2022-03-28'
tag:
- Coding
title: Jekyll - How To Display A Count Of Posts Per Tag Or Category
width: wide
---

My Changelog website (as of 20240126 this site has been decomissioned) is where I keep track of all my creative work online. It contains links to every article, newsletter edition, digital product, and project I create. 

I built it in [Jekyll](https://jekyllrb.com/), my static site generator of choice.

One of the first hurdles I had to navigate when building the site was how to display a [stats page](https://changelog.heymichellemac.com/stats). This would summarize all my content under a few different parameters. I wanted to display counts of posts per categories as well as tags.

Here's how I accomplished setting up a display of post counts per category and tag.

---

## Site Structure

Let's start with a summary of how things are set up on the Changelog site. 

I have the following tags:

- Coding
- Creation
- Design
- Milestone
- Productivity

These serve as the main buckets or topics I talk about most often. My niche if you will. 

Milestone is slightly different. It denotes various markers I want to celebrate like hitting 500 Twitter followers or growing my Medium following.

Then I have categories:

- Article
- Book Notes
- Digital Product
- Github Repo
- Newsletter
- Website

These denote the type of content I've created.

Here's a screenshot of my stats page to show you the end result:

![Stats Page](/assets/images/2022/MXB22012/stats-page.png)

As you can see, each component shows the tag/category name and a count of the posts under that tag/category. 

Each component also has a link to the relevant tag/category page to help with navigation.

I highly recommend you check out the live version of the site for more context: [Changelog Stats](https://changelog.heymichellemac.com/stats)

---

## Display Post Count By Tag

This couldn't be simpler. All you need to add is the following code:

```
{% raw %}
{{ site.tags.Creation | size }}
{% endraw %}
```

Just replace Creation with the name of your tag. The only thing that could potentially trip you up here is misspelling the tag name so be sure to double-check that.

---

## Display Post Count By Category

Post count by category is equally as easy to implement. Just use the following code:

```
{% raw %}
{{ site.categories.Article | size }}
{% endraw %}
```

Again, be sure to double-check spelling here as this is what usually trips me up.

---

## Display Post Count Of All Posts

If you want a count of all posts on your website, here's the code:

```
{% raw %}
{{ site.posts | size }}
{% endraw %}
```

Super simple 👍

---

## Count All Posts Minus A Specific Tag

Here's a fun one that will hopefully be helpful to you. 

On my homepage, there is a picture of me and underneath it is a level counter. I set this up to try and gamify my content creation. The higher the level, the more content I've created.

![Stats Page](/assets/images/2022/MXB22012/level-count.png)

To accomplish this, I needed to count all posts except for milestone type posts (as these aren't pieces of content I've created, they're just events).

Here's the pseudo-code: my current level = all posts - milestone posts. Then divide by 10 (*this step is optional for you*)

Here's the code I used to make that happen:

```
{% raw %}
 {% assign count_posts = site.posts | size %}

 {% assign milestone_posts = site.tags.Milestone | size %}

 {% assign total_posts = count_posts | minus: milestone_posts %}

 <span class="font-bold pl-2">Level {{ total_posts | divided_by: 10 }}</span>
{% endraw %}
```

Pretty cool right? 

Just replace the "Milestone" tag with your own tag.

In your case, you may not need "divided_by: 10" as this was something I added in to determine the level to display.

---

I hope you found this article helpful. I'm always finding new tips and techniques for building Jekyll websites and I really enjoy being able to share them with you!

If you enjoyed this, please consider sharing it with someone else who might find it useful 🤗