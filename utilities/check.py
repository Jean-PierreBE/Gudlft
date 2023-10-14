"""
this package containss functions to check
    the validiy
       mail for the registration
       number of places
       presence of club or competition with the name
"""
from utilities.constants import MAX_PLACES


def check_mail(email, clubs):
    """
    check existence of email adress
    return a code and eventually the record of club
    :param email: email adress
    :param clubs: list of the clubs
    :return: 0  email is in the list
             1  email is empty
             2  email isn't in the list
             if zero the record of club is also returned
                else none
    """
    if email == '':
        return 1, None
    else:
        for club in clubs:
            if club['email'] == email:
                return 0, [club][0]
        return 2, None


def check_name(name, groups):
    """
    check existence of name of club or competition
    return a code and eventually the record of or competition
    :param name: name of club or competition
    :param groups: list of the clubs or competititions
    :return: 0  name is in the list
             1  name is empty
             2  name isn't in the list
             if zero the record of club or competitions is also returned
                else none
    """
    if name == '':
        return 1, None
    else:
        for group in groups:
            if group['name'] == name:
                return 0, [group][0]
        return 2, None


def check_places(places_choosen, places_available, points_available):
    """
    check if the number of places filled by the user is correct
    eg : > 0 ; is there enough places etc ..
    :param places_choosen: number of places filled by the user
    :param places_available: places available in the competition
    :param points_available: number of points hold by the user
    :return: 0  number of places is ok
             1  number of places is empty
             2  number of places = 0
             3  number of places < 0
             4  number of places > number of places of the competition
             5  number of places > number maximum of places allowed
             6  number of places > number of points
    """
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
