import os
from datetime import datetime
from typing import Dict, Any

import gspread
from dotenv import load_dotenv
from gspread import SpreadsheetNotFound, WorksheetNotFound

load_dotenv()
SERVICE_ACCOUNT_JSON_DIRECTORY = os.environ.get('GOOGLE_SERVICE_ACCOUNT_JSON_DIRECTORY')
MY_EMAIL = os.environ.get('MY_EMAIL')


def write_data_to_google_sheet(indoor_temperature: float, outdoor_temperature: float, ac_status: Dict[str, Any]):
    gc = gspread.service_account(filename=SERVICE_ACCOUNT_JSON_DIRECTORY)

    try:
        sh = gc.open('thermoptify')
        sh.share(MY_EMAIL, perm_type='user', role='writer')
    except SpreadsheetNotFound:
        sh = gc.create('thermoptify')
        sh.share(MY_EMAIL, perm_type='user', role='writer')

    worksheet_name = datetime.now().strftime("%Y/%m")

    try:
        worksheet = sh.worksheet(worksheet_name)
    except WorksheetNotFound:
        worksheet = sh.add_worksheet(title=worksheet_name, rows=1, cols=9)
        worksheet.update('A1', 'Date & time')
        worksheet.update('B1', 'T°C (indoor)')
        worksheet.update('C1', 'T°C (outdoor)')
        worksheet.update('D1', 'AC (on/off)')
        worksheet.update('E1', 'AC (T°C set)')
        worksheet.update('F1', 'AC (T°C sensor)')
        worksheet.update('G1', 'AC (mode)')
        worksheet.update('H1', 'AC (fan speed)')
        worksheet.update('I1', 'AC (turbo)')
        worksheet.format('A1:I1', {'textFormat': {'bold': True, "fontSize": 8}})

    date_and_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    worksheet.append_row(
        (
            date_and_time,
            indoor_temperature,
            outdoor_temperature,
            ac_status['result'][0]['value'],
            ac_status['result'][1]['value'],
            ac_status['result'][2]['value'],
            ac_status['result'][3]['value'],
            ac_status['result'][4]['value'],
            ac_status['result'][5]['value']
        )
    )
