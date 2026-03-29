# Contact Book Application

A simple contact book application built with Python and Tkinter. This application allows users to manage their contacts through a graphical user interface, with data stored persistently in a JSON file.

## Features

- **Add Contacts**: Enter name, phone number, and email to add new contacts
- **View Contacts**: Display all stored contacts in a scrollable list
- **Edit Contacts**: Select and modify existing contact information
- **Delete Contacts**: Remove contacts with confirmation
- **Search Contacts**: Find contacts by name or phone number
- **Persistent Storage**: All data is saved to a JSON file (`contacts.json`)

## Requirements

- Python 3.6 or higher
- Tkinter (included with most Python installations)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/contact-book.git
   cd contact-book
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

## Usage

Run the application:
```bash
python contact_book.py
```

The GUI window will open with the following interface:
- Input fields for name, phone, and email
- Buttons for Add, Edit, Delete, and Search operations
- A listbox displaying all contacts

### How to Use:
1. **Adding a Contact**: Fill in the fields and click "Add Contact"
2. **Editing a Contact**: Select a contact from the list, click "Edit Contact", modify the fields, then click "Update Contact"
3. **Deleting a Contact**: Select a contact and click "Delete Contact" (confirmation required)
4. **Searching Contacts**: Click "Search Contact" and enter a name or phone number

## File Structure

```
contact-book/
├── contact_book.py    # Main application file
├── contacts.json      # Contact data storage
└── README.md          # This file
```

## Data Format

Contacts are stored in JSON format:
```json
{
  "John Doe": {
    "phone": "123-456-7890",
    "email": "john@example.com"
  },
  "Jane Smith": {
    "phone": "098-765-4321",
    "email": "jane@example.com"
  }
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Screenshots

*(Add screenshots of the application here if available)*

## Support

If you encounter any issues or have questions, please open an issue on GitHub.