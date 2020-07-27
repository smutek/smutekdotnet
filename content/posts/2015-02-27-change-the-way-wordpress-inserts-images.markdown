---
author: jimmy.smutek
date: 2015-02-27 23:40:00+00:00
draft: false
title: Change the way WordPress inserts images
type: post
url: /change-the-way-wordpress-inserts-images/
categories:
- WordPress
post_format:
- Video
tags:
- post editor
- quick-tips
---

## What's the deal here?





Part of a series of posts from my days of self employment.



This week I want to do a quick tip to show you how to change the way that WordPress inserts images. What I mean by this is that, by default, every time you insert an image into one of your WordPress posts, WordPress will default to linking to the image.

[caption id="attachment_786" align="alignnone" width="600"]![Image of the default insert media settings.](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214861/ScreenShot-MediaFile_wqgs3x.jpg)
This is the default setting.[/caption]

This is fine if this is the way you like your WordPress site to run. If you don't, and if you're like me, then you will find yourself changing this setting to none every time you insert an image into one of your posts.

[caption id="attachment_790" align="alignnone" width="600"]![Image of the insert media settings set to none.](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214861/ScreenShot-NoLink_olhcq3.jpg)
This is what I want, by default, every time.[/caption]

Also, if you are like me then you probably have been driving yourself crazy because you forget to change this setting. The result, for me, is that every time I insert an image I have to delete it, reset the option, and reinsert the image. Every. Single. Time. Almost...

This drives me a bit crazy. 

I don't usually link to my image files. It's like my mind is already on to the next task and I'm constantly forgetting to change this. Every single time. Almost. 

Okay, maybe you don't forget, but you'd just like to change this setting. If so, check out the short video, or read on.



## Just Change The Settings...

 

I looked around and there's no obvious way to change this in the WordPress settings. Well, luckily there is a super secret settings screen that we can access to change this functionality. It's not exactly super secret, but for some reason this setting is not publicly accessible to the user. Shout out to [Aizat Faiz](http://blog.aizatto.com/2010/05/04/changing-default-wordpress-media-link-url/) for the tip!

Just log in to your WP Admin screen and point your browser at this url - 


    
    http://example.com/wp-admin/options.php



Replace the "example.com" part with your site address. Once you are there, you'll see this screen.

![Image of the hidden settings page.](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214860/ScreenShot-SettingsPage_cvigfh.jpg)


Scroll down until you see the section labeled "image_default_type_link"

The settings here set the default for what's shown when you insert media into one of your posts.

This field has a few options, with the default being "file".



  * file - links directly to the attached file 
  * post - links to the media post for the attached file
  * none - nothing, does not add an HTML link. What I want


Just delete the word file, and type in the word none, just like this.

[caption id="attachment_795" align="alignnone" width="927"]![Image of image link type changed to none](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214860/ScreenShot-ChangedSettings_ruayeq.jpg)
Just type in none, as shown[/caption] 

Scroll down to the bottom of the page, click "save settings", and that's it.



Important - make sure that you **do not change any of the other settings** on this page.





To change this back to the default just return to this page and change "none" to "file".



If you are curious as to what these options do, take a look at [this entry](http://codex.wordpress.org/Option_Reference) on the [WordPress Codex](http://codex.wordpress.org).  

That's it for this weeks quick tip. This simple change makes my life much easier. I hope it helps you as well. 

If you have any WordPress stuff that makes you crazy, let me know in the comments or drop me a line through my contact form. 
