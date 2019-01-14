from douyin.utils import fetch
from douyin.config import music_list_url, common_headers
from douyin.utils.tranform import data_to_music, data_to_topic
from douyin.structures.hot import HotTrend
from douyin.utils.common import parse_datetime
from douyin.structures import MusicList


# define trend query params
query = {
    'version_code': '2.9.1',
    'count': '10',
}


def mclist(url=music_list_url, mc_name="", **kwargs):
    """
    get trend result
    :return:
    """
    # https://pastebin.com/pu06WqkQ
    result = fetch(url, **kwargs)
    category_list = result.get('music_list')
    datetime = parse_datetime(result.get('extra', {}).get('now'))
    final = []
    count = result["cursor"]
    offset = kwargs.get("offset", 0)
    has_more = result["has_more"]
    mc_id = result["mc_info"]["mc_id"]
    for item in category_list:
        # process per category
        item["create_time"] = datetime
        item["owner_nickname"] = item["author"]
        item["music_type"] = mc_name
        # mc = McList(**item)
        data = data_to_music(item)
        final.append(data)
    offset += count
    return MusicList(datetime=datetime, data=final, count=count,
                     offset=offset, has_more=has_more, mc_id=mc_id)
