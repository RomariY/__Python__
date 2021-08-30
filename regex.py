import shutil
import re
import os

# shutil.unpack_archive('/home/roman/Study/Byte_of_python/test/unzip_me_for_instructions.zip')
# with open('/home/roman/Study/Byte_of_python/test/extracted_content/Instructions.txt') as f:
#     content = f.read()
#     print(content)


def search_num(file, pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''



result = []
for folder, sub_folders, files in os.walk(os.getcwd() + '/extracted_content'):
    for f in files:
        full_path = folder + '/' + f
        result.append(search_num(full_path))
