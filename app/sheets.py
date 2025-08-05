import gspread
from google.oauth2.service_account import Credentials
from app.config import GOOGLE_CREDENTIALS_PATH, SHEET_ID

def get_google_sheet_data(head: str, tail: str) -> list:
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_PATH, scopes=scopes)
    gc = gspread.authorize(creds)

    worksheet = gc.open_by_key(SHEET_ID).get_worksheet(1)
    data = worksheet.get(f"{head}:{tail}", value_render_option="FORMATTED_VALUE")
    return data