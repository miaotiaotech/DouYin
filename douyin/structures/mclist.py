from douyin.structures import Base
from douyin.utils.fetch import fetch
from douyin.config import music_list_url, common_headers


class Mclist(Base):

    def __init__(self, **kwargs):
        """
        init topic object
        :param kwargs:
        """
        super().__init__()
        mc_info = kwargs.get('mc_info', {})
        self.has_more = kwargs.get("has_more", 0)
        self.cursor = kwargs.get("cursor", 30)
        self.offset = kwargs.get("offset", 0)
        self.id = mc_info.get("mc_id")
        self.aweme_cover = mc_info.get('aweme_cover', {}).get("url_list")
        self.cover = mc_info.get('cover', {}).get("url_list")
        self.name = mc_info.get('name')
        self.is_hot = mc_info.get('is_hot')

    def __repr__(self):
        """
        music to str
        :return:
        """
        return '<MusicList: <%s, %s>>' % (self.id, self.name)

    def musics(self, url=music_list_url, **kwargs):
        """
        get musics by class
        :return:
        """
        from douyin.utils.tranform import data_to_music
        query = kwargs.get("params", {})
        offset, count = 0, 0
        # define cursor
        query['cursor'] = str(offset)
        result = fetch(url, params=query, headers=common_headers, verify=False)
        mlist = []
        aweme_list = result.get('aweme_list', [])
        for item in aweme_list:
            item["music_type"] = self.name
            music = data_to_music(item)
            mlist.append(music)
        # next page
        if result.get('has_more'):
            offset += 18
        return mlist
