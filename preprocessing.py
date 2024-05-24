# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:29:51 2024

@author: taikurist, Zhizhe300
"""

import pandas as pd


def find_cols(df, column):
    
    global cols, names

    for column in cols:
        str_list = str((df[column]))
        if str_list.find(';') != -1:
            names.append(column)
            continue
    



def find_unique_words(df, name):
        filtered_values = df[name].dropna()
        words_list = filtered_values.str.split(';')
        all_words = [word for sublist in words_list for word in sublist]
        # Получение уникальных слов
        unique_words = list(set(all_words))
        if '' in unique_words:
            del unique_words[0]
        return unique_words
    

   


def su(df):
    global sets
    for key, value in sets.items():
        column_index = df.columns.get_loc(key)
        for i in range(1, len(value)):
            name = value[i]
            df.insert(column_index+i, key+value[i], [None] * len(df))
            
        for j in range(0, len(df)):
            for i in range(1, len(value)):
                name = value[i]
                cell_value = str(df.loc[j, key]).split(";")
                
                if name in cell_value:
                    #df[key][j] = 1
                    df.iloc[j, column_index+i] = 1
                else:
                    #df[key][j] = 0
                    df.iloc[j, column_index+i] = 0
                    
                    
df = pd.read_csv('ИТМО ФТМИ.csv')
    
cols= list(df.columns)
names = []
sets = {}

find_cols(df, cols)

for name in names:
    sets[name] = find_unique_words(df, name)


su(df)
df.to_csv('DataFrame.csv', encoding = 'UTF-8', sep = ';')

