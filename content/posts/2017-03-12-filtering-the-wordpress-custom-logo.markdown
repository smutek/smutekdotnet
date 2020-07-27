---
author: jimmy.smutek
date: 2017-03-12 19:10:15+00:00
draft: false
title: Filtering the WordPress Custom Logo
type: post
url: /filtering-the-wordpress-custom-logo/
categories:
- WordPress
tags:
- bootstrap
- php
- sage
- snippets
- Tips
---

WordPress 4.5 added the [custom logo feature](https://make.wordpress.org/core/2016/03/10/custom-logo/). It's pretty nice, and where possible I try to use native WordPress functionality, but the default markup returned by `get_custom_logo()` isn't always what I'm looking for. Fortunately there's [a filter included](https://core.trac.wordpress.org/browser/tags/4.7/src/wp-includes/general-template.php#L920) just for this.

I build my sites with [Sage](https://roots.io/sage), most of them using [Bootstrap](http://getbootstrap.com/) for the front end. Here's a little function I wrote to leverage the native Custom Logo function, and give me back the markup I want.



## The Goal



So, here's what I'm trying to achieve. The default custom logo gives us markup that looks like this -


    
    <code class="language-html">
    <a href="some-link" class="custom-logo-link" rel="home" itemprop="url">
      <img src="some-logo">
    </a>
    </code>



Whereas I'm generally lookng for something like this -


    
    <code class="language-html">
    <a class="navbar-brand" href="some-link">
      <span class="sr-only">Some Site</span>
      <img class="img-responsive" src="some-logo">
    </a>
    </code>



I like to include the site title regardless, and just hide it with a screen-reader friendly class when a logo is present. I also like to bake the conditional logic right into my function as a way of keeping my templates a little cleaner. Every little bit helps!



## The Stuff



For sarters, the first thing to do is enable custom-logo support. I use Sage, and in versions < 9 I'll generally drop it in `lib/setup.php`


    
    <code class="language-php">
    // Enable custom logo support
    // https://codex.wordpress.org/Theme_Logo
    add_theme_support( 'custom-logo' );
    </code>



And here's the function I use to filter the markup.

https://gist.github.com/smutek/d0daef2e46db7521661db48214762c0f#file-brand-php

Everything is commented, but here's the run-down.




  * The function is filtering the custom logo function, so it takes that html as its input.
  * The first thing I do is grab the site name, since I like to always include it with my output.
  * First I check to see if we're on the home page - if so I'll wrap the site title in an H1, otherwise I'll wrap it in a paragraph tag since those pages will use the H1's for their own titles. I'll stash that in a variable called `$title`.
  * Now that I've got the site title squared away I set up a variable containing the link to the home page, `$home` and a variable to hold my css classes, `$class`.
  * Next I set up my `$content` variable, which serves as my fallback, and check to see if there's a custom logo.

(I know, I'm kind of variable happy - Here's why I stash the site title in a variable called `$content`. `$home`, `$title` and `$class` remain constant, but `$content` will get updated if a custom logo is present, otherwise it just gets passed along to the output as is. Make sense?)
  * If `has_custom_logo()` returns true, I just mirror what's in the [native function](https://core.trac.wordpress.org/browser/tags/4.7/src/wp-includes/general-template.php#L890), with my own small tweaks. I update the content to include the src to the logo file, then append the title variable, wrapped in a span tag and hidden with Bootstraps sr-only class. Otherwise, the unaltered `$content` is passed along.
  * Finally, the markup is put together using [sprintf](http://php.net/manual/en/function.sprintf.php), again, mirroring the native function, and returned to the template file.




## Output





Since we're just filtering the existing custom logo function nothing special is required to use it. In a typical Sage 8 site, in my `header.php` template, I'll replace:

`<a class="navbar-brand" href="<?= esc_url(home_url('/')); ?>"><?php bloginfo('name'); ?></a>`

With:

`<?php the_custom_logo; ?>`

That's it!

The resulting markup looks something like this:


    
    <code class="language-html">
    <a href="http://local.wordpress.dev/" class="navbar-brand" rel="home" itemprop="url">
      <img width="150" height="150" src="/wp-content/uploads/2013/03/image-alignment-150x150.jpg" class="brand-logo img-responsive" alt="Image Alignment 150x150" itemprop="logo">
      <span class="sr-only"><h1>Local WordPress Dev</h1></span>
    </a>
    </code>



And the fallback, without a logo added:


    
    <code class="language-html">
    <a href="http://local.wordpress.dev/" class="navbar-brand" rel="home" itemprop="url">
      <h1>Local WordPress Dev</h1>
    </a>
    </code>



That's it! A quick, nice fallback that leverages various native WordPress super powers. :) Pretty handy.

How do you work with logos in WordPress?

Resources




  * Custom Logo ([codex](https://make.wordpress.org/core/2016/03/10/custom-logo/))
  * Custom Logo ([trac](https://core.trac.wordpress.org/browser/tags/4.7/src/wp-includes/general-template.php#L878))
  * [Sage](https://roots.io/sage)
  * [Bootstrap](http://getbootstrap.com/)
  * [GitHub Gist](https://gist.github.com/smutek/d0daef2e46db7521661db48214762c0f)

