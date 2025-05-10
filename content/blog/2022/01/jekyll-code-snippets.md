---
categories:
- blog
date: '2022-01-31'
tag:
- Coding
title: How To Include Jekyll Liquid Tags in Code Snippets
---

When I write about Jekyll on my website I often include code snippets to provide more context for how something works. You can easily copy these code snippets and paste them into your own Jekyll website to make them work for you. This is the advantage of being able to include code snippets in a how to article.

However when you include Jekyll specific code in default code snippets you'll notice all kinds of error messages start to appear in your terminal.

In this quick how to guide I'm going to show you how to include Jekyll-specific code into code snippets without breaking your Jekyll website.

---

## Here's How To Do It

Inside of the code snippet, wrap the code block with the following two tags: raw, endraw.

Here's what it looks like in my code editor:

![Code Editor Screenshot](/assets/images/2022/MXB22004/code-editor-screenshot.png)


Here's what it looks like in the front end:

```
{% raw %}

 Here is my jekyll code

{% endraw %}
```