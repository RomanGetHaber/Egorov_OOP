class Deal:
    a = 'введите значение'
    def __init__(self, title, data=a, time_deal=a, place=a, description=a):
        self.title = title
        self.data = data
        self.time_deal = time_deal
        self.place = place
        self.description = description

    def fill_deal(self):
        title = input('введите название сделки: ')
        self.title = title
        data = input('введите дату: ')
        self.data = data

november = Deal('November', '22.07.1987')

print(november.__dict__)