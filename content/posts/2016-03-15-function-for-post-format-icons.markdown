---
author: jimmy.smutek
date: 2016-03-15 04:54:39+00:00
draft: false
title: Function for Post Format Icons
type: post
url: /function-for-post-format-icons/
categories:
- WordPress
post_format:
- Aside
tags:
- php
- snippets
---

<code class="language-php">
    /**
     * Output Post Format icons
     * 
     * Outputs an icon for each post format. Set up to use Fontawesome,
     * but can be used with anything, or you can just use CSS.
     *
     * @return string
     */
    function post_format_icon() {
      global $post;
      // get current post ID
      $id     = $post->ID;
      // get post format
      $format = get_post_format( $id );
      // array of icons as $format => $icon key/value pairs
      $icons = [
        'standard' => 'fa-pencil',
        'aside'    => 'fa-sticky-note',
        'chat'     => 'fa-comments',
        'gallery'  => 'fa-picture-o',
        'link'     => 'fa-external-link',
        'image'    => 'fa-camera',
        'quote'    => 'fa-quote-left',
        'status'   => 'fa-commenting',
        'video'    => 'fa-video-camera'
      ];
      // format will return false if no format is set. So, evaluate against this..
      // if format = false then $icon = standard, else icon = selected format
      $format == ( false ) ? $icon = $icons['standard'] : $icon = $icons[ $format ];
      
      // string to be output
      // echo a full line of html or just drop the output in as a class
      $output = $icon;
      // return the output
      return $output;
    }
    </code>



[Github Gist](https://gist.github.com/smutek/f15e7723db1e5e84c23b)
