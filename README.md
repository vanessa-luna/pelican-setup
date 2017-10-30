
# PELICAN SETUP for vanessa-luna.github.io

This document will describe how I have configured  [Pelican](https://getpelican.com) for my website. I have no idea how my setup compares to others out there, but I think it has some oddities that may be useful to share and have documented.

> This may take a while to understand, and I may not do a good job of explaining it. However, since I've shared bits and pieces of it on my blog I figured the whole thing should be available in case someone needs it.


## High Level

My website has a few dimensions and a quirk or two. First, the root of the website is a blog. This is normal and Pelican handled this perfectly. The next bit is that I had a set of posts I wanted to be totally separate in a hidden location of the site. I had to create a second config to handle the generation of those posts so they didn't co-mingle with the other posts. The third bit is about images. I have a ton of images and use the thumbnailer plugin to generate smaller versions of the images. This requried yet another pelican config so I could reduce filesize by always placing thumbnails and images in production, and symlinking to dev. This MAY not be required but since I am still a novice at linux it helped. Finally, my last main component is a product page plus blog that lives in a subfolder. This needed a separate config to handle a tweak or two.

I have had to do a few things such as:

* Tweak the generators.py file in Pelican
* Tweak a couple of plugins to offer the features I needed
* Use inherited configs to be DRY
* Used template overrides
* Use 9 plugins
* Create my own dev and build script for simplicity

**NOTE:** I am super new to github and how to contribute to other projects. I have no idea how to do these things, so even though I have tweaked plugins and pelican I don't know how to let others know about it or whatnot.

## TOC

* [Compiling](#compiling)
* Scripts
    * build.sh
    * dev.sh
* Pelican tweaks
* Configs
    * referencing inherited Configs
    * each config's uniqueness
* Plugins
    * Using each plugin
    * tweaks made to plugins
* Theme
    * Templates
    * CSS




## Compiling

1. Install Pelican
2. Download this repo into a folder
3. Clone the [content repo](https://github.com/vanessa-luna/site-content) in content/
4. Download the raw media here, and place within respective content folders
5. run ./dev for local testing
6. run ./build.sh to compile

The raw media is kept in a Mega cloud account. Unfortunately I do not have a better way of storing these files right now. But they are there.



## Scripts

### build.sh

If you open this up, it will look fairly straitforward. Borrowing from the pelican-quickstart files, I simply run pelican on all the configs I have created, then move into the output folder and run git.

I understand that pelican can do something like this, but keeping it homegrown helps me feel in control.


### dev.sh

This one is a major tweak to what comes from pelican-quickstart. But gosh am I glad I had that starting dev file. I have never written shell before. But I am happy with how I've changed the API.

First, read the usage(). It is easy to understand.

I have abstracted out each config into a separate function. As well as maintained a "build all" function.

The most useful part of this new dev script is being able to build only a portion of my website at a time. It only takes < 1 second to build the gaff portion but > 12 seconds to build the blog.



## Pelican Tweaks

I only modified Pelican once. However it was crucial to my latest addition of the product page.

Pelican tends to live in `~/.local/lib/python2.7/site-packages/pelican/`

In order to make actual use of the EXTRA_TEMPLATES_PATHS option, I had to change the code `generators.py`


### ORIGINAL CODE
``` python
# templates cache
self._templates = {}
self._templates_path = []
self._templates_path.append(os.path.expanduser(
    os.path.join(self.theme, 'templates')))
self._templates_path += self.settings['EXTRA_TEMPLATES_PATHS']
```

### TWEAKED CODE
``` python
# templates cache
self._templates = {}
self._templates_path = self.settings['EXTRA_TEMPLATES_PATHS']
self._templates_path.append(os.path.expanduser(
    os.path.join(self.theme, 'templates')))
```

This actually allows you to override templates from a base theme.

### Fun advantages

However the Pelican/Jinja environment works, whatever is found in the EXTRA_TEMPLATES_PATHS first, is used, even if referencing hints otherwise. Also, by using a base.html template, you can override other parts of the theme easily.

#### referencing

So, even if my default index template references "base.html", because there is another "base.html" in my extras path, it will use that "base.html" instead.

```
theme/templates
    base.html
    index.html
otherTemplates/
    base.html
    page.html
```

Pretty awesome right!?

#### theme override

In my root templates, inside the base.html it looks like this:

``` html
<!DOCTYPE html>
<html lang="{{ DEFAULT_LANG }}">
<head>
	<title>{% block page_title %}{% endblock page_title %} | Vanessa & Luna</title>
	{% include 'fragments/head.html' %}
	{% block assets %} {% endblock %}
</head>
<body>
	{% include 'fragments/sidebar.html' %}
	<div class="content">
		{% block title %} {% endblock %}
		{% block content %} {% endblock %}
		{% include 'fragments/footer.html' %}
	</div>
</body>
</html>
```

Simple. Setup some blocks, and the foundation of the site. NOTE the sidebar and footer.

In my EXTRA_TEMPLATES_PATHS for the product site, I override the base.html with this:

``` html
<!DOCTYPE html>
<html lang="{{ DEFAULT_LANG }}">
<head>
	<title>{% block page_title %}{% endblock page_title %} | Liner Gaff</title>
	{% include 'fragments/head.html' %}
	{% block assets %} {% endblock %}
    {% assets "css-linergaff-base" %}
        <link rel="stylesheet" href="{{ SITEURL }}/{{ ASSET_URL }}">
    {% endassets %}
</head>
<body>
	<div class="content">
		{% include 'fragments/menu.html' %}
		{% block title %} {% endblock %}
		{% block content %} {% endblock %}
		{% include 'fragments/footer.html' %}
	</div>
</body>
</html>
```

They look similary, but I've added another CSS reference to override some of the original theme settings. DOPE!

And I have changed the layout of the html to include the menu and not the sidebar. But the footer reference remains the same even though I have not overriden it... Oooooh. This is because if Jinja cannot find the template in the extra path first, it looks in the next path, and finds it :)





## Configs

### referencing inherited Configs
### each config's uniqueness


## Plugins

### Using each plugin
### tweaks made to plugins


## Theme

### Templates
### CSS
