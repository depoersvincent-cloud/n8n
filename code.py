from datetime import datetime

now = datetime.now()

print("Date :", now.strftime("%d/%m/%Y"))
print("Heure :", now.strftime("%H:%M:%S"))
