from glob import glob
from subprocess import call
from os import remove

#the file extensions we want to convert from
bad_file_extensions=(".avi", ".mkv")

#laptop
folder_path=r"C:\Users\bruno\Desktop\anomalous\shared 2"

#LR-PC
#folder_path=r"C:\Users\bruno\Desktop\resilio shared"

#always run
folder_path+=r"\**\*"

#the list of all source file paths
files=[]

#for each bad extension, find all files with that extension and add them to the files list
for extension in bad_file_extensions:files.extend(glob(folder_path+extension, recursive=True))

#for each source file
for source in files:

    #this could be neater/more effecient, but we replace the file extension with .mp4
    for ext in bad_file_extensions:dest=source.replace(ext,".mp4")

    #blocking, fully utilises cpu so no need to thread
    #use the handbrake commandline interface to convert the file
    call(("HandBrakeCLI", "-i", source, "-o", dest))

    #delete the source file - the above line is blocking, so this is only done once the file has been fully converted
    remove(source)
