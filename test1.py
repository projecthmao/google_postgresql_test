
from googleapiclient.discovery import build

from google.oauth2 import service_account

import requests
import xml.etree.ElementTree as et

import psycopg2


SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SAMPLE_SPREADSHEET_ID = '1LTejK-Oo7L1bFreBIIcEZnF1W1RCC1s_jos3EuIP0jI'
SAMPLE_RANGE_NAME = 'Лист1!A2:D'

# Получение данных из таблицы google sheets
def google_api():
    creds = service_account.Credentials.from_service_account_file('token.json', scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    return values

# получение курсa доллара США с сайта Центрального Банка РФ
def rate_d_r():
    xml_response = et.fromstring(requests.get("https://cbr.ru/scripts/XML_daily.asp").text.encode("1251"))
    rate = xml_response.find("Valute[@ID='R01235']/Value").text.replace(',', '.')
    rate = float(rate)
    return rate

# Заполнение базы данных из прочитанной таблицы google sheets
def infill_table(values):
    rate = rate_d_r()
    try:
        connection = psycopg2.connect(user="postgres",
                                        # пароль, который указали при установке PostgreSQL
                                        password="123",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="postgres")

        cursor = connection.cursor()

        cursor.execute("DELETE FROM test_table")
        for row in values:
            num_pp = int(row[0])
            zakaz = int(row[1])
            sum_d = float(row[2])
            sum_r = float(row[2]) * rate
            date = row[3]
            postgres_insert_query = """ INSERT INTO test_table (num_pp, zakaz, sum_d, sum_r, date) VALUES (%s,%s,%s, %s, %s)"""
            cursor.execute(postgres_insert_query, (num_pp, zakaz, sum_d, sum_r, date))
        connection.commit()
        connection.close()
        print('OK')
    except:
        print('NOT OK')




def main():
    values = google_api()
    infill_table(values)




if __name__ == '__main__':
    main()