import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets API credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("\Users\daniejackson\PycharmProjects\DAY-32-SEND-EMAIL-SMTPLIB-MANAGE-DATES-100-DAYS-OF-CODE\birthdays.csv")
client = gspread.authorize(creds)

# Open the Google Sheet by title
sheet = client.open("Your Google Sheet Title").sheet1

# Get all values from the sheet
data = sheet.get_all_records()

# Print the data
print(data)