# teacher-praises
批量生成班主任评语/寄语

# 文件
- 评语：评语原始文件，来自[这里](https://m.diyifanwen.com/fanwen/gaozhongshengpingyu/3806493.html)
- 评语分段：顾名思义
- 去重：查过重复的评语段
- 是什么：是xxxxx的学生
- remove_dup.cpp：哈希查重，第一个参数就是要查重的文件，输出到“去重”文件
- teacher-praises.pyi：生成器，需要“去重””是什么“文件，俩参数：一行的字数，输出多少行
