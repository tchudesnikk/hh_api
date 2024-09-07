import requests
from abc import ABC, abstractmethod


class ConnectorHH(ABC):
    """
    Абстрактный класс для классов подключения по API
    """

    def __init__(self):
        self.__host = 'https://api.hh.ru'
        self.__headers = {'User-Agent': 'HH-User-Agent'}

    @property
    def host(self):
        return self.__host

    @property
    def headers(self):
        return self.__headers

    @staticmethod
    def check_status_code(status_code):
        if status_code == 200:
            return True
        else:
            return False

    @abstractmethod
    def load_info(self):
        pass


class GetVacations(ConnectorHH):
    """
    Класс для получения вакансий с API hh.ru
    """

    def __init__(self):
        super().__init__()
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.__url = f'{self.host}/vacancies'
        self.__keyword = ''
        self.vacancies = []

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def __str__(self):
        return f'Выполняет получение вакансий по пути: {self.url}'

    @property
    def url(self):
        return self.__url

    @property
    def keyword(self):
        return self.keyword

    @keyword.setter
    def keyword(self, keyword):
        self.keyword = keyword

    @keyword.deleter
    def keyword(self):
        self.keyword = None

    @property
    def path_request(self):
        return self.path_request

    @classmethod
    def create_new_class(cls, keyword):
        return cls()

    def load_info(self):
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


class GetAreas(ConnectorHH):
    """
    Класс для получения данных по зонам с hh.ru
    """

    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/areas'
        self.areas = []

    def load_info(self):
        response = requests.get(self.url, headers=self.headers)
        self.areas = response.json()
