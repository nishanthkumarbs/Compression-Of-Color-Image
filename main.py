import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps
import os



class CompressionOfColorImage:
    def __init__(self, root):
        self.root = root
        self.root.title("Compression of Color Image")
        self.root.geometry("1000x600")
        self.root.configure(bg='#eaeaea')  # Light background color for a fresh look

        self.create_sidebar()
        self.create_content_area()

    def create_sidebar(self):
        sidebar = tk.Frame(self.root, bg='#393e46', width=200, height=600)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        sidebar_title = tk.Label(sidebar, text="Menu", font=("Times New Roman", 16, "bold"), bg='#393e46', fg='white')
        sidebar_title.pack(pady=20)

        home_button = tk.Button(sidebar, text="Home", font=("Times New Roman", 14), command=self.create_content_area, bg='#00adb5', fg='white')
        home_button.pack(pady=10, fill=tk.X)

        about_button = tk.Button(sidebar, text="About", font=("Times New Roman", 14), command=self.show_about, bg='#00adb5', fg='white')
        about_button.pack(pady=10, fill=tk.X)

    def create_content_area(self):
        self.clear_content()

        content_canvas = tk.Canvas(self.root, bg='#eeeeee', width=800, height=600)
        content_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        scrollbar = tk.Scrollbar(content_canvas, orient=tk.VERTICAL, command=content_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        content_frame = tk.Frame(content_canvas, bg='#eeeeee')
        content_frame.bind("<Configure>", lambda e: content_canvas.configure(scrollregion=content_canvas.bbox("all")))
        content_canvas.create_window((0, 0), window=content_frame, anchor="nw")
        content_canvas.configure(yscrollcommand=scrollbar.set)

        content_canvas.bind_all("<MouseWheel>", lambda event: content_canvas.yview_scroll(-1*(event.delta//120), "units"))

        header_label = tk.Label(content_frame, text=" Compression of Color Image", font=("Times New Roman", 24, "bold"), bg='#eeeeee', fg='#393e46')
        header_label.pack(pady=20)

        self.open_button = tk.Button(content_frame, text="Open Image", font=("Times New Roman", 14), command=self.open_image, bg='#00adb5', fg='white')
        self.open_button.pack(pady=10)

        self.img_label = tk.Label(content_frame, bg='#eeeeee')
        self.img_label.pack(pady=10)

        self.original_size_label = tk.Label(content_frame, text="Original Size : N/A", font=("Times New Roman", 12), bg='#eeeeee', fg='#393e46')
        self.original_size_label.pack(pady=10)

        self.original_dimensions_label = tk.Label(content_frame, text="Original Dimensions : N/A", font=("Times New Roman", 12), bg='#eeeeee', fg='#393e46')
        self.original_dimensions_label.pack(pady=10)

        tk.Label(content_frame, text="Width :", font=("Times New Roman", 12), bg='#eeeeee', fg='#393e46').pack()
        self.width_entry = tk.Entry(content_frame)
        self.width_entry.pack(pady=5)

        tk.Label(content_frame, text="Height :", font=("Times New Roman", 12), bg='#eeeeee', fg='#393e46').pack()
        self.height_entry = tk.Entry(content_frame)
        self.height_entry.pack(pady=5)

        tk.Label(content_frame, text="Quality (1-100) :", font=("Times New Roman", 12), bg='#eeeeee', fg='#393e46').pack()
        self.quality_scale = tk.Scale(content_frame, from_=1, to=100, orient=tk.HORIZONTAL, bg='#eeeeee', highlightthickness=0)
        self.quality_scale.set(80)
        self.quality_scale.pack(pady=10)

        self.save_button = tk.Button(content_frame, text="Save Compressed Image", font=("Times New Roman", 14), command=self.save_compressed_image, bg='#00adb5', fg='white')
        self.save_button.pack(pady=10)

        # self.save_grayscale_button = tk.Button(content_frame, text="Save Grayscale Image", font=("Times New Roman", 14), command=self.save_grayscale_image, bg='#00adb5', fg='white')
        # self.save_grayscale_button.pack(pady=10)

        self.compressed_size_label = tk.Label(content_frame, text="Compressed Size : N/A", font=("Times New Roman", 12), bg='#eeeeee', fg='#393e46')
        self.compressed_size_label.pack(pady=10)

        self.compressed_dimensions_label = tk.Label(content_frame, text="Compressed Dimensions : N/A", font=("Times New Roman", 12), bg='#eeeeee', fg='#393e46')
        self.compressed_dimensions_label.pack(pady=10)

        self.saved_img_label = tk.Label(content_frame, bg='#eeeeee')
        self.saved_img_label.pack(pady=10)

    def show_about(self):
        self.clear_content()

        content_frame = tk.Frame(self.root, bg='#eeeeee', width=800, height=600)
        content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        about_label = tk.Label(content_frame, text="About", font=("Times New Roman", 24, "bold"), bg='#eeeeee', fg='#393e46')
        about_label.pack(pady=20)

        about_text = tk.Label(content_frame, text="This application provides a simple yet powerful tool for compressing color images.\n"
                                                  "Developed using Python and Tkinter, it allows users to open various image formats, resize them,\n"
                                                  "adjust compression quality, and save the compressed images in JPEG or PNG formats.\n"
                                                  "Enjoy efficient image management with this lightweight and intuitive application!", 
                              font=("Times New Roman", 14), bg='#eeeeee', fg='#393e46', justify=tk.CENTER)
        about_text.pack(pady=10)

    def clear_content(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Canvas) or (isinstance(widget, tk.Frame) and widget != self.root.children['!frame']):
                widget.destroy()

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if not file_path:
            return

        self.img = Image.open(file_path)
        self.original_width, self.original_height = self.img.size
        self.img.thumbnail((800, 600))
        self.img_tk = ImageTk.PhotoImage(self.img)

        self.img_label.config(image=self.img_tk)
        self.img_label.image = self.img_tk

        original_size = os.path.getsize(file_path)
        self.original_size_label.config(text=f"Original Size: {original_size / 1024:.2f} KB")
        self.original_dimensions_label.config(text=f"Original Dimensions: {self.original_width}x{self.original_height}")

    def save_compressed_image(self):
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())
        quality = self.quality_scale.get()

        resized_img = self.img.resize((width, height))

        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
        if not file_path:
            return

        resized_img.save(file_path, quality=quality)
        messagebox.showinfo("Image Saved", f"Image saved at {file_path} with compression.")

        compressed_size = os.path.getsize(file_path)
        self.compressed_size_label.config(text=f"Compressed Size: {compressed_size / 1024:.2f} KB")
        self.compressed_dimensions_label.config(text=f"Compressed Dimensions: {width}x{height}")

        self.display_saved_image(file_path)

    # def save_grayscale_image(self):
    #     width = int(self.width_entry.get())
    #     height = int(self.height_entry.get())
    #     quality = self.quality_scale.get()
    #
    #     grayscale_img = ImageOps.grayscale(self.img.resize((width, height)))
    #
    #     file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
    #     if not file_path:
    #         return
    #
    #     grayscale_img.save(file_path, quality=quality)
    #     messagebox.showinfo("Image Saved", f"Grayscale image saved at {file_path} with compression.")
    #
    #     compressed_size = os.path.getsize(file_path)
    #     self.compressed_size_label.config(text=f"Compressed Size: {compressed_size / 1024:.2f} KB")
    #     self.compressed_dimensions_label.config(text=f"Compressed Dimensions: {width}x{height}")
    #
    #     self.display_saved_image(file_path)

    def display_saved_image(self, file_path):
        saved_img = Image.open(file_path)
        saved_img.thumbnail((800, 600))
        saved_img_tk = ImageTk.PhotoImage(saved_img)

        self.saved_img_label.config(image=saved_img_tk)
        self.saved_img_label.image = saved_img_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = CompressionOfColorImage(root)
    root.mainloop()
