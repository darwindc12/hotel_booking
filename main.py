import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_credit_card = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pandas.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_number):
        self.hotel_number = hotel_number
        self.name = df.loc[df['id'] == self.hotel_number, "name"].squeeze()

    def book(self):
        df.loc[df['id'] == self.hotel_number, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def availability(self):
        available = df.loc[df['id'] == self.hotel_number, "available"].squeeze()
        if available == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number

    def validate(self, expiration, holder, cvc):
        card_data = {'number': self.card_number, 'expiration': expiration,
                     'holder': holder, 'cvc': cvc}

        if card_data in df_credit_card:
            return True
        else:
            return False


class CreditCardSecurity(CreditCard):
    def validation(self, given_password):
        password = df_card_security.loc[df_card_security['number'] == self.card_number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


class SpaTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your Spa reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


print(df)
hotel_id = input("Enter hotel number: ")
hotel = SpaHotel(hotel_id)

if hotel.availability():
    card = CreditCardSecurity(card_number='1234')
    if card.validate(expiration="12/26",  holder="JOHN SMITH", cvc="123"):
        if card.validation(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation = ReservationTicket(customer_name=name, hotel_object=hotel)
            (print(reservation.generate()))
            spa = input("Do you want to book spa package? ")
            if spa == 'yes':
                hotel.book_spa_package()
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                print(spa_ticket.generate())

        else:
            print("Credit card authentication failed")
    else:
        print("There was a problem with your payment")

else:
    print("Printer is not available")