from tkinter import ttk

import tkinter as tk

import sqlite3




def connect():

    conn = sqlite3.connect("entretient.sq3")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS carburant(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            now DATE,
            Lieux TEXT,
            ODO FLOAT,
            Litre FLOAT,
            PRIX INTEGER,
            ECART FLOAT
)
""")
    conn.commit()

    conn.close()


def View():

    conn = sqlite3.connect("entretient.sq3")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM carburant")

    rows = cursor.fetchall()    

    for row in rows:

        print(row) 

        tree.insert("", tk.END, values=row)        

    conn.close()


# connect to the database

connect() 

root = tk.Tk()

root.title("Maintenance Book")     # Add a title


tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4", "c5", "c6","c7", "c8" ), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="ID")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="DATE")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="LIEUX")

tree.column("#4", anchor=tk.CENTER)

tree.heading("#4", text="ODO")

tree.column("#5", anchor=tk.CENTER)

tree.heading("#5", text="LITRE")

tree.column("#6", anchor=tk.CENTER)

tree.heading("#6", text="PRIX")

tree.column("#7", anchor=tk.CENTER)

tree.heading("#7", text="ECART")

tree.pack()

button1 = tk.Button(text="Display data", command=View)

button1.pack(pady=10)

root.mainloop()