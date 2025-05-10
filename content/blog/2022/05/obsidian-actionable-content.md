---
categories:
- blog
date: '2022-05-09'
tag:
- Knowledge Management
title: How I Use Obsidian To Take Action On The Content I Consume
---

I consume a lot of articles, podcasts, and videos each week but I would never take action on this content.

I would read something that sparked an idea for me and think "this is a good idea to try out". Then I'd finish the article, take my notes, and never go back to try out the idea. 

It wasn't until I saw this Tweet from Sam Williams that I realized I was missing something:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What&#39;s your no. 1 tip for taking action on the content you consume?</p>&mdash; Sam Williams (@iamsam_williams) <a href="https://twitter.com/iamsam_williams/status/1520799214086799363?ref_src=twsrc%5Etfw">May 1, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

I realized I was missing a system for taking action. After replying to Sam's tweet, I decided to set up a system for this in my Obsidian vault:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I haven&#39;t tried this yet but going to do it starting today: <br><br>Add a section to my lit notes for &quot;Initiatives To Try&quot;.<br><br>So when I read a book or article, I can pick out the things I want to do and pull those into a list 🙂</p>&mdash; Michelle (51/100) (@MishaCreatrix) <a href="https://twitter.com/MishaCreatrix/status/1521086152031281155?ref_src=twsrc%5Etfw">May 2, 2022</a></blockquote>

This article outlines the current process I've set up in  Obsidian for taking action on the content I consume.

---

## The Power-Ups Concept

Essentially, this system is a way for me to track initiatives I want to try based on the inspiration I get from articles I read, videos I watch, and so on.

Some examples of potential initiatives include: 

- Add a section to my weekly note for work I've published
- Review/audit my Twitter lists to make sure they're up to date
- Try morning pages

In my current system, I use the term **Power-Ups** instead of Initiatives. 

If you didn't already know I'm a [big video game nerd](/dark-souls-failure) so whenever I can turn something into a game I do. I find it helps to keep me interested and motivated in what I'm doing. It's like my kind of gamification.

In my Obsidian vault, a Power-Up is a task item with the **#powerup** at the end.

Here's what it looks like:

![Power-Up Line Item](/assets/images/2022/MXB22017/power-up-line-item.png)

---

## Power-Ups Note

As I have Power-Ups spread out across my notes, I wanted a way to collect them in one place to view them.

To do this, I created a Power-Ups note that lives in my **[Life OS](/obsidian-setup-sep-2021)** directory.

Within this note I have 2 sections: 

1. To Do - For items I want to do
2. Done - For items I've done

As it turns out, I didn't need any fancy plugins or complicated code snippets to achieve what I wanted. All I needed was an [Obsidian query](https://help.obsidian.md/Plugins/Search#Embed+search+results).

Here's the query I used for the To Do items:

```query
tag:#powerup task-todo: "#powerup"
```

Here's the query I used for the Done items:

```query
tag:#powerup task-done: "#powerup"
```

Here's the end result:

![Power-Ups Note](/assets/images/2022/MXB22017/power-ups-note.png)

You might notice that each query embed is missing the heading section. I used the following CSS code snippet to remove it:

```css
/* Hide the query text */
.internal-query-header-title, .internal-query-header-icon {
    display: none !important;
}
```

---

## Weekly Template Power-Up Embed

To keep this list of Power-Ups top of mind, I needed to resurface them on a regular basis. 

Checking in with this daily would be too much so I settled for a weekly basis and added a new section to my weekly note.

The Power-Ups section in my weekly note is simply an embed that links to the To Do section of the Power-Ups note.

Here's the code:

![Weekly Note Embed Code](/assets/images/2022/MXB22017/weekly-note-code.png)

Here's the end result:

![weekly Note](/assets/images/2022/MXB22017/weekly-note.png)

Each week I review this list and see which Power-Ups I will try out in the next week or so.

---

## My Key Take Aways

- If you don't have a system, you're relying on your own mind to remember things. This is a recipe for failure as our minds can only remember so much.
- Basic Obsidian queries are more powerful than you think. Give it a try before you jump into Dataview or something more complex.
- Having a habit of [regular reflection](/regular-reflection) allows you to check in with yourself, see where you are, and course-correct if you need to.
- Take time to check in with your systems and tweak them. I honestly had a lot of fun implementing this system and learned a lot about Obsidian in the process.

If you enjoyed this, please consider sharing it with someone else who might find it useful 🤗