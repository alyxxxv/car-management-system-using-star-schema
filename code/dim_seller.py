import pandas as pd
from faker import Faker

# Initialize Faker with Indonesian locale
fake = Faker('id_ID')

# Load dim_city.csv to get kota_id
dim_city = pd.read_csv('/content/drive/MyDrive/Pacman/dim_city.csv')
kota_ids = dim_city['kota_id'].tolist()

# Data for dummy creation
domains = ["gmail.com", "yahoo.com", "outlook.com"]

# Function to create email
def create_email(first_name, last_name):
    domain = fake.random.choice(domains)
    email = f"{first_name.lower()}{last_name.lower()}@{domain}"
    return email

# Create dummy data
data = []
for i in range(1, 101):
    first_name = fake.first_name()
    last_name = fake.last_name()
    seller_name = f"{first_name} {last_name}"
    seller_address = fake.street_address()
    kota_id = fake.random.choice(kota_ids)
    phone_seller = f"08{fake.random_number(digits=10, fix_len=True)}"
    email_seller = create_email(first_name, last_name)
    data.append([i, seller_name, seller_address, kota_id, phone_seller, email_seller])

# Create DataFrame and save to CSV file
df = pd.DataFrame(data, columns=["seller_id", "seller_name", "seller_address", "kota_id", "phone_seller", "email_seller"])
df.to_csv("/content/drive/MyDrive/Pacman/dim_seller.csv", index=False)

print("Data dummy berhasil dibuat dan disimpan ke dim_seller.csv")

df.head()
