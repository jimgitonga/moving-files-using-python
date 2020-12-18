# from pynput.keyboard import Key, Listener
# import logging

# log_dir = ""

# logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
# 	level=logging.DEBUG, format='%(asctime)s: %(message)s')

# def on_press(key):
#     logging.info(str(key))

# with Listener(on_press=on_press) as listener:
#     listener.join()
# n=1
# p=0
# count=0
# while n>0:
#     n=n/2
#     print(n)
#     count+=1
# print(f'the final value of count is {count}')


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
        
        
        
    
    # if item.is_file():
        
    #     print(item)
        
    #     with open('uhuruBooks.txt',"a") as file:
    #         file.write(f'{item.name}')
    
                           
# file_names = os.listdir(basepath)    
# print(file_names)
# for file_name in file_names:
#     shutil.move(os.path.join(basepath, file_name),  target_file)
    
    
    
# names=['jim','ann','ken','carol','peter','zack','mary','betty','ann']

# print(sorted(names))


  
# import itertools 
  
  
# a_list = [("Animal", "cat"),  
#           ("Animal", "dog"),  
#           ("Bird", "peacock"),  
#           ("Bird", "pigeon")] 
  
  
# an_iterator = itertools.groupby(a_list, lambda x : x[0]) 
  
# for key, group in an_iterator: 
#     key_and_group = list(group) 
#     print(key_and_group) 