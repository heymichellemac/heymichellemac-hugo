---
categories:
- blog
date: '2021-10-25'
tag:
- Coding
title: How To Add Related Posts In Jekyll To Increase Engagement
---

Including links to related posts at the end of each post is a great way to keep users engaged with your content. 

With a WordPress website, you can install a plugin to achieve this functionality. On the other hand, if your website is built in Jekyll (like mine), it requires a little bit more work to achieve the same end result. I was able to incorporate related posts functionality pretty easily into my own Jekyll website so in this article, I'd like to share with you how I did it. 

Feel free to follow along and implement this for yourself using the code snippets I include.

## What Are Related Posts?

The Related Posts section refers to the section at the end of an article where similar posts are recommended for you to read next. 

This is a great way to encourage users to stay on your site and engage with your content. It's also very easy to implement on most website builders, frameworks, and CMSs.

Here's a screenshot of what this looks like on my website:

![Related Posts](/assets/images/2021/related-posts-screenshot.png){:style="border:2px solid #DB2777;"}
This is what we'll be implementing using the code below.

## Related Posts Setup - Jekyll Environment

Before we dive into the code I want to give you a little context as to the way my website is set up. 

This will help you to implement this functionality on your own Jekyll website.

I'm running a relatively standard [Jekyll](https://jekyllrb.com/) implementation using [Tailwind CSS](https://tailwindcss.com/) for the styling and a few simple plugins for SEO, table of contents, and pagination.

My posts are in the ```_posts``` folder. 

Each post has a "tag" field in it metadata to denote the tag of a post i.e. Design, Coding, Productivity. This is what the code looks at to determine related posts.

In the ```_layouts```  folder I have a file called article.html which stores the template for article type pages. This is where the code lives that implements the related posts section.

Your implementation may be quite different to mine but this is what works for me. Feel free to tweak things so they suit your work style.

## Related Posts Code

Here is the code snippet to add related posts to your Jekyll blog:

```
{% raw %}
<!-- Adds related posts to the end of an article -->

 <h2>Enjoy Reading This Article?</h2>

 <p>Here are some more articles you might like to read next:</p>

 {% assign maxRelated = 5 %}
 {% assign minCommonTags =  1 %}
 {% assign maxRelatedCounter = 0 %}

 <ul>
 {% for post in site.posts %}#

    {% assign sameTagCount = 0 %}
 
    {% for tag in post.tags %}
        {% if post.url != page.url %}
            {% if page.tags contains tag %}
                {% assign sameTagCount = sameTagCount | plus: 1 %}
            {% endif %}
        {% endif %}
    {% endfor %}
 
    {% if sameTagCount >= minCommonTags %}
        <li>
        <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
        </li>

        {% assign maxRelatedCounter = maxRelatedCounter | plus: 1 %}

        {% if maxRelatedCounter >= maxRelated %}
            {% break %}
        {% endif %}
    {% endif %}
 {% endfor %}
 </ul>
{% endraw %}
```

Here it is with the Tailwind syntax included:

```
{% raw %}
<!-- Adds related posts to the end of an article -->
<h2 class="text-3xl font-semibold mb-4 mt-12" >Enjoy Reading This Article?</h2>
<p class="mb-2">Here are some more articles you might like to read next:</p>
 
{% assign maxRelated = 5 %}
{% assign minCommonTags =  1 %}
{% assign maxRelatedCounter = 0 %}

<ul class="list-disc pl-8">
{% for post in site.posts %}

    {% assign sameTagCount = 0 %}

    {% for tag in post.tags %}
        {% if post.url != page.url %}
            {% if page.tags contains tag %}
                {% assign sameTagCount = sameTagCount | plus: 1 %}
            {% endif %}
        {% endif %}
    {% endfor %}

    {% if sameTagCount >= minCommonTags %}

    <li class="my-2">
    <a class="text-pink-700 underline font-semibold hover:text-pink-800" href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    </li>

    {% assign maxRelatedCounter = maxRelatedCounter | plus: 1 %}

    {% if maxRelatedCounter >= maxRelated %}
        {% break %}
    {% endif %}
    
    {% endif %}
{% endfor %}

</ul>
{% endraw %}

```

Let's break down each section of the code and examine how it works.

````
{% raw %}
 {% assign maxRelated = 5 %}

 {% assign minCommonTags =  1 %}

 {% assign maxRelatedCounter = 0 %}
{% endraw %}
````

Here we are assigning values to 3 variables: 

1. **maxRelated** is the number of posts to display in the related posts section.
2. **minCommonTags** is the minimum number of tags a related post must have in common with the current posts to be displayed in the related posts section.
3. **maxRelatedCounter** is a counter variable that will be used to ensure the correct number of related posts is displayed.

````
{% raw %}
  {% for post in site.posts %}
  
  {% endfor %}
{% endraw %}
````

The majority of the code is wrapped in a For statement to loop through posts on the Jekyll website. It will look for all posts, then carry out the next step in the sequence.

````
{% raw %}
 {% assign sameTagCount = 0 %}
 {% endraw %}
````

**sameTagCount** is another counter variable that counts the number of related tags.

 ````
 {% raw %}
 {% for tag in post.tags %}

	 {% if post.url != page.url %}

		 {% if page.tags contains tag %}

			 {% assign sameTagCount = sameTagCount | plus: 1 %}

		 {% endif %}

	 {% endif %}

 {% endfor %}
 {% endraw %}
 ````

Next we have another For statement, this time to loop through the tags in the current post. This looks for all of the items in the tag section of the post's metadata.

Inside the For statement, we have an If statement that checks if the URL of the post is NOT the same as the URL of the page. This ensures we only look for posts that don't include this current post.

Inside that If statement we have another If statement. This one checks if the current post's tags match any tags in other posts.

If it does, we use the next line of code to increment the **sameTagCount** variable.

 ````
 {% raw %}
{% if sameTagCount >= minCommonTags %}

	<li>
		<a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
	</li>

	{% assign maxRelatedCounter = maxRelatedCounter | plus: 1 %}

	{% if maxRelatedCounter >= maxRelated %}
		{% break %}
	{% endif %}

 {% endif %}
 {% endraw %}
 ````

The next section starts with an If statement. Here we are checking if the **sameTagCount** variable value is greater than or equal to the value set in the **minCommonTags** variable.

If it is we'll display that post, including the post name and a link to the post.

Following that, we'll increase the value in the **maxRelatedCounter** value by 1.

The last If statement checks if the value in the **maxRelatedCounter** variable is greater than or equal to the value in the **maxRelated** variable. This ensures we display the correct number of related posts.

If you've followed along and added the code to your own site you should see a shiny new related posts section at the end of your posts!

If not, here are a couple of things to check:

- Ensure you have a 'tag' entry in the metadata of all your posts.
- Check the variable names match correctly. This could happen if you try to change the name of variables and miss one or introduce a typo.
- Troubleshoot by adding some HTML into each part of the code to identify where it might be failing.

## Conclusion

I hope you found this article helpful and you were able to follow along and add a related posts section to your own Jekyll website.

If you found this helpful why not check out some of the other Jekyll articles I've written. You can find them in the Related Posts section down below 😉