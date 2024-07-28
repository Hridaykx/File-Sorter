import os, shutil

path = r"C:/Users/hrida/html_css_course/"
file_name = os.listdir(path)
folder_names = ['indices', 'stylesheets', 'scripts']

for loop in range(0, 3):
    if not os.path.exists(path + folder_names[loop]):
        # print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if ".html" in file and not os.path.exists(path + "indices" + file):
        shutil.move(path + file, path + "indices/" + file)
    elif ".css" in file and not os.path.exists(path + "stylesheets" + file):
        shutil.move(path + file, path + "stylesheets/" + file)
    elif ".js" in file and not os.path.exists(path + "scripts" + file):
        shutil.move(path + file, path + "scripts/" + file)

