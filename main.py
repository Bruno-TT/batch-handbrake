from glob import glob
from subprocess import call
from os import remove

bad_file_extensions=(".avi", ".mkv")

#folder_path=r"C:\Users\bruno\Desktop\anomalous\shared 2"
folder_path=r"C:\Users\bruno\Desktop\resilio shared"

folder_path+=r"\**\*"

files=[]
for extension in bad_file_extensions:files.extend(glob(folder_path+extension, recursive=True))

for source in files:
    for ext in bad_file_extensions:dest=source.replace(ext,".mp4")
    call(("HandBrakeCLI", "-i", source, "-o", dest))
    remove(source)
