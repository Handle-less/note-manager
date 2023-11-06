import sys
from PyQt6.QtWidgets import QMainWindow, QApplication

from NoteManager.database.db import DataBase
from NoteManager.src.ui.ui_main import Ui_NoteManager


class NoteApp(QMainWindow):
    def __init__(self) -> None:
        super(NoteApp, self).__init__()
        self.ui = Ui_NoteManager()
        self.ui.setupUi(self)

        self.DataBase = DataBase()

        self.ui.listWidget_noteLists.itemClicked.connect(self.view_note)

        self.ui.pushButton_addNote.clicked.connect(self.add_note)
        self.ui.pushButton_all_note.clicked.connect(self.load_notes)
        self.ui.pushButton_searchTitle.clicked.connect(lambda: self.search_note('title'))
        self.ui.pushButton_searchContent.clicked.connect(lambda: self.search_note('content'))
        self.ui.pushButton_deleteNote.clicked.connect(self.delete_note)

        self.load_notes()

    def add_note(self) -> None:
        title: str = self.ui.lineEdit_title.text()
        content: str = self.ui.textEdit_content.toPlainText()
        if title and content:
            self.DataBase.add_note(title=title, content=content)
            self.ui.lineEdit_title.clear()
            self.ui.textEdit_content.clear()
            self.load_notes()

    def load_notes(self) -> None:
        self.ui.listWidget_noteLists.clear()
        notes: list[tuple] = self.DataBase.all_notes()
        for note in notes:
            self.ui.listWidget_noteLists.addItem(f'{note[0]}. {note[1]}')

    def view_note(self, item) -> None:
        id_note: int = int(item.text().split('.')[0])
        note: tuple = self.DataBase.get_note(id_note=id_note)
        if note:
            self.ui.label_note.setText(
                "Title:\n"
                f"{note[0]}\n\n"
                "Content:\n"
                f"{note[1]}"
            )

    def search_note(self, by: str) -> None:
        notes: list[tuple] = self.DataBase.search_notes_by(by=by, value=self.ui.lineEdit_search.text())
        self.ui.listWidget_noteLists.clear()
        for note in notes:
            self.ui.listWidget_noteLists.addItem(f'{note[0]}. {note[1]}')

    def delete_note(self) -> None:
        item = self.ui.listWidget_noteLists.currentItem()
        if item:
            id_note = item.text().split('.')[0]
            self.DataBase.delete_note(id_note=id_note)
            self.load_notes()
            self.ui.label_note.clear()

    def close(self) -> None:
        self.DataBase.close_connection()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()

    sys.exit(app.exec())

