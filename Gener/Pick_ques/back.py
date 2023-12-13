import pypandoc
# =)) vẫn chưa tìm ra cách dọc hết mà nỏ cần for
input_file = r"E:\GENER\upload_file\Exam_test\main.md"  # :v nhớ add đúng vị trí file 
output_file = f"test.docx"  # file out ra .md file

try:
    pypandoc.convert_file(input_file, "docx", outputfile=output_file)
    print(f"Conversion complete. Output saved as {output_file}")
except Exception as e:
    print(f"Error: {e}")
