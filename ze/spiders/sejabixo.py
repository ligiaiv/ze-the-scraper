# -*- coding: utf-8 -*-
from . import ZeSpider


class SejaBixoSpider(ZeSpider):

    name = 'sejabixo'
    allowed_domains = ['sejabixo.com.br']
    items_refs = [{
        "item": "ze.items.creativework.ArticleItem",
        "fields": {
            "name": {
                "selectors": {
                    "css": [
                        "meta[property='og:title']::attr(content)",
                        "meta[name=title]::attr(content)",
                        '[itemprop=headline]::text',
                        '.materia h1::text'
                    ]
                }
            },
            "image": {
                "selectors": {
                    "css": [
                        "meta[property='og:image']::attr(content)",
                        "[itemprop='image'] img::attr(src)"
                    ]
                }
            },
            "description": {
                "selectors": {
                    "css": [
                        "meta[property='og:description']::attr(content)",
                        "meta[name=description]::attr(content)",
                        "[itemprop=description]::attr(content)",
                        "[itemprop=description]::text",
                        ".resumo h2::text"
                    ]
                }
            },
            "author": {
                "selectors": {
                    "css": [
                        "[itemprop=author]::text",
                        ".autor-nome::text"
                    ]
                }
            },
            "datePublished": {
                "selectors": {
                    "css": [
                        '[itemprop=datePublished]::attr(content)',
                        '.data::text',
                        'article div[align=center] strong::text',
                        'article i strong::text',
                        '"#content i strong"::text',
                        '.lrec1 i strong::text',
                    ]
                }
            },
            "dateModified": {
                "selectors": {
                    "css": [
                        "[itemprop=dateModified]::attr(content)"
                    ]
                }
            },
            "articleBody": {
                "selectors": {
                    "css": [
                        "[itemprop=articleBody]",
                        ".conteudo-materia",
                        "article"
                    ]
                }
            },
            "keywords": {
                "selectors": {
                    "css": [
                        "[itemprop=keywords] a::text",
                        "[rel=tag]::text",
                        "[onclick*=montaURL]::text"
                    ]
                }
            }
        }
    }]
