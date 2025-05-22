---
categories:
- project
date: 2022-08-17
title: Gaming Backlog Tracker
type: blog
width: wide
---

This project is a list of the games in my PlayStation backlog.

I recently subscribed to the new [Playstation Plus Extra](https://www.playstation.com/en-gb/ps-plus/#subscriptions) tier to be able to avail of all the games this plan has to offer. So as you can imagine my backlog grew enormously overnight.

It became a chore to look through a list and try to find my next game to play as I couldn't get a sense of the games I could play. 

My brain loves organization and pretty things so I thought about building my own tracker but didn't get anywhere with it so stayed using my Google Sheet to track my games.

By accident, I stumbled across [this thread](https://gaming.stackexchange.com/questions/365295/is-there-a-public-list-of-the-ps4-games-i-own#:~:text=My%20PlayStation%20Account,with%20all%20of%20your%20trophies) which inspired me to try building this project once again, and I succeeded (for the most part).

Turns out you can grab a JSON list of the games you've purchased via PSN. The coders out there know the value of a JSON list of data so you'll understand how happy I was after discovering this. 

I already track my games in an excel sheet ([which you can download here for free btw](https://heymichellemac.com/video-game-trackers)) so I already had a good amount of data to work with and manipulate.

The tech stack for this project is Jekyll, Tailwind CSS, and Netlify; pretty much my go to stack at the moment for fun projects like this.

I had a ton of fun working on this project and honestly there's a lot more I'd like to do with it but for now it's good enough to share with you.

Some things I'd like to experiment with adding in the near future:

- Adding PS3 games to the list.
- More automation to update the list more automatically.
- Experiment with web scraping a bit more to be able to pull trophy data from PSN profiles.

<div class="flex pt-4">
<a style="text-decoration:none;" href="https://backlog.heymichellemac.com" class="flex items-center bg-pink-500 px-4 py-2 rounded-md font-medium text-white shadow-md transition-all border-2 border-pink-500 hover:border-white" target="_blank" rel="noopener noreferrer">
    <span class="mr-1">View the live project</span> 
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="inline feather feather-external-link ml-2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" ></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
</a>
</div>