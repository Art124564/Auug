class Coffee:
    def __init__(self, ingredient=None):
        if ingredient != '':
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print('Кофе c ',self.ingredient)
        else:
            print('Обычное кофе')


drink1 = Coffee()
drink2 = Coffee('молоко')
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()


