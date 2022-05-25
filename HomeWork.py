from pprint import pprint
import os

def open_file_c_dict(file):
    cook_book = {}
    with open(file, encoding='UTF-8') as cook_book_file:
        for data in cook_book_file:
            meal_name = data
            quantity = int(cook_book_file.readline())
            book_ingridients = []
            for i in range(quantity):
                meals = {}
                data_f = cook_book_file.readline().strip().split('|')
                meals['ingridient name'] = data_f[0]
                meals['quantity'] = data_f[1]
                meals['measure'] = data_f[2]
                book_ingridients.append(meals)
            cook_book[meal_name.strip()] = book_ingridients
            cook_book_file.readline()
    return cook_book
pprint(open_file_c_dict('recipes.txt'))



def get_shop_list_by_dishes(dishes, person_count):
    cook_book = open_file_c_dict('recipes.txt')
    result = {}
    for meal_name in dishes:
        for book_ingr in cook_book[meal_name]:
            ingridient_name = book_ingr['ingridient name']
            quantity = book_ingr['quantity']
            measure = book_ingr['measure']
            if ingridient_name in result.keys():
                result[ingridient_name]['quantity'] += int(quantity) * person_count
            else:
                result[ingridient_name] = {'quantity': int(quantity) * person_count, 'measure': measure}
    return result

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))



def files_consolidate_func(consolidate_file_name):
    files = os.listdir(os.path.join(os.getcwd(), 'sorted'))
    consolidate_dict = {}
    for file in files:
        full_path_r_files = os.path.join(os.getcwd(), 'sorted', file)
        with open(full_path_r_files, encoding='UTF-8') as files_data:
            quiantity_lines = int(len(files_data.readlines()))
            files_data.seek(0)
            consolidate_dict[file] = quiantity_lines
            sort_dict = sorted(consolidate_dict, key=consolidate_dict.get)
    with open(consolidate_file_name, 'w', encoding='UTF-8') as result:
        for f, q in consolidate_dict.items():
            with open(os.path.join(os.getcwd(), 'sorted', f), encoding='UTF-8') as data_f:
                result.write(f + '\n' + str(q) + '\n')
                for data in data_f:
                    result.write(data)
                result.write('\n')

files_consolidate_func('result.txt')