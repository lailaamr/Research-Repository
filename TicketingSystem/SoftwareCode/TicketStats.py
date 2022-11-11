#The ticketstats class the will display the different stats of the tickets added to the system

class TicketStats():
    TicketsCreated = 0
    TicketsOpened = 0
    TicketsClosed = 0

    def DisplayStats():
        print('Tickets Created: ' + str(TicketStats.TicketsCreated) + '\nTickets Open: ' + str(TicketStats.TicketsOpened) + '\nTickets Closed: ' + str(TicketStats.TicketsClosed))
