# Get every mod in a21 and wip directories and remove the "salazar-" prefix
# from the folder name.

import os

# Get the current working directory
cwd = os.getcwd()

# Get the list of directories in the current working directory
dirs = os.listdir(cwd)

# Loop through the directories
for dir in dirs:
    # Check if the directory name starts with "salazar-"
    if dir.startswith("salazar-"):
        # Get the new directory name
        new_dir = dir[8:]
        # Rename the directory
        os.rename(dir, new_dir)
        # Print the old and new directory names
        print(dir + " -> " + new_dir)

print('Done!')