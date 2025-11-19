def isValid(email, password):
    if  "@" not in email or type(email) != str: return "not valid email"
    upper = 0
    number = 0
    if type(password) != str:
        return "not a valid password"
    if len(password) < 8:  
        return "password is not long enough"
    for char in password:
        if char.isupper():
            upper +=1
        if char.isdigit():
            number += 1
    if upper == 0:
        return "the password must contain atleast 1 uppercase letter."
    if number == 0:
        return "the password must contain atleast 1 number."
    return(email, password)
print(isValid("Seanhadley11@gmail.com", "helLo"))