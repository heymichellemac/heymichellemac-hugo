---
categories:
- blog
date: '2021-07-26'
tags:
- coding
title: Jekyll - Add Related Posts At The End Of A Post
width: wide
---

At the end of a blog post, it's a good idea to recommend similar posts to your readers. This helps them to find more great content on your website easily.

I used to manually add related posts at the end of each article but this became really tedious.

When I migrated my website from Wordpress to Jekyll, this similar posts feature was a must have for me. I wanted to make this process as automated as possible.

In this post, I want to share with you how I implemented a related posts section at the end of my blog posts on my Jekyll site.

---

## File Structure

Let's start by covering how the files are setup.

In the _layouts folder I have an article.html. This is the template used by articles and it's where the main code for this feature is implemented.

All I need to do is add the correct layout to any posts in the _posts folder.

I can do this by adding this to the file's metadata:

```
---
layout: dynamicpage
---
```

---

## Logic

To build this functionality, I first decided how similar posts should be determined.

I wanted similar posts to be found based on the Tags associated with posts.

If any posts have the same tag as the current post, they would be classed as similar posts and displayed in the similar posts section.

I also wanted to limit the number of similar posts displayed to 5.

---

## Code

Here's the code that's used to implement this feature:

```
{% raw %}
<h2>Enjoy Reading This Article?</h2>
<p>Here are some more articles you might like to read next:</p>
    
{% assign maxRelated = 5 %}
{% assign minCommonTags =  1 %}
{% assign maxRelatedCounter = 0 %}
    
<ul>
	{% for post in site.posts %}
    
    	{% assign sameTagCount = 0 %}
        {% assign commonTags = '' %}
    
		{% for tag in post.tags %}
        	{% if post.url != page.url %}
            	{% if page.tags contains tag %}
            	{% assign sameTagCount = sameTagCount | plus: 1 %}
            	{% endif %}
            {% endif %}
		{% endfor %}
    
        {% if sameTagCount >= minCommonTags %}
    		<li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
            {% assign maxRelatedCounter = maxRelatedCounter | plus: 1 %}
            
            {% if maxRelatedCounter >= maxRelated %}
                {% break %}
            {% endif %}
		{% endif %}
	{% endfor %}
</ul>
{% endraw %}
```

Let's look at the code in more detail.

The first three liquid tags create variables:

- maxRelated - this is for the maximum amount of related posts to display
- minCommonTags - this denotes the minimum amount of tags that need to be common to class posts as similar posts
- maxRelatedCounter - this is a counter variable that will be used to determine various logic at the end of the code

The code then loops through all of the posts on the website and looks at their tags.

If the tag matches the tag of the current post, then it will feed into the related posts list.

This happens until the maxRelatedCounter value is reached, in my case when 5 posts have been found.

If you're planning on implementing this functionality with your own Jekyll site, it's important to test the code out to ensure it's working correctly. 

While it might look correct by populating posts, it's important to see that the similar posts actually have the same tags.

---

## Conclusion

I hope this post has helped you with your Jekyll site. Anything here that you didn't understand or think could be improved? 

Reach out to me on Twitter and let me know.