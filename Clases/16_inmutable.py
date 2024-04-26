items = [
    {
        'product' : 'camisa',
        'price' : 100,
    },
    {
        'product' : 'pantalones',
        'price' : 300
    },
    {
        'product' : 'pantalones 2',
        'price' : 200
    }
]

def add_taxes(dict):
    new_dict = dict.copy()
    new_dict['taxes'] = new_dict['price'] * 0.19
    return new_dict

new_items = list(map(add_taxes, items))
print (new_items)
print (items)

