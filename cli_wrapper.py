# cli_wrapper.py
import sys
from markitdown import MarkItDown

def main():
    if len(sys.argv) < 2:
        # 如果没有参数，输出到 stderr 避免干扰重定向
        print("用法: markitdown.exe <输入文件路径> > 输出文件.md", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    md = MarkItDown()
    
    try:
        # 获取转换结果
        result = md.convert(file_path)
        # 直接打印转换后的文本内容到标准输出
        # sys.stdout.write 相比 print 更干净，不会处理换行符的特殊转义
        sys.stdout.write(result.text_content)
    except Exception as e:
        print(f"转换出错: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()