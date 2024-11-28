import os
import csv

class ImgIterator:
    def __init__(self, annotation_path: str):
        """
        Считывает строки из файла с аннотациями,
        после чего заполняет соотвествующие поля
        
        :param annotation_path: путь к файлу"""

        with open(annotation_path, "r") as file:
            reader = csv.reader(file)
            self.data = [row for row in reader]
            self.limit = len(self.data)
            self.counter = 0


    def __iter__(self):
        return self


    def __next__(self):
        """Итерируется по массиву и прибавляет
        единицу к счетчику"""
        
        if self.counter < self.limit:
            self.counter += 1
            return " ".join(self.data[self.counter-1])
        else:
            raise StopIteration