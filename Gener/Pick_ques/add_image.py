import docx2txt
import os

# Replace with the path to your .docx file
docx_file_path = r"E:\GENER\upload_file\media\media\DE_1.docx"
#docx_file_path = r'DE_1.docx'


# Replace with the path to the directory where you want to save the images
output_dir = 'output_images/'
os.makedirs(output_dir, exist_ok=True)

# Extract images from the .docx file and save them to the output directory
docx2txt.process(docx_file_path, output_dir)

print(f'Images extracted and saved to {output_dir}')
