import os

def count_folders(directory = r'E:\GENER\upload_file\OUTPUT_FILE\Ans_data'):
    # Get the list of items in the directory
    items = os.listdir(directory)
    
    # Initialize a counter for the folders
    folder_count = 0
    
    # Iterate over each item
    for item in items:
        # Check if the item is a directory
        if os.path.isdir(os.path.join(directory, item)):
            # If it is, increment the folder counter
            folder_count += 1
    
    # Return the final folder count
    return folder_count