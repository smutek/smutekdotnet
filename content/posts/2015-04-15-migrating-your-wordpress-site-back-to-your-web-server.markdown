---
author: jimmy.smutek
date: 2015-04-15 13:46:47+00:00
draft: false
title: Migrating Your WordPress Site Back To Your Web Server
type: post
url: /migrating-your-wordpress-site-back-to-your-web-server/
categories:
- WordPress
post_format:
- Video
tags:
- Local Server
- Migration
- plugins
---

In my last post I covered [how to get a copy of your WordPress site running on your computer](https://smutek.net/running-your-wordpress-site-from-your-computer/), in this post I will cover migrating your WordPress site back to your web server.

<!-- more -->



## Overview



There's 2 ways to go about this, the easy way and the really easy way. The easy way will show how to move your site back using the same free tools that we used to set up our local site. You'll need FTP access to your web server and access to phpMyadmin for this method. 

The really easy way uses the premium version of DB Migrate. Aside from a copy of DB Migrate Pro, you'll just need FTP access to your site. Aside from that, the really easy way is as easy as clicking a button.  Let's go ahead and get started. 



## The Easy Way



Here's a screen shot of my remote site, out on the internet, that I've cloned and set up to run on my computer... 

![Image of a WordPress site running on a remote server](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214826/live-site_rrbmke.jpg)


...and here's a shot of my redesigned, modified, local, running on my computer site that I'm going to clone back to the web...

![local-site-to-migrate](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214825/local-site-to-migrate_xiswws.jpg)


I'm going to point out that this site is strictly for example. Obviously the minor changes I've made here don't require setting up a cloned site, but the assumption is that you'll have made some pretty major changes to your site. 



### Getting Started


If you haven't checked out my last post, How To Get WordPress running on your computer, I would suggest doing that now. Basically what we are doing here is everything we did in the last post, in reverse. I don't mean the steps are in reverse, rather the data will be flowing in reverse, from our local site back up to our live site. 



### Copy Paths from Live Site & Export Local Database



The first thing we need to do is to export a copy of our local database. We're going to use DB Migrate to do this. If you followed along with my last post you should have DB Migrate installed on both the local site and the live site.

The first thing we need to do is to copy the settings from DB Migrate on our live site, and paste them in to our local site. Here's a screen shot of the settings that I need to grab on my live site - 

![Migrate DB Settings on Live Site](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214825/migrate-db-settings-1_r2zdy4.jpg)


I'm going to copy the contents of both find fields from my live site, then I'm going to switch over to my local site and paste these settings into the replace fields on my local site. Here's an image of DB Migrate on my local site, once I've pasted the settings. 

![Image of Migrate DB settings copied to the local install](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214824/migrate-settings-copied-to-local_c7wqyx.jpg)


What we are doing here is telling DB Migrate on our local site to make a copy of the new, modified, local database - but to make this copy using the file paths from the remote site. Once you've pasted the info from the live site as shown above, click migrate. DB Migrate will now export a copy of the modified local database to your downloads folder. This is the database with all our changes, we'll be using it to replace the database in our live site. 



**Important:** Make A Copy of your live database before continuing!



I cannot stress enough, _before you do anything else make a copy of your remote database_. Making a copy of your live database ensures that if something does go wrong you can quickly roll back and recover your site. If something goes wrong and you do not have a backup copy of your live database your site may not be recoverable.

**Make a copy of your live database!**



### Live Database Backup


To make a backup of your live database log in to your web hosting control panel and go to phpMyadmin. If you're not sure how to access phpMyAdmin get in touch with your web host. 

Once you're logged in to phpMyAdmin, select your database in the column on the left. 

![Image of phpMyAdmin screen](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214824/php-my-admin-1_lc6xk0.jpg)


With your database selected, choose "Export" from the top menu, and click the custom button, under "export method". Make sure all tables are selected, in the Tables section. They should be selected by default, but make sure just incase. They will be highlighted in grey, as shown in the screenshot below.  Click "Save Output to a file" if it is not already selected...

![php-my-admin-export](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214823/php-my-admin-export_nlrvf5.jpg)


Leave all of the other settings as they are, then scroll to the bottom of the page and click "Go". A copy of your live database will download to your computer. Make sure it does, then put it somewhere where you'll be able to find it if you need it. I like to put it in its own folder, called Backup DB.

![Image of live database downloaded and secured](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214823/live-db-backed-up_ojlm8f.jpg)
 



### Install Plugins, and Themes


The next step is pretty straight forward. We just need to make sure that any themes, plugins, and media files from our modified local site are also installed on our live site. 

In my case, I am using the Rams theme by Anders Noren on my local site. I've also set up a new contact form, using Gravity Forms. I'll need to make sure that the Rams theme and Gravity Forms are both installed on my live website before proceeding. You'll want to do the same with any new plugins and themes that you might have installed. 



### Upload Media Files



I've also added some new images to my site, so I'll need to make sure that these are uploaded as well. This is where FTP comes into play. If you haven't added new images or media to your site you can skip this step.

When I refer to media I mean anything that you've uploaded to your site using the WordPress media uploader. By default, WordPress keeps all the media that you add to your site in a folder called uploads, which lives in another folder called wp-content. Inside of the uploads folder media files are organized in subfolders by year, which in turn hold folders that are organized by month. 

If that sounds complicated, don't worry, it's not. As an example, media files that I've uploaded in April are stored in a folder titled "04", which is sorted in a folder called "2015", which is stored in a folder called "uploads". Here's a screen shot of the 2015 folder on my live site. 

![Image of WordPress uploads folder structure](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214822/wp-uploads-folder_hfjhdu.jpg)


Figuring out which files to upload is easy. I've done all of my work in March of 2015 so the media files I need to upload will be in the folder at wp-content/uploads/2015/03



### Swap Databases



Now, with our theme, plugins, and media files uploaded to our live site, we are ready to swap out the databases. Working with your sites database can be scary, and it's good to be cautious here since your database is arguably the single most important part of your WordPress website. It contains all your posts, pages, text content, and settings. **This is why we made a backup of our live database before moving forward**. 

The first thing we'll want to do is to go back to phpMyAdmin on the live site. Make sure your live database is still selected in the column to the left, and click the import button on the top row.

![Import button in phpMyAdmin](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214822/php-my-admin-import-button_flba0d.jpg)


Once you've done this you'll see the import screen. Leave all of the settings as is and click the choose file button.

![phpMyAdmin import screen](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214821/php-my-admin-import-screen_qwzxpu.jpg)


Browse to, and select the database file that you exported from your local site with DB Migrate.



Make sure you are importing the database file that you exported from DB Migrate, not your backup database.


 
![Importing the database](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214820/importing-db_x7h5ax.jpg)


Once you've selected your database, click Go. Once the database has imported you should see a screen that looks like this -

![Import database success screen](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214820/importing-db-success_u32cys.jpg)


Once you've imported the database switch back to your live WordPress site and navigate to settings/permalinks and click save. Most likely you will have to log back in. 

After saving the permalinks visit the font page of your site and, if all went well, you should see your modified site running on your live server!

![Image of live site after successful migration](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214819/site-migrated_huscoi.jpg)




### Finished!


That's it, you've successfully moved your WordPress site from your computer back to your live server. Congratulations!



## In case of disaster...


If something goes wrong, don't panic. This is why we made the backup of our database. Getting your site back up and running is as simple as going back to phpMyAdmin on your live site, dropping the tables you just imported, and then import you backup database. Once you've done this your site will be back to normal. 

Jump to the 9 minute mark of my video for a walkthrough on what to do if you mess up. 



## The Really Really Easy Way



I completely understand that everything above may seem complicated and if you've read this far you are truly my hero and I think you're awesome. :) 

I want to point out that I intentionally try to be as wordy as possible because I want to make sure that anyone reading has a solid understanding of the process before trying it themselves. Once you understand the process it really is quite easy. I'm able to move a site in about 5 minutes. In my work I clone sites back and forth dozens of times every week. 

With that said, if this moving databases business is not for you then you may want to check out DB Migrate Pro. Migrating your WordPress site back to your web server could not be easier than it is with this plugin.
 


### Enter DB Migrate Pro



![Delicious Brains home page](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214819/delicious-brains-website_af9lzo.jpg)


I'll be honest with you, DB Migrate Pro is what I use. I can tell you that as a professional working in the self hosted WordPress space, DB Migrate Pro has saved me more time, more money, and more frustration than any other plugin I've ever used. Hands down. If you are migrating a lot of databases in your day to day work then this is definitely the way to go. Or, if you have one site that you want to make a local copy of, and you just don't want to deal with phpMyAdmin and importing databases, then this is the plugin for you. 

A developers license is $199, and a personal license is $90. If you click the link at the bottom of this post you can get 20% off of your purchase.

Moving your site with Db Migrate Pro is as easy as clicking a button. Seriously. You'll still have to make sure your themes and plugins are installed, and that your media files are uploaded (unless you have a developers license, in which case you can use the media files add on), but there's no fiddling about with phpMyAdmin and databases. 

Once you've made sure that your themes, plugins, and media files have been uploaded, you just copy a special URL from your live site, paste it into the DB Migrate Pro settings page on your local site, and click migrate.

I cover moving a site with Db Migrate Pro in my video starting at around the 16 minute mark. If you're interested in grabbing a copy of DB Migrate Pro, use the banner below to get 20% off of your purchase. The coupon will be applied automatically and you'll see the discount at checkout once you've added a product to your cart. 

[Click Here for 20% Off DB Migrate Pro](http://t.deliciousbrains.com/aff_c?offer_id=2&aff_id=1272&file_id=20&coupon=SUPER20)

I hope this post has been helpful. If you have any questions feel free to leave me a comment or send me an email. Thanks for reading!
