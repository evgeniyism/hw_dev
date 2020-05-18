def main(dishes, quantity):
    book = ingredients()
    output = {}
    for dish in dishes:
        for item in book[dish]:
            item_quantity = int(item['quantity']) * quantity
            shopping_cart = {item['ingredient_name']:{'measure': item['measure'], 'quantity': item_quantity}}
            if item['ingredient_name'] in output.keys():
               output[item['ingredient_name']]['quantity'] = output[item['ingredient_name']]['quantity'] + item_quantity
            else:
                output.update(shopping_cart)
    for i in output.items():
        print(i)
    return (output)

def sorting():
    counter = []
    with open('reciepes.txt', 'r', encoding='utf8') as info:
        for line in info:
            newline = line.strip()
            counter.append(newline)
    return(counter)

def ingredients():
    book = {}
    counter = sorting()
    for element in counter:
        if element.isdigit() == True and len(element) == 1:
            idx = int(counter.index(element))
            key = counter[idx-1]
            value = []
            check = 1
            for i in range(int(element)):
                separate = counter[idx+check].split(sep = '|')
                separate = [i.strip() for i in separate]
                value.append({'ingredient_name': separate[0], 'quantity': separate[1], 'measure': separate[2]})
                check +=1
            ingredients_to_add = {key:value}
            book.update(ingredients_to_add)
            counter.remove(element)
    return (book)


main(['Омлет', 'Фахитос'], 2)
