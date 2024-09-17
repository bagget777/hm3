# hm1
night = 1,2,3,4,5,6
morning = 7,8,9,10,11,12
dinner = 13,14,15,16,17,18
evening = 19,20,21,22,23,00

time = int(input('Введите час: '))

if time in night:
  print(f'Время {time} Ночи')
elif time in morning:
  print(f'Время {time} утра')
elif time in dinner:
  print(f'Время {time} дня')
elif time in evening:
  print(f'Время {time} вечера')
else:
  print('Такого времени не существует')
  
# hm2

balls = int(input('Введите ваши баллы: '))
if 200 >= balls >= 90:
  print(f'Вы набрали {balls} поздравляем вы успешно сдали предмет на отлично')
elif 90 >= balls >= 80:
  print(f'Вы набрали {balls} поздравляем вы успешно сдали предмет на хорошо')
elif 80 >= balls >= 70:
  print(f'Вы набрали {balls} поздравляем вы успешно сдали предмет на удовлетворительно')
elif 70 >= balls >= 60:
  print(f'Вы набрали {balls} поздравляем вы успешно сдали предмет на неудовлетворительно')
elif 60 >= balls >= 0:
  print(f'Вы набрали {balls} вам нужно пересдать предмет')
else: print('ошибка')
  
# dop hm 1

one_items = [1,2,3,4,5]
two_items = [6,7,8,9,10]

item_praise_1 = 100
item_praise_2 = 200
item_praise_3 = 300

delivery_praise_1 = 0
delivery_praise_2 = 200
delivery_praise_3 = 300

items = int(input('Введите вес товара: '))
if items in one_items:
  items_praise = item_praise_1
  print(f'Ваш товар весит {items}kg его цена {item_praise_1} сом')
elif items in two_items:
  items_praise = item_praise_2
  print(f'Ваш товар весит {items}kg его цена {item_praise_2} сом')
else:
  items_praise = item_praise_3
  print(f'Ваш товар весит {items}kg его цена {item_praise_3} сом')

print(f'Приветствуем вас ваш товар весит {items},\nи его доставка зависит от вас\nу нас имеется три вида доставки\nобычная варьируется от 3-5 дней,\nстоимость услуги бесплатно\nэкспресс доставка варьируется от 2-3 дней,\nстоимость услуги 200 сом\nсверх-экспресс доставка варьируется от 1 дня\nстоимость услуги 300 сом\nчтобы выбрать обычную доставку введите: 1\nчтобы выбрать экспресс доставку введите: 2\nчтобы выбрать сверх-экспресс доставку введите: 3')
delivery = int(input('Введите выбор доставки от 1 до 3: '))
if delivery == 1:
  delivery_praise = delivery_praise_1
  print(f'ваш товар {items}kg будет отправлен обычной доставкой цена {delivery_praise_1} сомов')
elif delivery == 2:
  delivery_praise = delivery_praise_2
  print(f'ваш товар {items}kg будет отправлен экспресс доставкой цена {delivery_praise_2} сомов')
elif delivery == 3:
  delivery_praise = delivery_praise_3
  print(f'ваш товар {items}kg будет отправлен сверх-экспресс доставкой {delivery_praise_3}сомов')

if items_praise == item_praise_1 and delivery_praise == item_praise_1:
    print(f'{item_praise_1}+{delivery_praise_1}={item_praise_1+delivery_praise_1} это общая сумма')

elif items_praise == item_praise_1 and delivery_praise == item_praise_2:
    print(f'{item_praise_1}+{delivery_praise_2}={item_praise_1+delivery_praise_2} это общая сумма')

elif items_praise == item_praise_1 and delivery_praise == item_praise_3:
    print(f'{item_praise_1}+{delivery_praise_3}={item_praise_1+delivery_praise_3} это общая сумма')

elif items_praise == item_praise_2 and delivery_praise == item_praise_1:
    print(f'{item_praise_2}+{delivery_praise_1}={item_praise_2+delivery_praise_1} это общая сумма')

elif items_praise == item_praise_2 and delivery_praise == item_praise_2:
    print(f'{item_praise_2}+{delivery_praise_2}={item_praise_2+delivery_praise_2} это общая сумма')

elif items_praise == item_praise_2 and delivery_praise == item_praise_3:
    print(f'{item_praise_2}+{delivery_praise_3}={item_praise_2+delivery_praise_3} это общая сумма')

elif items_praise == item_praise_3 and delivery_praise == item_praise_1:
    print(f'{item_praise_3}+{delivery_praise_1}={item_praise_3+delivery_praise_1} это общая сумма')

elif items_praise == item_praise_3 and delivery_praise == item_praise_2:
    print(f'{item_praise_3}+{delivery_praise_2}={item_praise_3+delivery_praise_2} это общая сумма')

elif items_praise == item_praise_3 and delivery_praise == item_praise_3:
    print(f'{item_praise_3}+{delivery_praise_3}={item_praise_3+delivery_praise_3} это общая сумма')

# dop hm 2 

a = int(input('Введите число: '))
b = int(input('Введите число: '))
if a > b:
  print(f'число a={a} больше числа b={b}')
elif a < b:
  print(f'число b={b} больше числа a={a}')
elif a == b:
  print(f'число a={a} равен числу b={b}')

# dop hm 3

numb = int(input('Введите число: '))
if numb == 0:
  print(f'число {numb} это ноль')
elif numb > 0:
  print(f'число {numb} положительное число')
elif numb < 0:
  print(f'число {numb} отрицательный')
  
# dop hm 4

numb_1 = int(input('Введите первое число: '))
numb_2 = int(input('Введите второе число: '))
numb_3 = int(input('Введите третье число: '))

if numb_1 == numb_2 == numb_3:
  print(f'{numb_1} равен {numb_2} равен {numb_3}')
elif numb_1 == numb_2:
  print(f'{numb_1} = {numb_2} а {numb_3} не равен')
elif numb_1 == numb_3:
  print(f'{numb_1} = {numb_3} а {numb_2} не равен')
elif numb_2 == numb_3:
  print(f'{numb_2} = {numb_3} а {numb_1} не равен')
else:
  print('среди чисел нету равных')
  
# dop hm 5

degree = int(input('Введите градус в цифрах: '))
if degree > 25:
  print(f'на улице жарко тёплая одежда не нужна и на улице {degree} градусов')
elif 25 >= degree >= 15:
  print(f'на улице чуть прохладно одень лёгкую курточку и на улице {degree} градусов')
elif degree < 15:
  print(f'на улице холодно целых {degree} градусов оденься теплее ')