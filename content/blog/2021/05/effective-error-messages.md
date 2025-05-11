---
categories:
- blog
date: '2021-05-03'
tags:
- design
title: UI Design Patterns - How To Write Effective Error Messages
width: wide
---

Any well-designed application should have good error messages. When I say good error messages I'm not talking about a message like *"Critical Error x-299498sdkfjh"*. Let's face it, that helps no one. 

A good error message will tell the user what happened, why it happened, and how the user can fix it.

Errors will always happen no matter how well you build something. This is because you can't account for how every single user will interact with your app. 

Not every user will follow the happy path. 

There will be mistakes along the way that are caused either by the user or your app. 

That's why it's important to consider error handling and how to provide a better experience for your users.

I recently did some research into creating effective error messages to improve how I design them. 

In this article, I would like to share with you the best practices I have learned for writing effective error messages. The article is broken up into a list of guidelines to follow, with each section discussing a particular guideline. 

I hope you find this information helpful.

![How To Write Effective Error Messages - Pin](/assets/images/2021/effective-error-messages-pin.jpg){:class="image-pin"}

---

## #1 Error Messages Should Be Clearly Visible

You might be thinking "well duh?", but let's break this guideline down to discuss why it's so important and how you can put it into practice.

The simple fact is that if a user makes a mistake and an error occurs, the user should get some sort of feedback on the screen to let them know. 

If there's no feedback, either the user will assume everything is fine or they'll become frustrated because they don't know what's gone wrong.

This ties into rule number one of the [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/) - Visibility of System Status.

> "The design should always keep users informed about what is going on, through appropriate feedback within a reasonable amount of time." - Jakob Nielsen (NNGroup)

As a quick aside here, I always look to this set of principles when I'm reviewing my designs or performing a UI review of an existing system. 

They provide helpful guidance on how an app should look and behave. 

To ensure that the user stays informed about what's going on, they need to be alerted when something has gone wrong. This brings us back to clearly visible error messages.

The error message should stand out on the screen, either through use the of color contrast, different iconography, a modal window, or some combination of these design patterns.

To ensure there is enough contrast in your error messages, it's important to use a different color from the rest of your color palette. One that stands out. 

In practice, these are usually reds or oranges for critical or warning messages.

Something worth noting here is that you shouldn't rely on color alone to convey a message. Users with color-blindness won't pick up on these visual cues. 

It's important to make use of icons and other UI elements in addition to color to ensure the importance of the message is conveyed to the user.

---

## #2 Error Messages Should Have Human Readable Text Without Code or Jargon

This guideline lines up with the usability heuristic: match between system and the real world.

> "The system should speak the users' language, with words, phrases, and concepts familiar to the user, rather than system-oriented terms." - Jakob Nielsen (NNGroup)

What we should take from this guideline when talking about error messages is that we shouldn't output code or log lines as an error message to the user. 

It can be off-putting as a user to see something like "log output xesdk, critical, fail, exception 832843".

This type of output is difficult for any user to decipher. 

Not to mention it also seems unprofessional. After all, most users don't want to see how the sausage is made, they just want to use your app.

While I do agree that adding plenty of detail to the logs when an error is thrown is beneficial to developers, it shouldn't be seen on the front-end.

In a similar way to log output in an error message, you should also avoid any technical or discipline-specific jargon or abbreviations in your messages.

You shouldn't assume all users know what any of these buzzwords mean. Instead, opt for simple and clear wording that's easy to understand.

---

## #3 Error Messages Should Be Polite In Tone

This one can be easy to overlook. 

You may be more concerned about developing a well-designed error message pop-up than the tone of voice being used to explain the issue.

It can be easy to write an error message that we feel accurately describes the error but we can fail to see this message from the user's perspective.

Certain phrases such as "you did" or "you have entered the incorrect information" can sound like the user is being blamed for triggering the error.

Sure, this may even be the case, but blaming the user for making a mistake will only add to their frustration.

From the user's perspective, your app didn't behave as they expected which resulted in the error message. 

Then to add insult to injury, the user is being blamed for the error? 

Now they're likely frustrated and considering switching to a different app. All because of the language used in the error message.

It may sound extreme but it can happen.

To overcome this, you need to stop seeing the user as the problem and consider the system or app logic instead.

It's impossible to know how every single user will interact with what we design so with that in mind errors are bound to occur.

Oh, and one final note here as this is something I've been guilty of in the past.

Avoid upper case messages and those with ! at the end of a sentence. 

These are all things that make it seem like you're SHOUTING AT THE USER!!!

---

## #4 Error Messages Should Have Helpful Text

This guideline can be attributed to the following usability heuristic - Help users recognize, diagnose, and recover from errors.

> "Error messages should be expressed in plain language (no codes), precisely indicate the problem, and constructively suggest a solution." - Jakob Nielsen (NNGroup)

A helpful error message requires that you tell the user:

- What happened to cause the error
- Why the error happened
- What the user can do to resolve the error and prevent it from happening in the future.

The more complicated an error message seems, the more cognitive load this adds to the user's mind. 

This can build up and once it reaches a certain threshold the app is unusable to the user.

As a designer, it is your job to guide the user through an application that they have never used before.

In the context of error messages, you need to clearly and concisely explain to the user how they can fix the error and get on with their work.

If a user takes a long time to resolve an error, they may have forgotten what they were doing prior to that error message.

With that in mind, you want to make it as easy as possible for the user to resolve the error and continue doing what they were doing.

---

## #5 Error Messages Should Be Short And To The Point

Most users that interact with any website or app on a daily basis will scan a page rather than read everything. 

People are looking for something specific and want to find it quickly.

With that in mind, the more text, images, or videos you have on a screen, the harder it is for a user to scan. 

This can make it easy for them to miss something like an error message, especially if it's longer than a couple of sentences.

When it comes to the wording of error messages, keep things short and to the point. 

Remove any detail or words that aren't needed. You should be able to read the error message out loud and clearly understand its meaning. 

If the error requires more comprehensive troubleshooting steps to resolve, use [progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/) to provide that additional information if the user chooses to see it. 

Don't include all of this information in the error message box as it will add too much visual clutter.

---

## #6 Make Sure You Preserve The User's Work

When a user is in the middle of performing a task and they are interrupted by an error message, this stops their flow and directs them away from what they were doing.

This interruption of flow can have a negative impact depending on how the error is presented and how long it takes for the user to resolve it and resume work.

If it takes a long time for the user to determine the cause of the error and resolve it, they may have forgotten what they were doing before that error happened.

Similarly, if they have to start their task from scratch after recovering from an error, this can be frustrating.

It's your job as the designer to minimize the friction an error causes on the user's flow. 

With that in mind, it's important to ensure any progress the user made towards filling in a form for example is preserved. 

This allows them to continue filling in the form without having to fill in all the fields from scratch any time they hit an error.

Minimizing the friction experienced during an error is important to ensure users can recover from the error and continue their work.

---

## #7 Modal Or No Modal?

There are many ways error messages can be presented to the user and many different types of error messages.

This is why it's important to understand the reason behind each error message to determine how it should be presented to the user.

The main question a designer might have is whether to put the message in a pop-up modal or not.

With that said, the simplest way to boil this decision down is to ask yourself:

*Should the user be interrupted to see this error message?*

If the answer is yes, as might be the case with a critical message, then **you should** put it in a modal.

If the user doesn't need to be interrupted, then don't use a modal.

---

## #8 Review Your Use Of Error Messages

The final point I want to discuss here is the use of error messages in general.

I've talked at length now about how to design and structure error messages without talking about the merit or need for them.

An application filled with helpful error messages is still an application riddled with error messages.

Consider ways of preventing errors in the first place so that you can keep error messaging to an absolute minimum.

Alternatively, if you have analytics running on your application, you will see over time the errors that are being triggered by users. 

With this data at hand, you can develop ways to work around these errors to prevent them from happening. This will help to cut down on the number of error messages in your app.

---

## Conclusion

Thank you for reading this article. I hope you found some valuable insights from what I've shared with you today.

If you enjoyed reading this article, please consider sharing it on social media to help others to find it.

If there are any tips you'd like to add to this list, reach out to me on Twitter and let me know.