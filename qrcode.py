import qrcode
from PIL import Image
# qr is just a variable
qr = qrcode.QRCode(version= 1 , error_correction= qrcode.constants.ERROR_CORRECT_H , box_size=10 , border= 4 )
# pil ke under ka QRCODE name ka function hota jo version , body change kr skta hai and krta hai
qr.add_data("https://anuragsinghok.medium.com/")
# link hum de chuke hai to hum yaha deknge ki jo bhi value di hai humne upper agr wo true hai yani fit ki value to hi run ho create
qr.make(fit= True)
img = qr.make_image(fill_color="red", back_color = "blue") # changing color and background color here
# You create an image (img) from the QRCode object. Here, you specify the fill color (the color of the QR code elements) as red and the background color as blue. The make_image method returns a PIL Image object representing the QR code with the specified colors.
img.save("medium_anurag.png")
