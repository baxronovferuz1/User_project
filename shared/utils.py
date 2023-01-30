from rest_framework.exceptions import ValidationError
import phonenumbers
from django.template.loader import render_to_string


def send_email(email, code):
    html_content=render_to_string(
        "email/authentication/activate_account.html"
    )
    




def phone_checker(p_number):
    if not(p_number and isinstance(p_number,str) and p_number.isdigit()):
        raise ValidationError("phone number is'nt valid")




def phone_parser(p_number, c_code=None):
    try:
        phone_checker(p_number)
        p_number="+"+p_number
        return phonenumbers.parse(p_number, c_code)
    
    except Exception as e:
        raise ValidationError('phone number is not valid')
