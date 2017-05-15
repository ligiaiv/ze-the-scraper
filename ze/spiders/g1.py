# -*- coding: utf-8 -*-

from ze.spiders import ZeSpider

class G1Spider(ZeSpider):

    name = 'g1'
    allowed_domains = ['g1.com.br']
    parses = [{
        "ze.items.creativework.ArticleItem": {
            "fields": { 
                "name": [ 
                    "[itemprop=name]::text", 
                    ".content-head__title::text" 
                ], 
                "image": [ 
                    "[itemprop=image]::attr(content)", 
                    "[property='og:image']::attr(content)" 
                ], 
                "description": [ 
                    "[itemprop=description]::text", 
                    "[itemprop=alternativeHeadline]::text", 
                    ".content-head__subtitle::text" 
                ], 
                "author": [
                    "[itemprop=author]::text", 
                    "[itemprop=creator]::text"
                ], 
                "datePublished": [
                    "[itemprop=datePublished]::attr(datetime)", 
                    "[itemprop=datePublished]::text", 
                ], 
                "dateModified": [
                    "[itemprop=dateModified]::attr(datetime)" , 
                    "[itemprop=dateModified]::text", 
                ], 
                "articleBody": [
                    "[itemprop=articleBody]",
                    ".mc-body" 
                ], 
                "keywords": [
                    "[itemprop=keywords]::text", 
                    ".entities__list-itemLink::text"
                ]
            }
        }
    }]
