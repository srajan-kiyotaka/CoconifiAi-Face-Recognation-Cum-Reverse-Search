import os


def init(rootdir = "Database"):
    root_path = rootdir
    files_name = getFileName(root_path)
    files_path = getFilePath(root_path, files_name)
    images_path = getImagePath(files_path)
    return (files_name, files_path, images_path)

def getFileName( path):
        file_name = os.listdir(path)
        return file_name
    
def getFilePath( path, file_name):
        file_path = []
        for file in file_name:
            dir_path = os.path.join(path, file)
            if os.path.isdir(dir_path):
                file_path.append(dir_path)
                
        return file_path

def getImagePath( dir_path):
        images_path = []
        for path in dir_path:
            images = os.listdir(path)
            if(len(images) >= 1):
                temp = images[0]
                images_path.append(os.path.join(path, images[0]))

        return images_path
    
