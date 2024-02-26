from PySide6.QtWidgets import *


class MainWindow(QWidget):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("exStudio1")
        self.resize(800, 600)

        self.show()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
