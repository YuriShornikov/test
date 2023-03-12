#1 задание
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def rus_list(geo_logs):
    geo_rus = []
    for geo_dict in geo_logs:
        for key, value in geo_dict.items():
            if value[1] == 'Россия':
                geo_rus.append(geo_dict)
    return geo_rus

rus_list(geo_logs)

def test_rus_list():
    res = rus_list(geo_logs)
    assert [
        {'visit1': ['Москва', 'Россия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ] == res

test_rus_list()

#2 задание
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]
       }

def geo_ids_get(ids):
    geo_ids = []
    for value in ids.values():
        geo_ids.append(value)
    return geo_ids

geo_ids_get(ids)

def test_geo_ids_get():
    for res_item, check_item in zip(
            geo_ids_get(ids),
            [[213, 213, 213, 15, 213], [54, 54, 119, 119, 119], [213, 98, 98, 35]]
    ):
        assert res_item == check_item

test_geo_ids_get()

#3 задание

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

def count_words(queries):

    result = []
    count_block = len(queries)
    count_words = []
    for i in queries:
        count = i.count(" ") + 1
        count_words.append(count)

    count_2 = round(count_words.count(2) * 100/ count_block)
    result.append(count_2)
    count_3 = round(count_words.count(3) * 100/ count_block)
    result.append(count_3)
    # print(f'количество запросов из 2 слов - {count_2}%')
    # print(f'количество запросов из 3 слов - {count_3}%')
    return result

count_words(queries)

def test_count_words():
    count_block = 7
    count_2 = round(3 * 100 / count_block)
    count_3 = round(4 * 100 / count_block)
    result = count_words(queries)
    for res_item, check_item in zip(
        result,
        [count_2, count_3]
    ):
        assert res_item == check_item


test_count_words()