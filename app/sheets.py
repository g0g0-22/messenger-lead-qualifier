import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime


def add_summary_to_sheets(uid, name, summary):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "messenger-lead-qualifier-93e25bc3b87c.json", scope)
    client = gspread.authorize(creds)

    # Open the spreadsheet (use the name of your sheet)
    sheet = client.open("Leads").sheet1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append row: [UID, Name, Summary, Timestamp]
    sheet.append_row([uid, name, summary, timestamp])
