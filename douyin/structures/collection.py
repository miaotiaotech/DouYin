from douyin.structures import Base


class Collection(Base):

    def __init__(self, **kwargs):
        """
        init collection object
        :param kwargs:
        """
        super().__init__()
        self.mc_id = kwargs.get('mc_id')
        self.aweme_cover = kwargs.get('aweme_cover')
        self.id_str = kwargs.get('id_str')
        self.mc_name = kwargs.get('mc_name')
        self.is_hot = kwargs.get('is_hot')
        self.cover = kwargs.get('cover')
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.create_time = kwargs.get('create_time')

    def __repr__(self):
        """
        collection to str
        :return:
        """
        return '<Collection: <%s, %s>>' % (self.name, self.mc_id)
