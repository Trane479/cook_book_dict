
from pprint import pprint


# def txt_to_dict():
#     cook_book_dict = {}
#     while True:
#         dish = cook_book.readline().strip()
#         iteration_string = cook_book.readline()
#
#         i = 0
#         cook_book_dict[dish] = []
#         while i < int(iteration_string):
#
#             ingredient_string = (cook_book.readline().strip().split('|'))
#             ingredient = ingredient_string[0]
#             quantity = ingredient_string[1]
#             measure = ingredient_string[2]
#             cook_book_dict[dish].append({'ingredient name': ingredient, 'quantity': quantity, 'measure': measure})
#             i += 1
#         cook_book.readline()
#         if not dish:
#             break
#     return cook_book_dict


def txt_do_dict():
    with open('cook_book.txt') as cook_book:

        cook_book_dict = {}
        while True:
            dish = cook_book.readline().strip()  # Первая строка
            iteration_string = cook_book.readline()  # Вторая строка

            i = 0
            cook_book_dict[dish] = []
            while i < int(iteration_string):  # Цикл который читает n строк

                ingredient_string = (cook_book.readline().strip().split('|'))
                ingredient = ingredient_string[0]
                quantity = ingredient_string[1]
                measure = ingredient_string[2]
                cook_book_dict[dish].append({'ingredient name': ingredient, 'quantity': quantity, 'measure': measure})
                i += 1
            cook_book.readline()
            it = 'iteration'
            if i == 5:
                break
            return cook_book_dict


def get_shop_list(dishes, person):
    cook_book_dict = txt_do_dict()
    ingredient_to_buy = []
    for dish in cook_book_dict:
        if dish in dishes:
            for ingredient in cook_book_dict[dish]:
                ingredient['quantity'] = int(ingredient['quantity']) * person
                print(ingredient)

get_shop_list(['Омлет', 'Фахитос'], 2)


