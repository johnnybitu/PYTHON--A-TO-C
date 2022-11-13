import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=20,
                    border=2,
                    
)

qr.add_data("https://github.com/johnnybitu")
qr.make(fit=True)
img = qr.make_image(fill_color = "red", back_color="yellow")
img.save("E:\complete datascience\python\PROJECTS\QR_CODE\QR_image//johnny_git.png")

