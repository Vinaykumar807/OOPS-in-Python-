# Currency Converter 

from currency_converter import CurrencyConverter
from datetime import date
c = CurrencyConverter ()
print(c.convert(1,"USD","INR"))
print(c.convert(5,"USD","INR",date=date(2020,3,11))) # Using dates to check 

import qrcode

image = qrcode.make(" JAI SHREE RAM ")
image.save("vs_qr.png")
print("QR is genration success")