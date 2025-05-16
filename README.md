# Auto Copy Files from Home and Desktop (Windows Only)

This project creates a Windows-only executable that, when run, automatically copies all files from your **Home** and **Desktop** directories to a specified destination. The executable is built using [PyInstaller](https://pyinstaller.org/).

## Features

- **Windows only:** The script will not run on other operating systems.
- Copies all files (not directories) from:
  - Home directory (e.g., `C:\Users\YourName\`)
  - Desktop directory (e.g., `C:\Users\YourName\Desktop\`)
- Overwrites files with the same name in the destination.
- No additional setup: just run the executable.

## How to Build (for Developers)

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Edit the Script**

   - Set your desired `destination_dir` in `auto_copy.py` (e.g. `r"C:\Backup\CopiedFiles"`).

3. **Build the Executable**
   ```bash
   pyinstaller --onefile auto_copy.py
   ```
   - The executable will be found in the `dist` directory.

## How to Use

- **Run the executable:**  
  Double-click or run from a terminal on Windows.  
  All files from Home and Desktop will be copied automatically to your destination folder.

## Script

See `auto_copy.py` in this repository.

## Notes

- The script only copies files in the top level of Home and Desktop, not subfolders.
- Edit the `destination_dir` variable to set your preferred destination.
- For advanced options (e.g., recursive copy), modify the script as needed.
