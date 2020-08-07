---
author: jimmy.smutek
date: 2017-01-07 17:18:36+00:00
draft: false
title: Rich Semantic Titles in WordPress with ACF
type: post
url: /rich-semantic-titles-in-wordpress-with-acf/
categories:
- WordPress
tags:
- acf
- bootstrap
- php
- quick-tips
---

Last night while browsing the [Roots Discourse](https://discourse.roots.io/) I came across a cool share by a user who has written a little utility to handle a request he often gets from designers and content creators. 

User MWDelaney writes -




<blockquote>I can't count the number of times my designers have asked to make a single word in an otherwise semantic title bold, or italic, or larger, or whatever, so I wrote this tool to build complex title styling with a hopefully-intuitive ACF GUI (requires ACF Pro 5) with a live preview, which automatically replaces _the_title()_ in the loop.</blockquote>


  


So he wrote this cool little plugin that gives end users a set of fields to construct these complex titles. [The post is here](https://discourse.roots.io/t/advanced-custom-fields-complex-titles/8481), and [you can check his plugin out here](https://github.com/MWDelaney/acf-complex-titles). I'd suggest exploring his GitHub further as it looks like he's working on lot's of cool ideas like this.

Anyway, I'm reading his post and it reminded me of a solution I've been using [at work](https://ainsleyagency.com) to help make descriptive titles a bit more semantic.

Imagine we're building a new site for "Bob's Hermit Crab Sanctuary". Like most sites it has an About page. In the site map and wireframes the page is labeled "About" which is appropriate because it's a page about the business. At the same time, "About" is maybe a bit boring and not as descriptive as it could be, so in the design "About" becomes:  "A Safe Haven for Hermit Crabs Since 1861". 

Much nicer, but maybe a little long for the top nav, and in the comp the top nav is still labled as "About". I know I can change the menu text via the WordPress menu editor, but I want to step it up a little, and "About" still remains the shortest, most releavant keyword for the page.

[Moz says](https://moz.com/learn/seo/title-tag) that:



<blockquote>The title element of a web page is meant to be an accurate and concise description of a page's content. This element is critical to both user experience and search engine optimization. It creates value in three specific areas: relevancy, browsing, and in the search engine results pages.</blockquote>


  


According to Moz, the optimal format when constructing a title is: 
Primary Keyword | Secondary Keyword

The Moz article references [this quality assurance tip](https://www.w3.org/QA/Tips/good-titles) from the W3 Consortium which states:



<blockquote>Because only 60 to 80 characters are displayed in many window titles, menus, etc.; you can give a more detailed/pleasant title in the top level heading of your document, e.g. <h1>Section One: When has the Modern Time Commenced, Musicwise?</h1></blockquote>


  


I got the idea for how to handle this from Bootstrap's headings with "[lighter secondary text](http://getbootstrap.com/css/#type-headings)" example:

_<h1>h1. Bootstrap heading <small>Secondary text</small></h1>_

I like this execution because semantically, _<small>_ is used to represent small runs of secondary, or side text. This makes it great for displaying headers with sub-text, which is essentially what I am trying to do here. The difference in my case is that I want to hide the first portion of the title from viewers, but still have it as part of the document. Span tags have no semantic meaning, so I can extend the Bootstrap example by wrapping a _<span>_ around the first portion of the title to control its visibility. More on that below.

So for the backend, what I've started doing is setting up an ACF field group called something like "Title Override". I'll set the display settings to "High (Below the Title)" on the back end, and give it 2 fields - a true/false (checkbox) to toggle it on and off, and a text field for the description. I use the checkbox to hide and show the field on the backend, and to filter the output on the front end.

To the end user it looks something like this - 

![Animated gif showing ACF back end](/img/2017/01/example.gif)


The logic is simple and can go right in the template file, but I prefer to drop it in a function. It just needs to get the page title, check if we are doing an override, generate the appropriate markup if so, and return the results to the template.
      
{{<highlight php>}}
/**
 * Title override
 * @return string - title
 */
function overrideTitle()
{
  // true/false 
  $override = get_field('title_override');
  $title    = get_the_title();
  if ($override) {
    // If using the override, get the title description
    $description = get_field('title_description');
    // Setup the modified markup
    $output = '<span class="sr-only">' . $title . ': </span><small class="title-description">' . $description . '</small>';
  } else {
    // Not doing an override, use the regular title
    $output = $title;
  }

  // return the output to the template
  return $output;
}
{{</highlight>}}

Note the sr-only class; We use a lot of [Bootstrap](http://getbootstrap.com/), and in this case I'm using Bootstraps sr-only class to hide the "About:" keyword portion of the title. This way it doesn't display in the browser, but it's still visible to screen-readers and bots. Aside from that, the description is still wrapped in a _<small>_ tag which, aside from the semantic meaning it provides, also has the effect of making our text smaller. So it needs to be styled to match its parent. This is simple using the _@extend_ directive in Sass. 
    
{{<highlight scss>}}
h1 .override-title {
  @extend h1;
}
{{</highlight>}}

Then in my template I call the title like this - 
   
{{<highlight php>}}
<h1><?= overrideTitle(); ?></h1>
{{</highlight>}}

Now if there's no override the browser gets the regular title, but if override returns true the browser gets -
    
{{<highlight html>}}
<h1><span class="sr-only">About: </span><small class="override-title">A Safe Haven for Hermit Crabs Since 1861</small></h1>
{{</highlight>}}



Which, in terms of intent, reads as - 
About: A Safe Haven for Hermit Crabs Since 1861

That's it, screen readers and search-bots get rich, valid, semantic, and fully descriptive markup, and our client, content creators and designers have the control they need over the display. 

Good stuff!

* * *

Resources -

- [ACF](https://www.advancedcustomfields.com/pro/)
- [Roots](https://roots.io)
- [Bootstrap](https://getbootstrap.com/)
- [WordPress](https://wordpress.org/)
- [Moz](https://moz.com/)
- [W3C](https://www.w3.org/)
