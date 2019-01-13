import datetime

from douyin.structures import *
from douyin.config import music_collection_url
from douyin.structures import MusicCollection
from douyin.structures import Collection
from douyin.utils import fetch
from douyin.utils.common import parse_datetime
# from douyin.utils.tranform import data_to_video


def collection(url=music_collection_url, **kwargs):
    """
    get music collection result
    :return: MusicCollection object
    """
    # https://pastebin.com/G4s7Ca7i
    result = fetch(url, **kwargs)
    # process json data
    dt = datetime.datetime.now()
    collection_list = result.get('mc_list', [])
    collections = []
    count = result["cursor"]
    offset = kwargs.get("offset", 0)
    has_more = result["has_more"]
    for item in collection_list:
        item["create_time"] = dt
        collection = Collection(**item)
        collections.append(collection)
    # construct MusicCollection object and return
    offset += count
    return MusicCollection(datetime=dt, data=collections, count=count,
                           offset=offset, has_more=has_more)
