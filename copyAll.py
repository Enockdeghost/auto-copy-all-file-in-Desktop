# import from python libraries
import os 
import shutil 

# creat a fuction for source and destination of files
def copy_files_to_usb(source_folder, destination_folder):
     if not os.path.exists(source_folder): 
        print(f"Source folder {source_folder} does not exist.") 
        return 
     if not os.path.exists(destination_folder): 
        print(f"Destination folder {destination_folder} does not exist.") 
        return 
        # create a loop for get those data one by one
     for item in os.listdir(source_folder): 
        source_item = os.path.join(source_folder, item)
        destination_item = os.path.join(destination_folder, item) 
        try: 
            # if path is exits
            if os.path.isfile(source_item):
                print(f"Copying file: {source_item}") 
                shutil.copy2(source_item, destination_item) 
            elif os.path.isdir(source_item): 
                print(f"Copying directory: {source_item}") 
                shutil.copytree(source_item, destination_item) 
        except Exception as e: print(f"Error copying {source_item}: {e}")
if __name__ == "__main__": 
    # desktop path
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    # lebel of Letter of you drive
    usb_drive_path = 'G:\\' 
    copy_files_to_usb(desktop_path, usb_drive_path) 

