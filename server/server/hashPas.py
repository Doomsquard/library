import bcrypt


def hash(password):
    password=password.encode()
    return bcrypt.hashpw(password,bcrypt.gensalt())

def check(password,hash):
    return bcrypt.checkpw(password.encode('utf-8'),f'{hash}'.encode('utf-8'))

