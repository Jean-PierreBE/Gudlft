from utilities.constants import MAX_PLACES


def check_mail(email, clubs):
    if email == '':
        return 1, None
    else:
        for club in clubs:
            if club['email'] == email:
                return 0, [club][0]
        return 2, None


def check_name(name, groups):
    if name == '':
        return 1, None
    else:
        for group in groups:
            if group['name'] == name:
                return 0, [group][0]
        return 2, None


def check_places(places_choosen, places_available, points_available):
    if places_choosen == '':
        return 1
    else:
        if int(places_choosen) == 0:
            return 2
        elif (int(places_choosen) < 0):
            return 3
        elif (int(places_choosen) > places_available):
            return 4
        elif (int(places_choosen) > MAX_PLACES):
            return 5
        elif (int(places_choosen) > points_available):
            return 6
        else:
            return 0
