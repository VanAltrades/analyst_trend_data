import pygsheets
import gspread
import pandas as pd

def get_google_sheet_data(method, google_sheet_name, worksheet_name, credential_path):

    if method not in ("pygsheets","gspread"):
        raise "method must be set to either 'pygsheets' or 'gspread'"
    
    if method == "pygsheets":
        gc = pygsheets.authorize(service_file=credential_path)
        sh = gc.open(google_sheet_name)
        wks = sh.worksheet_by_title(worksheet_name)
        gsheet = wks.get_as_df()
        return gsheet
    
    if method == "gspread":
        gc = gspread.service_account(filename=credential_path)
        sh = gc.open(google_sheet_name)
        wks = sh.worksheet(worksheet_name)
        
        rows = wks.get_all_values() # get_all_values gives a list of rows.
        gsheet = pd.DataFrame.from_records(rows)
        new_header = gsheet.iloc[0] #grab the first row for the header
        gsheet = gsheet[1:] #take the data less the header row
        gsheet.columns = new_header #set the header row as the df header
        return gsheet