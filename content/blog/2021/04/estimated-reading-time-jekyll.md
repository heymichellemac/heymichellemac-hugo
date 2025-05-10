---
categories:
- blog
date: '2021-04-28'
tag:
- Coding
title: Jekyll - Add Estimated Reading Time To Posts
width: wide
---

Adding the estimated reading time of your article provides valuable context for readers. They can decide if they want to read your article now or bookmark it and save it for later.

It's a feature seen most commonly on the Medium platform but you can replicate this feature on your Jekyll site.

After some tweaking, I have been able to add this feature to my website (it's actually pretty simple) so I'd like to share the process with you.

## Site Structure

Let's start with the site structure to understand how things fit together.

In this case, there are two parts:

1. In the *_layouts* folder, I have a template file called *article.html*. This holds the code for article pages.
2. The CSS styling (in my case I'm working in SASS but it doesn't matter).

---

## Estimated Time To Read Code

Here's the code I added to achieve estimated reading time in article.html:

```
{%raw%}
{% capture words %}
{{ content | number_of_words }}
{% endcapture %}
        
<span class="readingTime">
<i class="fas fa-bookmark"></i> 
Reading Time: {{ words | divided_by: 180 | append: ' min' }}
</span>
{%endraw%}       
```

The first 3 lines of code will "capture" the number of words in the article and store it in the variable called words.

The next section calculates and outputs the estimated reading time.

To do this we divide the number of words in the article by 190. 

180 is the average amount of words per minute people read ([according to Wikipedia](https://en.wikipedia.org/wiki/Words_per_minute)).

As you can see I'm using a Font-Awesome bookmark icon but you can leave this out if you don't want it.

I finished by adding some CSS via the readingTime class to make the font pink.