from scrapy import Item, Field
from scrapy.loader import ItemLoader as ScrapyItemLoader
from scrapy.loader.processors import Join, TakeFirst, MapCompose
from ze.processors.article import ArticleProcessor
from ze.processors.common import CommonProcessor
from ze.processors.html import CleanHTML
from ze.processors.schema import AuthorProcessor

class ItemLoader(ScrapyItemLoader):
    
    def get_collected_values(self, field_name):
        return (self._values[field_name]
                if field_name in self._values
                else self._values.default_factory())

    def add_fallback_css(self, field_name, css, *processors, **kw):
        if not any(self.get_collected_values(field_name)):
            self.add_css(field_name, css, *processors, **kw)

    def add_fallback_xpath(self, field_name, css, *processors, **kw):
        if not any(self.get_collected_values(field_name)):
            self.add_xpath(field_name, css, *processors, **kw)
    
    def load_item(self):
        item = self.item
        
        for field_name in tuple(self._values):
            value = self.get_output_value(field_name)
            if value is not None:
                item[field_name] = value
        
        for field_name in self.item.fields:
            default_value = self.item.fields[field_name].get('default')
            if not item.get(field_name) and default_value:
                item[field_name] = self.item.fields[field_name].get('default')

        return item


class ThingItem(Item):
    
    additionalType = Field(
        output_processor=TakeFirst(),
    )
    alternateName = Field(
        output_processor=TakeFirst(),
    )
    description = Field(
        output_processor=TakeFirst(),
        schemas={
            'avro': {
                'field_type': 'STRING', 
            }, 
        }
    )
    disambiguatingDescription = Field(
        output_processor=TakeFirst(),
    )
    identifier = Field(
        output_processor=TakeFirst(),
    )
    image = Field(
        default=['null'], 
        schemas={
            'avro': {
                'field_type': 'STRING', 
            }, 
        }
    )
    mainEntityOfPage = Field(
        output_processor=TakeFirst(),
    )
    name = Field(
        output_processor=TakeFirst(),
        schemas ={
            'avro': {
                'field_type': 'STRING', 
            }, 
        }
    )
    potentialAction = Field(
        output_processor=TakeFirst(),
    )
    sameAs = Field(
        output_processor=TakeFirst(),
        # schemas = {
        #     'avro': {
        #         'field_type': 'STRING',
        #         'mode': 'REPEATED',
        #     }, 
        # }
    )
    url = Field(
        output_processor=TakeFirst(),
        schemas={
            'avro': {
                'field_type': 'STRING', 
            }, 
        }
    )


class CreativeWorkItem(ThingItem):
    about = Field(
        # schemas={
        #     'avro': {
        #         'field_type': 'STRING', 
        #         'mode': 'REPEATED', 
        #     }, 
        # }
    )
    accessMode = Field()
    accessModeSufficient = Field()
    accessibilityAPI = Field()
    accessibilityControl = Field()
    accessibilityFeature = Field()
    accessibilityHazard = Field()
    accessibilitySummary = Field()
    accountablePerson = Field()
    aggregateRating = Field()
    alternativeHeadline = Field()
    associatedMedia = Field()
    audience = Field()
    audio = Field()
    author = Field(
        default=[{'type': None, 'name': None}], 
        input_processor=MapCompose(
            ArticleProcessor.process_authors
        ), 
        output_processor=AuthorProcessor(),
        schemas = {
            'avro': {
                'field_type': 'RECORD', 
                'mode': 'REPEATED', 
                'fields': ({
                    'name': 'name', 
                    'field_type': 'STRING', 
                },{
                    'name': 'type', 
                    'field_type': 'STRING', 
                })
            }, 
        }
    )
    award = Field()
    character = Field()
    citation = Field()
    comment = Field()
    commentCount = Field(
        output_processor = TakeFirst(),
        # schemas={
        #     'avro': {
        #         'field_type': 'INTEGER', 
        #     }, 
        # }
    )
    contentLocation = Field()
    contentRating = Field()
    contributor = Field()
    copyrightHolder = Field()
    copyrightYear = Field()
    creator = Field()
    dateCreated = Field(
        # schemas = {
        #     'avro': {
        #         'field_type': 'TIMESTAMP', 
        #     }, 
        # }
    )
    dateModified = Field(
        input_processor=MapCompose(
            CommonProcessor.process_date_time
        ),
        output_processor=TakeFirst(),
        # schemas = {
        #     'avro': {
        #         'field_type': 'TIMESTAMP', 
        #     }, 
        # }
    )
    datePublished = Field(
        input_processor=MapCompose(
            CommonProcessor.process_date_time
        ),
        output_processor=TakeFirst(),
        schemas={
            'avro': {
                'field_type': 'TIMESTAMP',
            }
        }
    )
    discussionUrl = Field()
    editor = Field()
    educationalAlignment = Field()
    educationalUse = Field()
    encoding = Field()
    exampleOfWork = Field()
    fileFormat = Field()
    funder = Field()
    genre = Field()
    hasPart = Field()
    headline = Field()
    inLanguage = Field()
    interactionStatistic = Field(
        # schemas={
        #     'avro': {
        #         'field_type': 'RECORD',
        #         'mode': 'REPEATED',
        #         'fields': [{ 
        #                 'name': 'interactionType',
        #                 'field_type': 'STRING',
        #             },{
        #                 'name': 'userInteractionCount',
        #                 'field_type': 'INTEGER',
        #             },{ 
        #                 'name': 'type',
        #                 'field_type': 'STRING',
        #             },{
        #                 'name': 'interactionService',
        #                 'field_type': 'RECORD',
        #                 'mode': 'REPEATED',
        #                 'fields': [{ 
        #                         'name': 'url',
        #                         'field_type': 'STRING',
        #                     },{ 
        #                         'name': 'name',
        #                         'field_type': 'STRING',
        #                     },{ 
        #                         'name': 'type',
        #                         'field_type': 'STRING',
        #                 }]
        #         }]
        #     }
        # }
    )
    interactivityType = Field()
    isAccessibleForFree = Field()
    isBasedOn = Field()
    isFamilyFriendly = Field()
    isPartOf = Field()
    keywords = Field(
        input_processor=MapCompose(
            ArticleProcessor.process_keywords
        ),
        output_processor=Join(','),
        schemas={
            'avro': {
                'field_type': 'STRING'
            }
        }
    )
    learningResourceType = Field()
    license = Field()
    locationCreated = Field()
    mainEntity = Field()
    material = Field()
    mentions = Field()
    offer = Field()
    position = Field()
    producer = Field()
    provider = Field()
    publication = Field()
    publisher = Field()
    publishingPrinciples = Field()
    recordedAt = Field()
    releasedEvent = Field()
    review = Field()
    schemaVersion = Field()
    sourceOrganization = Field()
    spatialCoverage = Field()
    sponsor = Field()
    temporalCoverage = Field()
    text = Field()
    thumbnailUrl = Field()
    timeRequired = Field()
    translator = Field()
    typicalAgeRange = Field()
    version = Field()
    video = Field()
    workExample = Field()
