def isValid(email, password):
    if  "@" not in email or type(email) != str: return "not valid email"
    if type(password) != str:
        return "not a valid password"
    if len(password) < 8:  
        return "password is not long enough"
    if not password.isupper() > 0: 
        return "the password must contain atleast 1 uppercase letter."
    if not password.isdigit() > 0: 
        return "the password must contain atleast 1 number."
print(isValid("Seanhadley11@gmail.com", "Hello123"))