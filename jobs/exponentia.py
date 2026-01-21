########## -> Validate input parameters in Python using:
# age = 18
# if not isinstance(age, int):
#     raise TypeError("age must be an integer")

# if age < 0:
#     raise ValueError("age must be non-negative")

########## -> Encryption and Decryption 
# from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# cipher = Fernet(key)

# enceypted = cipher.encrypt(b"kalpesh")
# decrypted = cipher.decrypt(enceypted)

# print(enceypted)
# print(decrypted)

########### -> How to send email :  
# import smtplib
# from email.mime.text import MIMEText

# msg = MIMEText("I'm Kalpesh Shinde with 4 years of experience, including 3.5 in Python. I started as a PHP developer, later working as a Python/Django instructor. At Software Plus Electronics, I focused on web development and database management. Now, at PlayerzPot Media, I handle testing and debugging.")
# msg["subject"] = "Regarding Job Opportunity for Python Developer"
# msg["from"] = "kalpesh4111993@gmail.com"
# msg["to"] = "shinde4193@gmail.com"

# with smtplib.SMTP("smtp.gmail.com", 587) as server : 
#     server.starttls()
#     server.login("kalpesh4111993@gmail.com", "45434$%$#@SDERTnhgyt")
#     server.send_message()

# print("Email sent successfully!")

########## -> In Python, you can create arrays in a few ways:

# # **1. Using a list (most common in Python):**
# arr = [1, 2, 3, 4, 5]

# # **2. Using the `array` module (for type-specific arrays):**
# import array
# arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' = integer

# # **3. Using NumPy (for numerical operations):**
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])

########## -> create an empty DataFrame
# import pandas as pd
# df = pd.DataFrame(columns=["Name", "Age", "City"])
# print(df)

########## -> i want 5 as output 
# x = [1,2,3,4,4,5,5,6] 
# from collections import Counter
# op = [k for k,v in Counter(x).items() if v > 1  ]
# print(op[::-1][0])

