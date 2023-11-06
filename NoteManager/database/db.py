import sqlite3
import os


class DataBase:
    def __init__(self) -> None:
        if not os.path.exists('database'):
            os.mkdir('database')
        self.connector = sqlite3.connect("database/db.sqlite")
        self.cursor = self.connector.cursor()
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        content TEXT
                    )
                ''')
        self.connector.commit()

    def add_note(self, title: str, content: str) -> None:
        """
        Add a note to the database

        :param title: Note title.
        :param content: Content for note.
        """
        self.cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        self.connector.commit()

    def get_note(self, id_note: int) -> tuple:
        """
        Get a note by id in the database

        :param id_note: Note id.
        """
        self.cursor.execute("SELECT title, content FROM notes WHERE id = ?", (id_note,))
        note = self.cursor.fetchone()
        return note

    def search_notes_by(self, by: str, value: str) -> list[tuple]:
        """
        Search a note by title or content like value

        :param by: title or content.
        :param value: the keyword by which the search is performed.
        """
        self.cursor.execute(
            f"SELECT id, title FROM notes WHERE {'title' if by == 'title' else 'content'} LIKE ?",
            (f"%{value}%",)
        )
        notes = self.cursor.fetchall()
        return notes

    def all_notes(self) -> list[tuple]:
        """
        Get all notes from database
        """
        self.cursor.execute("SELECT id, title FROM notes")
        notes = self.cursor.fetchall()
        return notes

    def delete_note(self, id_note: int) -> None:
        """
        Delete the note from database

        :param id_note: Note id.
        """
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (id_note,))
        self.connector.commit()

    def close_connection(self) -> None:
        self.cursor.close()
        self.connector.close()
