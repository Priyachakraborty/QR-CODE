import qrcode
from datetime import datetime
import os

data = " #January10 mini project challenge  "
qr = qrcode.QRCode(version=1, box_size=20, border=10)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

output_location = "C:\\Users\\PRIYA CHAKRABORTY\\OneDrive\\Desktop\\new pr\\QR CODE ALL\\qr code"
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
filename = f"MyQRCode_{timestamp}.png"
output_path = os.path.join(output_location, filename)

img.save(output_path)
print(f"QR code saved at {output_path}")
