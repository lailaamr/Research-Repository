#The class that contains the attributes of the Ticket

from PasswordGenerator import PasswordGenerator
from TicketStats import TicketStats


class Ticket():
    counter = 2000
    name = ''
    email = ''
    staffID = ''
    ticketNumber = ''
    description = ''
    response = 'Not Yet Provided'
    ticketstatus = 'Open'

    def __init__(self, name='', email='', staffID='', description=''):
        self.name = name
        self.email = email
        self.staffID = staffID
        self.description = description
        Ticket.counter  += 1
        self.ticketNumber = Ticket.counter
        TicketStats.TicketsCreated += 1
        TicketStats.TicketsOpened += 1

        if ('password change' in self.description.lower()):
            self.response = "New password generated: " + PasswordGenerator.NewPassword(self.staffID, self.name)
            self.ticketstatus = "Closed"
            

    def RespondTicket(self, response):
        self.response = response
        self.ticketstatus = 'Closed'
        TicketStats.TicketsOpened -= 1
        TicketStats.TicketsClosed += 1
        print("\nTICKET CLOSED\n")

    def ReopenTicket(self):
        self.ticketstatus = "Reopened"
        print("\nTICKET REOPENED\n")
        TicketStats.TicketsOpened += 1
        TicketStats.TicketsClosed -= 1

    def getTicketNumber(self):
        return self.ticketNumber

    def DisplayTicket(self): 
        print('Ticket number: ' + str(self.ticketNumber) + '\nTicket Creator: ' + self.name + '\nStaff ID: ' + self.staffID + '\nEmail: ' + self.email + '\nDescription: ' + self.description + '\nResponse: ' + self.response + '\nTicket status: ' + self.ticketstatus + '\n')
        print("---------------------------\n")
