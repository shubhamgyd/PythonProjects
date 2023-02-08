'''This Code is to generate QR (Quick Response) code  for any URL you 
   paste in make() function and with the help of save that 
   QR with name dot extension.Generally png is preferred for QR code.'''
import qrcode as qr
img = qr.make("https://www.youtube.com/playlist?list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
img.save("Python_project.png")
