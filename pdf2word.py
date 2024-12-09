from pdf2docx import Converter

# 输入PDF文件和输出Word文件路径
pdf_file = input("请输入pdf路径：（不带双引号）")   # 替换为你的PDF文件路径
word_file = 'C:/yourPDF.docx'  # 替换为合适的输出路径

# 创建转换器对象
cv = Converter(pdf_file)

# 将PDF转换为Word
cv.convert(word_file, start=0, end=None)

# 关闭转换器
cv.close()

print(f"PDF文件已成功转换为Word，保存路径: {word_file}")
