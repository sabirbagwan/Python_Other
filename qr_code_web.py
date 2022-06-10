import qrcode

img = qrcode.make("sabirbagwan.pythonanywhere.com")

img.save("websiteqrcode.jpg")