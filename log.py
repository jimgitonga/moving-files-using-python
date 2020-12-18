


from pathlib import Path
import shutil
import os
basepath = Path("uhuru/")
target_file='jiyeueu/'
isdir = os.path.isdir(target_file)  
print(isdir)
if isdir:
    pass
else:
    os.mkdir(target_file)
    
files_in_basepath = basepath.iterdir()
file_names = os.listdir(basepath)
print(os.listdir(target_file))
for item in files_in_basepath:
    if item.name not in os.listdir(target_file):
        shutil.move(os.path.join(basepath, item.name),  target_file)
    else:
        continue
        
        
