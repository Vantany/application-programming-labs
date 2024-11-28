import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from main_window_ui import Ui_MainWindow
from iterator import ImgIterator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.iterator = None

        self.ui.selectFolderButton.clicked.connect(self.select_file)
        self.ui.nextImageButton.clicked.connect(self.show_next_image)

    def select_file(self):
        """
        Метод для получения файла с аннотацией
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл с путями к изображениям", "", "Text Files (*.csv)")
        if file_path:
            self.iterator = ImgIterator(file_path)
            self.ui.imageLabel.clear()

    def show_next_image(self):
        """
        Метод для вывода следующего изображения
        """
        if self.iterator is None:
            self.ui.imageLabel.setText("Сначала выберите файл с путями!")
            return

        try:
            image_path = next(self.iterator).split()[0]
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                self.ui.imageLabel.setPixmap(pixmap.scaled(
                    self.ui.imageLabel.width(),
                    self.ui.imageLabel.height(),
                    aspectRatioMode=True
                ))
            else:
                self.ui.imageLabel.setText(f"Невозможно загрузить изображение: {image_path}")
        except StopIteration:
            self.ui.imageLabel.setText("Конец списка изображений!")
            self.iterator.reset()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())