from faker import Faker


def random_output() -> None:
    fake = Faker()
    print("Name: ", fake.name())
    print("Address: ", fake.address())
    print("Email:", fake.email())
    print("Phone number:", fake.phone_number())
