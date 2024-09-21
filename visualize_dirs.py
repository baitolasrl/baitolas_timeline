import os

def list_project_structure_tree(root_dir, indent_level=0):
    indent = '  ' * indent_level  

    for dirpath, dirnames, filenames in os.walk(root_dir):
        filenames = [f for f in filenames if not f.endswith('.csv')]

        print(f"{indent}{os.path.basename(dirpath)}")

        for dirname in dirnames:
            print(f"{indent}├── {dirname}")

        for filename in filenames:
            print(f"{indent}└── {filename}")

        for dirname in dirnames:
            subdir = os.path.join(dirpath, dirname)
            list_project_structure_tree(subdir, indent_level + 1)
        break 

project_root = os.path.dirname(os.path.abspath(__file__))
list_project_structure_tree(project_root)
