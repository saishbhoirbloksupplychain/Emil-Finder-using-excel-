import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
from excel_handler import load_companies


class EmailFinderGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Email Finder Pro")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.file_path = ""
        self.data = None
        self.running = False

        # ==========================
        # Title
        # ==========================

        title = tk.Label(
            root,
            text="Email Finder Pro",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=15)

        # ==========================
        # File Selection
        # ==========================

        top_frame = tk.Frame(root)
        top_frame.pack(pady=10)

        self.file_label = tk.Label(
            top_frame,
            text="No Excel file selected",
            width=60,
            anchor="w"
        )

        self.file_label.grid(row=0, column=0, padx=10)

        browse_btn = tk.Button(
            top_frame,
            text="Browse",
            width=12,
            command=self.browse_file
        )

        browse_btn.grid(row=0, column=1)

        # ==========================
        # Progress Bar
        # ==========================

        self.progress = ttk.Progressbar(
            root,
            orient="horizontal",
            mode="determinate",
            length=700
        )

        self.progress.pack(pady=20)

        self.progress_label = tk.Label(
            root,
            text="0 / 0"
        )

        self.progress_label.pack()

        # ==========================
        # Buttons
        # ==========================

        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        self.start_btn = tk.Button(
            button_frame,
            text="Start Search",
            width=18,
            command=self.start_search
        )

        self.start_btn.grid(row=0, column=0, padx=15)

        self.stop_btn = tk.Button(
            button_frame,
            text="Stop",
            width=18,
            state="disabled",
            command=self.stop_search
        )

        self.stop_btn.grid(row=0, column=1)

        # ==========================
        # Log Box
        # ==========================

        self.log = tk.Text(
            root,
            width=95,
            height=18
        )

        self.log.pack(pady=10)

        # ==========================
        # Bottom Button
        # ==========================

        self.open_btn = tk.Button(
            root,
            text="Open Results Folder",
            command=self.open_results
        )

        self.open_btn.pack(pady=10)
        # ==========================
    # Browse Excel File
    # ==========================

    def browse_file(self):

        file = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[
                ("Excel Files", "*.xlsx *.xls")
            ]
        )

        if file:

            self.file_path = file

            self.file_label.config(
                text=os.path.basename(file)
            )

            self.write_log(f"Selected file : {file}")

    # ==========================
    # Start Search
    # ==========================

    def start_search(self):

        if self.file_path == "":
            messagebox.showwarning(
                "Warning",
                "Please select an Excel file first."
            )
            return

        try:

            self.data = load_companies(self.file_path)

            total = len(self.data)

            self.progress["maximum"] = total
            self.progress["value"] = 0

            self.progress_label.config(
                text=f"0 / {total}"
            )

            self.running = True

            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")

            self.write_log("--------------------------------")
            self.write_log(f"Loaded {total} companies.")
            self.write_log("Email search will start in Part 3.")
            self.write_log("--------------------------------")

            threading.Thread(
                target=self.demo_progress,
                daemon=True
            ).start()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================
    # Demo Progress
    # ==========================

    def demo_progress(self):

        total = len(self.data)

        for i in range(total):

            if not self.running:
                break

            self.progress["value"] = i + 1

            self.progress_label.config(
                text=f"{i+1} / {total}"
            )

            self.root.update_idletasks()

            import time
            time.sleep(0.02)

        self.running = False

        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")

        self.write_log("Finished.")

    # ==========================
    # Stop Search
    # ==========================

    def stop_search(self):

        self.running = False

        self.write_log("Search stopped by user.")

        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        # ==========================
    # Write Log
    # ==========================

    def write_log(self, text):

        self.log.insert(tk.END, text + "\n")
        self.log.see(tk.END)

    # ==========================
    # Open Results Folder
    # ==========================

    def open_results(self):

        folder = "output"

        if not os.path.exists(folder):
            os.makedirs(folder)

        try:
            os.startfile(folder)
        except AttributeError:
            messagebox.showinfo(
                "Folder",
                f"Results folder:\n{os.path.abspath(folder)}"
            )


# ==========================
# Main Program
# ==========================

if __name__ == "__main__":

    root = tk.Tk()

    app = EmailFinderGUI(root)

    root.mainloop()
