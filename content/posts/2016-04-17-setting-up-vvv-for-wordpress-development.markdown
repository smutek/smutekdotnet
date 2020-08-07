---
author: jimmy.smutek
date: 2016-04-17 17:27:14+00:00
draft: false
title: Setting up VVV for WordPress Development
type: post
url: /setting-up-vvv-for-wordpress-development/
categories:
- Tools
post_format:
- Video
tags:
- Local Server
- vagrant
- vvv
---

{{<vimeo 163160322>}}

This walkthrough video shows how to setup Varying Vagrant Vagrants for WordPress development on a Mac. Also covered is installation of Varying VVV site creation wizard & VVV Provision flipper, both by Brad Parbs, and how to install topdown VVV Dashboard by Jeff Behnke.

It's all pretty straight forward and, in my experience, working with Vagrant boxes is preferable over working with MAMP, or Desktop Server. Both of those are great products, for sure, but it's nice to run the development server on the same stack as the production server - which in most cases is going to be a LAMP stack, as opposed to a MAMP or WAMP stack.

Also, once you're comfortable with Vagrant it's possible to start exploring some of the other boxes out there, such as Trellis or Scotch, for example, and it becomes possible to setup the development stack to match the production stack exactly, for perfect parity between development and production environments.

Short of it is, it's pretty straight forward to set up and, in my case, taking the time to learn this has helped me to up my skill set.

Links -

  * **Virtual Box**
[https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)

  * **Vagrant**
[https://www.vagrantup.com/](https://www.vagrantup.com/)

   * **VVV**
[https://github.com/Varying-Vagrant-Vagrants/VVV](https://github.com/Varying-Vagrant-Vagrants/VVV)

  * **Homebrew** (optional)
[http://brew.sh/](http://brew.sh/)

  * **Variable VVV**
[https://github.com/bradp/vv](https://github.com/bradp/vv)

  * **VVV Provision Flipper**
[https://github.com/bradp/vvv-provision-flipper](https://github.com/bradp/vvv-provision-flipper)

  * **topdown**
[https://github.com/topdown/VVV-Dashboard](https://github.com/topdown/VVV-Dashboard)


If you prefer reading over watching, Brad Parbs wrote [an excellent walk-through](https://webdevstudios.com/2015/01/14/getting-started-vagrant-vvv-local-development/) on the WebDevStudios blog.

Note - around the 14 minute mark I ran into an issue with Varying VVV not remembering the path to my VVV installation folder. The fix was pretty easy.

In my case, VVV is in a folder called vvv, so just open the .vvv-config file in vim, or nano, or whatever.
   
{{<highlight bash>}}
vim ~/.vvv-config
{{</highlight>}}

Then update the path and save the file. In my case my install is located in my `home-directory/sites/vvv`
  
{{<highlight json>}}
{
    "path": "/Users/jimmysmutek/sites/vagrant-local"
}
{{</highlight>}}

changes to -
    
{{<highlight json>}}
{
    "path": "/Users/jimmysmutek/sites/vvv"
}
{{</highlight>}}

The next `vv-create` ran without issue.

Hope this post is helpful to someone!
