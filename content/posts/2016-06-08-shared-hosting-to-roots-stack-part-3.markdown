---
author: jimmy.smutek
date: 2016-06-08 02:43:32+00:00
draft: false
title: 'Shared hosting to Roots stack: Part 3'
type: post
url: /shared-hosting-to-roots-stack-part-3/
categories:
- WordPress
post_format:
- Video
tags:
- bedrock
- deployment
- Migration
- sage
- trellis
---

This is the third in a series of screencasts that will document the process of moving a WordPress website from a shared hosting provider to a Digital Ocean droplet with Trellis, Bedrock, and Sage, with an SSL from Let's Encrypt.



Correction: The video opens with: _...this is part four of a three part series..._ Sorry, It was late. :)





I didn't obscure any passwords in this video but, for obvious reasons, after recording I rebuilt my droplet, reset all passwords, and redeployed the project.



In the [first screen-cast](https://smutek.net/migrating-to-trellis-1/) I setup Trellis & Bedrock.

In the [second screen-cast](https://smutek.net/migrating-to-trellis-2/) I used Composer to get my theme & plugins installed, dealt with a couple of premium plugins, and migrated my data into my development environment.

In this screencast I setup my Digital Ocean droplet, prepare my project, provision the server and deploy the site. Yay! Thoughts and such below.


## Suggestions




### Read the docs carefully.


This is the best suggestion I have to offer. I read the docs carefuly and when my first deploy failed I realized I hadn't read the docs carefully enough. The documentation is comprehensive, it's your friend.


### Make sure site keys have been added correctly


This tripped me up a couple of times but sure enough upon closer inspection of each failed deploy there was a stray 'example.com' in place of 'smutek.net'. Generally if provisioning fails early on a missed site key is likely the culprit.


### Do a couple dry runs with a spare domain


Unless you're super comfortable with this I wouldn't suggest your first deploy be on a mission critical or time sensitive site. It pays to be patient, not get frustrated, and go through it a couple of times until the process and concepts sink in. If things aren't working out just destroy the DO box and try again. I'd say that I've done 5 or 6 deploys over the course of recording this screen-cast and at this point I'm comfortable enough with the process.


## Notes


Here's the order I did things:


### Digital Ocean Setup





 	  * Point DNS to DO
 	  * Choose droplet : Ubuntu 14.0.4
 	  * Add SSH Keys
 	  * Create droplet
 	  * Add domain to droplet (regular & www)



### Provision & Deploy




If setting up SSL with letsencrypt, be sure to have added www subdomain when adding domain to droplet





 	  * Make sure the project is added to github
 	  * Set up variables in _group_vars/production/wordpress_sites.yml_ 
 	  * Add the necessary settings for remote servers to _group_vars/production/vault.yml_

 	    * Generate password for _vault_mysql_root_password_

 	    * Generate crypted password for _vault_sudoer_passwords_

 	    * Generate _db_password_

 	    * Generate salts (be sure to use the Yaml, if using Trellis)
 	    * Generate password for _group_vars/all/vault.yml_



 	  * Set variables in group_vars/all/mail
 	  * Set 'sshd_permit_root_login: false' in_group_vars/all/security.yml_
 	  * Create a file called _.vault_pass_ in /trellis. Generate a random password and save it in this file.


This is your vault password. Make sure it's being git-ignored (it is, but double check .gitignore anyway)
 	  * Inform Ansible of the vault password by adding _vault_password_file = .vault_pass_ to _trellis/ansible.cfg_
 	  * Encrypt vault.yml files. Use as needed, or encrypt all with:

    
    <code class="language-bash">
    ansible-vault encrypt group_vars/all/vault.yml group_vars/development/vault.yml group_vars/staging/vault.yml group_vars/production/vault.yml
    </code>



 	  * Add server hostname to _hosts/production_
 	  * Add public SSH keys for web & admin_user groups in _group_vars/all/users.yml_





Note, make sure your public key has been added to github, or wherever. In the case of github,
_https://github.com/username.keys_

 	  * If using deploy hooks, uncomment the buildhooks in 'deploy-hooks/build-before.ym' and replace 'sage' with the name of your theme directory
 	  * Turn on caching if using it
 	  * Verify you can ssh to your box
 	  * Make sure all changes have been saved, committed, and pushed to VC
 	  * Run

    
    <code class="language-bash">
    ansible-playbook sever.yml -e env=production
    </code>



 	  * Run

    
    <code class="language-bash">
    ./deploy.sh production yoursite.com
    </code>



 	  * Go to your site & run through the WP Installer.
 	  * Migrate database (I used DB Migrate Pro)
 	  * Rejoice



## Links


[roots.io/trellis/](http://roots.io/trellis/)
[roots.io/bedrock/](http://roots.io/bedrock/)
[roots.io/sage/](http://roots.io/sage/)
[https://www.digitalocean.com/](https://www.digitalocean.com/)
[https://letsencrypt.org/](https://letsencrypt.org/)
