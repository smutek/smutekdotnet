---
author: jimmy.smutek
date: 2016-09-10 02:18:39+00:00
draft: false
title: A little function for oEmbed + ACF
type: post
url: /a-little-function-for-oembed-acf/
categories:
- WordPress
post_format:
- Aside
tags:
- acf
- php
- snippets
---

We've been doing a lot of videos on our sites lately. Well, we've always done a lot of videos on our sites. The model is usually an on-page embed, either directly in page or via a modal, and we set the back-end up to use the oEmbed field in Advanced Custom Fields Pro. It gives a great back-end experience - and why use WordPress if it's not going to be user configurable, right?

Anyway, in almost every case we need to disable the display of related videos. The [problem has already been solved](https://www.advancedcustomfields.com/resources/oembed/), but I'm doing this often enough that I wrote this simple, but handy little function to take care of it. Configure the parameters in the function itself, and just pass it your field name. Outputs the URL and everything in the _$params_ array gets passed in on the tail end as a query string. 


    
    <code class="language-php">
    /**
     * oEmbed Attributes
     *
     * Add parameters to oEmbed query string. Useful for
     * turning off related videos and such.
     *
     * Basic field use: $video = videoLink('your_field_name');
     * Add second param if in a repeater: $video - videoLink('your_subfield_name', true);
     *
     * @see https://www.advancedcustomfields.com/resources/oembed/
     *
     * @param $field
     * @param bool $repeater defaults to false / true if repeater
     * @return mixed  embed HTML
     */
    function videoLink($field, $repeater = false) {
    
      global $post;
    
      // get current post ID
      $id = $post->ID;
    
      if(!$repeater) {
        // get the field
        $videoFrame  = get_field( $field, $id );
      } else {
        // if we are in a repeater
        $videoFrame  = get_sub_field( $field, $id );
      }
    
      // use preg_match to find iframe src
      preg_match('/src="(.+?)"/', $videoFrame, $matches);
      $src = $matches[1];
    
      // add extra params to iframe src
      $params = array(
        'rel'    => 0
      );
    
      $new_src = add_query_arg($params, $src);
      $videoLink = str_replace($src, $new_src, $videoFrame);
    
      return $videoLink;
    
    }
    </code>



To use it somewhere just pass it your field name. So, if your ACF field is _my_video_:


    
    <code class="language-php">
    echo videoLink('my_video');
    </code>



If you're rolling with a repeater, just set the second parameter to true. 


    
    <code class="language-php">
    echo videoLink('my_video', true);
    </code>



[GitHub Gist](https://gist.github.com/smutek/f11531a44327761c9cb7b660a9a78b95)

