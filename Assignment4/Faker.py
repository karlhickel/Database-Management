from faker import Faker
import pandas as pd
fake = Faker()

name = (fake.name())


count = -1
table1 = []


rowNumber = int(input("How many rows of data would you like to print?"));



while count < rowNumber:
    count += 1
    name = (fake.name())
    job = (fake.job())
    phoneNumber = (fake.msisdn())
    state = fake.state_abbr(include_territories=True)
    zipcode = fake.zipcode_in_state(state_abbr=state)
    streetName = fake.street_name()
    buildingNumber = fake.building_number()
    city = (fake.city())
    creditCard = (fake.credit_card_number(card_type=None))
    creditProvider = (fake.credit_card_provider(card_type=None))
    socialSecurityNum = (fake.itin())

    table1.insert(count, [name, job, phoneNumber, state, zipcode, streetName, buildingNumber, city, creditCard, creditProvider, socialSecurityNum])

i = 0
for i in table1:
    print(i)

print("What is the name of your file that you'd like to output to?")
fileName = raw_input();


my_df = pd.DataFrame(table1)
my_df.to_csv(fileName + '.csv', index=False, header=False)
print my_df











