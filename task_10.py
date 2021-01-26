#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 10. Решите задачу: создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), c с помощью полученного объекта  dict_items создайте
# новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями – числа.

if __name__ == '__main__':
    number = {12: 'Декабрь', 1:'Январь', 2:'Февраль'}
    print(number)
    new_number = {}
    for key, value in number.items():
        new_number[value] = key
    print(new_number)