---
author: jimmy.smutek
date: 2015-03-13 19:33:20+00:00
draft: false
title: Running Your WordPress Site From Your Computer
type: post
url: /running-your-wordpress-site-from-your-computer/
categories:
- WordPress
post_format:
- Video
tags:
- Local Server
- plugins
- Tips
---

## Put your full site backups to good use.





Part of a series of posts from my days of self employment.



In last weeks post I covered [how to set up a WordPress backup plugin](https://smutek.net/how-to-set-up-a-wordpress-backup-plugin/) and how to have your backups sync to your Dropbox account. This week I'm going to cover how to take one of those full site backups and get a copy of your WordPress website running on your computer.



## Why would I want to do something like this?



You might be wondering, why on earth would I want to do something like this. Well, one benefit is that running your WordPress site from your computer gives you a perfect laboratory to experiment with. You can test new themes, test new plugins, and do anything else that you might not want to do with your live site. 



## Okay, but is running WordPress from your computer hard?



This is actually a really easy thing to get set up. The process is broken down into the following steps: 




  1. Get a web server running on our computer.
  2. Install WordPress on our computer. 
  3. Make sure our database prefixes match.
  4. Get a copy of our WP Content folder.
  5. Export the database from our live site.
  6. Import the database into our testing site.
  7. Replace WP Content in our testing site with the WP Content from our live site.


Some of that stuff, like the server and database stuff, might sound kind of complex (and it is) but you don't need to be any sort of expert to get this going. We'll be using one free piece of software, and 2 free plugins to do all the heavy lifting. Let's get started!



## Terminology



There's not really any fancy technical stuff in the article, but for the sake of clarity I want to cover two terms. When I write "remote" or "live", I'm referring to your real website that's living out there on the internet somewhere. When I write "local" I am referring to the website that is running on your computer.   



## Step 1, the web server.



The first thing that we have to do is install a web server. For this we will be using free software called Desktop Server, from a company called ServerPress. Desktop Server runs on Mac & Windows and comes in 2 flavors, free and premium. I own the premium version but everything I'm going to show in this blog post can be done with the free version. 

![Server Press Product Page](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214851/serverpess-products-page_sqzw8m.jpg)


To download Desktop Server [follow this link](http://serverpress.com/downloads/) and select the installer for your operating system. 

There's 2 download links for each installer. If your download is going really slow just cancel the download and try the other download link. When writing this post I found that download site 1 was running at a snails pace, but download site 2 was pretty fast. 



### Installation



Once the application has finished downloading go ahead and install it. I'm not going to cover installation, but it is pretty straight forward, just follow the prompts. The people at Server Press have [written a walkthrough here](http://serverpress.com/support/installing-desktopserver/) that you can check out if you'd like. 

Once the software has installed go ahead and launch the app.



## Step 2, configure the server, install WordPress



![Desktop Server launch page](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214850/desktop-server-launch-page_twyt8u.jpg)


When you first launch Desktop Server you'll see a screen like this. Leave "Yes" selected and click "Next". The app is going to quit and restart with administrative privileges. 

![OS Dialog asking for admin priivleges](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214850/os-asking-for-admin_dzlq5z.jpg)


If you are on a Mac you'll probably see this window. Desktop Server is asking, hey, is it okay if I run as an admin? You'll need to enter your admin password to continue. 

![Desktop Server starting web services](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214849/desktop-server-start-services_ziydpo.jpg)


Next you'll see a window that looks like this. Desktop Server is asking if you'd like it to go ahead and start the web services. We do.  Leave "Yes" selected and click next.

![Desktop Server incoming connections dialog](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214849/desktop-server-incoming-connections_gksuzh.jpg)


Again, if you are on a Mac, and if you have your firewall running (which you should) you may see this screen. If you are on a trusted network, such as your password protected home network (your home network is password protected, right?) go ahead and click allow. If you are on an insecure network, like the wifi at the local coffee shop, click deny. Desktop Server will work either way. 

![Web services started on Desktop Server](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214848/desktop-server-services-running_a0tzsp.jpg)


Now you'll see this screen. You've got a web server running on your computer, yay! Go ahead and click "Next".

![Desktop Server Create a new site](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214847/desktop-server-create-new-site_cowzhz.jpg)


Next you'll see this scree, with some options. The options on your screen may look different if you are using the free version. If so, that's okay. We just need to select the "Create a new development website" option, and click "Next".



### Configuration Stuff



![Desktop Server site options ](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214847/desktop-server-site-options_lhhymd.jpg)


This page contains 3 options. Desktop Server is going to do all the fancy database configuration stuff for you so that you can install WordPress.  



#### Site Name


Enter the name of your site here. This is the address you'll use to navigate to your local (on your computer) site in your web  browser. If your live (on the internet) site is named photoninja.com it's probably a good idea to enter www.photoninja here. Keep the www. part, leave off the .com - Desktop Server will handle the rest. 



#### Blueprint

 
Leave this at whatever the default is. For the curious; the blueprint is the WordPress configuration that Desktop Server is going to install. 



#### Site Root


This is the location on your computer where Desktop Server is going to put all the files that make up your local website. Unless you have a reason to change this, it's fine to leave it set to the default.

Make note of this location, we'll need it later. Mine is in documents/websites

Go ahead and click create.

![Desktop Server, site set up done.](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214846/desktop-server-done_hdibzm.jpg)


Once desktop server does its thing you'll see this screen. Click Next. 

![Desktop Server configuration complete](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214844/desktop-server-local-url_nux5p9.jpg)


Next you'll see this screen, it should show the local URL of your site. Go ahead and click the URL, your browser will open the WordPress install page. 



### Install WordPress



![Install WordPress, language screen](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214844/install-WordPress-language_lsasby.jpg)


Next you'll see this screen, select your native tongue and click continue. 

![Install WordPress site options](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214843/install-WordPress-options_shhkws.jpg)


Go ahead and enter the requested information. You can use the same info from your live site if you'd like. It really doesn't matter what you enter here because all this information is going to be overwritten when we import the database from the live site. 

Once you've filled this out, click install WordPress. 

![Install WordPress success screen](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214842/install-WordPress-success_ueo38z.jpg)




<blockquote>WordPress has been installed. Were you expecting more steps? Sorry to disappoint.</blockquote>



WordPress is now installed and running on your computer, click the login button and you'll see the familiar WordPress login screen.  Go ahead and log in to your site and take a look around.



If you have any update notifications, go ahead and run all updates now.





## Step 3 Check Database Prefixes



Before we go any further we need to make sure that the database table prefix on our local site matches what is already on our live site.

If you are wondering what a database prefix is, don't worry. We can handle this with a plugin. If you are curious, the database prefix is a string of characters prepended to the name of a database. It lets your server know which database tables to use for your installation of WordPress.

Most WordPress installs will use wp_ by default. Some hosts change this database prefix as a security precaution. I'm not going to get into that here, but if you want to learn more about why you should change your database prefix, [check out this article by Jeff Starr](http://digwp.com/2010/10/change-database-prefix/).



### Check prefix on your live site



![Change DB Prefix plugin install page](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214840/change-db-prefix-plugin_k9gwtm.jpg)


To check your database table prefix go ahead and log in to your live site and go to your install new plugins page. Search for "Change DB Prefix". Install the Change DB Prefix plugin and activate it. 

![Change DB Prefix plugin, prefix is different](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214840/change-db-prefix-prefix-different_ijzms9.jpg)


Once you've done this go to settings/Change DB Prefix. If the value in the Existing Prefix field is wp_ then you are done and can uninstall the plugin and move to the next step. If your prefix is something else, like the image above, read on. 



### Change prefix on local site.



My live prefix is d4x2_ so I need the prefix on my local site to be the same. Fortunately this change is super easy. Install and activate the Change DB Prefix plugin on your local site.

Once the plugin is installed and activated, go to the plugin settings page (settings/Change DB Prefix). 

Switch back over to your live site (I like to keep two browser tabs open for this, one with my live site, and one with my local site). Copy the existing prefix from your live site, and switch back over to your local site. 

[caption id="attachment_871" align="alignnone" width="1140"]![Fields correctly filled out inChange DB Prefix plugin](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214839/change-db-prefix-filled-correctly_x21rzt.jpg)
Here's the fields filled out correctly on my Local site![/caption]

Now, on your local site, and with the table prefix copied, paste the value into the New Prefix field, as shown, and click save.  

![Change DB Prefix plugin, process complete](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214839/change-db-prefix-finished_jscwcj.jpg)


It's going to look like nothing happened, but you should see these two messages, in blue - 


    
    All tables have been successfully updated with prefix (your prefix)_ !
    The wp-config file has been successfully updated with prefix (your prefix)_!



You may see a PHP warning at the top of the page, don't worry about this. At this point we are done with the table prefixes and you can go ahead and uninstall Change DB Prefix from both sites if you'd like. 



## Step 4 Get a copy of your content.



This is relatively straightforward if you have already setup a backup and synced it to Dropbox, like I covered in last weeks post. If so, go ahead to your dropbox folder (either on your computer or from the dropbox interface) and copy your most recent full site backup file to your computer.

![Image of uncompressed archive file.](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214838/backup-archive-file_buihyy.jpg)


Your backup file is in an archive, most likely with the file extension .gz 

[caption id="attachment_875" align="alignnone" width="1140"]![Image of backup up wp-content folder](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214837/backup-wp-content_rxzd9l.jpg)
This backup of the wp-content folder is what we need.[/caption]

Once you've copied the archive to your computer go ahead and double click it to open it. Inside of this folder you'll see a subfolder called wp-content - this folder contains all your media, themes, and plugins.

This is what we want. Leave this folder open and easily accessible.



If you don't have an easily accessible backup, you can also get this content by FTPing into your web hosting account and downloading your wp-content folder to your computer.





## Step 5 Export your live database.



Still with me? Good, because we are just about finished. Now that we have a copy of the content we need to grab a copy of our live database.



### Install WP Migrate DB



![WP Migrate DB Plugin install page](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214837/wp-migrate-db-plugin-install-page_uo2fj2.jpg)


On both the local and the live site, install the free WP Migrate DB plugin, by the good folks at Delicious Brains. From the install plugins page, just search for WP Migrate DB, it should be the first option, as shown above. Install this plugin and activate it on both sites. 

[caption id="attachment_877" align="alignnone" width="1140"]![WP Migrate DB Plugin migrate page](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214836/wp-migrate-db-plugin-migrate-page_q70ytq.jpg)
Here's the plugin running on my local site.[/caption]

On both sites, with the WP Migrate DB plugin activated, go to tools/Migrate DB



### Copy paths from local site



On your local site, from the Migrate DB page, you'll see  Find and Replace section, each with 2 fields. What we want to do is to copy the Find values from our local site, and paste them into the Replace values on our live site. 

On your local site, go ahead and copy the first value from the Find fields. This is the URL. Switch to your live site, and paste this value into the first Replace field (new URL) on your live site.

Next, switch back to your local site, copy the second value from the find fields, this is the file path. With the value copied, switch to your live site and paste the value into the second Replace field (new file path) on your live site.

[caption id="attachment_878" align="alignnone" width="1140"]![Migrate DB Plugin with all fields filled](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214836/wp-migrate-db-plugin-fields-filled_c42ebx.jpg)
Here's what the plugin looks like on my Live site once I've filled in all of the fields.[/caption]

When you're done, it should look something like the image above.



**Running this plugin on your live site is perfectly safe**. It is just going to make a **copy** of your database. Don't worry, it will only make the changes to the copy, not to your live site.



With the information entered on your live site, go ahead and click the "Migrate" button. Migrate DB is now going to make a copy of your database. The copy will include the necessary changes to make the database run on your local server.

![Migrate DB plugin, migration complete dialog](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214835/wp-migrate-db-plugin-migration-complete_pjoiv7.jpg)


Once Migrate DB has finished doing its thing you should see a screen like above, and Migrate DB will download the database copy to your computer. 

Remember where your computer put that file. It's probably in your downloads folder. It's probably going to be an archive file, like a .gz - There's no need to unzip this one, just leave it as it is.

You can go ahead and close your live site, we're finished with it.



## Step 6 Import the database to your local site.



We're in the home stretch here. No, really, I promise! Now that you've downloaded the database we have to import it into our local site. Switch back to your Desktop Server program.

[caption id="attachment_863" align="alignnone" width="886"]![Desktop Server configuration complete](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214844/desktop-server-local-url_nux5p9.jpg)
Here's where we left off with Desktop Server[/caption]

If your Desktop Server app still looks like this, just click the next button. 

[caption id="attachment_860" align="alignnone" width="886"]![Desktop Server Create a new site](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214847/desktop-server-create-new-site_cowzhz.jpg)
Back to the start page. Click that button in the lower left, that says "Sites"[/caption]

Now we are back to the start page. In the lower left hand corner of the Desktop Server window, click the button that is labeled "Sites". Your browser should open a page that looks something like the image below.

![Desktop Server, sites page](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214834/desktop-server-sites-page_fg8jsu.jpg)


Click the first link titled "MySQL Administration - phpMyAdmin". You'll see a page like this....

![phpMyAdmin page](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214834/phpmyadmin_hcyx7g.jpg)


This page is a program called phpMyAdmin. It manages all your databases. Mine probably has a lot more stuff in it, but that's okay. It should make it easier for you to find your local database. :)

[caption id="attachment_883" align="alignnone" width="1140"]![PHPMyAdmin enlarged.](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214833/phpmyadmin-enlarged_ctbday.jpg)
Here's a blow up. My test site is called photoninja.dev, my database name starts with photonin[/caption]

Your local sites database name will be prepended with the first few letters of your site name. Here's mine. My local site is called www.photoninja.dev, and the name of my local database starts with "photonin". Click the name of your database and you'll see another screen. 

[caption id="attachment_885" align="alignnone" width="1140"]![PHP MyAdmin site tables](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214833/phpmyadmin-site-tables_eyfa72.jpg)
Click import![/caption]

This is all of the tables from your local database. Click the import button, as shown.

![PHPMyAdmin import page](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214832/phpmyadmin-import-page_v9qo0d.jpg)


Click the browse button....

[caption id="attachment_887" align="alignnone" width="1140"]![PHPMyAdmin browsing for the DB](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214832/phpmyadmin-browse-for-db_eaj9rz.jpg)
Find your database file that was downloaded by WP Migrate DB and click Open[/caption]

Locate your downloaded database, and click "Open".

[caption id="attachment_888" align="alignnone" width="1140"]![phpMyAdmin, importing the databse](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214831/phpmyadmin-click-go_hsd9f0.jpg)
Click Go![/caption]

Scroll down to the bottom the page, and click "Go".

![phpMyAdmin success page](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214830/phpmyadmin-success_rtt1et.jpg)


Once you're done you should see a success message that says something like "Import has been successfully finished..." with the number of queries that were executed. Close out phpMyAdmin, we're finished with it. 

[caption id="attachment_890" align="alignnone" width="1140"]![WordPress login screen](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214830/WordPress-login_harzjj.jpg)
Just what we want! Don't log in or go to the front page yet.[/caption]

Now, you'll probably notice that you've been logged out of your local site, as shown above. This is good! This means that all of the database tables, and users, from our local site have been replaced with the info from our live site. 

Go ahead and leave this window open, **but don't log in just yet, and don't try to visit your local site yet either**. You won't break anything, but the site isn't going to work properly yet. We still have to move the content over. 



## Step 7 Final step, move the content



Go ahead and find your local site installation. Mine is located at documents/websites/www.photoninja.dev
Also, open the window with your full site backup, that we copied to your computer back in step 4.

[caption id="attachment_891" align="alignnone" width="1140"]![Swapping wp-content folders](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214829/replace-files_je86ar.jpg)
Do not put the wp-content folder in the other. Replace the other one![/caption]

Position these two windows side by side and drag the wp-content folder from your backup into your local site folder as shown. We're just replacing the wp-content folder in our local site with the wp-content folder from our backup file.



Don't put the wp-content folder inside of the other one. We want to replace the local site's folder with this one.



[caption id="attachment_892" align="alignnone" width="511"]![Replace warning dialog](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214829/replace-warning-dialog_kffyyx.jpg)
Yes, replace all the things.[/caption]


You'll probably see a warning, like this. It's okay, just click "Replace" and, believe it or not, you're done, mostly. :-p

You can go ahead and delete the rest of the *backup* site that you saved to your computer as you won't be needing it anymore. Go ahead and go back to your web browser and login with the credentials that you would normally use on your live site.



### Flush Permalinks



![WordPress permalinks page](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214828/WordPress-permalinks_dhljp8.jpg)


Before you do anything else, go to settings/permalinks, scroll to the bottom of the page, and click save. No need to change any settings. Just hit save. This will flush out any random weirdness that sometimes creeps up after a migration.
 
That's it, you're done. Go ahead and visit the front page of your local site. You now have a copy of your live site running on your computer!
 


## Thanks for reading!



Thanks for reading. I hope this was helpful and as always, if you have any comments or suggestions leave a comment or drop me a line via my [contact page](https://smutek.net/contact/). 

Next week I'll be showing you how to take any changes that you've made to your local site, and move them back to your live site using WP Migrate DB Pro, the premium version of WP Migrate DB.



### A Note about Desktop Server



When you are finished with Desktop Server make sure to shut the web services down before quitting the app. Just go to the Desktop Server home page, choose Stop or restart the web and database services, and follow the prompts. If you just quit the app without doing this, the web services will still be running on your computer.

Once you've stopped the services go ahead and quit the app. When you want to work with your local site again, just launch Desktop Server and start the web services back up. 



               

