'''User se total_minutes input lo aur usko:
hours + minutes mein convert karo.'''

total_minutes = int(input("Enter total minutes: "))
hours = total_minutes // 60 
remaining_minutes = total_minutes % 60
print("Hours:", hours)  
print("Remaining minutes:", remaining_minutes)