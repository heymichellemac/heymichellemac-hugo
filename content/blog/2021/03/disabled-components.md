---
categories:
- blog
date: '2021-03-03'
tag:
- Design
title: UI Design Patterns - How To Handle Disabled Components
width: wide
---

I recently had to do some research to figure out how to properly handle disabled fields and buttons (I'm collectively calling them components). This design pattern is quite often used across my designs so I wanted to be sure I was implementing it correctly.

It turns out there was a lot I didn't know about this design pattern. 

Despite that, I continued to research and develop my knowledge of designing disabled components.

In this article, I'd like to share with you everything I have learned about how to handle disabled components. We'll look at when to use them, when not to use them and best practices for styling disabled components.

![How To Handle Disabled Components - Pin](/assets/images/2021/disabled-components-pin.jpg){:class="image-pin"}

---

## Disabled Vs Readonly Attributes

The first thing worth talking about is that functionally there are 2 ways to go about "disabling" or preventing a user from interacting with a component.

This can be done by using either the [disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/disabled) or [readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/readonly) attribute.

Each of these attributes behaves slightly differently and can only be used on specific HTML elements so it's important to consider how each one works.

This helps you to make an informed decision for which one to use in your project.

### The properties of the disabled attribute:

- The component will NOT be focusable. This means that trying to select the component or tab to it using your keyboard won't work.
- The component value CANNOT be changed by the user. If used on an input box for example, a user won't be able to enter text into that field or modify existing field text.
- The component CANNOT be submitted via form submission. This means that the data in the field won't be submitted along with the other form detail.
- The component will display in the browser as greyed out (unless additional styling is added).

### The properties of the readonly attribute:

- The component WILL be focusable. This means that you will be able to select the component or tab to it using your keyboard.
- The component value CANNOT be changed by the user. If used on an input box for example, a user won't be able to enter text into that field or modify existing field text.
- The component CAN BE submitted in a form. This means that the data in the field will be submitted along with the other form detail.
- Unless additional styling is added, the component will not display any differently to an editable field.

---

## When To Use Disabled Components

Now that we've looked at the difference between the disabled and readonly attributes, let's talk about when to actually use disabled components.

Ultimately, from the research I've done into this design pattern, I can say that there are a lot more reasons *not to* use disabled components than there are to use them. 

However, we'll talk about that in more detail in the rest of this article.

For now, the best scenario for using disabled attributes is during form submission. It's a good idea to disable all of the fields in a form (including the submit button) when a user submits the form. 

This prevents the user from updating any information while the submission process is happening. It also prevents the user from clicking the submit button which might try to submit the form multiple times. 

Trust me, I've seen this happen a lot so it's worth factoring into your project both from a design and a coding perspective.

That's essentially it as far as using disabled components is concerned. 

Sure, there are a few other scenarios that could benefit from this design pattern, but there are nearly always alternative and more user-friendly ways to implement something and these would be the preferred methods.

With that said, if it's absolutely essential to incorporate disabled elements into your design I did manage to collect some helpful styling information that I'd like to share with you in the next section.

---

## Styling Disabled Components

When it comes to styling a disabled component there are some helpful guidelines I've put together below. These should help you to create disabled components that are clear and easy to understand.

1. **If an option is disabled, like a submit button or a form field, it's important to state why it's disabled.**
   - For instance, if you can't book a dental appointment because there are no free slots on that date. Simply tell the user "There are no appointment slots available for the date selected".
   - By telling the user the reason for the disabled option, they will understand why they can't interact with it and change their selection accordingly. This doesn't add to the user's cognitive load and they can easily continue with their task.
   - By allowing the user to step back if they've made a mistake, you're allowing for a smoother experience.


2. **Don't use grey for disabled buttons (unless it's part of your color palette).**
   - By using grey for disabled buttons, the user may still think they are selectable. When they press it and nothing happens, they become frustrated because they expect it to work.
   - Instead, reduce the opacity of a button to denote that it is disabled.
   - This will create a visual difference in the buttons to the user and will help them to understand when a button is disabled.
   - A good rule of thumb is to reduce the opacity to below 40% (depending on the background).


3. **Group disabled buttons next to enabled buttons where possible.** 
   - This works in line with the previous guideline.
   - This will help to build the user's mental model of how the buttons work. 


4. **Don't change the font size or font weight of disabled buttons**
   - While you want disabled and enabled buttons to look visually different, changing the font size or weight creates too much of a difference.
   - Stick to the rule of reducing the opacity of disabled buttons and this should create enough of a visual difference.

---

## When To Avoid Using Disabled Components

Now that we've talked about when to use disabled components and how they should be styled, it's time to move on to scenarios when you should avoid disabled components.

### 1 Avoid using a disabled or readonly component in the initial state of a workflow

**Example Scenario:**

- Imagine you have a form that contains a user's information.
- You don't want to allow the user to change their email address
- However, they do need to see the email address to ensure it's correct

**Potential Solution:**

- One solution might be to display the email address inside of a disabled input box.

**Usability Concerns:**

- What if the email address is incorrect? 
- If the email address is displayed as an input box, the user will assume it is editable. 
- If the input box is disabled, this will frustrate the user when they can't edit this field.

**The Solution:**

- The solution to this scenario is to show the email address as regular text, without any sort of input box or styling.
- Additionally, it's helpful to provide a help message outlining how to proceed if the email address is incorrect.

### 2 Don't Disable The Submit Button

**Example Scenario:**

- Imagine you have another form that a user fills in.
- You might want to prevent the user from submitting the form before all of the required fields are filled in.

**Potential Solution:**

- A common solution to this is to disable the submit button until the user has filled out all the required fields.

**Usability Concerns:**

- This doesn't provide any clear feedback to the user, only that they can't submit the form. 
- They do not know how to enable the button and this adds to the cognitive load of the user.

**The Solution:**

- Keep the button enabled so the user can press it.
- When they submit the form before all of the required fields are filled in, they will be shown the relevant errors on the form.

**Additional Notes:**

- The only time a disabled button should be used is if there's no other way to proceed on a single form field.

- In relation to the submit button, avoid using the generic term Submit on the button. 
  - Use a term that more appropriately describes the action being performed.

---

## Disadvantages Of Using Disabled Components

Based on what I've talked about so far, we can summarize the disadvantages of using disabled components:

- **Disabled buttons increase the user's cognitive load and can prevent them from completing a task.**
  - Discovering the component is disabled and thinking about how to enable it adds to a user's work load. The more actions required to complete a task multiplies the cognitive load.
  - A UI shouldn't need a disabled component unless it can easily be enabled on the same screen. 
  
- **Not all users understand the conventions of a disabled button or component.**
  - Some users that aren't familiar with this mental model will have a hard time understanding it if they're seeing it for the first time.
  - As a result, they will click a button and won't know why it isn't working. This will cause them frustration.

- **Keep in mind users who use screen-reader technology**
  - These users won't be able to see disabled elements so won't even know they exist on the screen.
  - Also, consider the order the components appear as screen-readers will work in a linear fashion.
  
---

## Conclusion

I hope this article has helped you to understand the advantages and disadvantages of using disabled components in your designs. 

Hopefully you'll be able to apply what you've learned here to create a clear and user-friendly design for your own projects.