# 软件工程实验
20201050307 宋瑜晴

## 目录
- [一、项目描述](#一项目描述)
- [二、项目结构文件说明](#二项目结构文件说明)
  - [2.1 getSru2Vec.py文件](#getsru2vecpy文件)
  - [2.2 embddings_process.py文件](#embddings_processpy文件)
  - [2.3 process_single_corpus.py文件](#process_single_corpuspy文件)
  - [2.4 python_structured.py文件](#python_structuredpy文件)
  - [2.5 sqlang_structured.py文件](#sqlang_structuredpy文件)
  - [2.6 word_dict.py文件](#word_dictpy文件)
  - [2.7 run.py文件](#runpy文件)
- [三、总结](#三总结)

## 一、项目描述
  此项目的python文件是对文本数据进行预测处理。通过给出python文件，对文件进行代码代码规范调试
## 二、项目结构文件说明
### 结构说明：
```
├── hnn_preprocessing  
│   └── embaddings_process.py  
│   └── getStru2Vec.py
│   └── process_single_corpus.py
│   └── python_structured.py
│   └── sqlang_structured.py
│   └── word_dirt.py
|   └── run.py

```
### 文件说明

### process_single_corpus.py文件

#### 1. 概述
  把语料中的单候选和多候选分隔开
#### 2. 导入依赖库
该文件导入了以下依赖库：
 - pickle：用于读取和写入 pickle 文件
 - Counter： ：用于计数数据中元素的频率

#### 3. 类和方法说明

###### 方法
- load_pickle(filename)：读取pickle二进制文件。filename为文件路径
- single_list(arr, target)：计算一个列表中指定元素的出现次数。arr为列表，target为指定的元素
- data_staqc_prpcessing(filepath,single_path,mutiple_path):把语料中的单候选和多候选分隔开。filepath表示源文件路径，single_path为单候选文件的保存地址，mutiple_path为多候选文件的保存地址。
---
### word_dirt.py文件
#### 1. 概述
  构建语料词典
#### 2. 导入依赖库
该文件导入了以下依赖库：
 - pickle：用于读取和写入 pickle 文件

#### 3. 类和方法说明

###### 方法
- load_pickle(filename)：读取pickle二进制文件。filename为文件路径
- get_vocab(corpus1, corpus2)：构建初步词典的具体步骤1，查找两个文本语料库中的单词并生成词汇表。corpus1表示第一个文本语料的路径，corpus2表示第二个文本语料的路径。
- vocab_prpcessing(filepath1,filepath2,save_path)：构建初步词典，从两个文本数据集中获取全部出现过的单词，并将单词保存到文件中。filepath1表示第一个文本语料的路径,filepath2表示第二个文本语料的路径,save_path表示生成的文本的保存路径。
- final_vocab_prpcessing(filepath1,filepath2,save_path):最终构建的词典，获取两个文本数据集中出现的单词的集合，并且仅返回在第二个数据集中出现过而未在第一个数据集中出现过的单词的集合。filepath1表示第一个文本语料的路径,filepath2表示第二个文本语料的路径,save_path表示生成的文本的保存路径。
---
### python_structured.py文件
#### 1. 概述
  解析 Python 代码，修复代码中的变量命名问题；
  代码重构，添加变量名的注释。
#### 2. 导入依赖库
该文件导入了以下依赖库：
 - re：用于正则表达式匹配和替换
 - ast:
 - sys:
 - token 和 tokenize：用于解析 Python 代码中的 token
 - io.StringIO：用于在内存中操作字符串作为文件
 - inflection：用于进行单词的单复数转换
 - nltk：自然语言处理工具包，用于词性标注、分词和词形还原

#### 3. 类和方法说明

###### 方法
---
### sqlang_structured.py文件
#### 1. 概述
  把语料中的单候选和多候选分隔开
#### 2. 导入依赖库
该文件导入了以下依赖库：
 - import pickle：用于读取和写入 pickle 文件
 - from collections import Counter： ：用于计数数据中元素的频率

#### 3. 类和方法说明

###### 方法
---
### getStru2Vec.py文件
#### 1. 概述
  把语料中的单候选和多候选分隔开
#### 2. 导入依赖库
该文件导入了以下依赖库：
 - import pickle：用于读取和写入 pickle 文件
 - from collections import Counter： ：用于计数数据中元素的频率

#### 3. 类和方法说明

###### 方法
---
### embaddings_process.py文件
#### 1. 概述
  把语料中的单候选和多候选分隔开
#### 2. 导入依赖库
该文件导入了以下依赖库：
 - import pickle：用于读取和写入 pickle 文件
 - from collections import Counter： ：用于计数数据中元素的频率

#### 3. 类和方法说明

###### 方法
---
### run.py文件
#### 1. 概述
  把语料中的单候选和多候选分隔开
#### 2. 导入依赖库
该文件导入了以下依赖库：
 - import pickle：用于读取和写入 pickle 文件
 - from collections import Counter： ：用于计数数据中元素的频率

#### 3. 类和方法说明

###### 方法
---


## 三、总结

