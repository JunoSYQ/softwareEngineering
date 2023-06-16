'''

从大词典中获取特定于于语料的词典
将数据处理成待打标签的形式
'''

from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from gensim.models import KeyedVectors

#词向量文件保存成bin文件
def trans_bin(word_path,bin_path):
    wv_from_text = KeyedVectors.load_word2vec_format(word_path, binary=False)
    # 如果每次都用上面的方法加载，速度非常慢，可以将词向量文件保存成bin文件，以后就加载bin文件，速度会变快
    wv_from_text.init_sims(replace=True)
    wv_from_text.save(bin_path)
    '''n
    读取用一下代码
    model = KeyedVectors.load(embed_path, mmap='r')
    '''

#构建新的词典和词向量矩阵
def get_new_dict(type_vec_path,type_word_path,final_vec_path,final_word_path):  #词标签，词向量
    #原词159018 找到的词133959 找不到的词25059
    #添加unk过后 159019 找到的词133960 找不到的词25059
    #添加pad过后 词典：133961 词向量 133961
    # 加载转换文件
    model = KeyedVectors.load(type_vec_path, mmap='r')

    with open(type_word_path,'r')as f:
        total_word= eval(f.read())
        f.close()

    # 输出词向量
    word_dict = ['PAD','SOS','EOS','UNK']#其中0 PAD_ID,1SOS_ID,2E0S_ID,3UNK_ID

    fail_word = []
    rng = np.random.RandomState(None)
    pad_embedding = np.zeros(shape=(1, 300)).squeeze()
    unk_embediing = rng.uniform(-0.25, 0.25, size=(1, 300)).squeeze()
    sos_embediing = rng.uniform(-0.25, 0.25, size=(1, 300)).squeeze()
    eos_embediing = rng.uniform(-0.25, 0.25, size=(1, 300)).squeeze()
    word_vectors = [pad_embedding,sos_embediing,eos_embediing,unk_embediing]
    print(len(total_word))
    for word in total_word:
        try:
            word_vectors.append(model.wv[word]) #加载词向量
            word_dict.append(word)
        except:
            print(word)
            fail_word.append(word)
    #关于有多少个词，以及多少个词没有找到
    print(len(word_dict))
    print(len(word_vectors))
    print(len(fail_word))



    #判断词向量是否正确
    '''
    couunt = 0
    for i in range(4,len(word_dict)):
        if word_vectors[i].all() == model.wv[word_dict[i]].all():
            continue
        else:
            couunt +=1

    print(couunt)
    '''



    word_vectors = np.array(word_vectors)
    #print(word_vectors.shape)
    word_dict = dict(map(reversed, enumerate(word_dict)))
    #np.savetxt(final_vec_path,word_vectors)
    with open(final_vec_path, 'wb') as file:
        pickle.dump(word_vectors, file)

    with open(final_word_path, 'wb') as file:
        pickle.dump(word_dict, file)

    v = pickle.load(open(final_vec_path, 'rb'), encoding='iso-8859-1')
    with open(final_word_path, 'rb') as f:
        word_dict = pickle.load(f)
    couunt = 0

    print("完成")

#得到词在词典中的位置
def get_index(type,text,word_dict):
    location = []
    if type == 'code':
        location.append(1)
        len_c = len(text)
        if len_c+1 <350:
            if len_c == 1 and text[0] == '-1000':
                location.append(2)
            else:
                for i in range(0, len_c):
                    if word_dict.get(text[i]) != None:
                        index = word_dict.get(text[i])
                        location.append(index)
                    else:
                        index = word_dict.get('UNK')
                        location.append(index)

                location.append(2)
        else:
            for i in range(0, 348):
                if word_dict.get(text[i]) != None:
                    index = word_dict.get(text[i])
                    location.append(index)
                else:
                    index = word_dict.get('UNK')
                    location.append(index)
            location.append(2)
    else:
        if len(text) == 0:
            location.append(0)
        elif text[0] == '-10000':
            location.append(0)
        else:
            for i in range(0, len(text)):
                if word_dict.get(text[i]) != None:
                    index = word_dict.get(text[i])
                    location.append(index)
                else:
                    index = word_dict.get('UNK')
                    location.append(index)

    return location

# 将训练、测试、验证语料序列化
# 查询：25 上下文：100 代码：350
def Serialization(word_dict_path,type_path,final_type_path):

    with open(word_dict_path, 'rb') as f:
        word_dict = pickle.load(f)

    with open(type_path,'r')as f:
        corpus= eval(f.read())
        f.close()

    total_data = []


    for i in range(0, len(corpus)):
        qid = corpus[i][0]

        Si_word_list = get_index('text',corpus[i][1][0],word_dict)
        # Si+1
        Si1_word_list = get_index('text',corpus[i][1][1],word_dict)

        # code
        #tokenized_code = get_index('code',corpus[i][2][0],word_dict) #训练语料
        tokenized_code = get_index('code', corpus[i][2][0], word_dict) #staqc
        # query
        query_word_list = get_index('text',corpus[i][3],word_dict)
        #block_length = corpus[i][4]
        #label = corpus[i][5]
        block_length = 4
        label = 0
        if(len(Si_word_list)>100):
            Si_word_list = Si_word_list[:100]
        else:
            for k in range(0, 100 - len(Si_word_list)):
                Si_word_list.append(0)

        if (len(Si1_word_list) > 100):
            Si1_word_list = Si1_word_list[:100]
        else:
            for k in range(0, 100 - len(Si1_word_list)):
                Si1_word_list.append(0)

        if (len(tokenized_code) < 350):
            for k in range(0, 350 - len(tokenized_code)):
                tokenized_code.append(0)
        else:
            tokenized_code = tokenized_code[:350]

        if (len(query_word_list) > 25):
            query_word_list = query_word_list[:25]
        else:
            for k in range(0, 25 - len(query_word_list)):
                query_word_list.append(0)

        one_data = [qid, [Si_word_list, Si1_word_list], [tokenized_code], query_word_list, block_length, label]
        total_data.append(one_data)

    with open(final_type_path, 'wb') as file:
        pickle.dump(total_data, file)
# 文件append_word_path中包含的新词添加到词典中，
# 并在原有的词向量词表中按顺序添加相应的词向量。
# 函数会先加载类型为word2vec的词标签及其对应的词向量。
def get_new_dict_append(type_vec_path,previous_dict,previous_vec,append_word_path,final_vec_path,final_word_path):  #词标签，词向量
    #原词159018 找到的词133959 找不到的词25059
    #添加unk过后 159019 找到的词133960 找不到的词25059
    #添加pad过后 词典：133961 词向量 133961
    # 加载转换文件

    model = KeyedVectors.load(type_vec_path, mmap='r')

    with open(previous_dict, 'rb') as f:
        pre_word_dict = pickle.load(f)

    with open(previous_vec, 'rb') as f:
        pre_word_vec = pickle.load(f)

    with open(append_word_path,'r')as f:
        append_word = eval(f.read())
        f.close()

    # 输出词向量

    print(type(pre_word_vec))
    word_dict =  list(pre_word_dict.keys()) #'#其中0 PAD_ID,1SOS_ID,2E0S_ID,3UNK_ID
    print(len(word_dict))
    word_vectors = pre_word_vec.tolist()
    print(word_dict[:100])
    fail_word =[]
    print(len(append_word))
    rng = np.random.RandomState(None)
    unk_embediing = rng.uniform(-0.25, 0.25, size=(1, 300)).squeeze()
    h = []

    for word in append_word:
        try:

            word_vectors.append(model.wv[word]) #加载词向量
            word_dict.append(word)
        except:
            fail_word.append(word)
    #关于有多少个词，以及多少个词没有找到
    print(len(word_dict))
    print(len(word_vectors))
    print(len(fail_word))
    print(word_dict[:100])

    '''
    #判断词向量是否正确
    print("----------------------------")
    couunt = 0

    import operator
    for i in range(159035,len(word_dict)):
        if operator.eq(word_vectors[i].tolist(), model.wv[word_dict[i]].tolist()) == True:
            continue
        else:
            couunt +=1

    print(couunt)
    '''

    word_vectors = np.array(word_vectors)
    #print(word_vectors.shape)
    word_dict = dict(map(reversed, enumerate(word_dict)))
    #np.savetxt(final_vec_path,word_vectors)
    with open(final_vec_path, 'wb') as file:
        pickle.dump(word_vectors, file)

    with open(final_word_path, 'wb') as file:
        pickle.dump(word_dict, file)


    print("完成")