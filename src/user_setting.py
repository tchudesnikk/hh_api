

class UserSetting:
    """
    Класс для хранения настроек пользователя по поиску
    """

    __solid__ = ('search_query', 'top_n', 'salary_min', 'salary_max', 'keywords', 'area')

    def __init__(self):
        self.__search_query = ''
        self.__top_n = 0
        self.__salary_min = 0
        self.__salary_max = 0
        self.__keywords = []
        self.__area = ''

    @classmethod
    def create_new_object(cls):
        return cls()

    @property
    def search_query(self):
        return self.__search_query

    @search_query.setter
    def search_query(self, search_query):
        self.__search_query = search_query

    @property
    def __top_n(self):
        return self.__search_query

    @__top_n.setter
    def __top_n(self, top_n):
        self.__top_n = top_n

    @property
    def salary_min(self):
        return self.__salary_min

    @salary_min.setter
    def salary_min(self, salary_min):
        self.__salary_min = salary_min

    @property
    def salary_max(self):
        return self.__salary_max

    @salary_max.setter
    def salary_max(self, salary_max):
        self.__salary_max = salary_max

    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keyword):
        self.__keywords.append(keyword)

    @keywords.deleter
    def keywords(self):
        self.__keywords = []

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area
