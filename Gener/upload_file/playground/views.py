# views.py
import subprocess
from django.http import HttpResponse
from django.shortcuts import render
from .forms import DocumentForm

def upload_and_run_scripts(request):
    script_outputs = []
    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Define the relative paths to your Python scripts
            scripts = [
                subprocess.run(["python", "E:/GENER/Pick_ques/convert.py"]),
                subprocess.run(["python", "E:/GENER/Pick_ques/add_image.py"]),
                subprocess.run(["python", "E:/GENER/Pick_ques/main.py"]),
                subprocess.run(["python", "E:/GENER/Pick_ques/Add_ex.py"]),
                subprocess.run(["python", "E:/GENER/Pick_ques/gener/main.py"]),
                subprocess.run(["python", "E:/GENER/Pick_ques/back.py"]),
            ]
    else:
        form = DocumentForm()
        # Run the process_files.py script
    subprocess.run(['python', 'process_files.py'], text=True)

    return render(request, 'upload_and_run_scripts.html', {'form': form})

