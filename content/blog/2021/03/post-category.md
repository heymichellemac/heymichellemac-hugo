---
categories:
- blog
date: '2021-03-24'
tag:
- Coding
title: How To Remove A Post Category From The Blog Page In WordPress
---

If you have many different post categories on your WordPress website, you might want to funnel them to different pages. This is especially important to consider if you have included each of your post categories in your navigation menu.

An overly-cluttered navigation structure can immediately turn users off from your website and can cause them to leave.

On my website, for instance, you'll see that I have an Articles section and a Book Notes section. 

The Articles section contains all of my "article" posts, whereas the Book Notes section only contains my "book notes" posts.

These are both types of posts but I've separated them to help readers find what they're looking for.

In this article, I want to walk you through the process of removing a specific post category from the blog page on a WordPress website.


## Determine The Category You Want To Remove

The first thing you'll need to do is find the ID value of the post category you want to exclude from the blog page. 

This is called the **category ID**.

To do this, go to **Posts > Categories** and open the category you're looking for.

From here, look at the URL for the page and you'll see a section like this:

```
category&tag_ID=10
```

This number value (in this case 10) is the category ID you need for the next step.

---

## Functions.php

To exclude a specific category from the blog page you need to paste a code snippet into the functions.php file. 

This file can be found inside of your active theme's directory.

```
function exclude_category_home( $query ) {
    if ( $query->is_home ) {
        $query->set( 'cat', '-20' );
    }
    return $query;
}
 
add_filter( 'pre_get_posts', 'exclude_category_home' );
```

All you need to do now is replace the number with the category ID you got from the previous step. 

Be sure to keep the minus (-) in there otherwise it won't work.

Once you have made the update, you should now see that specific post category no longer appears on the blog posts page on your site.

If it doesn't, I recommend clearing your browser's cache and/or opening a new incognito tab to make sure it's working as expected.

---

## For Child Themes

If you're like me and you're working with a child theme, you'll need to be sure you add this code to the correct functions.php file.

If you add the code to the parent theme, the next time that theme updates you'll lose all your lovely changes and you'll have to add them again.

This is the main benefit of utilizing a child theme as all of your customizations will stay the same any time your parent theme updates.

This honestly happened to me about 3 times before I corrected it properly as I initially added the file to the parent theme in my laziness.

To resolve this, you need to create a functions.php file in your child theme's directory if it's not there already and add the code snippet to that file.

Note here: if you followed the steps outlined in [this detailed post on WPBeginner.com](https://www.wpbeginner.com/wp-themes/how-to-create-a-WordPress-child-theme-video/) then you probably wouldn't have run into this issue because you already created the functions.php file. 

In which case, I congratulate you for being much more diligent than me!

---

## Conclusion

I hope you found some value in reading this article. 

I'm sure you'll agree that WordPress is a very powerful CMS and there certainly is a lot you can do with it.

If you liked this article and found it helpful, please consider sharing it on social media. That will help others to find it which I would really appreciate.