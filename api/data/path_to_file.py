import os


class PathToFile:
    PATH_TO_PHOTO = os.path.normpath(os.getcwd() + os.sep + r"\test\data_api\picture\picture.jpg")
    PATH_TO_PHOTO_DOWNLOAD = os.path.normpath(os.getcwd() + os.sep + r"\test\data_api\picture\picture2.jpg")
