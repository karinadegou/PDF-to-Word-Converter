# PDF-to-Word-Converter

这个脚本用于将 PDF 文件转换为 Word 文件（```.docx```）。它使用了```pdf2docx```库来执行转换，并保存为```.docx```格式，便于编辑和后续处理。

## 功能
- 将 PDF 文件转换为 Word 文档。
- 支持从指定页面范围进行转换。
- 输出 Word 文件保存为 .docx 格式。

## 安装

确保你已经安装了 Python 和 Conda 环境。可以通过以下步骤安装所需的依赖包：

- 创建一个新的 Conda 环境（可选）：

``` bash
conda create --name pdf2word python=3.8
conda activate pdf2word
```

- 安装依赖项：

``` bash
pip install pdf2docx
```

## 使用方法
- 准备文件：确保你有一个要转换的 PDF 文件，并指定输出的 Word 文件路径。
- 运行脚本：使用以下命令运行 Python 脚本：

``` bash
python pdf2word.py
```

- 参数说明：
- ```pdf_file```：输入 PDF 文件的路径。
- ```word_file```：输出的 Word 文件路径（```.docx```）。
- ```start```和```end```：指定需要转换的页面范围，默认为整个 PDF。
你可以根据需求修改脚本中的```pdf_file```和```word_file```路径，以及选择是否指定页面范围。

## 输入和输出
- 输入：一个 PDF 文件，位于你指定的路径（例如```input.pdf```）。
- 输出：一个转换后的 Word 文件，保存为```.docx```格式（例如```output.docx```）。
## 错误与调试
- PermissionError：如果遇到权限错误（```PermissionError: [Errno 13] Permission denied```），请确保指定的输出路径具有写权限，或者尝试使用不同的路径。

- Unicode 错误：如果路径中包含反斜杠（例如```C:\Users\Username```），请使用原始字符串（```r'path'```）或双反斜杠（```C:\\Users\\Username```）来避免```UnicodeError```。

## 常见问题
- PDF 格式不兼容：
  - 对于一些复杂的 PDF 格式（如扫描版 PDF），转换结果可能不完全准确。可以尝试其他工具或手动调整输出文档。
- 转换速度：
  - 转换速度取决于 PDF 文件的大小和复杂性。对于大文件或复杂布局的 PDF，转换过程可能需要更长时间。
