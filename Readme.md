# Note Manager

This is a simple Python application for managing and organizing your notes. The application is built using PyQt6 and
allows you to add, view, search, and delete notes. You can store notes with titles and content in a database.

## Features

- **Add a New Note**: You can add a new note by providing a title and content. The note will be saved in the database.

- **View List of All Notes**: The application displays a list of all notes along with their titles. You can select a
  note from the list to view detailed information.

- **Search for Notes**: You can search for notes by entering a keyword or phrase. The application will display a list of
  notes containing the given keyword.

- **Delete a Note**: You can select a note from the list and delete it. The note will be removed from the database.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Handle-less/note-manager.git
   ```

2. Install the required dependencies (ensure you have PyQt6 and sqlite3 (it is usually installed by default)):

    ```bash
    pip install PyQt6
    ```

3. Go to the NoteApp directory and run the application:

    ```bash
    python main.py
   ```

4. Or you can run the NoteManager.exe

## Usages

- Click "Add a Note" to create a new note with a title and content.
- Select a note from the list to view its details.
- Use the "Search" input to find notes containing a specific keyword.
- Click "Delete" to remove a selected note from the database.