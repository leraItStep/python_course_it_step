"""
В вашем распоряжении имеется вложенный список people, в котором хранятся имена и телефоны.
Ваша задача создать словарь при помощи генератора словарей,
в котором в качестве ключей будут храниться номера телефонов, а значениями будут имена владельцев.
Обязательно сохраните этот словарь в переменной phone_book.
"""
people = [
    ('Amy Smith', '694-322-8133'),
    ('Brian Shaw', '593-662-52-338'),
    ('Christian Sharp', '118-197-88-10'),
    ('Sean Schmidt', '97 22527521'),
    ('Thomas Long', '163.814.9938'),
    ('Joshua Willis', '+1-978-530-6971x601'),
    ('Ann Hoffman', '434.104.4302'),
    ('John Leonard', '(956)182-8435'),
    ('Daniel Ross', '870-365-8303x416'),
    ('Jacqueline Moon', '+1-757-865-4488x652'),
    ('Gregory Baker', '705-576-1122')
]

phone_book = {phone: name for name, phone in people}
print(phone_book)