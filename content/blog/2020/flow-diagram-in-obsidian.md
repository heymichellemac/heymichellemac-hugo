---
categories:
- blog
date: '2020-12-21'
tags: 
- pkm
title: How To Build A Flow Diagram In Obsidian Using Mermaid
width: wide
---

As an avid Obsidian user, I am always curious to learn how I can get the most out of this application. 

I love watching YouTubers live-stream their work process in Obsidian and I'm constantly scouring the Obsidian Forums for nuggets of helpful tips and tricks.

If you're not familiar with Obsidian, it is a popular knowledge management tool built on markdown files. 

I started using it after reading the book How To Take Smart Notes and learning about the concept of Zettelkasten and permanent notes.

Anyway, after building up a good amount of notes in my knowledge management system (KMS) I continued to look through YouTube for videos of Obsidian in use. That's when I came across a super-comprehensive video by [Bryan Jenks about his Obsidian workflow](https://youtu.be/Ewhfok91AdE).

What particularly stood out to me was the use of a flow diagram to illustrate Bryan's workflow for processing content across multiple different sources.

As someone who was looking to define this process for myself, this was more than enough motivation for me to try to create my own version of this flow diagram (even though this meant completely procrastinating from other work for a good chunk of an afternoon).

With all of that in mind, in this article, I want to share with you how to create a flow diagram in Obsidian using Mermaid.js. 

We'll look at the benefits of these diagrams, the basics of Mermaid as well as the step by step process of creating a knowledge management flow diagram.


## The Benefits of Using Diagrams In Your Knowledge Management System (KMS)

If you're here and reading this article, you may already know why you want to create diagrams in Obsidian. 

With that said, there are plenty of benefits to making use of diagrams in your KMS that I think are worth mentioning. 

Let's take a look at them in more detail:

### #1 It gives your thoughts a visual organized structure

When we think about something even slightly complex in our heads, it's difficult to understand how all the pieces fit together. 

Similarly, in the book [The Bullet Journal Method](/bullet-journal-method-ryder-carroll), the author Ryder Carroll explains that: 

> If each thought were a word, that means our minds are generating enough content to produce a book, every day.

By learning to create a helpful diagram, using Mermaid for instance, you can quickly get those most important thoughts and ideas out of your head and into a structured visual that you can look at whenever you need to.

In addition to creating a visual for your thought, this also have the effect of removing those thoughts from your head so you can focus on other things. 

If you've ever heard of the [Zeigarnik Effect](https://link.springer.com/chapter/10.1007/978-3-030-46463-9_10) then you'll know what I mean here. This concept is widely referenced from Getting Things Done to The Productivity Project so there's a lot of merit to this idea of getting thoughts out of your head.

### #2 You can share your process with others

Once you've created something tangible from your thoughts, you can easily share this with others to see what they think.

Capture a screenshot of your diagram and share it on Twitter or on the [Obsidian forums](https://forum.obsidian.md/) to talk about your process with others.

This is a great way to garner feedback from like-minded people and perhaps it will shed some light on things you hadn't thought about before.

If I learned anything from the book [Show Your Work by Austin Kleon](/show-your-work-austin-kleon) it's that there will always be someone interested in what you have to share.

What's more, the area of personal knowledge management and KMSs is extremely talked about right now so something like a Mermaid flow diagram would be extremely useful to someone getting started in this area.

### #3 You can cement your understanding of a topic

Understanding things is the key to being able to remember them. 

I learned about this concept from the book [How To Take Smart Notes by Sönke Ahrens](/how-to-take-smart-notes-sonke-ahrens) and I've tried to apply it to every new topic or concept I learn about.

If you're struggling to understand or learn something new, sometimes an excellent way to improve your understanding is by creating a visual like a diagram. 

This allows your brain to create the nodes and the connections in a logical way that makes sense. 

Once you've created the diagram, you can see the elements of a topic and how those elements are connected in a way you may not have before.



## The Basics of Mermaid.js

Now that I've spent some time gushing about the merits of diagrams in your KMS, let's look closer at the tool that's used for creating diagrams inside of Obsidian.

### What is Mermaid.js?

[Mermaid.js](https://mermaid-js.github.io/mermaid/#/) is a Javascript-based programming syntax that is used to create and generate diagrams including flow charts, pie charts, user journey maps, and more. 

It offers a pretty simple and straightforward syntax for constructing diagrams and charts that even people with little coding knowledge can pick up fairly easily.

By making use of this language you can construct helpful diagrams inside of Obsidian for example to outline your processes and workflows.

### What Types Of Diagrams Can You Create In Mermaid.js?

As of the time of writing here is the list of diagram types you can create in Mermaid:

- Flow charts
- Sequence diagrams
- Class diagrams
- State diagrams
- Entity relationship diagrams
- User journey maps
- Gantt charts
- Pie charts

You can always check out the [Mermaid Docs page](https://mermaid-js.github.io/mermaid/#/) to keep up to date with what each of these diagrams is and how they work. 

For this exercise, I just worked with the flow chart type of diagram.

### What Are The Benefits of Mermaid.js

There are many benefits to Mermaid specifically that makes it a great tool to add to your toolkit.

- It can be used in other places outside of just Obsidian - this means you can learn this tool once and apply it in other areas of your work or personal life.
- Diagrams are easy to update and maintain - because these integrate into Obsidian, you can easily update diagrams as your process changes. What's more, if you have your [Obsidian vault synced to GitHub](https://effectiveremotework.com/2020/09/obsidian-sync-your-vaults-with-git-github/) then you won't have to worry about losing it.
- It's relatively easy to pick up without programming experience - as we already mentioned the simple syntax makes it an easy tool to learn.



## Plan Out Your Diagram On Paper

The most important piece of advice I can give to you before starting to create your flow diagram in Mermaid is to draw it out on a piece of paper first. 

This helps you to get things straight on paper so you can focus on building it in Mermaid in one go. 

Once you've been building diagrams enough that you know what you're doing, this process may become less important but it's essential when starting off in Mermaid, in my opinion.

If you have some notes or ideas for your own KMS workflow, spend some time sketching it out now before heading onto the next section where we'll look at the build process.



## Creating Your Flow Diagram In Obsidian

Now it's time to get to the good stuff, actually creating a flow diagram in Obsidian.

### Setup a new Mermaid diagram

Ideally, you'll create a new note for your diagram to keep things clear but wherever you choose to start is up to you.

To create a new Mermaid diagram enter the following text:

```javascript
​```mermaid
graph TD

​```
```

The top and bottom lines tell Obsidian that this is a Mermaid diagram.

The line that says "graph TD" is Mermaid syntax that denotes this is a Top Down (TD) graph i.e. a flow chart.

You could also say "graph RL" to change the orientation of the chart to Right To Left instead of Top Down, but in this case, we'll stick with top down.

### Create your top row of nodes

Next, you can start creating the top row of nodes in your diagram. This can be done by adding this code after "graph TD":

```javascript
id1(Incoming Media)
id1.1(Feedly)
id1.2(YouTube)
id1.3(Pocket Casts)
id1.4(Google Play Books)
id1.5(General Research)
```

Here you can see I've defined the "Incoming Media" node as well as the nodes that define my sources of information (Feedly, YouTube, Pocket Casts, Google Play Books, General Research).

The term id1 is basically a variable for the node. 

This means if you want to refer to this node in other places in the diagram to make connections, you only need to reference id1.

This process might seem quite convoluted but as someone who has a background in programming, this way made the most logical sense for me.

At this stage, you can now switch Obsidian to preview mode to see what you've created. 

You can of course have two panes open, one for edit and one for preview but I prefer to switch between them to prevent distraction.

### Create the next row of nodes

With your first set of nodes in place, you can simply repeat this for the next set. In my case, these are the nodes that define the type of media I'm consuming:

```javascript
id2.1(Web Articles)
id2.2(Books)
id2.3(Videos)
id2.4(Courses)
id2.5(Podcasts)
```

Here you can see I increased the numbering from id1.1 to id2.1 to keep it straight in my head how the nodes are to be ordered.

Again you can preview your work to ensure all is going according to plan. 

Don't worry, it will all be an unconnected mess of nodes at this point but so long as all of your nodes show up you're doing ok. 

### Use comments to help you find your way

As you continue to add more nodes and connections, your code area will become a mess of gibberish.

To overcome this, as any good programmer would, make use of comments to segment your pieces of content:

```javascript
%% Top Node
id1(Incoming Media)

%% Media Sources
id1.1(Feedly)
id1.2(YouTube)
id1.3(Pocket Casts)
id1.4(Google Play Books)
id1.5(General Research)

%% Types Of Media
id2.1(Web Articles)
id2.2(Books)
id2.3(Videos)
id2.4(Courses)
id2.5(Podcasts)
```

As you can see to write a comment we use "%%". 

These comments won't show up in the preview window but help you to navigate through the code if you come back to it at a later point in the future.

### Connect the nodes

Now for the fun part, making connections between the first 2 rows of nodes. In this case the topmost node "Incoming Media" and the media sources i.e. Feedly, YouTube etc.

This is where your paper diagram will come in handy to refer to.

```javascript
id1 --> id1.1 & id1.2 & id1.3 & id1.4 & id1.5
```

This line of code will connect 

- the node id1 (which is "Incoming Media") 
- to id1.1 (which is "Feedly") 
- and id1.2 (which is "YouTube") 
- and so on.

You can see from the code above that the symbol "-->" denotes a connection between nodes.

You'll also see that you can connect one node to many nodes by using "&" after each node.

By switching between preview and edit mode after each change to your code, you'll start to see how each piece of code affects the finished diagram.

Now you can connect the next two sets of rows. In this case the Media Sources with the Types of Media.

Again, be sure to refer to your paper diagram to ensure you're making the right connections:

```javascript
id1.1 --> id2.1
id1.2 --> id2.3
id1.3 --> id2.5
id1.4 --> id2.2
id1.5 --> id2.4
```

### Continue creating nodes and connecting them

Continue with the process of adding nodes and connecting them until you've finished outlining your flow diagram. 

Refer back to the code you previously wrote to ensure you're using the same conventions.

### Add text between connections

If you want to add more detail to your diagram, you can add text between the connections as I've done here:

```javascript

id2.1 -- To Read --> id2.1.1
id2.1.1 -- In Progress --> id2.1.2
id2.1.2 -- To Be Reviewed --> id2.1.3
id2.1.3 -- To Be Processed --> id2.1.4
id2.1.4 --> id2.1.5

```

Simply use "-- TEXT HERE -->" to add text in the connection between two nodes.

### Preview frequently to ensure things look as you expect

As I mentioned above, be sure to preview the diagram often to ensure things are going as expected.

This for me was the best way to learn Mermaid. 

By seeing how what I was writing was changing the output I could understand how it all worked.

### Styling your diagram

There is a whole heck of a lot more stuff you can do with your diagrams that I haven't even touched on in my diagram. 

In my case, the theme I'm using does the job of styling everything simply and clearly, so I didn't even start looking at styling each of the nodes or connections.

I also found that nodes and connections were all I needed to create my diagram so I didn't look too deeply into the other types of components like different shaped nodes or differently styled connections.

If you want to explore the whole area of custom styling for your diagram you can find more information in the [Mermaid Docs page](https://mermaid-js.github.io/mermaid/#/).

### Once you're finished, share your diagram with others

By the end of this process, you should have a clear and comprehensive diagram that showcases your knowledge management workflow i.e. your process for processing information.

As I talked about at the start of this article, the best way to get feedback on your work is to share it with others. 

With that in mind, check out the [Obsidian forums](https://forum.obsidian.md/) which is an excellent resource full of very helpful people.