# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:29:51 2024

@author: taikurist, Zhizhe300
"""

import pandas as pd

# Функция находит все колонки с определённым символом
# Символ можно заменить в зависимости от условия содержания, будут затронуты все колонки, в которых содержится хотя-бы !один! такой символ
def find_cols(df, column):
    global cols, names
    for column in cols:
        str_list = str((df[column]))
        if str_list.find(';') != -1:
            names.append(column)
            continue
    



def find_unique_words(df, name):
        filtered_values = df[name].dropna()
        # Символ-разделитель можно менять в зависимости от условия
        words_list = filtered_values.str.split(';')
        # Получение уникальных слов
        all_words = [word for sublist in words_list for word in sublist]
        unique_words = list(set(all_words))
        if '' in unique_words:
            del unique_words[0]
        return unique_words
    

   


def su(df):
    global sets
    # key - название колонки, value - список уникальных слов, содержащиеся в столбце
    for key, value in sets.items():
        # Находим столбец по названию(key)
        column_index = df.columns.get_loc(key)
        for i in range(1, len(value)):
            # Вставляем пустые столбцы после столбца key по количеству уникальных ответов в столбе key
            name = value[i]
            df.insert(column_index+i, key+value[i], [None] * len(df))
            
        for j in range(0, len(df)):
            for i in range(1, len(value)):
                # Отбираем уникальные слова в столбце key, строке j
                name = value[i]
                cell_value = str(df.loc[j, key]).split(";")
                
                if name in cell_value:
                    #если уникальное слово присутсвует в ячейке
                    df.iloc[j, column_index+i] = 1
                else:
                    #если уникальное слово отсутсвует в ячейке
                    df.iloc[j, column_index+i] = 0
                    
                    
df = pd.read_csv('ИТМО ФТМИ.csv')
    
cols= list(df.columns)
names = []
sets = {}

find_cols(df, cols)

for name in names:
    # Наполнение наборов для последующей отборки по key и value
    sets[name] = find_unique_words(df, name)


su(df)
df.to_csv('DataFrame.csv', encoding = 'UTF-8', sep = ';')

