import os
import shutil

# Define source and destination folders
source_folder = ['devesion_level','output_images','DATA','Exam_test','media','Ans_data']
source_file = 'test.docx'
source_excel = 'test.xlsx'
main_folder = 'OUTPUT_FILE'
for i in range(6):
    destination_folder = f'{main_folder}\{source_folder[i]}'

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List files in the source folder
    files = os.listdir(source_folder[i])

    # Move files to the destination folder
    for file in files:
        source_path = os.path.join(source_folder[i], file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
    os.rmdir(source_folder[i])
shutil.move(source_file, os.path.join(main_folder, os.path.basename(source_file)))
shutil.move(source_excel, os.path.join(main_folder, os.path.basename(source_excel)))
    # Optionally, remove the source folder if needed
    # os.rmdir(source_folder)