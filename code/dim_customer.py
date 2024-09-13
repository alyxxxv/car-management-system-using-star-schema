import csv
import random
import faker
from google.colab import drive


# Initialize Faker
fake = faker.Faker('id_ID')

# Define the number of records
num_records = 300

# Define the common occupations in Indonesia in Indonesian language
occupations = ['Insinyur', 'Guru', 'Dokter', 'Perawat', 'Pengacara', 'Akuntan', 'Manajer', 'Penjual', 'Pegawai', 'Teknisi', 'Wirausaha', 'Karyawan Swasta', 'PNS', 'Karyawan BUMN']

# Define the income types
income_types = ['Pendapatan Tetap', 'Pendapatan Tidak Tetap']

# Define additional columns for customer information
genders = ['Laki-laki', 'Perempuan']
marital_statuses = ['Lajang', 'Menikah', 'Duda/Janda']

# Path to save the file in Google Drive
file_path = '/content/drive/MyDrive/Pacman/dim_customer.csv'

# Open a CSV file to write the data
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['customer_id', 'customer_name', 'customer_address', 'customer_age', 'customer_phone', 'customer_email',
                     'occupation', 'salary', 'income_type', 'gender', 'marital_status'])

    # Generate and write the data rows
    for i in range(1, num_records + 1):
        customer_id = f"CUS{i:04d}"
        first_name = fake.first_name()
        last_name = fake.last_name()
        customer_name = f"{first_name} {last_name}"
        customer_address = fake.street_address()
        customer_age = random.randint(18, 70)
        customer_phone = f"08{random.randint(1000000000, 9999999999)}"
        email_domain = random.choice(['@gmail.com', '@yahoo.com', '@outlook.com'])
        customer_email = f"{first_name.lower()}.{last_name.lower()}{email_domain}"
        occupation = random.choice(occupations)
        salary = random.randint(3000000, 20000000)
        income_type = random.choice(income_types)
        gender = random.choice(genders)
        marital_status = random.choice(marital_statuses)

        writer.writerow([customer_id, customer_name, customer_address, customer_age, customer_phone, customer_email,
                         occupation, salary, income_type, gender, marital_status])

print("Dummy data for 1000 customers has been generated and saved to dim_customer.csv in your Google Drive")

