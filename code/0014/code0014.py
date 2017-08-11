"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中，如下图所示：

student.xls
"""

# pip install xlsxwriter
import xlsxwriter

workbook = xlsxwriter.Workbook('student.xlsx')
worksheet = workbook.add_worksheet()

dataset = {
    "1": ["张三", 150,120, 100],
    "2": ["李四", 90, 99, 95],
    "3": ["王五", 60, 66, 68]
}
keys = sorted(dataset.keys())

for row_index, key in enumerate(keys):
    values = dataset[key]
    worksheet.write(row_index, 0, str(key))
    for col, value in enumerate(values):
        worksheet.write(row_index, col + 1, value)

workbook.close()
