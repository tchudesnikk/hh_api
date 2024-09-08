import pytest


@pytest.fixture
def custom_settings_template():
    return {'search_query': 'developer Python',
            'top_n': 50,
            'salary': '10000 15000',
            'keywords': ['Python', 'developer', 'программист', 'разработчик'],
            'area': 'Россия'}
