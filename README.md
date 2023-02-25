# Hotels Reservation System
This code is a simple reservation system for hotels and spa packages. It includes classes for Hotel, SpaHotel, ReservationTicket, CreditCard, CreditCardSecurity, and SpaTicket. The system stores data in CSV files, and the data is read and manipulated using the pandas library.

## Installation
This code requires Python 3.x and pandas library. Install pandas using pip by running the following command:

pip install pandas

## Usage
Clone or download the code to your local machine.
Open your terminal and navigate to the folder containing the downloaded code.
Run the code using the command: python hotels.py.
Enter the hotel number when prompted.
Enter your name when prompted.
If you want to book a spa package, type yes when prompted.
Follow the instructions to complete the reservation process.

## Classes

### Hotel
The Hotel class represents a hotel and has the following methods:

__init__(self, hotel_number): Initializes the Hotel object with the specified hotel_number.
book(self): Books the hotel room by setting the hotel's availability to "no" in the CSV file.
availability(self): Checks if the hotel is available for booking.

###SpaHotel
The SpaHotel class represents a spa hotel and inherits from the Hotel class. It has an additional method:

book_spa_package(self): Books a spa package for the hotel room.

### ReservationTicket
The ReservationTicket class represents a reservation ticket and has the following methods:

__init__(self, customer_name, hotel_object): Initializes the ReservationTicket object with the specified customer_name and hotel_object.
generate(self): Generates a reservation ticket with the customer name and hotel name.
### CreditCard

The CreditCard class represents a credit card and has the following methods:

__init__(self, card_number): Initializes the CreditCard object with the specified card_number.
validate(self, expiration, holder, cvc): Validates the credit card using the provided expiration date, cardholder name, and CVC code.
CreditCardSecurity
The CreditCardSecurity class represents a credit card with additional security and inherits from the CreditCard class. It has an additional method:

validation(self, given_password): Validates the credit card's password.

### SpaTicket
The SpaTicket class represents a spa reservation ticket and has the following methods:

__init__(self, customer_name, hotel_object): Initializes the SpaTicket object with the specified customer_name and hotel_object.
generate(self): Generates a spa reservation ticket with the customer name and hotel name.
