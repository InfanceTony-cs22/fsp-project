# File System Simulator in Python

## Overview
This repository contains a Python implementation of a File System Simulator, which replicates essential functionalities of a real-world file system. It serves as an educational tool for understanding file system organization and management principles. Users can perform operations akin to those found in operating systems, gaining practical experience in managing digital assets.

## Features
- **File Management**
  - Create, delete, read, and write files within specified directories.
- **Directory Management**
  - Create directories and navigate through directory structures.
- **Project Management**
  - Organize files and directories into projects.
- **Command-Line Interface**
  - User-friendly interface for interacting with the file system.

## Components
### `FileSystem` Class
- **Purpose**
  - Entry point of the application, manages file and directory operations, and organizes projects.
- **Methods**
  - `create_file(path, content='')`: Creates a file at the specified path with optional initial content.
  - `delete_file(path)`: Deletes the file at the specified path.
  - `read_file(path)`: Retrieves the content of the file at the specified path.
  - `write_file(path, content)`: Updates the content of the file at the specified path.
  - `create_directory(path)`: Creates a directory at the specified path.
  - `list_directory(path)`: Lists files and directories in the specified directory path.
  - `create_project(project_name)`: Creates a project with the specified name, organizing related files and directories.
  - `list_projects()`: Lists all created projects.
  - `list_project_contents(project_name)`: Lists contents (files and directories) of the specified project.

### `FileSystemGUI` Class
- **Purpose**
  - Graphical User Interface (GUI) for interacting with the File System Simulator.
- **Features**
  - Widgets include labels, entry fields, buttons, and text areas for user input and output display.
- **Functionality**
  - Provides an intuitive interface for performing file system operations such as creating projects, files, directories, and managing their contents.

## Dependencies
- Python 3.x
- No external libraries beyond standard Python libraries are required.

## Future Enhancements
- Support for additional file system operations such as copy, move, and rename.
- Enhanced error handling and input validation mechanisms.
- Integration with larger systems for more comprehensive file system simulations.

## Usage
1. **Setting Up**
   - Clone the repository and ensure Python 3.x is installed.
   
2. **Creating Projects and Files**
   - Use `create_project` and `create_file` methods to organize and populate the file system.
   
3. **Performing Operations**
   - Perform read, write, delete, and list operations on files and directories.
   
4. **Using GUI**
   - Optionally use `FileSystemGUI` class for a graphical interface to interact with the simulator.

## Conclusion
This project demonstrates a basic implementation of a file system simulator in Python, providing essential functionalities for managing files, directories, and projects. It serves as an educational tool for understanding fundamental concepts in operating systems and can be expanded for more advanced simulations and applications.

## Contributors

- Infance Tony ([@InfanceTony-cs22](https://github.com/InfanceTony-cs22))

