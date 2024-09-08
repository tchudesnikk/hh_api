

class UserSetting:
    """
    Класс для хранения настроек пользователя по поиску
    """

    __solid__ = ('search_query', 'top_n', 'salary_min', 'salary_max', 'keywords', 'area')

    def __init__(self, search_query):
        self.__search_query = search_query
        self.__top_n = 10
        self.__salary = {'salary_min': 0, 'salary_max': 0}
        self.__salary_min = 0
        self.__salary_max = 0
        self.__keywords = []
        self.__area = ''

    @classmethod
    def create_new_object(cls, search_query):
        return cls(search_query)

    @staticmethod
    def check_for_number(user_value) -> int:
        try:
            value = int(user_value)
        except ValueError:
            value = 0
        return value

    @property
    def search_query(self):
        return self.__search_query

    @search_query.setter
    def search_query(self, search_query):
        self.__search_query = search_query

    @property
    def top_n(self):
        return self.__top_n

    @top_n.setter
    def top_n(self, top_n):
        self.__top_n = top_n

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary_range: str):
        if salary_range.strip() == '':
            self.__salary['salary_min'] = 0
            self.__salary['salary_max'] = 0
        else:
            salary = salary_range.split(' ')
            self.__salary['salary_min'] = self.check_for_number(salary[0])
            self.__salary['salary_max'] = self.check_for_number(salary[1])

    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keyword):
        self.__keywords.extend(keyword)

    @keywords.deleter
    def keywords(self):
        self.__keywords = []

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area
