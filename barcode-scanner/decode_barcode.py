# https://towardsdatascience.com/building-a-barcode-qr-code-reader-using-python-360e22dfb6e5
# https://www.dynamsoft.com/codepool/locating-and-decoding-ean13-python-opencv.html
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('coke-can1.jpg')
result = decode(img)
decoded = []
for i in result:
    decoded.append(i.data.decode("utf-8"))
barcode = [*decoded[0]]
print(barcode)

country_code = ''.join(barcode[:3])
# country codes: https://www.barcodestalk.com/learn-about-barcodes/resources/barcode-country-codes#:~:text=Barcode%20prefixes%20do%20not%20provide,country%20code%20of%20070%20%E2%80%93%20079.\
print("Country code: "+country_code)

manufacturer_code = ''.join(barcode[3:7])
print("Manufacturier code: " + manufacturer_code)

product_code = ''.join(barcode[7:-1])
print("Product code: " + product_code)

check_digit = ''.join(barcode[-1:])
print("Check digit: "+ check_digit)