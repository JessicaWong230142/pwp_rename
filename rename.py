import os
import re

#open folder
def open_folder(folder_path):
  files = os.listdir(folder_path)
  file_list = []
  for file in files:
    file_list.append(file)
  file_list = sorted(file_list)
  return file_list



#get a list of new names of files
def get_new_names(file_list):
  new_names = []
  for file in file_list:
    new_query = re.search(r'\d+\.JPG',file)
    next_name = new_query.group()
    next_name = next_name.split(".")
    if file.startswith("IMG"):
      new_name = "PWP2024_000" + next_name[0] + "J_JESSICA." + next_name[1]
    elif file.startswith("MMA"):
      new_name = "PWP2024_000" + next_name[0] + "Je_JESSICA." + next_name[1]
    elif file.startswith("SM"):
      new_name = "PWP2024_000" + next_name[0] + "Jes_JESSICA." + next_name[1]
    elif file.startswith("WJ2"):
      new_name = "PWP2024_000" + next_name[0] + "Jess_JESSICA." + next_name[1]
    new_names.append(new_name)
  return new_names



#Align the list of new names with the list of old names
def align_names(final_names):
  i = []
  m = []
  s = []
  w = []
  final_list = []
  for name in final_names:
    split_name = name.split("_")
    if split_name[1].endswith("Jess"):
      w.append(name)
      w.sort()
    elif split_name[1].endswith("Jes"):
      s.append(name)
      s.sort()
    elif split_name[1].endswith("Je"):
      m.append(name)
      m.sort()
    elif split_name[1].endswith("J"):
      i.append(name)
      i.sort()
  final_list = i + m + s + w
  return final_list



#rename files
def rename(folder_path, new_names):
  old_names = open_folder(folder_path)
  counter = 0
  for file in old_names:
    if counter <= 1000:
      os.rename(folder_path + "/" + file, folder_path + "/" + new_names[counter])
      counter += 1
    else:
      break
