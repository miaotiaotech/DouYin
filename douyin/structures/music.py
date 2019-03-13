from douyin.structures import Base
from douyin.utils.fetch import fetch
from douyin.config import music2video_url, common_headers


class Music(Base):
    
    def __init__(self, **kwargs):
        """
        music init args
        :param kwargs:
        """
        super().__init__()
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.cover_url = kwargs.get('cover_url')
        self.play_url = kwargs.get('play_url')
        self.owner_id = kwargs.get('owner_id')
        self.owner_name = kwargs.get('owner_name')
        self.hot_count = kwargs.get('hot_count')
        self.music_type = kwargs.get('music_type')
        self.source = kwargs.get('source', "douyin")
    
    def __repr__(self):
        """
        music to str
        :return:
        """
        return '<Music: <%s, %s>>' % (self.id, self.name)
    
    def videos(self, url, max=None, **kwargs):
        """
        get videos of topic
        :return:
        """
        if max and not isinstance(max, int):
            raise RuntimeError('`max` param must be int')
        from douyin.utils.tranform import data_to_video
        query = {
            'device_id': '33333333',
            'music_id': self.id,
            'count': '18',
        }
        offset, count = 0, 0
        query = kwargs.get("params", query)
        while True:
            # define cursor
            query['cursor'] = str(offset)
            result = fetch(url, params=query, headers=kwargs.get("headers", common_headers), verify=False)
            aweme_list = result.get('aweme_list', [])
            for item in aweme_list:
                video = data_to_video(item)
                count += 1
                yield video
                if max and count >= max:
                    return
            # next page
            if result.get('has_more'):
                offset += 18
            else:
                break
