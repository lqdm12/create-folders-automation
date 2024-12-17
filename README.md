# README for Folder Creation Script

## Overview

This script automates the creation of a nested folder structure based on a defined hierarchical organization. It uses Python's `os` module to dynamically generate directories and subdirectories, making it particularly useful for organizing educational resources, project files, or any structured data.

---

## Features

- **Recursive Folder Creation**: Creates folders and subfolders based on a nested dictionary structure.
- **Flexible Structure**: Supports a mix of dictionaries (for nested folders) and lists (for collections of subfolders).
- **Customizable Base Path**: Define the root directory where the structure will be created.
- **Error Handling**: Ensures folders are created only if they don’t already exist.

---

## Usage

### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Copy the script to your local environment.
2. Modify the `materias` dictionary to reflect your desired folder structure.
3. Set the `base_path` variable to the root directory where the folders should be created.
4. Run the script using:

   ```bash
   python script_name.py
   ```

---

## Folder Structure Example

The `materias` dictionary provided in the script represents a detailed folder structure for educational subjects like Chemistry, Biology, Physics, and others. Below is a simplified example:

```plaintext
materias_ensino/
├── Química/
│   ├── Materiais: suas propriedades e uso/
│   │   ├── Estados físicos da matéria e mudanças de estado/
│   │   ├── Fenômenos físicos e químicos/
│   │   └── ...
│   └── Átomo/
│       ├── Teorias e modelos atômicos dos átomos/
│       └── ...
├── Biologia/
│   ├── Bases da Biologia Molecular/
│   │   ├── Glicídios e Lipídios/
│   │   └── ...
│   └── ...
└── Matemática/
    ├── Conhecimentos Numéricos/
    │   ├── Razão e Proporção/
    │   └── ...
    └── ...
```

---

## Customization

- **Folder Names**: Adjust the keys and values in the `materias` dictionary.
- **Base Path**: Update the `base_path` variable to change the root directory.
- **Additional Logic**: Extend the script to create files or add content to the folders.

---

## Code Description

### Key Function

```python
def create_nested_folders(base_path, structure):
    """
    Recursively create folders based on a nested dictionary structure.
    """
```

This function takes two arguments:
1. `base_path`: The root directory for folder creation.
2. `structure`: A dictionary defining the folder hierarchy.

It iterates through the structure and creates folders recursively.

---

## Output

After running the script, a folder structure like the one defined in the `materias` dictionary will be created under the specified `base_path`. A confirmation message will be printed upon successful completion:

```plaintext
Folder structure created successfully in 'materias_ensino'!
```

---

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute.

---

## Contributions

Contributions are welcome! If you have suggestions for improvements, please submit an issue or a pull request on GitHub.

