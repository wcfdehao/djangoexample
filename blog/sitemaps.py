#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
# __author__: xinlan 2017/12/31
from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.publish