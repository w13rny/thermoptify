import os
from datetime import datetime
from typing import Dict, Any

import gspread
from dotenv import load_dotenv
from gspread import SpreadsheetNotFound, WorksheetNotFound, Client, Spreadsheet, Worksheet

load_dotenv()
SERVICE_ACCOUNT_JSON_DIRECTORY = os.environ.get('GOOGLE_SERVICE_ACCOUNT_JSON_DIRECTORY')
MY_EMAIL = os.environ.get('MY_EMAIL')


def get_or_create_spreadsheet(client: Client, name: str) -> Spreadsheet:
    try:
        spreadsheet = client.open(name)
        return spreadsheet
    except SpreadsheetNotFound:
        spreadsheet = client.create(name)
        spreadsheet.share(MY_EMAIL, perm_type='user', role='writer')
        return spreadsheet


def get_or_create_worksheet(spreadsheet: Spreadsheet, name: str) -> Worksheet:
    try:
        worksheet = spreadsheet.worksheet(name)
        return worksheet
    except WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(title=name, rows=1, cols=9)
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
        return worksheet


def write_data_to_google_sheet(indoor_temperature: float, outdoor_temperature: float, ac_status: Dict[str, Any]):
    client = gspread.service_account(filename=SERVICE_ACCOUNT_JSON_DIRECTORY)

    spreadsheet_name = 'thermoptify'
    spreadsheet = get_or_create_spreadsheet(client, spreadsheet_name)

    worksheet_name = datetime.now().strftime("%Y/%m")
    worksheet = get_or_create_worksheet(spreadsheet, worksheet_name)

    payload = (
        datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        indoor_temperature,
        outdoor_temperature,
        ac_status['result'][0]['value'],
        ac_status['result'][1]['value'],
        ac_status['result'][2]['value'],
        ac_status['result'][3]['value'],
        ac_status['result'][4]['value'],
        ac_status['result'][5]['value']
    )
    worksheet.append_row(payload)
