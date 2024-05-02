class Ticket:
    def __init__(self, ticket_id, price):
        self.ticket_id = ticket_id
        self.price = price
        self.is_booked = False

    def display_info(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Price: ${self.price}")
        print(f"Status: {'Booked' if self.is_booked else 'Available'}")
        print("------------------------------")

    def book_ticket(self):
        if not self.is_booked:
            print(f"Booking ticket {self.ticket_id}...")
            self.is_booked = True
            print("Ticket booked successfully!")
        else:
            print(f"Ticket {self.ticket_id} is already booked.")

class MovieTicket(Ticket):
    def __init__(self, ticket_id, price, movie_name, show_time):
        super().__init__(ticket_id, price)
        self.movie_name = movie_name
        self.show_time = show_time

    def display_info(self):
        super().display_info()
        print(f"Movie: {self.movie_name}")
        print(f"Show Time: {self.show_time}")
        print("------------------------------")

class ConcertTicket(Ticket):
    def __init__(self, ticket_id, price, artist, venue, date):
        super().__init__(ticket_id, price)
        self.artist = artist
        self.venue = venue
        self.date = date

    def display_info(self):
        super().display_info()
        print(f"Artist: {self.artist}")
        print(f"Venue: {self.venue}")
        print(f"Date: {self.date}")
        print("------------------------------")

class BookingSystem(Ticket):
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def display_all_tickets(self):
        print("All Tickets:")
        for ticket in self.tickets:
            ticket.display_info()

