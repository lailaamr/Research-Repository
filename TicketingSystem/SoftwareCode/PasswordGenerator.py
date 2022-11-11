from TicketStats import TicketStats

class PasswordGenerator:
    @staticmethod
    def NewPassword(staffID, staffName):
            firstPart = staffID[0:2]
            secondPart = staffName[0:3]
            newPassword = firstPart + secondPart
            TicketStats.TicketsClosed += 1
            TicketStats.TicketsOpened -= 1

            return newPassword