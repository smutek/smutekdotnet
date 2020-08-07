---
author: jimmy.smutek
date: 2016-06-25 17:23:22+00:00
draft: false
title: Maintaining the Roots Stack
type: post
url: /maintaining-the-roots-stack/
categories:
- WordPress
post_format:
- Video
tags:
- bedrock
- composer
- deployment
- maintenance
- plugins
- trellis
---

{{<vimeo 172232346>}}

Here's a short screen cast showing how to maintain the Roots stack once it's been deployed. In this screen cast I update WordPress core, Jetpack, and the WordPress SEO Framework plugin. The SEO plugin is a little quirky with updating, but aside from that you'll see that everything goes smoothly and it's a super easy process. 

It's as easy as:

  * Update version numbers as needed in /site/composer.json
  * Run _composer update_
  * Make sure everything works.
  * Add & commit to VC _git add all_ & _git commit_
  * Push to your master repo, in my case _git push origin master_
  * CD to your trellis directory and deploy to your target environment, for me: _./deploy.sh production smutek.net_

If you haven't seen my other videos, I recently did a 3 part series on moving a WordPress website from shared hosting to a Roots stack running on a Digital Ocean droplet. Check them out here - 

- [Part 1: Setting up Trellis & Bedrock](/migrating-to-trellis-1/)
- [Part 2: Install plugins & import data](/migrating-to-trellis-2/)
- [Part 3: Set up Digital Ocean & deploy](/shared-hosting-to-roots-stack-part-3/)

## Links
- [roots.io/trellis/](http://roots.io/trellis/)
- [roots.io/bedrock/](http://roots.io/bedrock/)
- [roots.io/sage/](http://roots.io/sage/)
- [getcomposer.org/](https://getcomposer.org/)
