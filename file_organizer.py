import os
import shutil

class Organize:
    images = ["jpg","jfif","jpeg","png","gif","tiff"]
    audio = ["mp3","wav","m4a"]
    video = ["mp4","mov","avi","wmv"]
    exe = ["exe","aa"]
    documents =["ppt","pttx","doc","docx","xls","xlsx","txt","pdf"]
    directories = ["images","audios","videos","documents","exe"]
    sub_directories_of_documents = ["power point","excel","word","pdf","txt"]
    __path =""
    types = {
        "documents":documents,
        "images":images,
        "videos":video,
        "audios":audio,
        "exe":exe,
    }
    sub = {
            "power point":["ppt","pptx"],
            "excel":["xls","xlsx"],
            "word":["doc","docx"],
            "pdf":"pdf",
            "txt":"txt"
        }
    def __init__(self) -> None:
        pass
       
    def set_path(self,path):
        self.__path = path

    def CreateDirectory(self):
        for i in self.directories:
            directory_path = self.__path +"\\"+i
            if os.path.isdir(directory_path)==False:
                os.mkdir(directory_path)
    
        for i in self.sub_directories_of_documents:
            directory_path = self.__path+"\\"+"documents"+"\\"+i
            if os.path.isdir(directory_path)==False:
                os.mkdir(directory_path)

    def organize(self):
            for i in os.listdir(self.__path):
                if(os.path.isfile(self.__path+"\\"+i)):
                    ext = i.split(".")[1]
                    for j in self.types:
                        if (ext in self.types[j]) and (ext in self.documents):
                            for k in self.sub:
                                if ext in self.sub[k]:
                                    shutil.move(self.__path+"\\"+i,self.__path+ "\\" + j + "\\" + k + "\\")
                                    break
                            break
                        elif ext in self.types[j]:
                            shutil.move(self.__path+"\\"+i,self.__path+"\\"+j+"\\")
                            break
    def check_path(self):
        if(os.path.isdir(self.__path)):
            return True
        return False

