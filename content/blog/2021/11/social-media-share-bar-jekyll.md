---
categories:
- blog
date: '2021-11-01'
tags:
- coding
title: How To Add A Social Media Share Bar In Jekyll
width: wide
---

Adding a social media share bar at the beginning or end of each post is a great way to encourage readers to share your content on social media.

In the past when my website ran on WordPress I used a plugin to add this functionality. This felt very clunky and slow to configure and interact with. Now that my site runs on Jekyll, I have a code snippet that accomplishes the same thing. It is simple, easy to use, and can be replicated across my entire website wherever I need it.

In this article, I share with you the code snippet I use to add a social media share bar to my Jekyll site. Follow along and make use of this code snippet on your own website. 

## What Is A Social Media Share Bar?

A social media share bar is something you've likely seen before on a website or a blog.

It refers to the section of an article where there is a group of social media buttons. Clicking a button will share the article on that social media platform via the reader's account. These can often be seen in line with content but can also be seen floating to the side of the main page's content.

This type of component is great to include on your website as it encourages readers to share your content with others across social media. 

Here's a screenshot of what this looks like on my website:

![Social Media Share Bar](/assets/images/2021/share-bar.png)

This is what we'll be implementing using the code below.

## Social Media Share Bar Setup - Jekyll Environment

Before we look at the code itself, I'd like to go through my Jekyll setup to give you a bit more context about how this all runs.

I'm running a pretty standard [Jekyll](https://jekyllrb.com/) implementation using [Tailwind CSS](https://tailwindcss.com/) for the styling and a few simple plugins for SEO, table of contents, and pagination.

My posts are in the ```_posts``` folder.

In the ```_layouts``` folder I have a file called article.html which stores the template for article type pages. This is where the code lives that implements the social media share bar component.

You may choose a different implementation than the one I'm running with and that's perfectly fine. 

For instance, instead of my approach you could create a social-media-share.html file in the ```_includes``` folder and include it on pages using an Include statement:

````
{% raw %}
 {% include social-media-share.html %}
{% endraw %}
````

## Social Media Share Bar Code

Here's the code snippet for adding a social media share bar to your Jekyll site (note it includes the Tailwind CSS syntax):

```
{% raw %}
<div class="hidden md:block">
	<div class="flex justify-center gap-x-5 mt-6 mb-8">   

		<!-- FACEBOOK --!>
		<a class="text-white text-2xl" href="https://www.facebook.com/sharer/sharer.php?u={{ site.url }}{{ page.url }}" onclick="window.open(this.href, 'mywin',
		'left=20,top=20,width=500,height=500,toolbar=1,resizable=0'); return false;" >
		<div class="rounded-md py-2 flex px-6 items-center bg-social-facebook hover:shadow-md transition-all">
			<svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="facebook-f" class="w-5 h-5 mr-2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><path fill="currentColor" d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"></path></svg>
			<span> Facebook</span></div></a>

		<!-- Twitter --!>
		<a class="text-white text-2xl" href="https://twitter.com/intent/tweet?text={{ page.title }}&url={{ site.url }}{{ site.baseurl }}{{ page.url }}" onclick="window.open(this.href, 'pop-up', 'left=20,top=20,width=500,height=500,toolbar=1,resizable=0'); return false;" title="Share on Twitter">
		<div class="rounded-md flex items-center py-2 px-6 bg-social-twitter hover:shadow-md transition-all">
			<svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="twitter" class="w-5 h-5 mr-2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"></path></svg>
			<span> Twitter</span></div></a>

		<!-- LINKEDIN --!>
		<a class="text-white text-2xl" href="https://www.linkedin.com/shareArticle?mini=true&url={{ site.url }}{{ page.url }}&title=&summary=&source=webjeda" onclick="window.open(this.href, 'mywin',
		'left=20,top=20,width=500,height=500,toolbar=1,resizable=0'); return false;" >
			<div class="rounded-md flex items-center py-2 px-6 bg-social-linkedin hover:shadow-md transition-all">
				<svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="linkedin" class="w-5 h-5 mr-2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96 102.2 96c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9V416z"></path></svg>
				<span> Linkedin</span></div></a>

		<!-- EMAIL --!>
		<a class="text-white text-2xl" href="mailto:?subject=&amp;body=Check out this article {{ site.url }}{{ page.url }}">
		<div class="rounded-md flex items-center py-2 px-6 bg-gray-600 hover:shadow-md transition-all">
			<svg width="20" height="20" class="w-5 h-5 mr-2" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2.00333 5.88355L9.99995 9.88186L17.9967 5.8835C17.9363 4.83315 17.0655 4 16 4H4C2.93452 4 2.06363 4.83318 2.00333 5.88355Z" fill="#FFFFFF"/><path d="M18 8.1179L9.99995 12.1179L2 8.11796V14C2 15.1046 2.89543 16 4 16H16C17.1046 16 18 15.1046 18 14V8.1179Z" fill="#FFFFFF"/></svg>
			<span> Email</span> 
		</div>
		</a>

	</div>
</div>

{% endraw %}
```

As you can see I've included: Facebook, Twitter, LinkedIn, and email. Feel free to add or remove buttons as you need them.

Also, be sure to test each button for yourself to make sure it works as you expect it. It turns out there's a lot you can do with these so take some time to customize them how you like.

## Conclusion

I hope you found this article helpful and you were able to follow along and add a social media share bar to your own Jekyll website.
