import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            return f"Contact {name} already exists."
        self.contacts[name] = {'phone': phone, 'email': email}
        self.save_contacts()
        return f"Contact {name} added successfully."

    def view_contacts(self):
        if not self.contacts:
            return "No contacts found."
        result = ""
        for name, info in self.contacts.items():
            result += f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}\n"
        return result.strip()

    def search_contact(self, query):
        found = []
        for name, info in self.contacts.items():
            if query.lower() in name.lower() or query in info['phone']:
                found.append(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        if not found:
            return "No contacts found matching the query."
        return "\n".join(found)

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            return f"Contact {name} deleted successfully."
        return f"Contact {name} not found."

    def edit_contact(self, name, phone, email):
        if name in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email}
            self.save_contacts()
            return f"Contact {name} updated successfully."
        return f"Contact {name} not found."

class ContactBookGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Book")
        self.geometry("600x500")
        self.book = ContactBook('contacts.json')

        # Create frames
        self.input_frame = tk.Frame(self)
        self.input_frame.pack(pady=10)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)

        self.list_frame = tk.Frame(self)
        self.list_frame.pack(pady=10)

        # Input fields
        tk.Label(self.input_frame, text="Name:").grid(row=0, column=0, sticky='e')
        self.name_entry = tk.Entry(self.input_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5)

        tk.Label(self.input_frame, text="Phone:").grid(row=1, column=0, sticky='e')
        self.phone_entry = tk.Entry(self.input_frame, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5)

        tk.Label(self.input_frame, text="Email:").grid(row=2, column=0, sticky='e')
        self.email_entry = tk.Entry(self.input_frame, width=30)
        self.email_entry.grid(row=2, column=1, padx=5)

        # Buttons
        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit Contact", command=self.edit_contact)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=0, column=3, padx=5)

        # Listbox and scrollbar
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contacts_listbox = tk.Listbox(self.list_frame, width=60, height=15, yscrollcommand=self.scrollbar.set)
        self.contacts_listbox.pack(side=tk.LEFT)

        self.scrollbar.config(command=self.contacts_listbox.yview)

        self.load_contacts_to_listbox()

    def load_contacts_to_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for name, info in self.book.contacts.items():
            self.contacts_listbox.insert(tk.END, f"{name} - {info['phone']} - {info['email']}")

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        if not name or not phone or not email:
            messagebox.showerror("Error", "All fields are required.")
            return
        message = self.book.add_contact(name, phone, email)
        if "added successfully" in message:
            self.load_contacts_to_listbox()
            self.clear_entries()
        messagebox.showinfo("Info", message)

    def edit_contact(self):
        selected = self.contacts_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a contact to edit.")
            return
        index = selected[0]
        contact_text = self.contacts_listbox.get(index)
        name = contact_text.split(" - ")[0]
        info = self.book.contacts[name]
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, info['phone'])
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, info['email'])
        # Change add button to update
        self.add_button.config(text="Update Contact", command=self.update_contact)

    def update_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        if not name or not phone or not email:
            messagebox.showerror("Error", "All fields are required.")
            return
        message = self.book.edit_contact(name, phone, email)
        if "updated successfully" in message:
            self.load_contacts_to_listbox()
            self.clear_entries()
            self.add_button.config(text="Add Contact", command=self.add_contact)
        messagebox.showinfo("Info", message)

    def delete_contact(self):
        selected = self.contacts_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a contact to delete.")
            return
        index = selected[0]
        contact_text = self.contacts_listbox.get(index)
        name = contact_text.split(" - ")[0]
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}?"):
            message = self.book.delete_contact(name)
            self.load_contacts_to_listbox()
            messagebox.showinfo("Info", message)

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name or phone to search:")
        if query:
            result = self.book.search_contact(query)
            if "No contacts found" in result:
                messagebox.showinfo("Search Result", result)
            else:
                messagebox.showinfo("Search Result", result)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

def main():
    app = ContactBookGUI()
    app.mainloop()

if __name__ == "__main__":
    main()