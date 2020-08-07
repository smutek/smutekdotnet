---
author: jimmy.smutek
date: 2016-08-30 03:03:21+00:00
draft: false
title: Trellis + Xdebug + PhpStorm
type: post
url: /trellis-xdebug-phpstorm/
categories:
- Tools
post_format:
- Video
tags:
- debugging
- PhpStorm
- trellis
- Xdebug
---

{{< vimeo 180681909 >}}

I love running Xdebug through PhpStorm's built in debugger but have had the hardest time getting it to work with Trellis. I have no problem getting it going with VVV but have never been able to get my path mappings correct in Trellis.

Well, turns out it's really simple with PhpStorm's Zero-Configuration debugging. Here's the [JetBrains documentation](https://www.jetbrains.com/help/phpstorm/2016.2/zero-configuration-debugging.html) on that - but the short of it is:

* Install a bookmarklet or browser extension. I use The easiest Xdebug on Firefox, and Xdebug Helper on Chrome.
 
* On your browser extension, set the IDE key to _XDEBUG_
* Set a breakpoint somewhere

* Tell PhpStorm to start listening for connections

* Start the debugger on your browser and refresh the page

The first time you run the debugger PhpStorm will pop up a window showing the path mappings it has detected. These are fine to select as defaults. 

Also, I've found that eventually the browser will time out, however this does not seem to effect the debugger as I'm still able to step through code and use the debugger normally. So, I've been able to live with that. 

Links - 

* [PhpStorm Zero-Configuration Debugging](https://www.jetbrains.com/help/phpstorm/2016.2/zero-configuration-debugging.html)

* [Easiest Xdebug (Firefox)](https://addons.mozilla.org/en-US/firefox/addon/the-easiest-xdebug/)

* [Xdebug Helper (Chrome)](https://chrome.google.com/webstore/detail/xdebug-helper/eadndfjplgieldjbigjakmdgkmoaaaoc?hl=en)

* [Trellis ](https://roots.io/trellis/)




