class TicketStats():
    TicketsCreated = 0
    TicketsOpened = 0
    TicketsClosed = 0

    def DisplayStats():
        print('Tickets Created: ' + str(TicketStats.TicketsCreated) + '\nTickets Open: ' + str(TicketStats.TicketsOpened) + '\nTickets Closed: ' + str(TicketStats.TicketsClosed))