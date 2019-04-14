from douyin.structures import Base
from douyin.utils.fetch import fetch
from douyin.config import topic2video_url, common_headers


class Fascinating(Base):

    def __init__(self, **kwargs):
        """
        init topic object
        :param kwargs:
        """
        super().__init__()
        self.id = kwargs.get('cid')
        self.aweme_id = kwargs.get(
                "category_cover_info", {}).get("aweme_id", "")
        self.type = kwargs.get('type')
        self.sub_type = kwargs.get('sub_type')
        self.name = kwargs.get('cha_name')
        self.desc = kwargs.get('desc')

    def __repr__(self):
        """
        music to str
        :return:
        """
        return '<Topic: <%s, %s>>' % (self.id, self.name)

    def videos(self, url, max=None, **kwargs):
        """
        get videos of topic
        :return:
        """
        return []

    def video(self, url, max=None, **kwargs):
        """
        get videos of topic
        :return:
        """
        from douyin.utils.tranform import data_to_video
        if max and not isinstance(max, int):
            raise RuntimeError('`max` param must be int')

        query = {
            'device_id': '58097798460',
            'ch_id': self.id,
            'count': '18',
            'aid': '1129'
        }
        query = kwargs.get("params", query)
        query["aweme_ids"] = "[%s]" % self.aweme_id
        # define cursor
        # query['cursor'] = str(offset)
        result = fetch(url, params=query, headers=kwargs.get("headers", common_headers), verify=False)
        aweme_list = result.get("aweme_details", [])
        item = aweme_list[0] if aweme_list else {}
        if not item:
            return
        v = data_to_video(item)
        return v
