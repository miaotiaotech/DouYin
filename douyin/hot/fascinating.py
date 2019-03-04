from douyin.utils import fetch
from douyin.config import fascinating_url, common_headers
from douyin.utils.tranform import data_to_music, data_to_topic
from douyin.structures import FascinatingList, Fascinating
from douyin.utils.common import parse_datetime


# define trend query params
query = {
    'version_code': '2.9.1',
    'count': '10',
}


"""
dict_keys(['log_pb', 'category_list', 'extra', 'has_more', 'status_code',
    'status_msg', 'cursor', 'ning', 'ad_info'])
"""

"""
d["category_list"][0] =
{'challenge_info': {'user_count': 0,
  'author': {},
  'category_cover_info': {'aweme_id': '6663282270238936324',
   'cover': {'url_list': ['https://p3-dy.bytecdn.cn/aweme/300x400/177a00012b3e65a31ae32.jpeg',
     'https://p9-dy.bytecdn.cn/aweme/300x400/177a00012b3e65a31ae32.jpeg',
     'https://p22-dy.bytecdn.cn/aweme/300x400/177a00012b3e65a31ae32.jpeg'],
    'uri': '177a00012b3e65a31ae32'},
   'dynamic_cover': {'url_list': ['https://p3-dy.bytecdn.cn/obj/1b9d100076ed6741aa5fa',
     'https://p9-dy.bytecdn.cn/obj/1b9d100076ed6741aa5fa',
     'https://p1-dy.bytecdn.cn/obj/1b9d100076ed6741aa5fa'],
    'uri': '1b9d100076ed6741aa5fa'}},
  'cid': '1626969180319747',
  'is_commerce': False,
  'challenge_i18n': {},
  'is_pgcshow': False,
  'is_challenge': 0,
  'cha_name': '瞧我这张魔性的嘴',
  'schema': 'aweme://aweme/challenge/detail?cid=1626969180319747',
  'type': 0,
  'sub_type': 0,
  'desc': '青蛙🐸的嘴，魔性的美~ 戴上口罩能唱歌能晒牙，分分钟就出道！打开拍摄页面，在【热门】中选择“青蛙口罩”道具，一秒变成魔性的嘴😁'}}
"""

def fascinating(url=fascinating_url, **kwargs):
    """
    get trend result
    :return:
    """
    result = fetch(url, **kwargs)
    category_list = result.get('category_list')
    datetime = parse_datetime(result.get('extra', {}).get('now'))
    final = []
    count = result["cursor"]
    offset = kwargs.get("offset", 0)
    has_more = result["has_more"]
    for item in category_list:
        # process per category
        info = item.get("challenge_info", {})
        info["create_time"] = datetime
        # mc = McList(**item)
        data = Fascinating(**info)
        final.append(data)
    offset += count
    return FascinatingList(datetime=datetime, data=final, count=count,
                     offset=offset, has_more=has_more)
