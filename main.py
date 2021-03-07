import sys
import json
# wegene_utils 库会包含在每个应用的环境当中，无需自行打包上传
# 这里提供源代码以供应用完整运行
from wegene_utils import process_raw_genome_data
from wegene_utils import is_genotype_exist
from wegene_utils import is_wegene_format
body = sys.stdin.read()
try:
    inputs = json.loads(body)['inputs']
    user_genome = process_raw_genome_data(inputs)
    list1 = list(user_genome.keys())
    list2 = list(user_genome.values())
    rs_type = []
    num = len(list1)
    for i in list2:
        rs_type.append(i['genotype'])
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
    P = str(round(hybrid/all_SNP*100,3))
    result = '您的杂合SNP占比为：' + P +'%'
    print(result)
except Exception as e:
    sys.stderr.write('计算时出现错误，请联系作者')
    sys.stderr.write(str(e))
    exit(2)

