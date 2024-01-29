import random
import string

import cv2
import requests


class Utils:
    __RUSSIAN_LETTER = "абвгдежзийклмнопрстуфхцчшщъыьэю"

    @staticmethod
    def random_text(len_text: int = 15):

        return ''.join(random.choices(
            string.ascii_letters
            + string.digits
            + Utils.__RUSSIAN_LETTER
            + Utils.__RUSSIAN_LETTER.upper(),
            k=len_text))

    @staticmethod
    def download_photo(url, path):
        """Загружает фото из url по пути path"""
        response = requests.get(url)
        with open(path, 'wb') as file:
            file.write(response.content)

    @staticmethod
    def compare_images(path_image1: str, path_image2: str):
        """
        Сравнивает 2 фото и возвращает True если фото одинаковые на 95%
        """
        img1 = cv2.imread(path_image1)
        img2 = cv2.imread(path_image2)

        if img1.size == img2.size:
            mse = ((img1 - img2) ** 2).mean()
            if mse < 5:
                return True
            else:
                return False
        else:
            return False
