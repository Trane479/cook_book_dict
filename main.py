from pprint import pprint


def txt_do_dict():
    with open('cook_book.txt') as cook_book:

        cook_book_dict = {}
        while True:
            dish = cook_book.readline().strip()
            iteration_string = cook_book.readline()

            i = 0
            cook_book_dict[dish] = []
            while i < int(iteration_string):
                ingredient_string = (cook_book.readline().strip().split('|'))
                ingredient = ingredient_string[0]
                quantity = ingredient_string[1]
                measure = ingredient_string[2]
                cook_book_dict[dish].append({'ingredient name': ingredient, 'quantity': quantity, 'measure': measure})
                i += 1
            cook_book.readline()
            if i == 5:
                break
    return cook_book_dict


# pprint(txt_do_dict())


def get_shop_list(dishes, person):
    cook_book_dict = txt_do_dict()
    ingredients_to_buy = {}
    for dish in dishes:
        if dish in cook_book_dict:
            for ingredient in cook_book_dict[dish]:
                # print(ingredient['ingredient name'])

                if ingredient['ingredient name'] not in ingredients_to_buy:
                    ingredients_to_buy[ingredient['ingredient name']] = {'measure': ingredient['measure'],
                                                                         'quantity': int(ingredient['quantity'])}
                else:
                    ingredients_to_buy[ingredient['ingredient name']] = {'measure': ingredient['measure'],
                                                                         'quantity': int(ingredient['quantity']) +
                                                                                     int(ingredient['quantity'])}
    for ingredient in ingredients_to_buy:
        ingredients_to_buy[ingredient]['quantity'] = ingredients_to_buy[ingredient]['quantity'] * person
    return ingredients_to_buy


def main():
    pprint(get_shop_list(['Омлет', 'Омлет'], 2))


main()

