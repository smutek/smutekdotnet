---
author: jimmy.smutek
date: 2015-03-06 15:50:10+00:00
draft: false
title: How to set up a WordPress Backup Plugin
type: post
url: /how-to-set-up-a-wordpress-backup-plugin/
categories:
- WordPress
post_format:
- Video
tags:
- backup
- plugins
- quick-tips
---

## Backups are so important





Part of a series of posts from my days of self employment.



This week I'm going to cover how to set up a WordPress backup plugin. Think of this as a form of disaster insurance. Nobody knows more than you just how important your website is to the health of your business. It's just super important to make sure that you have a proper backup of your WordPress website; not just your files, but your database as well. 



### Meet BackWPup



![Image of backwpup plugin on the plugin directory](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214859/backup-plugin-page_arhtj3.jpg)


Luckily this is a super easy thing to get going. There are tons of great options on the market. The one that I am going to cover today is called BackWPup, a free plugin from MarketPress. [You can find the plugin here](https://wordpress.org/plugins/backwpup/) on the WordPress plugin directory. For this post I will be using the free version, but MarketPress also offers a [premium version](https://marketpress.com/product/backwpup-pro/) of the plugin that does lots of extra cool stuff.



### Installation



![Backwpup plugin from the wp admin plugin browser](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214858/backup-plugin-in-admin_e8u3pc.jpg)


Installation is super easy. Just go to your WP Admin page, select plugins, and add new. Search for BackWPup and the plugin will be the first in the list. Check out those stats, the plugin has 4 stars, with 240 reviews and at the time of this writing nearly 1.7 million downloads! That's pretty impressive.



### Configure Backup Jobs



Once you've installed and activated the plugin you'll be directed to the landing page for the plugin. You will also notice that a new menu item for BackWPup has been added to your WordPress admin menu. The next thing that we want to do is to configure some backup tasks to run. Each backup task is called a job, in this blog post we are going to configure 2 jobs. We are going to configure a weekly full site back up, and a daily database backup. 



#### Weekly Backup vs. Daily Backup



The weekly full site backup will be an all inclusive backup of our entire site. All our site files, themes, plugins, and database will be included in this back up. I run this task weekly because it generates a larger backup and takes more server resources to run. I find that the database backup is the most critical thing to keep backed up regularly. The database is also a much smaller file and it takes less resources to run the task. That's why I am going to configure the database to backup daily. 

![Adding a job to BackWPup](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214857/backup-plugin-adding-a-job_qq6cgt.jpg)


The next thing to do it to add a new job. In the general tab of the BackWPup plugin, type in the name of your job as shown. I've named mine "Weekly Full Site Backup".  All of the default settings are fine for this page. The default settings are pretty robust and unless you have a specific need they should work pretty well for you.



#### Job Destination



[caption id="attachment_834" align="alignnone" width="1349"]![Backup to dropbox option in BackWPup](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214857/backup-to-dropbox-option-selected_gizwq3.jpg)
The backup to Dropbox option selected[/caption]

One thing that I am going to change on the general page is the Job Destination settings. I'm going to use the backup to Dropbox feature for this post but it's just as easy to backup to Amazon S3. The option for "Backup to folder" will store the backups on your server. I don't recommend this for the simple fact that your backups are now stored in the same location as your website. If something happens with your web host and the server is wiped out, you've now lost your sit and your backups. 

It's kind of like having a backup hard drive attached to your computer at home. It's great to have backups, if something happens to your computer you are covered. But, what is there's a fire and you lose the computer and the hard drives?

**It's a good idea to keep your backups in a separate location!**

Go ahead and click save, then click on the schedule job tab. This is where we will tell the plugin when to run our back up job. The default is manual, which means you'll need to remember to come here and run backups. We don't want to do this, we want to set this up, let WordPress take care of it for us, and not have to worry about it.

[caption id="attachment_836" align="alignnone" width="1349"]![The default backup schedule tab](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214856/backup-schedule-page-manually_oagyv0.jpg)
The default backup schedule tab[/caption]

If you click on the WP Cron radio button you'll be able to set up a time for the job to run. I'm leaving mine at the default, which is 3:00 am on Sundays. I suggest choosing a time where you have minimal traffic on your site. Once you've set up your schedule, click save. 

[caption id="attachment_839" align="alignnone" width="1140"]![The weekly backup task configured](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214855/backup-schedule-page-weekly_lyt1ca.jpg)
The backup task set to run weekly[/caption]



#### Connect to Dropbox



The next thing to do is to configure the Dropbox settings. This is super easy. Go ahead and click on the "To:Dropbox" tab. 

[caption id="attachment_840" align="alignnone" width="1349"]![The dropbox settings page un-configured.](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214854/dropbox-settings-blank_vtwswb.jpg)
The Dropbox settings page[/caption]

If you don't have a Dropbox account head over to Dropbox.com and sign up for a free account. The free account offers 2GB of storage for free, which will be more than enough to back up most basic sites. If you're a photographer you likely will have a much larger site, and will need more space. Dropbox offers 1 Terabyte of storage for around $10 per month, and unlimited storage for $15 dollars a month.

Once you have your Dropbox account set up go ahead and click on the "Get Dropbox auth code" button. You're going to be directed to a Dropbox page which is going to ask you if it is okay for WordPress to interact with it. Click allow here, and use your mouse to copy the code that appears once you've clicked allow. 

![the dropbox handshake](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214854/dropbox-handshake_nasdcy.jpg)


Head back over to your WordPress site and paste the Dropbox code into the auth field, as shown.

[caption id="attachment_842" align="alignnone" width="1140"]![Dropbox successfully authenticated!](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214853/dropbox-settings-success_dqtodq.jpg)
Dropbox successfully authenticated![/caption]

Next, click save. If you've done everything correctly you should now see a success message as shown. 



#### How many backups to keep?



Now we're going to change the file deletion settings. All this is saying is, "Hey, how many copies of this backup do you want to keep?". I'm going got set mine to 5, which will give me access to 5 weeks of backups. This means that, should disaster strike, I can roll my site back to any of the backs that were taken over the past 5 weeks. You can set this however you'd like, but realize that the more backups you keep, the more space you need. Go ahead and click save again. 

[caption id="attachment_843" align="alignnone" width="1140"]![File deletion settings](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214853/dropbox-settings-file-deletion_suc904.jpg)
I set my file deletion setting to 5[/caption]



#### Run the backup!



With these settings configured I'm going to go ahead and run the back up. You can run the job by going to the Jobs section of the plugin or, there should be a link titled "Run Now" that appears on the page after you click save. Either one is fine. 

Depending on the size of your site, this may take quite a while. It's important to make sure that you have enough space at your destination to hold your back up. If your site is 3GB and you are trying to backup to a 2GB Dropbox account, the backup will fail. 

![Backup job completed](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214852/dropbox-process-complete_u4tqho.jpg)


Looks like the backup task ran successfully! Now it's time to configure the daily database backup. I run database backups daily because the database file is just a fraction of the size of a full site backup. This task uses less server resources to run and requires less space to store. 



### Protect that database!



The database is also, arguably, the most important thing to keep backed up. It's sort of like the brain of your site. It contains all your posts, all your pages, and all your configurations. When a visitor comes to your WordPress site, it's the database that tells WordPress what content to put together for them as they browse through your site. If you lose your database, it's kind of game over. This is why it's super important to keep the database backed up, and protected.



#### Configure the job



The process for setting this task up is the same as the full site backup. The exceptions being that we will configure the general tab to just backup the database. Give the task a name, I'm using "Daily Database Backup" for mine. 

![Daily database settings](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214851/daily-db-backup-configured_ygczml.jpg)


In the Job Tasks section, uncheck everything but "Database Backup", like shown. I'm going to choose to send my database backups to Dropbox as well, but in most cases you can also have the database backups sent to your email. If you'd like to do this go ahead and click the "Backup sent via email" checkbox, along with the Dropbox checkbox. Next, click save. 



#### Schedule the job



![Database daily backup scheduled](http://res.cloudinary.com/dqrbt3vps/image/upload/v1448214851/daily-db-backup-scheduled_emadcm.jpg)


Next click the Schedule tab and schedule your database back up to run daily. I've set mine up to run every day at 2am. Once you've configured the schedule, click save.



#### Authenticate with Dropbox again



If you are sending your database to Dropbox, head over to the Dropbox tab next. We need to authenticate with Dropbox for each backup job that we set up, so just follow the same steps that we went thorough earlier, when we authenticated our weekly backup. 

Once you've done that, click save.



### You're done.


 
That's it. If you've followed along you now not only know how to Install and configure a WordPress backup plugin, but you've also got 2 backup jobs setup to backup your entire site once a week, and your database once a day. 
 


Important: Check with your host about their backup policies.


 
It's important to mention that it might be a good idea to check with your web host about their backup policies. Running backups puts additional strain on a server. Also, if you do opt to keep your backups on your server then you'll want to make sure you are mindful of your space. Even "unlimited" storage isn't really unlimited, as your host will likely remind you if you've got 15 copies of a 10 gig website sitting on a shared hosting account. 
 
I suggest reading this article, [Beware of shared hosting and the storage of backups](http://wpandlegalstuff.com/beware-shared-wordpress-hosting-storing-backups/), by Richard Best. Richard runs a site called [WP and Legal Stuff](http://wpandlegalstuff.com/) that covers, you guessed it, legal issues relevant to business owners running their own websites. It's definitely a site to bookmark and follow. 



### Thanks for reading!


  
That does it for this week. I hope this walk through was helpful. As always, if you have any questions or suggestions please feel free to drop me a line or leave a comment. 
  
Next week I'll be covering how to take one of these backups and get a copy of your WordPress website running on your computer. This is a great way to safely test out new themes and plugins without having to change your live site.
