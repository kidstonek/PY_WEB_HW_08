from random import randint

from faker import Faker

fake_info = Faker('uk_UA')
# іві
# print(dir(fake_info), end='\\n')
# b = ['Вища матиматика', 'Тригонометрія', 'Фізика трердого тіла', 'Фізкультура']
# for i in range(5):
#     x = b[randint(0, 2)]
#     print(x)
# randint()
# print(fake_info.user_name())
# gp = ['Фин-01', "ПЗ-04", "ИЛ-05", "ФІН-21"]
# for i in range(5):
#     x = gp[randint(0, 3)]
#     print(x, i)
# # randint()
# # print(fake_info.user_name())
# print(fake_info.ripe_id())

for i in range(20):
    for j in range(5):
        print(i+1, j+1)