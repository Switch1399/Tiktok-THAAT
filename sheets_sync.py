import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def sync_to_sheets():
    creds = ServiceAccountCredentials.from_json_keyfile_name("your_key.json", ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive'])
    client = gspread.authorize(creds)

    sheet = client.open("TikTok Tracker").worksheet("Hashtags")
    df = pd.read_csv("data/hashtag_trends_log.csv")

    sheet.clear()
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

if __name__ == "__main__":
    sync_to_sheets()