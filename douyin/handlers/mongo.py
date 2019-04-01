from douyin.handlers import Handler
from motor.motor_asyncio import AsyncIOMotorClient
from douyin.structures import *


SCRAPY_SOURCE = {"douyin": 2, "quanmin": 3}


class MongoHandler(Handler):

    def __init__(self, conn_uri=None, db='douyin'):
        """
        init save folder
        :param folder:
        """
        super().__init__()
        if not conn_uri:
            conn_uri = 'localhost'
        self.client = AsyncIOMotorClient(conn_uri)
        self.db = self.client[db]

    async def process(self, obj, **kwargs):
        """
        download to file
        :param url: resource url
        :param name: save name
        :param kwargs:
        :return:
        """
        query = {'id': obj.id}
        collection_name = 'default'
        if isinstance(obj, Video):
            collection_name = 'videos'
        elif isinstance(obj, Music):
            collection_name = 'musics'
        if collection_name == "musics" and not obj.play_url:
            print('Do not save %s into MongoDB for missing play url.'
                    % collection_name)
            return
        if collection_name == "musics" and not obj.name:
            print('Do not save %s into MongoDB for missing name.'
                    % collection_name)
            return
        if collection_name == 'musics' and obj.source == SCRAPY_SOURCE["quanmin"]:
            query = {'name': obj.name}
        collection = self.db[collection_name]
        # save to mongodb
        print('Saving', obj, 'to mongodb...')
        if await collection.update_one(query, {'$set': obj.json()}, upsert=True):
            print('Saved', obj, 'to mongodb successfully')
        else:
            print('Error occurred while saving', obj)
