
import os
import random
import shutil
import re

main_folder = r"E:\GENER\upload_file\Exam_test"  # Name of the main folder
#main_folder = r"Exam_test"
save = 1
Data = []



Data.append({"a[1]": "Co_ban","start": 1, "range": 20, "n": 10})
Data.append({"a[2]": "Thong_dung","start": 21, "range": 35, "n": 7})
Data.append({"a[3]": "Van_dung","start": 36, "range": 45, "n": 5})
Data.append({"a[4]": "Van_dung_cao","start": 46, "range": 50, "n": 3})
for item in Data:
    if item.get("a[1]") == "Co_ban":
        x = item.get("range")
        n = item.get("n")
        start = item.get("start")
        level = "Co_ban"
    elif  item.get("a[2]") == "Thong_dung":
        x = item.get("range")
        n = item.get("n")
        start = item.get("start")
        level = "Thong_dung"
    elif  item.get("a[3]") == "Van_dung":
        x = item.get("range")
        n = item.get("n")
        start = item.get("start")
        level = "Van_dung"
    elif  item.get("a[4]") == "Van_dung_cao":
        x = item.get("range")
        n = item.get("n")
        start = item.get("start")
        level = "Van_dung_cao"
    
    numbers = list(range(start, x + 1))

    # Create the main folder if it doesn't exist
    if not os.path.exists(main_folder):
        os.mkdir(main_folder)

    i = save
    for i in range(i,save+n):
        save +=1 
        x = random.choice(numbers)
        numbers.remove(x)
        folder_name = f"Câu{x}"
        folder_path = os.path.join(main_folder, folder_name)

        source_path = os.path.join(f"DATA/{level}/questions_data", folder_name)
        source_path2 = os.path.join(f"DATA/{level}/Ques_make_exam/{folder_name}", f"{folder_name}.md")
        source_path3 = os.path.join(f"Ans_data/{folder_name}","ans.md" )

        if os.path.exists(source_path) and os.path.isdir(source_path):
             # Clone the folder from "questions" to "Exam_test"
            shutil.copytree(source_path, folder_path)
            
        if os.path.exists(source_path3):
            shutil.copy(source_path3, folder_path)
        if os.path.exists(source_path2):
            shutil.copy(source_path2, folder_path)

             # Create or open the main.md file and append the contents
            main_md_path = os.path.join(main_folder, "main.md")
            with open(main_md_path, "a",encoding='utf-8') as main_md_file:
                main_md_file.write(f"Câu {i}:\n")
                file_path = os.path.join(folder_path, f"{folder_name}.md")
               #if os.path.exists(file_path):
                with open(file_path, "r",encoding='utf-8') as subfile:
                        main_md_file.write(subfile.read())
                main_md_file.write("\n\n\n")
