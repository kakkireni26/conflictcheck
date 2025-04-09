#validate password using regex

'''
import re

pa=input()
m_pa=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*(\d))(?=.*[@#$%^&*()-+=])[a-zA-Z0-9@#$%^&*()-+=]{8,}$"
c_pa=re.fullmatch(m_pa,pa)
if c_pa:
    print("password is strong")
else:
    print("Password is not strong")
'''

#Validation URL

'''
import re

url="http://www.google.com/"
ch=r"^(https?://)?(www\.)[a-zA-Z0-9]+(\.)[a-zA-Z]{2,}(/.*)?$"
ch_url=re.match(ch,url)

if ch_url:
    print("URL is validated")
else:
    print("URL not validated")

'''

#Indentation Error

'''code=def outer():
#     def inner():
#         if True:
#             print("Ram")
#                 print("Sita")
#     return inner()
try:
    exec(code)
except IndentationError as e:
    print(e)
    print("Indentation Error Catched")'''

#ZeroDivisionError

'''try:
    x=1/0
except Exception as e:
    print(e)
    print("Error has been catched")
finally:
    print("The Code has been Executed")'''

#Type Error


        



