---
categories:
- blog
date: '2022-02-21'
tag:
- Knowledge-Management
title: How I Do My Weekly Review In Obsidian
width: wide
---

If I didn't have a weekly review process I simply wouldn't make consistent progress towards my goals.

I have been doing my weekly review inside of Obsidian for over a year and have found it to be a really helpful process. It gives me the space to look back at the last week and plan for the next week. 

My weekly review process has evolved considerably [since I wrote about it last](https://www.mishacreatrix.com/restarting-the-weekly-review-process). I recently finished the latest revision of my weekly note template so I thought it would be a great time to share it with others who might find it helpful.

In this article, I share with you my weekly review note in Obsidian. I go through how everything is set up including the code and the plugins I use.

---

## Plugins Used

Here are the plugins I use in Obsidian to make my weekly review note work:

- [Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes) - This generates my weekly review note.
- [Calendar](https://github.com/liamcain/obsidian-calendar-plugin) - This works in conjunction with Periodic Notes to make sure my weekly note is created on a Monday.
- [Templater](https://github.com/SilentVoid13/Templater) - This allows me to use some code snippets to pull in dates that I can use for file referencing.
- [Dataview](https://github.com/blacksmithgu/obsidian-dataview) - This allows me to query my Obsidian vault and retrieve my list of OKRs and projects.

---

## Note Metadata

![Weekly Note Metadata](/assets/images/2022/MXB22007/weekly-note-metadata.png)


The naming convention for my weekly note is: 

- W-202202-09
- W to denote this is a weekly note
- 202202 - the year and the month
- 09 - the week number 

Here's how I have the weekly note set up in Periodic Notes: 

![Periodic Notes Setup](/assets/images/2022/MXB22007/periodic-plugin-setup.png)

Below the note name/note title I have links to my yearly note and my quarterly note. This allows for quick access to those notes when necessary.

---

## This Week's Goals

![This Week's Goals](/assets/images/2022/MXB22007/this-weeks-goals.png)

This section contains my top 3 goals/action items for the week. 

This is based on my current active goals/OKRs/projects and doesn't include all the other work I do each week.

During the weekly review on Friday, I'll create next week's weekly note and fill this in. 

I typically do this at the end of the weekly review but it's top of the list so when I sit down on Monday morning, I have my top 3 goals ready to go.

My previous weekly review note template didn't have a section for weekly action items so I found making concrete progress towards my goals wasn't being made a priority. 

Now I have a system to keep my goals and current action items top of mind, I know what my priorities are each week. P.S. I've read the 12 Week Year probably 3 times now and the fact that I haven't been doing this already is pretty embarrassing... 😳

---

## Weekly Review Prep

### Prep Tasks

![Prep Tasks](/assets/images/2022/MXB22007/prep-tasks.png)

This section contains a checklist of things I should do to get me in the right frame of mind to do my weekly review. For instance, I have checkboxes for cleaning my desk and for tidying up my inboxes.

I try not to have too much here. Otherwise, it would be easier for me to procrastinate on these tasks instead of actually doing the weekly review.

### Last Week

![Last Week](/assets/images/2022/MXB22007/last-week.png)

This section is an embed of last week's Reflections section. I find it helpful to look at the previous week to see what has changed and what has stayed the same. This also helps to get me in the right frame of mind for doing my weekly review.

To achieve this, I include a code snippet with Templater code to generate the link to last week's note. 

This honestly works about half the time so if you can think of a better way to achieve this send me a DM on Twitter!!

---

## Reflections

![Reflections](/assets/images/2022/MXB22007/weekly-reflections.png)

The first three questions here are taken from this article I read: [The Retrospective: A Personal Review Template](https://alphaprep.medium.com/the-retrospective-a-personal-review-template-c7e9fd9c55e1). 

I love the idea of the rose, thorn, bud approach to evaluating my week:

- 🌹 Rose: What went well this week?
- 🌵 Thorn: What should I stop doing?
- 🌱 Bud: What could be improved

I have two additional questions which help me to keep an eye on where I am mentally:

- 🔋What Gave Me Energy This Week?
- 📉 What Drained Me This Week?

For the things that give me energy each week, I want to make sure I do more of that. 

For the things that drain me each week, I want to make sure I do less of that.

Sounds simple, but it works really well for me.

---

## Next Week Planning

This section contains everything I need for planning for the next week. 

I look at the goals and projects I'm currently working on and try to pick out 2-3 tasks to work on next week. 

My top tip: if you do nothing else during your weekly review do this i.e. pick 2-3 key tasks you want to work on for next week. 

### OKRs

This section contains a list of my current in-progress goals/OKRs. 

I am currently looking at moving to OKRs from SMART goals so this is still a little bit of work in progress, however, the concept is still the same.

I use a Dataview query to retrieve goals/OKRs that have a status of in progress.

![OKRs Code Snippet](/assets/images/2022/MXB22007/okr-code-snippet.png)

### Projects

This section contains a list of my current in progress projects.

I use a Dataview query to retrieve projects that have a status of in progress.

![Projects Code Snippet](/assets/images/2022/MXB22007/projects-code-snippet.png)

---

So there you have it; my weekly review process inside of Obsidian. If you enjoyed this article, please consider sharing it with someone else who might find it useful 🤗

Oh and one last thing: I'm thinking about putting together all of my Obsidian templates into a GitHub repo so if that's something you'd be interested in just let me know so I can get working on it!