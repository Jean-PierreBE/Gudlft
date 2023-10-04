
def check_mail(email, clubs):
    if email == '':
        return 1, None
    else:
        for club in clubs:
            if club['email'] == email:
                return 0, [club][0]
        return 2, None
