---
categories:
- blog
date: '2022-03-28'
tags:
- coding
title: Jekyll - How To Display A Count Of Posts Per Tag Or Category
width: wide
---

My Changelog website (_as of 20240126 this site has been decomissioned_) is where I keep track of all my creative work online. It contains links to every article, newsletter edition, digital product, and project I create. 

I built it in [Jekyll](https://jekyllrb.com/), my static site generator of choice.

One of the first hurdles I had to navigate when building the site was how to display a stats page. This would summarize all my content under a few different parameters. I wanted to display counts of posts per categories as well as tags.

Here's how I accomplished setting up a display of post counts per category and tag.

## Site Structure

Let's start with a summary of how things are set up on the Changelog site. 

I have the following tags:

- coding
- creation
- design
- Milestone
- productivity

These serve as the main buckets or topics I talk about most often. My niche if you will. 

Milestone is slightly different. It denotes various markers I want to celebrate.

Then I have categories:

- Article
- Book Notes
- Digital Product
- Github Repo
- Newsletter
- Website

These denote the type of content I've created.

Each component shows the tag/category name and a count of the posts under that tag/category. 

Each component also has a link to the relevant tag/category page to help with navigation.

## Display Post Count By Tag

All I did was to add the following code:

```
{% raw %}
{{ site.tags.Creation | size }}
{% endraw %}
```

To use this yourself, just replace `Creation` with the name of your tag. The only thing that could potentially trip you up here is misspelling the tag name so be sure to double-check that.


## Display Post Count By Category

Post count by category is equally as easy to implement. Just use the following code:

```
{% raw %}
{{ site.categories.Article | size }}
{% endraw %}
```

Again, be sure to double-check spelling here as this is what usually trips me up.


## Display Post Count Of All Posts

If you want a count of all posts on your website, here's the code:

```
{% raw %}
{{ site.posts | size }}
{% endraw %}
```

Super simple 👍


## Count All Posts Minus A Specific Tag

Here's a fun one that will hopefully be helpful to you. 

On my homepage, there is a picture of me and underneath it is a level counter. I set this up to try and gamify my content creation. The higher the level, the more content I've created.

To accomplish this, I needed to count all posts except for milestone type posts (as these aren't pieces of content I've created, they're just events).

Here's the pseudocode: `my current level = all posts - milestone posts. Then divide by 10.`

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

Just replace the `Milestone` tag with your own tag.

In your case, you may not need `divided_by: 10` as this was something I added in to determine the level to display.
