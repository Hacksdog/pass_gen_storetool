import random, csv, os
from datetime import datetime

numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*"]
alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

def generate_password(parts=4):
    password_list = []
    for _ in range(parts):
        password_list.append(random.choice(numbers))
    for _ in range(parts):
        password_list.append(random.choice(symbols))
    for _ in range(parts):
        password_list.append(random.choice(alphabets))
    random.shuffle(password_list)
    return "".join(password_list)

pw = generate_password(4)
service = input("Service (e.g. Facebook): ").strip()
username = input("Username/email (optional)/Number: ").strip()
timestamp = datetime.now().isoformat()

csv_file = "passwords.csv"
write_header = not os.path.exists(csv_file)

with open(csv_file, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if write_header:
        writer.writerow(["timestamp", "service", "username", "password"])
    writer.writerow([timestamp, service, username, pw])

print(f"Saved to {os.path.abspath(csv_file)}")
print("Password:", pw)
