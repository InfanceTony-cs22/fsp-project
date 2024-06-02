import tkinter as tk
from tkinter import scrolledtext

class FileSystem:
    def __init__(self):
        self.files = {}
        self.directories = {'/': []}
        self.projects = {}

    def create_file(self, path, content=''):
        if path in self.files:
            return f"File '{path}' already exists."
        else:
            directory = '/'.join(path.split('/')[:-1])
            if directory == '':
                directory = '/'
            if directory not in self.directories:
                return f"Directory '{directory}' does not exist."
            else:
                self.files[path] = content
                self.directories[directory].append(path)
                return f"File '{path}' created."

    def delete_file(self, path):
        if path in self.files:
            directory = '/'.join(path.split('/')[:-1])
            if directory == '':
                directory = '/'
            self.directories[directory].remove(path)
            del self.files[path]
            return f"File '{path}' deleted."
        else:
            return f"File '{path}' does not exist."

    def read_file(self, path):
        if path in self.files:
            return self.files[path]
        else:
            return f"File '{path}' does not exist."

    def write_file(self, path, content):
        if path in self.files:
            self.files[path] = content
            return f"Written to '{path}'."
        else:
            return f"File '{path}' does not exist."

    def create_directory(self, path):
        if path in self.directories:
            return f"Directory '{path}' already exists."
        else:
            parent_directory = '/'.join(path.split('/')[:-1])
            if parent_directory == '':
                parent_directory = '/'
            if parent_directory not in self.directories:
                return f"Parent directory '{parent_directory}' does not exist."
            else:
                self.directories[path] = []
                self.directories[parent_directory].append(path)
                return f"Directory '{path}' created."

    def list_directory(self, path):
        if path in self.directories:
            return '\n'.join(self.directories[path])
        else:
            return f"Directory '{path}' does not exist."

    def create_project(self, project_name):
        if project_name in self.projects:
            return f"Project '{project_name}' already exists."
        else:
            project_path = f'/{project_name}'
            self.projects[project_name] = project_path
            return self.create_directory(project_path)

    def list_projects(self):
        return '\n'.join(self.projects.keys())

    def list_project_contents(self, project_name):
        if project_name in self.projects:
            project_path = self.projects[project_name]
            return self.list_directory(project_path)
        else:
            return f"Project '{project_name}' does not exist."

class FileSystemGUI:
    def __init__(self, root, fs):
        self.fs = fs
        self.root = root
        self.root.title("File System Simulator")

        self.project_label = tk.Label(root, text="Project Name")
        self.project_label.grid(row=0, column=0, padx=5, pady=5)

        self.project_entry = tk.Entry(root)
        self.project_entry.grid(row=0, column=1, padx=5, pady=5)

        self.create_project_button = tk.Button(root, text="Create Project", command=self.create_project)
        self.create_project_button.grid(row=0, column=2, padx=5, pady=5)

        self.list_projects_button = tk.Button(root, text="List Projects", command=self.list_projects)
        self.list_projects_button.grid(row=0, column=3, padx=5, pady=5)

        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.output_text.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        self.file_label = tk.Label(root, text="File Name")
        self.file_label.grid(row=2, column=0, padx=5, pady=5)

        self.file_entry = tk.Entry(root)
        self.file_entry.grid(row=2, column=1, padx=5, pady=5)

        self.file_content_label = tk.Label(root, text="File Content")
        self.file_content_label.grid(row=3, column=0, padx=5, pady=5)

        self.file_content_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=5)
        self.file_content_text.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

        self.create_file_button = tk.Button(root, text="Create File", command=self.create_file)
        self.create_file_button.grid(row=4, column=0, padx=5, pady=5)

        self.read_file_button = tk.Button(root, text="Read File", command=self.read_file)
        self.read_file_button.grid(row=4, column=1, padx=5, pady=5)

        self.write_file_button = tk.Button(root, text="Write File", command=self.write_file)
        self.write_file_button.grid(row=4, column=2, padx=5, pady=5)

        self.delete_file_button = tk.Button(root, text="Delete File", command=self.delete_file)
        self.delete_file_button.grid(row=4, column=3, padx=5, pady=5)

        self.list_project_contents_button = tk.Button(root, text="List Project Contents", command=self.list_project_contents)
        self.list_project_contents_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

    def create_project(self):
        project_name = self.project_entry.get()
        if project_name:
            result = self.fs.create_project(project_name)
            self.output_text.insert(tk.END, result + '\n')

    def list_projects(self):
        result = self.fs.list_projects()
        self.output_text.insert(tk.END, "Projects:\n" + result + '\n')

    def create_file(self):
        project_name = self.project_entry.get()
        file_name = self.file_entry.get()
        content = self.file_content_text.get("1.0", tk.END).strip()
        if project_name and file_name:
            file_path = f'/{project_name}/{file_name}'
            result = self.fs.create_file(file_path, content)
            self.output_text.insert(tk.END, result + '\n')

    def read_file(self):
        project_name = self.project_entry.get()
        file_name = self.file_entry.get()
        if project_name and file_name:
            file_path = f'/{project_name}/{file_name}'
            result = self.fs.read_file(file_path)
            self.output_text.insert(tk.END, f"Reading {file_path}:\n" + result + '\n')

    def write_file(self):
        project_name = self.project_entry.get()
        file_name = self.file_entry.get()
        content = self.file_content_text.get("1.0", tk.END).strip()
        if project_name and file_name:
            file_path = f'/{project_name}/{file_name}'
            result = self.fs.write_file(file_path, content)
            self.output_text.insert(tk.END, result + '\n')

    def delete_file(self):
        project_name = self.project_entry.get()
        file_name = self.file_entry.get()
        if project_name and file_name:
            file_path = f'/{project_name}/{file_name}'
            result = self.fs.delete_file(file_path)
            self.output_text.insert(tk.END, result + '\n')

    def list_project_contents(self):
        project_name = self.project_entry.get()
        if project_name:
            result = self.fs.list_project_contents(project_name)
            self.output_text.insert(tk.END, f"Contents of {project_name}:\n" + result + '\n')

if __name__ == "__main__":
    fs = FileSystem()
    root = tk.Tk()
    app = FileSystemGUI(root, fs)
    root.mainloop()
