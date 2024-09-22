# -- coding: cp1251 --
from collections import deque
import datetime
import random

# �������� ������
grades = {
    '�������': 5,
    '���������': 4,
    '������� ������': 4,
    '���������� ��������': 5,
    '�����': 3,
    '����������': 4,
    '������� ����': 5,
    '��������': 4,
    '����������': 4,
    '����������': 5,
    '���': 3,
    '����������': 4,
    '���������': 4,
    '���������': 5
}

actor = ("���� ����", datetime.date(1907, 5, 26))

names_list = [
    '����', '������', '���������', '������', '�������', '�������', '������',
    '��������', '�������', '�����'
]
surnames_list = [
    '������', '������', '�������', '���������', '�������', '�������', '��������', '�����'
]

def generate_names():
    full_names = []
    for i in range(30):
        name = random.choice(names_list)
        surname = random.choice(surnames_list)
        full_names.append(f"{name} {surname}")
    return full_names

animal_name = "������� �������"

# �������
# 1.
print(f"������� ����: {sum(grades.values()) / len(grades)}\n")

# 2.
print(f"���������� �����: {set(names_list)}\n")

# 3.
print(f"��������� ����� ���� �������� ���������: {sum(len(grade) for grade in grades.keys())}\n")

# 4.
print(f"���������� ����� � ��������� ���������: {set(''.join(grades.keys()))}\n")

# 5.
print(f"��� ��������� � �������� ����: {' '.join([bin(ord(char))[2:] for char in animal_name])}\n")

# 6.
print(f"{actor[0]} ������� {(datetime.date.today() - actor[1]).days} ���� �����\n")

# 7.
queue = deque()
print("������� �������� ���������� (������� '����' ��� ����������): ")
while True:
    material = input()
    if material.lower() == '����':
        break
    queue.append(material)

print(f"��������� � ������� ����������: {list(queue)}\n")

# 8.
sorted_names_list = sorted(generate_names())
b_day, b_month, b_year = actor[1].day, actor[1].month, actor[1].year
index = (b_day + b_month ** 2 + b_year) % 10
print("������� ����� �� 0 �� 9:")
index = int(input())
sorted_names_list[index] = "�����-����"
print(f"���������� ������: {sorted_names_list}\n")

# 9.
values = []
links = []
head = None

def add(idx, value):
    global head, values, links
    if head is None:
        values.append(value)
        links.append(None)
        head = 0
    else:
        new_idx = len(values)
        values.append(value)
        links.append(None)

        if idx == 0:
            links[new_idx] = head
            head = new_idx
        else:
            prev = head
            for _ in range(idx - 1):
                if links[prev] is None:
                    break
                prev = links[prev]
                
            links[new_idx] = links[prev]
            links[prev] = new_idx

def remove(value):
    global head, values, links
    if head is None:
        return
    
    if values[head] == value:
        head = links[head]
    else:
        prev = head
        current = links[prev]
        while current is not None and values[current] != value:
            prev = current
            current = links[current]
        
        if current is not None:
            links[prev] = links[current]

def display():
    global head, values, links
    current = head
    while current is not None:
        print(values[current])
        current = links[current]

add(0, "������� �����")
add(2, "������� �����")
add(1, "���")
add(3, "�������")

print("������� �������� ��� ��������:")
remove(input())

print("������� ������ ��� �������:")
add(int(input()), "�����")

print("������ ��������� �������:")
display()
