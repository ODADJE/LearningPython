## Gerer des donnnees aleatoires...
from faker import Faker

fake = Faker(locale="fr_FR")

print(fake.name())
print(fake.address())
print(fake.text())
print(fake.job())
print(fake.file_path(depth=5, category='video'))
print(fake.numerify(text="%%-%%%-%%-%%"))
print(fake.credit_card_number(), fake.credit_card_expire(), fake.credit_card_security_code())

for _ in range (10):
    print(fake.job())