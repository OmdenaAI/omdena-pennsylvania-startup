from __future__ import print_function
import requests
import pandas as pd
import json
import numpy as np
from googleapiclient.discovery import build
from google.oauth2 import service_account

# TRADINGVIEW URL
url = "https://scanner.tradingview.com/america/scan"

performancePayload = json.dumps({
  "filter": [
    {
      "left": "description",
      "operation": "nempty"
    }
  ],
  "options": {
    "lang": "en"
  },
  "symbols": {
    "query": {
      "types": [
        "industry"
      ]
    },
    "tickers": []
  },
  "columns": [
    "description",
    "change",
    "change|1W",
    "change|1M",
    "Perf.3M",
    "Perf.6M",
    "Perf.YTD",
    "Perf.Y"
  ],
  "sort": {
    "sortBy": "description",
    "sortOrder": "asc"
  },
  "range": [
    0,
    150
  ]
})

overviewPayload = json.dumps({
  "filter": [
    {
      "left": "description",
      "operation": "nempty"
    }
  ],
  "options": {
    "lang": "en"
  },
  "symbols": {
    "query": {
      "types": [
        "industry"
      ]
    },
    "tickers": []
  },
  "columns": [
    "description",
    "market_cap_basic",
    "dividend_yield_recent",
    "change",
    "volume",
    "sector",
    "elements"
  ],
  "sort": {
    "sortBy": "description",
    "sortOrder": "asc"
  },
  "range": [
    0,
    150
  ]
})

headers = {
  'Content-Type': 'application/json'
}

perfResponse = requests.request("POST", url, headers=headers, data=performancePayload,verify = False)
overResponse = requests.request("POST", url, headers=headers, data=overviewPayload,verify = False)

perfJsonResp = perfResponse.json()
overJsonResp = overResponse.json()

def extract(respType,jsonResp):
  tempdf = pd.DataFrame()
  if respType.lower() == 'performance':
    pos = 0
    for ind in jsonResp['data']:
      perftemp = ind['d'] 
      tempdf.loc[pos,'Industry'] = perftemp[0]
      tempdf.loc[pos,'CHG %'] = perftemp[1]
      tempdf.loc[pos,'1W CHG %'] = perftemp[2]
      tempdf.loc[pos,'1M CHG %'] = perftemp[3]
      tempdf.loc[pos,'3-Month Perf %'] = perftemp[4]
      tempdf.loc[pos,'6-Month Perf %'] = perftemp[5]
      tempdf.loc[pos,'YTD Perf %'] = perftemp[6]
      tempdf.loc[pos,'Yearly Perf %'] = perftemp[7]
      pos+=1
  elif respType.lower() == 'overview':
    pos = 0
    for ind in jsonResp['data']:
      overtemp = ind['d']
      tempdf.loc[pos,'Industry'] = overtemp[0]
      tempdf.loc[pos,'MKT CAP'] = overtemp[1]
      tempdf.loc[pos,'DIV YIELD'] = overtemp[2]
      tempdf.loc[pos,'CHG %'] = overtemp[3]
      tempdf.loc[pos,'VOLUME'] = overtemp[4]
      tempdf.loc[pos,'SECTOR'] = overtemp[5]
      tempdf.loc[pos,'STOCKS'] = overtemp[6]
      pos+=1
  return tempdf


df1 = extract("overview",overJsonResp)
print("OVERVIEW DATA EXTRACTED")
df2 = extract("performance",perfJsonResp)
print("PERFORMANCE DATA EXTRACTED")



# GOOGlE SHEET API WORKING STARTS HERE--
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Give the path on key file
SERVICE_ACCOUNT_FILE = "startup-success-321415-4539ba07e549.json"

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes = SCOPES)
# The ID and range of both spreadsheets.
OVERVIEW_SPREADSHEET_ID = '15SzbNhVbfigMShSOc-3UsC2oTPijINEzHrAjE3PtwNE'
PERFORMANCE_SPREADSHEET_ID = '11XDT4eJUPbBKwZhIAGkdK94_WNYyF0sEBzK4gO96zrc'

service = build('sheets', 'v4', credentials=creds)

# CODE TO UPDATE OVERVIEW SPREADSHEET
overviewvalues = [
    ['Industry', 'MKT CAP', 'DIV YIELD', 'CHG %', 'VOLUME', 'SECTOR', 'STOCKS']
]

df1['DIV YIELD'] = df1['DIV YIELD'].replace(np.nan,"")

overviewvalues.extend(df1.values.tolist())
overview_range_name = "Sheet1!A1:G130"
value_input_option = "USER_ENTERED"
overviewdata = [
    {
        'range': overview_range_name,
        'values': overviewvalues
    }
]
overviewbody = {
    'valueInputOption': value_input_option,
    'data': overviewdata
}
overviewresult = service.spreadsheets().values().batchUpdate(
    spreadsheetId=OVERVIEW_SPREADSHEET_ID, body=overviewbody).execute()
print('{0} cells updated for Overview.'.format(overviewresult.get('totalUpdatedCells')))

# CODE TO UPDATE PERFORMANCE SPREADSHEET
perfvalues = [df2.columns.tolist()]

perfvalues.extend(df2.values.tolist())
performance_range_name = "Sheet1!A1:H130"
value_input_option = "USER_ENTERED"
perfdata = [
    {
        'range': performance_range_name,
        'values': perfvalues
    }
]
perfbody = {
    'valueInputOption': value_input_option,
    'data': perfdata
}
perfresult = service.spreadsheets().values().batchUpdate(
    spreadsheetId=PERFORMANCE_SPREADSHEET_ID, body=perfbody).execute()
print('{0} cells updated for Performance.'.format(perfresult.get('totalUpdatedCells')))


