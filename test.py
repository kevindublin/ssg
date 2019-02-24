import glob
source_files = glob.glob("content/*.html")
print(source_files)

import os
file_path = "content/blog.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)
