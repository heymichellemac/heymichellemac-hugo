---
categories:
- blog
date: '2021-09-20'
tags:
- pkm
title: A Walkthrough Of My Obsidian Setup
width: wide
---

I last wrote about my Obsidian Setup [way back in March](/obsidian-setup-2021). I was still finding my feet with Obsidian and trying lots of different things to see what worked well for me.

Since then, I've made a lot more changes to develop the system I use today. 

This system allows me to track my goals, remember content I consume, and manage my content creation process.

In this comprehensive article I would like to share with you my current Obsidian setup. I'll be going into detail on how my vault is structured, naming conventions, tags, templates.

---

## Technical Details

As with the last Obsidian Setup article I'd like to share some technical details with you before we dive into the actual content of my system.

### How I Have Setup My Obsidian Vault

My primary Obsidian vault sits inside of Google Drive. This allows me to view my notes from anywhere.

I don't use the Obsidian Sync service, the Obsidian Publish service, or the Mobile app (I don't know of a way to use it currently with Drive).

I keep my **Knowledge Vault** which I use personally and a **Work Vault** which I use for work-related material. 

This article will focus on my **Knowledge Vault** because it has the most fun and interesting stuff to talk about.

### How I Backup My Obsidian Vault

As mentioned I have my Vault stored on Google Drive. 

I also sync my vault to a private GitHub repo manually.

I've worked my backups this way for the last several months and have had no issues.

### What Plugins I Use

Here is a list of the Obsidian community plugins I currently use as part of my Obsidian setup:

- **Advanced Tables** - Really useful for managing tables. [Github URL](https://github.com/tgrosinger/advanced-tables-obsidian)
- **Better Word Count** - Shows word count and character count of notes. [Github URL](https://github.com/lukeleppan/better-word-count)
- **Cycle Through Panes** - Allows you to cycle through panes like browser tabs with **CTRL + Tab**. [Github URL](https://github.com/phibr0/cycle-through-panes)
- **Dataview** - Is a big part of my current setup, it allows me to add metadata to my notes and query based on that metadata to retrieve relevant notes. [Github URL](https://github.com/blacksmithgu/obsidian-dataview)
- **Day Planner** - I don't use this much any more as I don't really plan out my days other than the main 4 or 5 things I plan to do that day. [Github URL](https://github.com/lynchjames/obsidian-day-planner)
- **Kanban** - I'm just messing around with this plugin at the moment but it works very well so far. [Github URL](https://github.com/mgmeyers/obsidian-kanban)
- **Reading Time** - Adds estimated reading time to notes. Don't have too much of a use for this but sometimes it's nice to know the length of some notes. [Github URL](https://github.com/avr/obsidian-reading-time)

### Directories

My Obsidian vault is divided up into different directories/folders to help me organize my content.

Here is my current directory setup:

- 00-inbox
- 01-life-os
- 02-literature
- 03-evergreen
- 04-resources
- 05-Creation
- 06-topics
- 07-people
- 08-sources
- 99-attachments
- 99-daily-notes
- 99-templates


## The perfect system doesn't exist

It's important to mention that this setup has evolved over time. Take a look at my [last Obsidian setup article](/obsidian-setup-2021) and you'll see a lot has changed.

I didn't start out with a perfect setup on day one. I still don't have a perfect setup. It's always evolving based on what I need and any new experiments I try out.

If you like a particular part of this system, try it out for yourself or modify it to suit your needs. Your own system should always be evolving as you evolve. 

For me it's the most enjoyable part of this whole system. I can create something completely tailored to me!

The rest of this article will go through each directory in detail talking about what it's for and how I use it. 

I'll try to be as detailed as possible and include screenshots where relevant. With that said, if there's anything you'd like to know more about, let me know over on [Twitter](https://twitter.com/MishaCreatrix).

---

## 00-inbox


![Inbox Directory Screenshot](/assets/images/2021/obsidian-setup-inbox.png)

The inbox directory is where all the random uncategorized, unfinished notes live. 

This can include:

- drafts for articles I'm writing (like this one)
- ideas for future articles
- concepts I'd like to learn more about
- whatever random stuff crosses my path throughout the day

If you're familiar with the GTD methodology you'll recognize this as one of [my content inboxes](/inboxes-to-manage-thoughts-and-ideas). I use it along with my Bullet Journal and Todoist to capture any stray thoughts or ideas that come into my head.

I try to review this directory once a week (during [my weekly review](/restarting-the-weekly-review-process)) to clear it out and move notes to the right location.

Sometimes I'll add a tag #inbox or #towrite to these notes to further categorize them but I'm not sold on the value of this so I don't always do it. 

For me, it's enough to have all of these items stored in the Inbox directory itself.



---

## 01-life-os

The Life OS directory is where I keep notes relating to 'big picture' items like goals, projects, and weekly reviews.

This is where a lot of templates and other fun tricks start to come into play.

This directory contains the following sub-directories:

- 01-years
- 02-quarters
- 03-goals
- 04-projects
- 05-weeks

### 01-years

![Years Directory Screenshot](/assets/images/2021/obsidian-setup-years.png)

The Years directory contains a note for each year. There's not a lot in here yet but as I continue with this process I'll have a lot to show for it over the next number of years.

#### **Naming Format**

The naming format for year notes is: *Y-2021*. Y denotes this is a year note and then the year shows me which year it belongs to.

#### **Years Index**

The first note in this directory is years-index which is an index of all my year notes.

This is generated using the Dataview plugin which queries the metadata/frontmatter of each note like querying a database.

Note: the code/syntax is written in Edit Mode, then when I switch to Preview Mode, I can see a list of all relevant notes.

![Years Index Screenshot](/assets/images/2021/obsidian-setup-years-2.png)


years-index Dataview Syntax:
```dataview
list
from "01-life-os/01-years"
where contains(file.name, "Y")
sort file.name desc
```

#### **Year Note Template**


Each year note itself is generated from my Year Note Template. When I start a new year note, I simply press **CTRL + T**, then select Year Note Template and my note will auto-populate with everything I need.

The first section of the template contains the file name.

I also like to have a yearly theme so I put that right underneath the title.

{% raw %}
```
# {{title}}
Theme: 
```
{% endraw %}

The next 3 sections are lists of my Quarter, Goal, and Project notes. These are all automatically pulled in using the Dataview plugin once again.

**Quarters:**

```dataview
list
from "01-life-os/02-quarters"
where contains(file.name, "2021")
sort file.name asc
```

**Goals:**

```dataview
list
from "01-life-os/03-goals"
where theYear = 2021
sort file.name asc
```

**Projects:**
```dataview
list
from "01-life-os/04-projects"
where theYear = 2021
sort file.name asc
```

Following this, I have my year end review section. 

These questions have been added over time as I continue to use this template and research other ways of doing yearly reviews. This is what I've settled on for now.

```
## Year End Review

### Review Of The Past Year
-   How did my yearly theme help me this year?
-   What went really well this year?
-   What surprised me?
-   What am I most proud of accomplishing?
-   What challenged me?
-   What am I most grateful for?
-   What have I learned this year?
-   My top 5 favorite things from this year
-   Describe this year in 3 words

### Looking Ahead To Next Year
-   What is my yearly theme and why?
-   What am I most looking forward to next year?
-   What am I feeling apprehensive about?
-   What do I want to do differently?
-   What area of y life to I most want to develop?
-   What do I want to accomplish next year?
-   What challenges am I likely to face?

### Taking Action
-   I will make more time for:
-   I will learn about:
-   I will say NO to:
-   I will say YES to:

```

At the end of each year, I review this note and perform a **yearly review**. 

This might sound really daunting but once you see everything in the quarters, goals, and projects sections, you'll realize there is a lot to work from.

### 02-quarters

![Quarters Directory Screenshot](/assets/images/2021/obsidian-setup-quarters.png)


The Quarters directory contains a note for each quarter. 

I try to follow **The 12 Week Year** process as I have found it helps to keep me on track towards my goals and projects. 

You can check out my book notes for that book here: [The 12 Week Year by Brian Moran - Book Notes, Summary, Review](/12-week-year-brian-moran)

#### **Naming Format**

The naming format for quarter notes is: *Q1-2021*. Q1 for example denotes the quarter (quarter 1) and the year shows me which year it belongs to.

#### **Quarters Index**

The first note in this directory is quarters-index which is an index of all my quarter notes.

This is automatically generated using the Dataview plugin which queries the frontmatter of each note like querying a database.

```dataview
list
from "01-life-os/02-quarters"
where contains(file.name, "Q")
sort file.name desc
```

#### **Quarter Note Template**


The first section of the template contains the file name.

Underneath that, I link the quarter to the appropriate year with a backlink. This allows me to easily navigate to the correct year from inside the quarter note.

The next 3 sections are lists of my Goal, Project, and Week notes. These are all automatically pulled in using the Dataview plugin.


**Goals:**

```dataview
list
from "01-life-os/03-goals"
where theQuarter = "Q1-2021"
sort file.name asc
```

**Projects:**

```dataview
list
from "01-life-os/04-projects"
where theQuarter = "Q1-2021"
sort file.name asc
```

**Weeks:**

```dataview
list
from "01-life-os/05-weeks"
where theQuarter = "Q1-2021"
sort file.name desc
```

Following this, I have my quarterly review section that I fill out at the end of each quarter. 

```
## Quarterly Review:

### Review Of Goals
- Look back at the goals I set for the quarter
- What were the themes/buckets associated with these goals?
- Did I achieve my goals?
- If not why not?
- Will any of these goals carry forward into the next quarter?
- If so, what needs to change to ensure success this time around?

### Review Of Projects
- Look back at the projects I undertook in the last quarter
- What were the themes/buckets associated with these projects?
- Were these linked to any of my goals?
- What one thing did I learn from each project?
- What one thing would I change if starting each project again?

### Review Of Weekly Reviews
- Look back at the weekly reviews from the last quarter:
- What were the 3 most important lessons I learned

### Start Stop Continue
- What should I start doing next quarter?
- What should I stop doing next quarter?
- What should I continue doing next quarter?

### Setting New Goals
-   Pick 1-2 new goals to work on for the next quarter
-   Fill them out in the Goals DB
-   Define any related projects that need to be created to accomplish the goal(s)
```


### 03-goals

![Goals Directory Screenshot](/assets/images/2021/obsidian-setup-goals.png)


The Goals directory contains a note for each goal I set for myself. These will usually come from my **quarterly and yearly reviews**. 

The process if picking goals during my quarterly + yearly reviews helps to keep me focused and prevents me from trying to do too much at once.

#### **Naming Format**

I use icons at the start of the note to denote the goal's status:

- ⚪ - To Do
- 🟠 - In Progress
- 🟢 - Complete
- 🔴 - Failed

Yes, believe it or not, I fail at some of the goals I set for myself. 

I still like to keep those goals in my Obsidian system to review every once in a while. I definitely try to **learn from my failures** and this is a big part of that process.

As for the actual note name, I try to keep the name of the goal concise and understandable so I know what it is at a glance. 

#### **Goals Index**

The first note in this directory is goals-index which is an index of all my goal notes.

This is generated using the Dataview plugin which queries the frontmatter of each note like querying a database.

```dataview
list
from "01-life-os/03-goals"
sort file.name
```

I also keep a list of **potential goals** I might like to work on in the future in this note.

#### **Goal Note Template**

This template starts with the front matter which is used by the Dataview plugin.

I have the year (theYear) and the quarter (theQuarter) which is what most of my Dataview queries look for.

{% raw %}
```
---
 theYear: 2021 
 theQuarter: Q3-2021
---
```
{% endraw %}

Next, I have some more note data including the title, status, year, quarter, and project. 

I realize that I'm duplicating the Quarter and the Year but this way I can use backlinks as well as the Dataview functionality.


{% raw %}
```
# {{title}}
Status:
Year: [[🔄 Y-2021]]
Quarter: [[🔄 Q3-2021]]
Project:
```
{% endraw %}

The next section relates to defining the goal itself. What it will entail, and what success looks like.

````
## Goal Background

## Goal Outline
**_Specific_**
**_Measurable_**
**_Achievable_**
**_Relevant_**
**_Time-Bound_**

## Definition Of Success

## 3 Reasons For Failing
What are the top 3 reasons why I might fail at this goal?

## How To Stack The Deck In Your Favor
Based on my reasons for failing, what strategies can I make use of to achieve my goals?

## Action Plan
Include the next actionable task I can do right now to start working towards my goal.
````

The final section is for my **goal review**. 

When I have accomplished (or failed) at a goal, I reflect on what went well and what I could improve on next time.

````
## Goal Review

### Did I Achieve This Goal?

### Why or Why Not?

### What 1 thing would I have done differently?

### What 1 thing did I learn from this experience?
````


### 04-projects

![Projects Directory Screenshot](/assets/images/2021/obsidian-setup-projects.png)

The Projects directory contains a note for each project I want to work on. 

These typically stem from the goals I'm currently working on. 

I also create projects that aren't directly tied to my goals but I try not to do this too often to prevent working on too much at once. 

You might be noticing a trend here of trying to prevent overwhelm and only focus on the most important stuff.

#### **Naming Format**

I use icons at the start of the note to denote the project's status:

- ⚪ - To Do
- 🟠 - In Progress
- 🟢 - Complete
- 🔴 - Failed

I then use a key: MXP21001

- *MXP* - Mishacreatrix Project
- *21* - the year (2021)
- *001* - the project number

Following the key I have the name of the project itself: "*blank-page-as-a-creator-ebook*".

Here's what an example note name looks like for a project: **🟢 MXP21011-blank-page-as-a-creator-ebook**

#### **Project Index**

The first note in this directory is project-index which is an index of all my project notes.

This is generated using the Dataview plugin which queries the frontmatter of each note like querying a database.

```dataview
list
from "01-life-os/04-projects"
where contains(file.name, "MXP")
sort file.name
```

#### **Project Note Template**

This template starts with the front matter which is used by the Dataview plugin.

I have the year (theYear) and the quarter (theQuarter) which is what most of my Dataview queries look for.

```
---
 theYear: 2021 
 theQuarter: Q1-2021
---
```

Next, I have some more note data including the title, status, year, quarter, and goal. 

{% raw %}
```
# {{title}}
Status:
Year: [[🔄 Y-2021]]
Quarter: [[🔄 Q1-2021]]
Goal:
```
{% endraw %}

The next section relates to defining the project itself. What it will entail, my workings and what I learned from the project once it's completed.

````
## Project Background
## Proposed Implementation
## Time Frame
## Notes
## Daily Notes
## What I Learned
## What Could Be Improved Next Time
````

#### **Project Ideas Kanban Board**

I have recently been playing around with the Kanban Board plugin and have found it to be extremely useful. 

So much so that I created a Project Ideas kanban board note.

Any time I think of a potential new project idea, it gets a note on the Kanban board. I currently have each note grouped based on the type of project.

For example: 

- Websites - ideas for websites to build
- Notion Files - ideas for Notion files + templates
- Figma Files - ideas for Figma files + templates
- eBooks, PDFs, Guides
- Needs more research - not yet sure what the implementation will look like so needs more thought.

When it comes to my quarterly and yearly reviews, I look at this board to pick what projects I can work on next.

### 05-weeks

![Weeks Directory Screenshot](/assets/images/2021/obsidian-setup-weeks.png)


The Weeks directory contains a note for each weekly review I do. 

I do my weekly review on Friday afternoons but quite honestly I've missed the last couple. 

*This article will serve as a reminder for me to get my butt back in gear and do my weekly reviews!*

#### **Naming Format**

The naming format for these types of notes is:

- *W10* - the week number
- *20210319* - the year (2021), month (03), and date (19)

#### **Weeks Index**

The first note in this directory is weeks-index which is an index of all my week notes.

This is generated using the Dataview plugin which queries the frontmatter of each note like querying a database.

```dataview
list
from "01-life-os/05-weeks"
sort file.name desc
```

#### **Week Note Template**

This template starts with the front matter which is used by the Dataview plugin.

I have the year (theYear) and the quarter (theQuarter) which is what most of my Dataview queries look for.

```
---
 theYear: 2021 
 theQuarter: Q1-2021
---
```

Next, I have some more note data including the title, year, and quarter. 

{% raw %}
```
# {{title}}
Year: [[🔄 Y-2021]]
Quarter: [[🔄 Q1-2021]]
```
{% endraw %}

Next, I have the main content of the weekly review:

```
## Get Started
-   Clear Desk space
-   Zero Inboxes
-   Review last week's entry
-   Review daily reflections

## Reflections
### What Went Well This Week?

### What Should I Start Doing?

### What Should I Stop Doing?

### What Should I Continue Doing?

## Work Log

## Planning
- Review next week's time blocks
- Add & schedule tasks for the next week

## Shut Down
"I am finished work for today"
```

---

## 02-literature

The Literature directory contains notes for all the content I consume and learn from. This includes articles, books, videos, courses, and even social media posts.

### **Naming Format**

I start each note with the content type:

- *{a}* - article
- *{b}* - book
- *{v}* - video

Then I simply include the name of the book, article, or video.

### **Labels**

The labels I use depend on the type of content:

- #literature/article - article
- #literature/book - book
- #literature/video - video

### **Literature Note Templates**

The template I use will vary depending on the type of content:

#### Article Template

This is for notes based on the articles I read. 

I clip articles from the web into a Notion DB. You can check out my [Notion Library Tour](https://www.heymichellemac.com/notion-library-tour) to see how I capture this content.

Once I've read an article and taken rough notes, I create an Article note in Obsidian and refine my notes.


{% raw %}
```
# {{title}}
URL:[Article Link]()
URL:[Notion Link]()
Source:
Tags: #literature/article
Topics:
```
{% endraw %}

#### Book Template

This is for notes based on the books I read. Similar to Article notes, Book notes start life in Notion and are then refined in Obsidian.

I publish the book notes I create [here on my website](/tag/book-notes) as well as add them to my [Knowledge Vault of Digital Notes](/knowledge-vault-digital-notes).

{% raw %}
```
# {{title}}
Author:
Tags: #literature/book
Topic:
URL:[Notion Book Notes]()
URL:[Mishacreatrix Book Notes]()

## The Book In 3 Sentences
## Who Should Read This Book?
## How The Book Changed Me
```
{% endraw %}

#### Video Template

This is for notes based on videos I watch.

{% raw %}
```
# {{title}}
URL:[Video Link]()
URL:[Notion Link]()
Channel:
Tags: #literature/video
Topics:
```
{% endraw %}

---

## 03-evergreen

The Evergreen directory contains all my evergreen notes. 

There are lots of definitions of [evergreen notes](https://maggieappleton.com/evergreens) but for me, these are atomic ideas or concepts that I find useful, I learn something from, and are interesting to me.

#### **Naming Format**

There is no naming convention for these types of notes, I just try to make sure they are understandable out of context as they should stand on their own.

#### **Labels**

These types of notes are labeled: *#evergreen.* 

#### **Evergreen Note Template**

This is a simple template with the tags, topics, note content itself, then the source at the bottom of the note.

````
Tags: #evergreen
Topics:


Source:
````

---

## 04-resources

The Resources directory is where I store other useful things like code snippets, various lists, and guides.

This directory contains the following sub-directories:

- 01-code-snippets 
- 02-guides
- 03-lists

### 01-code-snippets

If I come across useful code snippets I make sure to put them in this directory for later use.

This includes things I want to try for myself or code snippets that might be useful for work to achieve a specific effect.

There's no real template for these files, I simply copy and paste the code snippet into a dedicated note.

#### **Labels**
The label I use for these types of notes is: *#resource/codesnippet.*

### 02-guides

In this directory I store any useful guides, walkthroughs or step by step processes I use on a regular basis.

For example, I have a note on Jekyll which is simply a collection of things I learn about that platform.

I also have a fun note on how to solve a Rubiks cube from [the time I challenged myself to learn how to solve one](/rubiks-cube-focus).

#### **Labels**

These notes are labeled: *#resource/guide.* 

### 03-lists

As you might have guessed, this directory holds a lot of lists. Nothing too exciting here but very helpful nonetheless.

Some examples include: 

- gift ideas for family and friends
- bookmarks
- mechanical keyboard resources (yup, I've gone down that rabbit hole..)
- digital product inspiration

#### **Labels**

These notes are labeled: *#resource/list*.

---

## 05-Creation

The Content Creation directory is where I store everything related to the content I create. This includes articles, social media posts, my newsletter, and the design tips I share.

This section is the secret sauce of my content creation process so you'll have to see it first hand to see what it involves 😉

- [Design Insight Newsletter](https://designinsight.substack.com/welcome)
- [Mishacreatrix Website](https://heymichellemac.com/)
- [Mishacreatrix - Twitter](https://twitter.com/heymichellemac)

---

## 06-topics

This directory contains the notes that serve as my Topic anchors. 

These notes are typically blank but serve as a useful way to navigate notes based on topic.

### **Naming Format**

The naming format for these types of notes is simply the topic name.

Some examples include: 

- Agile Development
- Color Theory
- Cognitive Bias
- design Patterns.

#### **Topics Index**

The first note in this directory is topics-index which is an index of all my topic notes.

This is generated using the Dataview plugin which queries the frontmatter of each note like querying a database.

---

## 07-people

This directory contains notes for people, as weird as that sounds. 

Anytime I reference a person in one of my notes I make sure they have their own People note. 

By doing this I can easily see other notes related to that person. This can be useful when you're looking for a particular quote or piece of insight from a specific person.

Similar to the Topics section, I don't have a lot of content in these notes, they are an anchor for all the other notes they're linked to.

#### **Naming Format**

People notes are formatted like this *@Ali Abdaal*. The @ denotes a person. This makes them easy to spot in a note or on a search results page.

#### **People Index**

The first note in this directory is people-index which is an index of all my people notes.

This is generated using the Dataview plugin which queries the frontmatter of each note like querying a database.

---

## 08-sources

The Sources directory contains notes for 'sources' i.e. Blogs, Websites, Podcasts.

Again, these notes serve as an anchor for all of the other notes they are linked to.

#### **Naming Format**

The naming format for these notes is simply the name of the source e.g. Medium Blog, Bookworm Podcast, NNGroup Blog.

#### **Sources Index**

The first note in this directory is sources-index which is an index of all my sources notes.

This is generated using the Dataview plugin which queries the frontmatter of each note like querying a database.

---

## 99-attachments

The Attachments directory is where all the images I add to Obsidian live.

I don't do a lot of maintenance on this directory so it's probably a huge mess right now!

This can be configured in Obsidian under *Settings > File & Links > Default location for new attachments*.

---

## 99-daily notes

I use the Daily Notes core plugin which creates a new note for each day. This folder is where those notes are stored.

Quite honestly I use this feature off and on depending on how I'm feeling. I use it every day for my work vault but not that often in my primary vault.

In the past, it has been useful to write notes about my day but there were times when I felt this was just taking up space and wasn't necessary to be keeping track of. 

Besides, I also use a Bullet Journal so most things I need to get out of my head are stored there.

I'm keeping this folder around for now. Perhaps I'll try and experiment with using it more often to see how useful it could be.

---

## 99-templates

The templates directory is where I store all my note templates. This all works in conjunction with the **Templates core plugin**. 

On a new note, I simply press *CTRL + T* and select the template to populate the note with.

This process alone saves me more time than anything else in this whole system so I'm always reviewing each template to make sure it's up to date and useful.

---

## Conclusion

Whew, you made it to the end of this article! A sincere thank you for reading all the way to the end.

I hope this article provided you with some inspiration for ways to tweak and improve your own Obsidian setup. 

If you found this helpful or you learned something new, please consider sharing it on social media as it will help others to find it.

As always, if you have any questions, comments, or feedback please let me know over on Twitter.