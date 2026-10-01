''' ₹5000 ka product hai. Us par 18% GST lagta hai.
Arithmetic operators ka use karke:
GST amount
Final price  
'''

product_price = 5000
gst_percentage = 18

gst_amount = (product_price * gst_percentage) / 100
final_price = product_price + gst_amount
print("GST amount:", gst_amount)
print("Final price:", final_price)
