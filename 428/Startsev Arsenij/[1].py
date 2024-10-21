import random
from datetime import datetime
#исходные данные(в порядке, в котором они указаны в задании):
# 1.предметы в школьном аттестате (не меньше 14), как словарь (dictionary) их названия и оценки:
grades_in_certificate = {
    "алгебра": 3,
    "химия": 3,
    "литература": 5,
    "биология": 4,
    "история": 5,
    "физика": 3,
    "геометрия": 3,
    "физкультура": 5,
    "обж": 5,
    "обществознание": 5,
    "информатика": 3,
    "черчение": 4,
    "рисование": 5,
    "музыка": 5}

#полное имя с фамилией и дату рождения любого актера из вестерна 1960х годов как кортеж (tuple):
#актер: Клин(или Клинтон) Иствуд (31.05.1930)
Western_actor_birthday = datetime(1930, 5, 31)
Western_actor = ("Clinton", "Eastwood", (Western_actor_birthday.year, Western_actor_birthday.month, Western_actor_birthday.day)) 

#список (list) из имени и фамилии, составленные случайно по таблице из самых популярных:
#Нижний Новгород
popular_names = ['Александр', 'Иван', 'Сергей', 'Дмитрий', 'Алексей','Андрей', 'Максим', 'Евгений', 'Михаил', 'Владимир']
popular_surnames = ['Иванов', 'Смирнов','Петров', 'Кузнецов', 'Волков', 'Соколов', 'Васильев', 'Белов', 'Морозов']
names_list = [(name, surname) for name in popular_names for surname in popular_surnames]
random.shuffle(names_list)

#имя из прилагательного и существительного, которое я бы дали своему домашнему тамандуа:
tamandya_name = "вольный бродяга" 
#конец исходных данных:
    
    #летим дальше 🚀

#действия:
#сначала все что связано с оценками в аттестате и предметами(1,3,4 задания):
#средняя оцена в аттестате(задание 1):
sred_znach = sum(grades_in_certificate.values()) / len(grades_in_certificate) 
print(f"Средняя оценка в аттестате: {sred_znach}")

#общая длина всех названий предметов(3 задание):
dlina = sum(len(grades_in_certificate) for grades_in_certificate in grades_in_certificate)
print(f"Общая длина всех названий предметов: {dlina}")

#уникальные буквы в названиях предметов(4 задание):
unical_bykvi = set("".join(grades_in_certificate.keys()))
print(f"Уникальные буквы в названиях предметов: {unical_bykvi}")

    #летим дальше 🚀

#работа с именами (2,5,6,8)
#вывод уникальных имен среди взятых из таблицы популярных(2 задание):
print("Список имен и фамилий:", names_list)
unique_names = list(set([name for name, _ in names_list]))
print(f"Уникальные имена: {unique_names}")

#имя домашнего тамандуа в бинарном виде (5 задание)
binary_tamandya_name = "".join(format(ord(char), '08b') for char in tamandya_name)
print(f"Имя домашнего тамандуа в бинарном виде: {binary_tamandya_name}")

#количество дней от даты рождения актера вестерна до текущей даты
days_since_birth = (datetime.now() - Western_actor_birthday).days
print(f"Количество дней со дня рождения актера до сегодняшней даты: {days_since_birth}")

#замена по индексу имени на имя китайского императора (получилось 51, Цзи Юй (ну есть шанс что я поститал плохо))(8 задание)
index = int(input("Введите индекс имени в списке популярных имен и фамилий для замены на имя китайского императора: "))
names_list.sort()
names_list[index] = ("Цзи", "Юй")
print(f"Имя китайского императора династии Чжоу для замены в списке имён: {names_list[index]}")
print("Список имён с замененным именем на имя китайского императора", names_list)


    #летим дальше 🚀

# FIFO очередь для стройматериалов (7 задание)
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)

    def get_all_items(self):
        return self.items

def main():
    queue = Queue()
    print("Введите названия стройматериалов (для завершения введите 'стоп'): ")
    
    while True:
        item = input()
        if item.lower() == 'стоп':
            break
        queue.enqueue(item)
    
    print("Список стройматериалов в очереди: ")
    for material in queue.get_all_items():
        print(material)

if __name__ == "__main__":
    main()

#создать и напечатать связный список странных названий населенных пунктов любым способом 
#(например, как словарь, где ключ - имя, а значение -- ссылка на индекс следующего элемента), 
#удалить элемент по введеному с клавиатуры названию, вставить город "Конец" в указанное с клавиатуры место по индексу
#задание 9
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, name):
        current = self.head
        prev = None
        while current and current.name != name:
            prev = current
            current = current.next
        if not current:
            print(f"Элемент с именем {name} не найден.")
            return
        if not prev:
            self.head = current.next
        else:
            prev.next = current.next
        print(f"Элемент с именем {name} удален.")

    def insert(self, index, name):
        new_node = Node(name)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(index - 1):
            if not current.next:
                break
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.name)
            current = current.next

def main():
    ll = LinkedList()
    places = ["Болотная Рогавка", "Хреновое", "Красная Могила", "Новые Алгаши", "Новопозорново", "Ломки", "Дно", "Кокаиновые горы"]
    for place in places:
        ll.append(place)
    
    print("Исходный список населенных пунктов:")
    ll.print_list()
    
    name_to_remove = input("\nВведите название населенного пункта для удаления: ")
    ll.remove(name_to_remove)
    
    print("\nСписок после удаления:")
    ll.print_list()
    
    index_to_insert = int(input("\nВведите индекс для вставки города 'Конец': "))
    ll.insert(index_to_insert, "Конец")
    
    print("\nСписок после вставки города 'Конец':")
    ll.print_list()

if __name__ == "__main__":
    main()