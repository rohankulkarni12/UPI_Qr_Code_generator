import qrcode

#Tallking Upi as a input
upi_id = input("Enter your UPI ID = ")
#Payment URL Formet
#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
# Defining the payment Url Based on the UPI and the payment app
#you can modify these URL's based on the payment Apps you want to support
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
#Create QR Codes For each Payment App
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)
# Save The Qr Code To image File (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")
#Display the QR Codes (you need to install PIL/Pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()