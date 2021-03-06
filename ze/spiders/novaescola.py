# -*- coding: utf-8 -*-

from ze.spiders import ZeSpider

class NovaEscolaSpider(ZeSpider):

    name = 'novaescola'
    allowed_domains = ['novaescola.org.br']
    parses = [{
        "ze.items.creativework.ArticleItem": {
            "fields": {
                "name": [
                    '[itemprop=headline]::text',
                    '.materia h1::text'
                ],
                "image": [
                    '[itemprop="image"] img::attr(src)',
                    '.image img::attr(src)'
                ],
                "description": [
                    '[itemprop=description]::attr(content)',
                    '[itemprop=description]::text',
                    '.resumo h2::text'
                ],
                "author": [
                    '[itemprop=author]::text',
                    '.autor-nome::text'
                ],
                "datePublished": [
                    '[itemprop=datePublished]::attr(content)',
                    '.data::text'
                ],
                "dateModified": [
                    '[itemprop=dateModified]::attr(content)'
                ],
                "articleBody": [
                    '[itemprop=articleBody]',
                    '.texto'
                ],
                "keywords": [
                    '[itemprop=keywords] a::text',
                    '[rel=tag]::text',
                    '[onclick*=montaURL]::text'
                ]
            }
        }
    }]
