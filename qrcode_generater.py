# import tkinter as tk
# import qrcode
# from PIL import ImageTk


# upi_id = input("Ener your UPI id : ")

# pytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
# amazonpay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# pytm_qr = qrcode.make(pytm_url)
# amazonpay_qr = qrcode.make(amazonpay_url)

# pytm_qr.show()
# amazonpay_qr.show()




import tkinter as tk
import qrcode
from PIL import ImageTk

def show_qr():
    upi_id = entry.get()
    url = f'upi://pay?pa={upi_id}&pn=User'
    
    img = qrcode.make(url).resize((250, 250))
    tk_img = ImageTk.PhotoImage(img)
    
    canvas.config(image=tk_img)
    canvas.image = tk_img


root = tk.Tk()
root.title("UPI Generator")
root.geometry("600x500")

entry = tk.Entry(root)
entry.pack(pady=10)

btn = tk.Button(root, text="Show QR Code", command=show_qr)
btn.pack(pady=5)

canvas = tk.Label(root)
canvas.pack(pady=10)

root.mainloop()