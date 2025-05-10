---
categories:
- blog
date: '2020-12-11'
tag: Design
title: UI Design Patterns - What’s The Difference Between Search and Filter?
width: wide
---

As a UI designer at the company where I work, I am often tasked with creating new designs for complex systems that manage a lot of data. 

One thing I can be sure of is that the design will require tables of some sort. The next most frequently used components are either searches or filters to manage data.

Over time designing these complex UIs, I found that what I imagined in my head and my prototypes weren't always what came into fruition. 

Certain interactions didn't work the way they were expected or colors caused issues and confused users into thinking something couldn't be interacted with. The concepts of search and filter were mushed together based on whatever design framework being used implemented those features.

I eventually realized this disconnect was happening because I didn't have the proper vocabulary when describing search vs filter.

That's when I set about researching for this article.

**This article will outline the difference between search and filter so you'll learn the vocabulary and the reasons to use each component as well as how to implement each component.** 

---

## Searching

### What Is Search?

When you search, you start from a blank screen and enter a search term to return a list of results based on that search term. 

Google is a great example of search in action so pay close attention to the little details the next time you're searching for something there.

Search is described as a more general way of finding data. This is because the results returned will display all of the data that matches the keywords in your search query.

Because searching has been around for so long on the web, [users have built up solid mental models](https://www.nngroup.com/articles/mental-models-for-search/) of how it's expected to work. 

This is extremely important to know as a UI or UX designer. 

If your design conflicts with the user's existing mental models for searching, they will have a hard time interacting with your system. 

Your job as a UI designer is to create a smooth and positive experience to ensure users return to your product.

### What Are The Components Of A Search Feature?

We're still out on the outskirts of the term search so let's examine what makes up a search feature.

A search feature is made up of 3 components:

- An input box - where a user can type their search term
- A search button - that is selected to run the search
- A list of search results - that return data or information matching the keywords of the user's search term

In addition to these 3 core features, users often expect search to be in certain places on a website. 

They typically expect a search component to be available on the top right of the screen. What's more, the search component should be a search box and not a link.

Another thing to keep in mind is the size of the search component. The search box itself should be wide enough to fit almost all search terms. Otherwise, this will cause the user to have to scroll as they type and this will negatively affect usability.

With that in mind, it's useful to understand the types of search terms that will be entered into the search box by a user so you can prevent this from happening. 

This requires research beforehand to understand the user and their goals. 

Additionally, you can also monitor the search terms entered via Google Analytics or similar analytics programs.

### When Is Search Used?

Now that we know what search is, let's take a closer look at when it should be used.

**#1 To bring users to what they're looking for quickly**

Search lets users bypass the intended navigation of a website. In most cases, a user simply wants to find the thing they are looking for. This is the [paradox of the active user](https://www.nngroup.com/articles/paradox-of-the-active-user/) in action.

The paradox of the active user is basically that the user never reads the manual. They would much rather get started using something immediately. 

I'm sure you've experienced this yourself when using a new piece of software or when you've tried to build IKEA furniture without the manual!

This phenomenon is a paradox because the user would actually end up saving themselves lots of time in the long run if they just spent some time at the start reading the manual or watching training videos.

With this paradox in mind, designers need to design for the way users actually behave, even if this is in an irrational way.

**#2 To allow users to escape if they get lost**

Search is also used as an escape option for a user if they get lost on your website. 

If they somehow get lost down a rabbit hole of information or similar, the first thing a user will likely do is to turn to the search bar to navigate them somewhere else.

With that in mind, it's important to have a search feature on every screen as you don't know when a user will become lost and look for something else.

**#3 To bring users to what they're looking for easily**

Typical users are not great at query reformulation. 

This means that if they don't get the results they are looking for on the first try, chances are they will give up and go somewhere else. 

This is why it's important to increase the chances that a user will find what they're looking for on the first attempt.

As well as this, users will rarely scan beyond the first page of web results. 

That is why prioritizing the search results is also something important to consider. 

Examine the most common queries in your logs to determine the best strategy for this.

One final piece of advice is to offer advanced search only if the user needs it. In most cases, the user simply wants the search box. 

With that said, some power users would find value in an advanced search feature. 

Consider design patterns that Amazon and other big data companies use: "Didn't find what you were looking for? Try Advanced Search".



## Filtering

### What Is Filtering?

When you are filtering, you are refining/reducing the number of items from a full list of data (If you remember, this is the opposite of a search which starts from a blank screen).

This is described as a more accurate way of finding data because the filters are selected by the user from an existing list of items. 

Filtering helps to refine the data based on categories or characteristics. 

As well as this, filters eliminate results that do not specifically match the selected criteria.

This is all especially useful if the user doesn't know the dataset very well and wants to explore.

### Using Different Types Of Filters

While search is a more straightforward component as far as its structure goes, there are different types of filters that can be used. Let's look at this in more detail.

The type of filter you choose will depend on the speed of your website as well as the user's intent when navigating your site.

By being able to determine the user's intent when looking for something, you can determine the most efficient type of filter to use (interactive or batch filtering - we'll describe in more detail below). 

This creates a smooth experience and allows the user to find what they're looking for.

Page speed is also a factor in determining which type of filter to use as this can impact the user's experience when interacting with the filter.

**Interactive Filtering**

Interactive filtering occurs when you select one filter and the list of results immediately updates. As you continue to select more filters the results list updates each time.

This is good for users who are in an "exploratory mindset" and want to learn about the data that's available to them.

If used incorrectly, like if the user has a different mindset (as in they know what they want to filter for) or if the site is slow to retrieve the data, then this can become disruptive for the user as the results will refresh each time a filter is selected.

A disadvantage of interactive filtering is that continuous page updates can become visually distracting to the user. 

To overcome this, you can simply overlay a dark color on the results set and show a progress indicator before displaying the new results.

**Batch Filtering**

Batch filtering occurs when you select a number of filters before the list of results updates. 

This is of benefit to users that have a clearly defined set of criteria. They simply want to enter their filters and get to their data.

This is also good for slow sites where data retrieval may take some time. That's why this is the best option to implement on mobile devices.

Batch filtering is certainly the safest option as regards filters as it allows the users to tell you when they're done selecting filters.

**Wait For System Response**

Another way of implementing filters is by allowing the system to wait 1-2 seconds and if there has been no user input in that time, then refresh the results.

With that in mind, the system should still indicate that the first input has been received as this gives immediate feedback to the user ([Visibility of System Status - Usability Heuristic](https://medium.com/nyc-design/1-visibility-of-system-status-with-examples-5e3bc9adfe7b)).



## An Example That Describes The Difference Between Search & Filter

Now that we've looked at each type of component, let's look at a great example that highlights the differences between both search and filter.

Imagine you are looking for a pair of Bose Noise Canceling Headphones.

You will probably go to Amazon and type in "Bose Noise Canceling Headphones" into the search bar (This is performing a search).

The results returned will match Bose, Noise Canceling, and Headphones. The first page or so will return the most accurate products.

However, as you click through more pages, you'll find different brands of headphones other than Bose, or headphones that aren't noise canceling, or other Bose products than headphones. 

As you continue the products become less and less relevant to what you initially searched for.

Now, if you were to perform a filter based on the category headphones, the brand Bose, and select noise canceling as a feature, you'll find a more accurate set of results that match those filters.

Any other brands should be eliminated from the results list. You should only see headphones on the list plus those headphones should have the noise canceling feature.



## Conclusion

Hopefully from reading this article you've been able to learn the basics between search and filter and you can start using them more effectively in your designs.

I was able to learn quite a bit from my research into these topics and hope you found some value in what you've read.