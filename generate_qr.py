# generate_qr.py

import qrcode

url = "http://127.0.0.1:8000/mark/"
img = qrcode.make(url)
img.save("qr_attendance.png")
