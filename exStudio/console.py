import sys
from PySide6 import QtCore, QtGui, QtWidgets


class PythonConsole(QtWidgets.QPlainTextEdit):
    def __init__(self):
        super().__init__()

        self.document().setPlainText(">>> ")

        self.cursorPositionChanged.connect(self.on_cursor_position_changed)

    def on_cursor_position_changed(self):
        cursor = self.textCursor()

        if cursor.positionInBlock() == 0:
            cursor.insertText(">>> ")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter:
            print("Entered")
            text = self.toPlainText().replace(">>> ", "").strip()
            print(text)

            # Execute the Python code in the text variable
            print(exec(text))  # exec(text)

            self.document().setPlainText(">>> ")

        super().keyPressEvent(event)


app = QtWidgets.QApplication(sys.argv)

console = PythonConsole()
console.show()

app.exec()
