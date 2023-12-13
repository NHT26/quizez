import re
import os

main_folder = 'DATA'
import_folder = r'E:\GENER\upload_file\devesion_level'
#import_folder = 'devesion_level'
categories = ['Co_ban', 'Thong_dung', 'Van_dung', 'Van_dung_cao']

z = 0
i = 0
m = 0
m1 = 0
i2 = 0 

replacements = {
    '**[A.]{.underline}**': '**A.**',
    '**[B.]{.underline}**': '**B.**',
    '**[C.]{.underline}**': '**C.**',
    '**[D.]{.underline}**': '**D.**'
}
for category in categories:
    category_folder = os.path.join(main_folder, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    if not os.path.exists(os.path.join(category_folder, 'Ques_make_exam')):
        os.makedirs(os.path.join(category_folder, 'Ques_make_exam'))

    if not os.path.exists(os.path.join(category_folder, 'questions_data')):
        os.makedirs(os.path.join(category_folder, 'questions_data'))

    z = z + 1
    name_file = f"{category}\output{z}.md"

    # Read the converted Markdown content
    with open(os.path.join(import_folder, f"{name_file}"), 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    with open(os.path.join(import_folder, f"{name_file}"), 'r', encoding='utf-8') as file:
        markdown_text2 = file.read()

    for old,new in replacements.items():
        markdown_text = markdown_text.replace(old, new)
    #print(markdown_text)
    
    # Define a regex pattern to find questions and choices
    pattern = re.compile(r'\*\*Câu \d+:.*?(?:\*\*[A-D]\.\*\*.*?)(?=\*\*Câu \d+|\Z)', re.DOTALL)

    # Find all matches in the text
    matches = pattern.findall(markdown_text)
    matches2 = pattern.findall(markdown_text2)
    # Create a list to store the questions
    questions_list = []
    # Process each match
    for match in matches2:
        i2 += 1
        # Remove the '**Câu :**' part from the match
        question_text = match.replace(f"**Câu {i2}:**", '').strip()
        questions_list.append(question_text)
                
    
    questions_list1 = []
    # Process each match
    for match in matches:
        i += 1
        # Remove the '**Câu :**' part from the match
        question_text = match.replace(f"**Câu {i}:**", '').strip()
        questions_list1.append(question_text)

        # Tạo cái thằng Ques_make_exam
        check_file = "media/"
        question_dir = os.path.join(category_folder, 'Ques_make_exam', f'Câu{i}')
        os.makedirs(question_dir, exist_ok=True)
        with open(os.path.join(question_dir, f'Câu{i}.md'), 'w', encoding='utf-8') as question_file:
            match_fix = match.replace(f"**Câu {i}:**", '').strip()
            if check_file in match:
                match_fix2 = match.replace(f"media/", 'output_images/')
                match_fix3 = match_fix2.replace(f"**Câu {i}:**", '').strip()
                question_file.write(match_fix3)
            else:
                question_file.write(match_fix)

    # Process each match for questions_data
    for  match in questions_list1:
        question, *choices = re.split(r'\*\*[A-D]\.\*\*', match)
        m += 1
        # Create a directory for the question
        question_dir = os.path.join(category_folder, 'questions_data', f'Câu{m}')
        os.makedirs(question_dir, exist_ok=True)

        # Save the question text
        with open(os.path.join(question_dir, 'question.md'), 'w', encoding='utf-8') as question_file:
            question_check = question.replace(f'>', '').strip()
            question_file.write(question_check)

        # Process and save answer choices
        for choice_index, choice_content in enumerate(choices):
            choice_letter = chr(65 + choice_index)  # Convert 0, 1, 2, 3 to A, B, C, D

            choice_file_path = os.path.join(question_dir, f'Choice_{choice_letter}.md')
            choice_dot = choice_content.replace(f'.', '').strip()
            choice_finish1 = choice_dot.strip()
            choice_finish2 = choice_finish1.replace(f'>', '').strip()
            with open(choice_file_path, 'w', encoding='utf-8') as choice_file:
                choice_file.write(f"${choice_finish2}$")

    #Ouput đáp án từng câu
    for match in questions_list:
        # Use re.findall to find all matches in the `match` string
        choices = re.findall(r'\*\*\[[A-D]\.\]\{\.underline\}\*\*', match)
        question = re.sub(r'\*\*\[[A-D]\.\]\{\.underline\}\*\*', '', match)
        
        m1 += 1
        question_ans = os.path.join('Ans_data', f'Câu{m1}')   # Create a folder named 'Câu{m1}' in 'Ans_data'
        os.makedirs(question_ans, exist_ok=True)
        
        ans_file_path = os.path.join(question_ans, 'ans.md') # Create a file named 'ans.md' in the 'Câu{m1}' folder

        for choice_index, choice_content in enumerate(choices):
            ans_letter = chr(65 + choice_index)  # Convert 0, 1, 2, 3 to A, B, C, D
            
            # Remove the formatting and store the choice in the ans_file
            choice_text = re.sub(r'\*\*\[([A-D])\.\]\{\.underline\}\*\*', r'\1', choice_content)
            with open(ans_file_path, 'a', encoding='utf-8') as choice_file:
                choice_file.write(f"{choice_text}\n")
                