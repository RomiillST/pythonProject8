class Somsa():
    def __init__(self, x,y,z):
        # Начинка
        # Тип сомсы
        # Вкус
        self.type = x
        self.filling = y
        self.mark = z

    def eating(self):
        print('Сомса съедена (┬┬﹏┬┬)')
        print('Она была: {}, с {}, {} из 10 по оценке критиков'.format(self.type, self.filling, self.mark))
    def sale(self):
        x = self.mark
        print('Сомса была продана за {} сум'.format(x*500))


ravshan = Somsa('TONDIR', 'GUSHT',8)
ravshan.eating()
ravshan.sale()