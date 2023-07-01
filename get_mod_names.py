# For each dir in a21/, get the dir name and print it in a file
# Usage: python get_mod_names.py
# Output: mods_to_load.txt

import os

# Get the current working directory
cwd = os.getcwd()

# Rewrite the output file
with open("mods_to_load.txt", "w") as f:
    f.write("")
    f.close()

# Open the output file
with open("mods_to_load.txt", "a") as f:
    # For each dir in cwd/a21/
    for dir in os.listdir(cwd + "/a21"):
        # Write the dir name to the output file
        f.write(dir + "\n")
    f.close()

# Print a message
print("Done!")