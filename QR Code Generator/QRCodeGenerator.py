import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk


def generate_qrcode():
    url = entry_url.get()
    
    if not url:
        messagebox.showerror("Error","Please enter a valid URL")
        return
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create and save the QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save("qrcode.png")
    
    # Display the QR code
    qr_image_tk = ImageTk.PhotoImage(Image.open("qrcode.png"))
    qr_label.config(image=qr_image_tk)
    qr_label.image = qr_image_tk
    messagebox.showinfo("Success","QR Code generated Successfully!")


# Create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x600")
root.configure(bg="#f0f4f7")

# URL input
label_url = ttk.Label(root, text="Enter URL: ", background="#f0f4f7")
label_url.pack(pady=10)
entry_url = ttk.Entry(root, font=("Helvetica",12), width=40)
entry_url.pack(pady=10)

# Generate button
button_generate = ttk.Button(root, text="Generate QR Code", command=generate_qrcode)
button_generate.pack(pady=20)

# Label to display the QR code
qr_label = ttk.Label(root, background="#f0f4f7")
qr_label.pack(pady=10)

# Result label
label_result = ttk.Label(root, text="", font=("Helvetica", 14), background="#f0f4f7", foreground="#333")
label_result.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()