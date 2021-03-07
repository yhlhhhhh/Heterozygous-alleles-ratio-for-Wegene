# Heterozygous-alleles-ratio-for-Wegene
对微基因用户的杂合位点计数并计算占比
# import相关库
微基因用户的数据是以JSON形式存在的
``` python
import sys
import json
from wegene_utils import process_raw_genome_data
from wegene_utils import is_genotype_exist
from wegene_utils import is_wegene_format
``` 
# 用户数据读取
``` python
body = sys.stdin.read()
``` 
# 用户数据处理
将用户数据转换成合适的字典
``` python
inputs = json.loads(body)['inputs']
user_genome = process_raw_genome_data(inputs)
``` 
把字典的keys和values（每个value以字典形式存在，里面有染色体号，position和基因型）分别放入list1和list2中
``` python
list1 = list(user_genome.keys())
list2 = list(user_genome.values())
``` 
把values中的基因型提取出来并放入新建的rs_type的list里（遍历）
``` python
rs_type = []
for i in list2:
    rs_type.append(i['genotype'])
``` 
# 计数
把非I和D的检出位点总数（all_SNP）和非I和D的杂合位点总数（hybrid）利用while循环数出来
``` python
count = 0
hybrid = 0
all_SNP = 0
while count < num:
    alleles = rs_type[count]
    if alleles in ['ID','DI','II','DD','--','__']:
        count = count + 1
    elif alleles in ['AA','GG','CC','TT']:
        all_SNP = all_SNP + 1
        count = count + 1
    else:
        all_SNP = all_SNP + 1
        hybrid = hybrid + 1
        count = count + 1
``` 
# 计算
将结果保留小数点后3位并将数字转化成字符串形式
``` python
P = str(round(hybrid/all_SNP*100,3))
``` 
# 整理 输出结果
``` python
result = '您的杂合SNP占比为：' + P +'%'
print(result)
``` 
