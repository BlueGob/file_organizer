from http.server import executable
import os
import shutil
x = input("give me path ")

images = ["jpg","jfif","jpeg","png","gif","tiff"]
audio = ["mp3","wav","m4a"]
video = ["mp4","mov","avi","wmv"]
exe = ["exe","aa"]

documents =["ppt","pttx","doc","docx","xl","xlx","txt","pdf"]
directories = ["images","audioes","videoes","documents","exe"]
sub_directories_of_documents = ["power point","excel","word","pdf","txt"]
types = {
 "documents":documents,
 "images":images,
 "videoes":video,
 "audioes":audio,
 "exe":exe,
 "sub": {
     "power point":["ppt","pptx"],
     "excel":["xl","xlx"],
     "word":["doc","docx"],
     "pdf":"pdf",
     "txt":"txt"
 }
}

def createDirectories():
    for i in directories:
        directory_path = x+"\\"+i
        if os.path.isdir(directory_path)==False:
            os.mkdir(directory_path)

def createSubDirectories():
    for i in sub_directories_of_documents:
        directory_path = x+"\\"+"documents"+"\\"+i
        if os.path.isdir(directory_path)==False:
            os.mkdir(directory_path)

def organize():
    for i in os.listdir(x):
        if(os.path.isfile(x+"\\"+i)):
            ext = i.split(".")[1]
            for j in types:
                if (ext in types[j]) and (ext in documents):
                    for k in types["sub"]:
                        if ext in types["sub"][k]:
                            shutil.move(x+"\\"+i,x+ "\\" + j + "\\" + k + "\\")
                            break
                elif ext in types[j]:
                    shutil.move(x+"\\"+i,x+"\\"+j+"\\")
                    break




createDirectories()
createSubDirectories()
organize()
