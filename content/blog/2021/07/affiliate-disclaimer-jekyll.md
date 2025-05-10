---
categories:
- blog
date: '2021-07-12'
tag:
- Coding
title: Jekyll - Add An Affiliate Disclaimer To Specific Posts
---

On this website some of the links used are affiliate links. To let people know this, I include a disclaimer at the top of relevant pages.

Instead of manually copying and pasting this text for each new article I write, here's how I implemented an affiliate disclaimer to specific posts or pages.


In the **_includes** folder, create a file called affiliate-disclaimer.html

Add the following code to that file:

```
{% raw %}
{% if page.has-affiliate-link %}
<p><i>This article contains affiliate links.</i></p>
{% endif %}
{% endraw %}
```

Feel free to change the actual content of the affiliate disclaimer message.

In the **_layouts** folder, add the code below to any page templates that may have affiliate links. In my case I have 2 files: **article.html** and **book-note.html**

This code will include the affiliate disclaimer file to those page templates:

```
{% raw %}
{% include affiliate-disclaimer.html %}
{% endraw %}
```

The final step is to include a line of YAML metadata to relevant articles and pages:

```
has-affiliate-link: true
```

When this code is added to your pages and articles, it will trigger the first piece of code that includes the affiliate disclaimer text.


If you're trying to save on load/build times and want to cut down on the amount of includes you use, you could just copy and paste the **affiliate-disclaimer.html** code directly into your page templates.