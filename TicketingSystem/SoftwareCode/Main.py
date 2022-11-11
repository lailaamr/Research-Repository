from Ticket import Ticket
from TicketStats import TicketStats

class Main():
    def Main():
        Tickets = []
        program = 'on'
        print("---------------------------\n")
        print("The Best tickting System created by Laila :)")

        while(program == 'on'):
            print("\n* To add a ticket press: \"T\".")
            print("* To access the helpdesk press: \"H\".")
            print("* To close the program press: \"C\".\n")
            print("---------------------------\n")

            userInput = input("Enter your value: ").upper()
            if(userInput == 'T'):
                running = 'yes'
                while(running == 'yes'):
                    isStaff = input("Are you a staff member (Y/N): ").upper()
                    if(isStaff == 'N'):
                        print("You have to be a staff member to use this system.")
                        running = 'no'

                    elif(isStaff == 'Y'): 
                        name = input("Please enter your name: ")
                        staffId = input("Please enter your Staff ID: ")
                        email = input("Please enter your email: ")
                        desc = input("Please enter description of the problem: ")

                        newTicket = Ticket(name, email, staffId, desc)
                        Tickets.append(newTicket)
                        print("Ticket Added\n")
                        print("---------------------------\n")

                        running = 'no'

                    else:
                        print("That is not a valid entry, please try again.") 
            
            elif(userInput == 'H'):
                print("---------------------------\n")
                print("-----Helpdesk Dashboard-----")
                running = 'yes'

                while(running == 'yes'): 
                    TicketStats.DisplayStats()
                    print("---------------------------\n")
                    print("To Display tickets press: \"D\".")
                    print("To resolve a ticket press \"S\".")
                    print("To reopen a ticket press \"R\".")
                    print("To go back to main menu press:  \"B\".\n")
                    helpDeskInput = input("Enter your value: ").upper()

                    if(helpDeskInput == 'D'):
                        print("\n----------PRINTING TICKETS----------\n")
                        for x in range(len(Tickets)):
                            Tickets[x].DisplayTicket()

                    elif(helpDeskInput == 'S'):
                        ticketNum = input("Enter the number of ticket you want to resolve: ")
                        ticketResponse = input("Please enter your response: ")
                        for x in range(len(Tickets)):
                            ticketCheck = Tickets[x]
                            if (ticketCheck.getTicketNumber() == int(ticketNum)):
                                ticketCheck.RespondTicket(ticketResponse)

                    elif(helpDeskInput == 'R'):
                        ticketNum = input("Enter the number of ticket you want to resopen: ")
                        for x in range(len(Tickets)):
                            ticketCheck = Tickets[x]
                            if (ticketCheck.getTicketNumber() == int(ticketNum)):
                                    ticketCheck.ReopenTicket()
                    
                    elif(helpDeskInput == 'B'):
                        running = 'no'

                    else: 
                        print("Please enter a valid letter.")
            
            elif(userInput == 'C'):
                print("Thank you for using my amazing application :)")
                program = 'off'

            else:
                print("Please enter a valid letter.")

    Main()