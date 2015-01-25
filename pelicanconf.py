#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Juannell Riley'
SITENAME = u'Do Nothing, Say Nothing'
SITEURL = ''
PATH = '/home/kirk/juannell/c_fork/content/blog_content'
OUTPUT_PATH = '/var/www/output'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RELATIVE_URLS = True
# Blogroll

DISQUS_SITENAME = "jrileyopinion"
DEFAULT_PAGINATION = 10
THEME = '/home/kirk/pelican-elegant/' 
PLUGIN_PATHS = ['/home/kirk/pelican-plugins', '/home/kirk/pelican-elegant/static/']
PLUGINS = ['tipue_search', 'summary', 'liquid_tags.img', 'extract_toc', 'sitemap', 
            'neighbors', 'latex', 'related_posts', 'share_post']
SITEMAP = {'format': 'xml', 'priorities': { 'articles': 0.5, 'indexes': 0.5, 'pages': 0.5},
        'changefreqs': { 'articles': 'daily', 'indexes': 'daily', 'pages': 'daily'}}
SUMMARY_END_MARKER = '<!--more-->'
TYPOGRIFY = True
DEFAULT_PAGINATION = False
MD_EXTENSIONS = ['extra', 'headerid', 'toc(permalink=true)']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
RECENT_ARTICLES_COUNT = 10
RELATED_POSTS_LABEL = 'Keep Reading'
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = u'Get Weekly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = u'Keep Me Informed'
MAILCHIMP_FORM_ACTION = u'//jrileyopinion.us10.list-manage.com/subscribe/post?u=17a0e0fa18cb9be1af193b100&amp;id=989a56e8de' 
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

LANDING_PAGE_ABOUT = {'title': 'Why a Blog?', 'details':  """<p>I've often thought of blogs as excercises in vanity. I'm not sure my thoughts on them have changed. I, however, have been asked to start one on many occasions; often enough to convince me I might have some things to say that are worth sharing with a larger audience. But, I'll let the audience decide. I implore any and all viewers to comment, even if it's in disagreement. I want this to be a learning experience for me. That's only possible if those who read also engage in dialogue. Aristotle said the only way to avoid criticism is to do nothing, say nothing. I've decided to name my blog that. Beautifully ironic, no?</p>
        <p>This blog, I hope, will be primarily concerned with social commentary, philosophy, and intellectual ramblings. I will try to keep me out of it. By that I mean I won't saturate my opinions with facts about myself. Everything I say will stand or fall on the merit of its accuracy and logical integrity unless, and only if, my anecdotal experience is paramount and provides an objective metric. Lastly, I have no interest in avoiding controversy. Be outraged! It's what this society is missing!</p>"""}

