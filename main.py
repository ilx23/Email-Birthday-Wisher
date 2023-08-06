import pandas
import datetime as dt
import random
import smtplib

# Required information
MY_EMAIL = "iliakeshavarz23@gmail.com"
EMAIL_PASSWORD = "xmirsznagclmrzyn"

# Update the birthdays.csv file
birth_data = pandas.read_csv("birthdays.csv")
birth_data_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birth_data.iterrows()}



# Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_tuple = (today.month, today.day)

if today_tuple in birth_data_dict:
    person_name = birth_data_dict[today_tuple]['name']
    person_email = birth_data_dict[today_tuple]['email']
    random_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_number}.txt") as letter_data:
        message = letter_data.read()
        message = message.replace("[NAME]", person_name)


# Send the letter
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=person_email, msg=f"Subject:Happy Birthday\n\n {message}")



