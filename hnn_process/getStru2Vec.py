'''
并行分词
'''
import os
import pickle
import logging

import sys
sys.path.append("..")

# 解析结构
from python_structured import *
from sql_structured import *

#FastText库  gensim 3.4.0
from gensim.models import FastText

import numpy as np

#词频统计库
import collections
#词云展示库
import wordcloud
#图像处理库 Pillow 5.1.0
from PIL import Image

# 多进程
from multiprocessing import Pool as ThreadPool

#python解析
def multipro_python_query(data_list):
    result = [python_all_context_parse(line) for line in data_list]
    return result

def multipro_python_code(data_list):
    result = [python_query_parse(line) for line in data_list]
    return result

def multipro_python_context(data_list):
    result = []
    for line in data_list:
        if (line == '-10000'):
            result.append(['-10000'])
        else:
            result.append(python_part_context_parse(line))
    return result

#sql解析
def multipro_sql_query(data_list):
    result=[sql_all_context_parse(line) for line in data_list]
    return result

def multipro_sql_code(data_list):
    result = [sql_query_parse(line) for line in data_list]
    return result

def multipro_sql_context(data_list):
    result = []
    for line in data_list:
        if (line == '-10000'):
            result.append(['-10000'])
        else:
            result.append(sql_part_context_parse(line))
    return result

# 最终的python版解析函数
def python_parse_final(python_list,split_num):

    acont1_data =  [i[1][0][0] for i in python_list]

    acont1_split_list = [acont1_data[i:i + split_num] for i in range(0, len(acont1_data), split_num)]
    pool = ThreadPool(10)
    acont1_list = pool.map(multipro_python_context, acont1_split_list)
    pool.close()
    pool.join()
    acont1_cut = []
    for p in acont1_list:
        acont1_cut += p
    print('acont1条数：%d' % len(acont1_cut))

    acont2_data = [i[1][1][0] for i in python_list]

    acont2_split_list = [acont2_data[i:i + split_num] for i in range(0, len(acont2_data), split_num)]
    pool = ThreadPool(10)
    acont2_list = pool.map(multipro_python_context, acont2_split_list)
    pool.close()
    pool.join()
    acont2_cut = []
    for p in acont2_list:
        acont2_cut += p
    print('acont2条数：%d' % len(acont2_cut))



    query_data = [i[3][0] for i in python_list]

    query_split_list = [query_data[i:i + split_num] for i in range(0, len(query_data), split_num)]
    pool = ThreadPool(10)
    query_list = pool.map(multipro_python_query, query_split_list)
    pool.close()
    pool.join()
    query_cut = []
    for p in query_list:
        query_cut += p
    print('query条数：%d' % len(query_cut))

    code_data = [i[2][0][0] for i in python_list]

    code_split_list = [code_data[i:i + split_num] for i in range(0, len(code_data), split_num)]
    pool = ThreadPool(10)
    code_list = pool.map(multipro_python_code, code_split_list)
    pool.close()
    pool.join()
    code_cut = []
    for p in code_list:
        code_cut += p
    print('code条数：%d' % len(code_cut))

    qids = [i[0] for i in python_list]
    print(qids[0])
    print(len(qids))

    return acont1_cut,acont2_cut,query_cut,code_cut,qids

# 最终的sql版解析函数
def sql_parse_final(sql_list,split_num):

    acont1_data =  [i[1][0][0] for i in sql_list]

    acont1_split_list = [acont1_data[i:i + split_num] for i in range(0, len(acont1_data), split_num)]
    pool = ThreadPool(10)
    acont1_list = pool.map(multipro_sql_context, acont1_split_list)
    pool.close()
    pool.join()
    acont1_cut = []
    for p in acont1_list:
        acont1_cut += p
    print('acont1条数：%d' % len(acont1_cut))

    acont2_data = [i[1][1][0] for i in sql_list]

    acont2_split_list = [acont2_data[i:i + split_num] for i in range(0, len(acont2_data), split_num)]
    pool = ThreadPool(10)
    acont2_list = pool.map(multipro_sql_context, acont2_split_list)
    pool.close()
    pool.join()
    acont2_cut = []
    for p in acont2_list:
        acont2_cut += p
    print('acont2条数：%d' % len(acont2_cut))

    query_data = [i[3][0] for i in sql_list]

    query_split_list = [query_data[i:i + split_num] for i in range(0, len(query_data), split_num)]
    pool = ThreadPool(10)
    query_list = pool.map(multipro_sql_query, query_split_list)
    pool.close()
    pool.join()
    query_cut = []
    for p in query_list:
        query_cut += p
    print('query条数：%d' % len(query_cut))

    code_data = [i[2][0][0] for i in sql_list]

    code_split_list = [code_data[i:i + split_num] for i in range(0, len(code_data), split_num)]
    pool = ThreadPool(10)
    code_list = pool.map(multipro_sql_code, code_split_list)
    pool.close()
    pool.join()
    code_cut = []
    for p in code_list:
        code_cut += p
    print('code条数：%d' % len(code_cut))
    qids = [i[0] for i in sql_list]

    return acont1_cut ,acont2_cut,query_cut,code_cut,qids

# 将两个版本的解析集合到一个函数中
def main(lang_type,split_num,source_path,save_path):
    total_data = []
    with open(source_path, "rb") as f:
        #  存储为字典 有序
        corpus_lis  = pickle.load(f) #pickle

        #corpus_lis = eval(f.read()) #txt

        # [(id, index),[[si]，[si+1]] 文本块，[[c]] 代码，[q] 查询, [qcont] 查询上下文, 块长度，标签]

        if lang_type =='python':
            parse_acont1, parse_acont2,parse_query, parse_code,qids  = python_parse_final(corpus_lis, split_num)
            for i in range(0,len(qids)):
                total_data.append([qids[i],[parse_acont1[i],parse_acont2[i]],[parse_code[i]],parse_query[i]])
        if lang_type == 'sql':

            parse_acont1,parse_acont2,parse_query, parse_code,qids = sql_parse_final(corpus_lis, split_num)
            for i in range(0,len(qids)):
                total_data.append([qids[i],[parse_acont1[i],parse_acont2[i]],[parse_code[i]],parse_query[i]])


    f = open(save_path, "w")
    f.write(str(total_data))
    f.close()

python_type= 'python'
sql_type = 'sql'
words_top = 100
split_num = 1000

def test(path1,path2):
    with open(path1, "rb") as f:
        #  存储为字典 有序
        corpus_lis1  = pickle.load(f) #pickle
    with open(path2, "rb") as f:
        corpus_lis2 = eval(f.read()) #txt

    print(corpus_lis1[10])
    print(corpus_lis2[10])


