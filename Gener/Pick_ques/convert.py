import os
import pypandoc
import re

# Input and output file paths
input_file = r"E:\GENER\upload_file\media\media\DE_1.docx"
#input_file = r'DE_1.docx'


output_file = "output.md"

# Create a main folder to hold subfolders
main_folder = "devesion_level"
if not os.path.exists(main_folder):
    os.makedirs(main_folder)

# Categories diction này cách nhận diện level của đề
categories = {
    'Co_ban': 'g1',
    'Thong_dung': 'g2',
    'Van_dung': 'g3',
    'Van_dung_cao': 'g4'
}


try:
    pypandoc.convert_file(input_file, "md", outputfile=os.path.join(main_folder, "output.md")) # Để convert từ file .docx sang file: output.md
    print(f"Conversion complete. Output saved as {os.path.join(main_folder, 'output.md')}")     

    # Nơi để xử lí devesion level
    for category, marker in categories.items(): 
        category_folder = os.path.join(main_folder, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder) # Tạo một folder {category_folder} ở trong main_folder 
        output_filename = f"output{list(categories.keys()).index(category) + 1}.md" # Tạo name của file output{..}.md

        with open(os.path.join(main_folder, "output.md"), 'r', encoding='utf-8') as file: # Mở file output.md lên để read
            markdown_text = file.read()
        # Find the questions within the specified markers and save to the output file
        pattern = re.compile(rf'{marker}(.*?){marker}', re.DOTALL) # để tìm kiếm các đoạn văn bản trong chuỗi markdown_text
        matches = pattern.findall(markdown_text) #  tìm kiếm tất cả các kết quả pattern khớp trong chuỗi markdown_text
        with open(os.path.join(category_folder, output_filename), 'w', encoding='utf-8') as category_output: # Mở file có name {output_filename} ở trong folder {category_folder} 
            ans= '\n'.join(matches) # Gọi trên chuỗi '\n' để kết hợp các phần tử trong danh sách matches thành một chuỗi duy nhất
            category_fix = ans.replace('\>','') # Xử lí chuỗi kỹ tự thừa
            category_fix1 = category_fix.replace('\<','')
            category_output.write(category_fix1) # In chuỗi ký tự đã được sửa vào file
            
            

        print(f"Saved {category} questions to {os.path.join(category_folder, output_filename)}")
except Exception as e:
    print(f"Error: {e}")