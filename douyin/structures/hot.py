import collections

HotSearch = collections.namedtuple('HotSearch', ['datetime', 'data'])
HotVideo = collections.namedtuple('HotVideo', ['datetime', 'data'])
HotEnergy = collections.namedtuple('HotVideo', ['datetime', 'data'])
HotMusic = collections.namedtuple('HotMusic', ['datetime', 'data'])
HotTrend = collections.namedtuple('HotTrend', ['datetime', 'data', 'count', 'offset'])
MusicCollection = collections.namedtuple('MusicCollection', ['datetime', 'data', 'count', 'offset', "has_more"])
MusicList = collections.namedtuple('MusicList', ['datetime', 'data', 'count', 'offset', "has_more", "mc_id"])
FascinatingList = collections.namedtuple('FascinatingList', ['datetime', 'data', 'count', 'offset', "has_more"])
