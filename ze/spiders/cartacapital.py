# -*- coding: utf-8 -*-

from ze.spiders import ZeSpider

class CartaCapitalSpider(ZeSpider):

    name = 'cartacapital'
    allowed_domains = ['cartacapital.com.br', 'cartaeducacao.com.br']
    parses = [{
        "ze.items.creativework.ArticleItem": {
            "fields": { 
                "name": [ 
                    "[itemprop=name]::text", 
                    ".documentFirstHeading::text" 
                ], 
                "image": [ 
                    "[itemprop=image]::attr(content)", 
                    "[property='og:image']::attr(content)" 
                ], 
                "description": [ 
                    "[itemprop=description]::text", 
                    ".documentDescription::text" 
                ], 
                "author": [
                    "[itemprop=author]::text", 
                    ".documentAuthor a::text"
                ], 
                "datePublished": [
                    "[itemprop=datePublished]::text",
                    ".documentPublished::text"
                ], 
                "dateModified": [
                    "[itemprop=dateModified]::text"
                ], 
                "articleBody": [
                    "[itemprop=articleBody]",
                    "#content-core",
                    ".td-post-content",
                ], 
                "keywords": [
                    "[itemprop=keywords]::text", 
                    "[property='rnews:keywords']::text", 
                    "[rel='tag']::text", 
                    "#category .link-category::text" 
                ]
            }
        }
    }]
