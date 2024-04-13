#Name: Jeffrey Guaman
#Date:october 26, 2023
#A program that computes LIRR transit fares.


def computeFare(zone, ticketType):
    fare = 0
    if zone == 1:
        if ticketType == 'peak':
            fare = 8.75
        elif ticketType == 'off-peak':
            fare = 6.25
    elif zone == 2 or zone == 3:
        if ticketType == 'peak':
            fare = 10.25
        elif ticketType == 'off-peak':
            fare = 7.50
    elif zone == 4:
        if ticketType == 'peak':
            fare = 12.00
        elif ticketType == 'off-peak':
            fare = 8.75
    elif zone == 5 or zone == 6 or zone == 7:
        if ticketType == 'peak':
            fare = 13.50
        elif ticketType == 'off-peak':
            fare = 9.75
    elif zone > 8:
        fare =  -1.00
    return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   

