import os

filename = "demo_file.txt"

# print(f"--- 1. WRITING TO A FILE ('w' mode) ---")
# # The 'with' statement is a Context Manager.
# # It automatically closes the file even if errors occur.
# # 'w' mode overwrites the file if it exists, or creates it if it doesn't. 'r' -> read, 'a' -> append
# with open(filename, 'w', encoding='utf-8') as f:
#     f.write("Line 1: Python is versatile.\n")
#     f.write("Line 2: Input/Output operations are essential.\n")
#     # writelines takes a list of strings
#     f.write("Line 3: This was written using basic write().\n")
#     print(f"Successfully wrote data to '{filename}'")

# print(f"\n--- 2. APPENDING TO A FILE ('a' mode) ---")
# # 'a' mode adds data to the end without deleting existing content.
# with open(filename, 'a', encoding='utf-8') as f:
#     f.write("Line 4: This line was appended later.\n")
#     print("Successfully appended a new line.")

# print(f"\n--- 3. READING FROM A FILE ('r' mode) ---")
# # 'r' is the default mode.
# with open(filename, 'r', encoding='utf-8') as f:
#     # Method A: read() gets the whole file as a single string
#     full_content = f.read()
#     print("A) FULL CONTENT READ:")
#     print(full_content.strip())  # .strip() removes the last extra newline for clean printing
#
#     print("-" * 20)
#
#     # Method B: seek() and readline()
#     # Because we read the file above, the cursor is at the end. We must reset it.
#     f.seek(0)  # Move cursor back to the start (byte 0)
#
#     print("B) READING LINE BY LINE:")
#     # You can iterate over the file object directly
#     line_number = 1
#     for line in f:
#         # line includes the \n, so we use end='' in print to avoid double spacing
#         print(f"   Reading loop {line_number}: {line}", end='')
#         line_number += 1
#
print(f"\n\n--- 4. HANDLING ERRORS (Try/Except) ---")
try:
    # Trying to read a file that usually doesn't exist
    with open(".\\sample\\ghost_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error Caught: The file 'ghost_file.txt' does not exist.")
except PermissionError:
    print("Error Caught: You do not have permission to read this file.")

# print(f"\n--- 5. CLEANUP ---")
# # Removing the file we created to keep your computer clean
# if os.path.exists(filename):
#     os.remove(filename)
#     print(f"Cleanup: '{filename}' has been deleted.")