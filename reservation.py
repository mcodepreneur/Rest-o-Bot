SEAT_CAP = 30
TIMES = ['3:00', '3:30', '4:00', '4:30', '5:00', '5:30',
         '6:00', '6:30', '7:00', '7:30', '8:00', '8:30', '9:00']
resev = []
inp = ''

print('-------------------------\nWelcome to Rest-o-Bot, Michael\'s restaurant reservation manager.\nEnter "cancel" on a feild other than name to start over entering a reservation, and enter "exit" on the name feild to quit the program.\n')

print('Restaurant capacity:', SEAT_CAP , '\n\nDefined timeslots:', TIMES, '\nReservations are one hour each.\n-------------------------')

def print_eve():  # print evening/everything
    print('-------------------------\nCurrent Roster:')
    for thuck in TIMES:
        print(thuck + ':')
        for item in resev:
            if item[2] == thuck:
                print(item[0] + ': ' + item[1] + ' people')
        print()
    print('-------------------------')


def get_in():  # reservations are one hour
    print('Enter new reservation')
    name = input('Name: ')
    if name == 'exit':
        print('Thank you for using Rest-o-Bot! Exiting...')
        exit()
    if name == 'back':
        c = resev.pop()
        print(c[0], 'with', c[1], 'people removed')
        return False

    peep = input('Number of people: ')
    if peep == 'cancel':
        return get_in()

    while True:
        try:
            int(peep)
            break
        except:
            print('This input needs to be a number')  # defined by TIMES, one hour reservations, 0:00 format
            peep = input('Number of people: ')
            

    time = input('Time: ')
    if time == 'cancel':
        return get_in()
    hur = False
    while hur is False:
        if TIMES.count(time) == 0:
            print('Stick to the time slots')
            time = input('Time: ')
            continue
        if conf([name, peep, time]) > 0:
            print('This reservation does not fit into this time')
            time = input('Time: ')
            continue
        if TIMES.count(time) != 0 and conf([name, peep, time]) < 1:
            hur = True

    return [name, peep, time]


def conf(pro):  # returns excess dining room seats + or -
    i = 0
    for item in resev:
        if item[2] == TIMES[TIMES.index(pro[2])] or item[2] == TIMES[TIMES.index(pro[2]) - 1] or item[2] == TIMES[TIMES.index(pro[2]) + 1]:
            i = i + int(item[1])
    i = i + int(pro[1])
    return i - SEAT_CAP


while inp != 'exit':
    prop = get_in()
    if prop is not False:
        resev.append(prop)
    print_eve()
