import os
from pathlib import Path


while True:
    project_name = input("Enter the Src Folder Name: ")
    if project_name != '':
        break


list_of_files = [
".github/workflows/.gitkeep",
f"{project_name}/__init__.py",
f"{project_name}/components/data_ingestion.py",
f"{project_name}/components/data_preproceesing.py",
f"{project_name}/components/model_loading.py",
f"{project_name}/components/model_evaluation.py",
f"{project_name}/pipeline/inference.py",
f"{project_name}/pipeline/training.py",
f"{project_name}/exception.py",
f"{project_name}/logger.py",
"templates/index.html",
"statics/style.css",
"notebook/research.ipynb",
"init_setup.sh",
"requirements.txt",
"Dockerfile",
"app.py",
"setup.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
    if not os.path.exists(filepath):
        with open(filepath,"w") as f:
            pass
    

