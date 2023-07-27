##################### Extra Hard Starting Project ######################
import pandas, datetime as dt, smtplib, random
from dotenv import load_dotenv
import os

load_dotenv()
my_email = "yusuffkazeem63@gmail.com"
password = os.environ.get("PASSWORD")

# 2. Check if today matches a birthday in the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
day = now.day
month = now.month

# Convert DataFrame to list of dicts
data = birthdays.to_dict(orient="records")

for birthday in data:
    if birthday["day"] == day and birthday["month"] == month:
        letter = random.choice((1,2,3))
        with open(f"letter_templates/letter_{letter}.txt") as letter:
            text = letter.read()
            # Replace placeholder with actual name
            text = text.replace("[NAME]", birthday["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                # Transport layer security make connection secure
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=birthday["email"],
                                    msg=f"Subject:Happy Birthday\n\n{text}")





# 4. Send the letter generated in step 3 to that person's email address.




