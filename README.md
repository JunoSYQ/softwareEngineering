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
 - ast:用于处理Python代码抽象语法树
 - sys:用于程序与解释器交互
 - token 和 tokenize：用于解析 Python 代码中的 token
 - io.StringIO：用于在内存中操作字符串作为文件
 - inflection：用于进行单词的单复数转换
 - nltk：自然语言处理工具包，用于词性标注、分词和词形还原

#### 3. 类和方法说明
- format_io(code):修复 Python 程序中的标准输入/输出（I/O）格式。code表示输入的io数据。
- get_vars(ast_root)：获取变量名。ast_root表示ast语法树名。
- get_all_vars(code):一个具有启发式的解析器，旨在从 code 字符串中尽可能多地提取变量名。code表示输入的io数据。

- PythonParser(code): 将代码字符串解析为Token 序列，并且执行变量解析。code表示输入的io数据。
- └──first_trial(_code):尝试将该代码字符串解析为token令牌序列。code表示输入的io数据。

- revert_abbrev(line):缩略词处理，将常见的英语缩写还原为它们的原始形式。line表示需要处理的文本。
- get_word_pos(tag):获取词性。
- preprocess_sentence(line):对传入的一行文本进行处理预处理：空格，还原缩写，下划线命名，去括号，去除开头末尾空格。line表示需要处理的文本。
- process_words(line):对一个句子进行分词、词性标注、还原和提取词干的功能。line表示需要处理的文本。
- filter_all_invachar(line)：过滤掉Python代码中不常用的字符，以减少解析时的错误。line表示需要处理的文本。
- filter_part_invachar(line):过滤掉Python代码中部分不常用的字符，以减少解析时的错误。line表示需要处理的文本。
- python_query_parse(line):解析 python 查询语句，进行文本预处理。line表示需要处理的文本。
- python_all_context_parse(line):将提供的文本进行标准化和归一化处理,除去所有特殊字符。line表示需要处理的文本。
- python_part_context_parse(line):将提供的文本进行标准化和归一化处理,除去部分特殊字符。line表示需要处理的文本。
---
### sql_structured.py文件
#### 1. 概述
  解析 SQL 代码，修复代码中的变量命名问题；
  代码重构，添加变量名的注释。
#### 2. 导入依赖库
该文件导入了以下依赖库:
 - re：用于正则表达式匹配和替换
 - ast:用于处理Python代码抽象语法树
 - sys:用于程序与解释器交互
 - sqlparse：sql解析
 - inflection：用于进行单词的单复数转换
 - nltk：自然语言处理工具包，用于词性标注、分词和词形还原

#### 3. 类和方法说明

```
├── SqlParser(): SQL语句处理。
│   └──formatSql(sql):对输入的SQL语句进行清理和标准化。
│   └──parseStringsTokens(self, tok):将输入的SQL解析为一个SQL令牌列表,并对其进行处理
│   └──renameIdentifiers(self, tok):重命名 SQL 语句中的标识符。
│   └── __hash__(self):将 SQL 解析器对象哈希化。
│   └──_init__(self, sql, regex=False, rename=True):初始化。
│   └──getTokens(parse):获取令牌序列
│   └── removeWhitespaces(self, tok):删除多余空格。
│   └──identifySubQueries(self, tokenList):识别 SQL 表达式中的子查询。
│   └──identifyLiterals(self, tokenList):用于标识 SQL 解析器对象中的不同类型的文本字面量。
│   └──identifyFunctions(self, tokenList):从给定的token列表中识别SQL语句中的函数并设置ttype类型。
│   └──identifyTables(self, tokenList):
│   └──__str__(self):
│   └──parseSql(self):
```
---
### getStru2Vec.py文件
#### 1. 概述
  把语料中的单候选和多候选分隔开
#### 2. 导入依赖库
该文件导入了以下依赖库：
 - import pickle：用于读取和写入 pickle 文件
 - collections.Counter： ：用于计数数据中元素的频率

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

