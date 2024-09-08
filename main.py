from src.user_setting import UserSetting


platforms = ["HeadHunter"]
search_query = input("Введите поисковый запрос: ")
user_setting = UserSetting.create_new_object(search_query)
user_setting.top_n = int(input("Введите количество вакансий для вывода в топ N: "))
user_setting.keywords = input("Введите ключевые слова для фильтрации вакансий: ").split()
salary_range = input("Введите диапазон зарплат через пробел (пример: 10000 15000): ").split() # Пример: 100000 - 150000
user_setting.salary = salary_range

#filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#sorted_vacancies = sort_vacancies(ranged_vacancies)
#top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#print_vacancies(top_vacancies)