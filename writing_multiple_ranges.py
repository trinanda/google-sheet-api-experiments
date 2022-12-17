from __future__ import print_function
import os.path

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/spreadsheets',
]


def batch_update_values(spreadsheet_id, range_name,
                        value_input_option, _values):
    """
        Creates the batch_update the user has access to.
        Load pre-authorized user credentials from the environment.
        TODO(developer) - See https://developers.google.com/identity
        for guides on implementing OAuth2 for the application.
            """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_274233513361-j6noneg6me6t5jes9mgsdspoaj1p3qlm.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('sheets', 'v4', credentials=creds)

        values = [
            [
                # Cell values ...
                'A',
                'B',
                'C',
            ],
            [
                # Cell values ...
                'A',
                'B',
                'C',
            ],
            [
                # Cell values ...
                'A',
                'B',
                'C',
            ],
            [
                # Cell values ...
                'A',
                'B',
                'C',
            ],
            [
                # Cell values ...
                'A',
                'B',
                'C',
            ],
            # Additional rows
        ]
        data = [
            {
                'range': range_name,
                'values': values
            },
            # Additional ranges to update ...
        ]
        body = {
            'valueInputOption': value_input_option,
            'data': data
        }
        result = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id, body=body).execute()
        print(f"{(result.get('totalUpdatedCells'))} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


if __name__ == '__main__':
    # Pass: spreadsheet_id, range_name value_input_option and _values)
    batch_update_values("17rkVniBQLZOrOy6uH-BloWK6nXqfd7IWap64dCu07N8",
                        "A:C", "USER_ENTERED",
                        [
                            ['F', 'B'],
                            ['C', 'D']
                        ])
