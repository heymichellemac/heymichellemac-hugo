---
categories:
- blog
date: '2021-03-31'
tags:
- coding
title: Jekyll - Creating External Links That Open In A New Tab
width: wide
---

A common convention for external links is that they open in a new tab. The idea behind this is that you can easily go back to the previous tab if you need to. This makes it easy for users to return to your website.

You might already know how to do this in plain HTML. 

However, if you've built your website in Jekyll like me, you'll want to know how this can be achieved on your Jekyll website.

---

Let's step through the process.

In regular HTML this is how you create a link that opens in a new tab:

```html
<a href="link.com" target="_blank" rel="noopener noreferrer">External Link</a>
```

The attributes rel="noopener noreferrer" are added alongside the target="_blank" attribute to ensure security.

More on that here: [Links to cross-origin destinations are unsafe](https://web.dev/external-anchors-use-rel-noopener/).

In Jekyll, if you're writing your articles in markdown, you can use the traditional markdown link syntax with Jekyll's liquid structure:


```markdown

// plain markdown:

[Link To A Page](/pageurl/)

// or using liquid:
{%raw%}
[Link To A Page]( {% post_url 2021-02-12-book-getting-things-done %} )
{%endraw%}
```

However, when you click on these links, they open in the same tab.

To add the target and rel attributes you need to add the following:

```markdown
[Mishacreatrix Website](https://mishacreatrix.com/)
```

This will give you links that open in a new tab.

If you're looking to take this to the next level, add the code snippet to a text expander so you don't have to remember and type the code each time. 

I use [Espanso](https://espanso.org/) and have it tied to the command `;ext`:

```
- trigger: ";ext"
    replace: ''
```

I hope you found this article helpful!