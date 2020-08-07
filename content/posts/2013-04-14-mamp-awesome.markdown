---
author: jimmy.smutek
date: 2013-04-14 15:43:26+00:00
draft: false
title: Local WordPress with MAMP!
type: post
url: /mamp-awesome/
categories:
- Web Design
---

I no longer use MAMP, I suggest checking out something like [VVV](/setting-up-vvv-for-wordpress-development/), or
 [Trellis](/migrating-to-trellis-1/).



This quick post will explain how to quickly and easily get a local development environment up and running on your Mac, using a free tool called MAMP. With MAMP, you’ll be able to work on WordPress, or Drupal, or Joomla (hark!), or any similar software from the comfort of your own computer, no web host needed.



### What's this WordPress with MAMP stuff all about, anyway?





This is the one and only post that I decided to leave from my old site. :)



I’m on a Mac but, if you’re running a different operating system don’t fret, there’s equivalents to MAMP for your operating system as well.

If you’re running Windows check out [WAMP](http://www.wampserver.com/en/) or [XAMP](http://www.apachefriends.org/en/xampp.html), and if you’re on a Linux box... well, I doubt that you need me to tell you anything. Some of the specifics may vary between MAMP, WAMP & XAMP, but the concepts are the same. I’ll be focusing solely on MAMP for this post.

Okay, first, what is MAMP? MAMP stands for Mac, Apache, Mysql, PHP. The short of it is that MAMP is an application that will allow you to easily set up and run a web server on your Mac. For the long of it have a look at [this Wiki](http://en.wikipedia.org/wiki/MAMP).



* * *





### tl;dr - The Video Version

{{<vimeo 64028966>}}

[Here's the "too long; didn't read" video version](https://vimeo.com/64028966). Actually, the video is kind of long too. It seems that I just can't help being long winded at times. If there's something in the video that doesn't make sense just refer to the text below or drop me a comment or an email and I'll do my best to sort you out. Really, this is a pretty simple process. Once you've done it once, it's a snap.



* * *





### Part 1 - Download & Install MAMP


In order to get up and running we’re going to need to download and install MAMP. Head on over to [mamp.info](http://www.mamp.info/en/index.html) and click the big ‘ole download now button. This will download a .zip file, containing the MAMP installer, to your computer.

[![1_goGetMAMP-770x700](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215272/1_goGetMAMP-770x700_qmdzif.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215272/1_goGetMAMP-770x700_qmdzif.jpg)

Once the zip file has finished downloading, find it and double click it to unzip. You’ll end up with an install package on your desktop. Double click the install package to run the installer.

[![2_installMAMP_1-425x300](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215272/2_installMAMP_1-425x300_b4cy1s.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215272/2_installMAMP_1-425x300_b4cy1s.jpg)

[![2_installMAMP_2-425x300](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215271/2_installMAMP_2-425x300_h4azsj.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215271/2_installMAMP_2-425x300_h4azsj.jpg)

[![2_installMAMP_3-425x300](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215270/2_installMAMP_3-425x300_rmczqz.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215270/2_installMAMP_3-425x300_rmczqz.jpg)

[![2_installMAMP_5-425x301](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215268/2_installMAMP_5-425x301_bbji9g.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215268/2_installMAMP_5-425x301_bbji9g.jpg)

Installation is standard fare. You’ll go through a series of steps similar to what's shown above. When the actual install begins, the MAMP installer will ask you to authenticate with your admin user name and password. Go ahead and do that. Once the install has completed, MAMP and MAMP Pro will be installed in your applications directory.



* * *





#### A quick note on MAMP Pro


MAMP Pro offers a lot of cool advanced features and by default is installed along with MAMP. MAMP Pro is not free, but it wont cost you any money unless you decide to use it. For this post we will be using the free version of MAMP because.... it’s free, and it gets the job done. So, with that said, go ahead and navigate to applications/MAMP and double click on the MAMP app to launch it.



* * *





### Part 2 - Launching MAMP!


Once you launch MAMP two things are going to happen. First, the MAMP control panel is going to launch. It looks like this -

[![3_MAMP_cp_1](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215269/3_MAMP_cp_1_qbm4an.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215269/3_MAMP_cp_1_qbm4an.jpg)

[![3_mamp_cp_2](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215270/3_mamp_cp_2_flkcca.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215270/3_mamp_cp_2_flkcca.jpg)

On launch MAMP will boot the Apache server and the MySQL server and the status lights on the MAMP control panel should turn from red, as shown at left above, to green, as shown at right above. Once the servers are booted MAMP will open the MAMP start page in your default browser. I’m using Chrome, here’s what my start page looks like -

[![4_mamp_startpage-694x700](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215268/4_mamp_startpage-694x700_kwx3rd.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215268/4_mamp_startpage-694x700_kwx3rd.jpg)

Notice the URL! localhost!! YES!!! This means we’re up and running with our local server! Okay..... now, the only thing left to do is to go ahead and install WordPress.



* * *





### Part 3- Go Grab WordPress!


Let’s go ahead and jump over to [wordpress.org/download](http://wordpress.org/download/) to download and install WordPress.

[![5_getWordPress-892x700](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215267/5_getWordPress-892x700_c6nshj.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215267/5_getWordPress-892x700_c6nshj.jpg)

Go ahead and download the latest version of WordPress. As of this writing the latest version is 3.5.1 Double click to open the zip file, and you’ll end up with a folder called Wordpress. Drag this folder to wherever you would like your local WordPress site to live. I like to keep mine in my Sites folder, at user/sites. You can change the name of the folder from “wordpress” to whatever you’d like your site to be called. I’m going to go ahead and leave mine as is.

[![6_place_WordPress-687x700](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215267/6_place_WordPress-687x700_erf7bb.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215267/6_place_WordPress-687x700_erf7bb.jpg)



* * *





### Part 4- Setting up the Database


Next, and probably the most complex part of this entire endeavor, we’re going to need to set up a MySQL database for our Wordpress install. No worries though, it’s super simple. On the MAMP start page go ahead and click the top nav button titled “phpMyAdmin”.

[![7_makedb_1-425x286](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215266/7_makedb_1-425x286_j7tqhk.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215266/7_makedb_1-425x286_j7tqhk.jpg)

[![7_makedb_2-425x295](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215266/7_makedb_2-425x295_fdao4p.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215266/7_makedb_2-425x295_fdao4p.jpg)

Once in phpMyAdmin look for the input box that says “create new database”, as shown above, right. Enter the name of your database here. Don’t use any spaces in the name. I usually keep the database name relatively simple, lowercase and, when possible, one word. Choose a database name that reflects the name of your project. For example - “myproject” or “my_project” are both fine. For this post I’ve named my new database “awesome”. Once you’ve entered the name of your database click the create button. There’s no need to fiddle with any other settings.

Now that our database is set up we need to point MAMP at our WordPress site. Hop over to the MAMP control panel and click the preferences button. Click the Apache Tab, then using the select button, navigate to and choose the folder where your local WordPress site lives. Click open, then click okay.

[![8_Mamp_prefs_1](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215264/8_Mamp_prefs_1_q6qpik.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215264/8_Mamp_prefs_1_q6qpik.jpg)

[![8_mamp_prefs_2](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215115/8_mamp_prefs_2_nind3p.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215115/8_mamp_prefs_2_nind3p.jpg)

[![8_mamp_prefs_3-425x265](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215115/8_mamp_prefs_3-425x265_uyayeg.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215115/8_mamp_prefs_3-425x265_uyayeg.jpg)

[![8_mamp_prefs_4](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215114/8_mamp_prefs_4_zmanot.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215114/8_mamp_prefs_4_zmanot.jpg)

Since we’ve changed the Apache settings the servers will reboot. Once the lights return to green on your MAMP control panel go ahead and open a new tab or window in your browser and enter the URL “localhost:8888” - and.... BAM!!! We can install WordPress!



* * *





### Part 4 - Install & Configure WordPress!!!



[![9_install_wordpress_1-914x574](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215113/9_install_wordpress_1-914x574_lqqugp.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215113/9_install_wordpress_1-914x574_lqqugp.jpg)

Click the button to create a configuration file, then, on the next screen, click the “let’s go” button!

[![9_install_wordpress_2-914x619](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215112/9_install_wordpress_2-914x619_c2wwpu.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215112/9_install_wordpress_2-914x619_c2wwpu.jpg)

Now we will need to tell WordPress how to connect to our database. For “Database Name” enter the name of the database you created in phpMyAdmin - my database was named “awesome” so that’s what I’m going to enter.

_**Note**_ that the next two fields, “User Name” and “Password” are referring to your MySQL database, not to your WordPress install. Don’t confuse this with your WordPress login, right now all we are doing is telling WordPress how to access the database we’ve set up for it. By default the MySQL settings in MAMP are “root” for both the user name and password, so go ahead and fill those in as shown below.

[![9_install_wordpress_3-914x693](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215113/9_install_wordpress_3-914x693_s7omtc.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215113/9_install_wordpress_3-914x693_s7omtc.jpg)

Database Host and Table Prefix are fine as is, so go on and click the submit button. Go on, you know you want to! Once you get to the next screen click to run the installer and...

**BOOM!!!** Fill out the site info that you’ll want to work with. One word of advice, _never, never, **never, ever, never,**_ use the username admin. **Just don’t do it.** "admin" is so commonly used that it’s become a security vulnerability. I could blather on about it but I’ve already written waaayyy more than I had planned to, but - if you’d like to know more, just google “wordpress, don’t use admin”, or take a quick gander at point number two of this article in _[.net magazine](http://www.netmagazine.com/features/20-common-wordpress-mistakes-myths-and-misgivings)_. At any rate, here’s what my setup for this site looks like -

[![9_install_wordpress_4-667x700](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215111/9_install_wordpress_4-667x700_txckl9.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215111/9_install_wordpress_4-667x700_txckl9.jpg)

For my password I’ve just used “password”, mainly for ease of use. This is fine on a local site but make sure to use a secure password on any site that is deployed on the web! Go ahead and click the “install Wordpress” button -

Next you’ll be prompted to log in.

[![10_login-914x583](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215111/10_login-914x583_udbdf0.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215111/10_login-914x583_udbdf0.jpg)

Go ahead and log in with the username and password that you set up for your WordPress site. And, the next thing you know....

[![11_and_done-811x700](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215110/11_and_done-811x700_a9jz9i.jpg)
](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448215110/11_and_done-811x700_a9jz9i.jpg)



* * *





### Victory!


You now have a local, fully functioning WordPress site installed.

That about does it. Go forth, go crazy, break things & learn. I hope this post has been useful!
