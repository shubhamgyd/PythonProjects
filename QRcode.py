import qrcode as qr
img = qr.make("https://www.youtube.com/playlist?list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
img.save("Python_project.png")