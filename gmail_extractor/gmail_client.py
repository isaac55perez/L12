import os
import pickle
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import re

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

class GmailClient:
    def __init__(self, credentials_file='secrets/client_secret_564310052883-tt62d2chr6j00tgt20om0cbqav3siis7.apps.googleusercontent.com.json'):
        self.credentials_file = credentials_file
        self.service = None
        self.authenticate()
    
    def authenticate(self):
        """Authenticate and create Gmail API service"""
        creds = None
        # The file token.pickle stores the user's access and refresh tokens.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        
        self.service = build('gmail', 'v1', credentials=creds)
        print("Gmail API service created successfully!")
    
    def get_messages(self, query='', max_results=10):
        """Get messages based on query"""
        try:
            results = self.service.users().messages().list(
                userId='me', q=query, maxResults=max_results).execute()
            messages = results.get('messages', [])
            return messages
        except HttpError as error:
            print(f'An error occurred: {error}')
            return []
    
    def get_message_details(self, message_id):
        """Get detailed information about a specific message"""
        try:
            message = self.service.users().messages().get(
                userId='me', id=message_id, format='full').execute()
            return message
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None
    
    def extract_message_data(self, message):
        """Extract useful data from a message"""
        payload = message['payload']
        headers = payload.get('headers', [])
        
        # Extract headers
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown Sender')
        date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown Date')
        to = next((h['value'] for h in headers if h['name'] == 'To'), 'Unknown Recipient')
        
        # Extract body
        body = self.extract_body(payload)
        
        return {
            'id': message['id'],
            'thread_id': message['threadId'],
            'subject': subject,
            'sender': sender,
            'date': date,
            'to': to,
            'body': body,
            'snippet': message.get('snippet', ''),
            'labels': message.get('labelIds', [])
        }
    
    def extract_body(self, payload):
        """Extract body text from message payload"""
        body = ""
        
        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/plain':
                    data = part['body']['data']
                    body = base64.urlsafe_b64decode(data).decode('utf-8')
                    break
                elif part['mimeType'] == 'text/html':
                    data = part['body']['data']
                    html_body = base64.urlsafe_b64decode(data).decode('utf-8')
                    # Simple HTML tag removal
                    body = re.sub('<[^<]+?>', '', html_body)
                    break
        else:
            if payload['mimeType'] == 'text/plain':
                data = payload['body']['data']
                body = base64.urlsafe_b64decode(data).decode('utf-8')
            elif payload['mimeType'] == 'text/html':
                data = payload['body']['data']
                html_body = base64.urlsafe_b64decode(data).decode('utf-8')
                body = re.sub('<[^<]+?>', '', html_body)
        
        return body.strip()
    
    def search_emails(self, query='', max_results=10):
        """Search emails and return detailed information"""
        messages = self.get_messages(query, max_results)
        detailed_messages = []
        
        for message in messages:
            details = self.get_message_details(message['id'])
            if details:
                extracted_data = self.extract_message_data(details)
                detailed_messages.append(extracted_data)
        
        return detailed_messages
    
    def get_recent_emails(self, days=7, max_results=20):
        """Get recent emails from the last N days"""
        date_filter = (datetime.now() - timedelta(days=days)).strftime('%Y/%m/%d')
        query = f'after:{date_filter}'
        return self.search_emails(query, max_results)
    
    def get_emails_from_sender(self, sender_email, max_results=10):
        """Get emails from a specific sender"""
        query = f'from:{sender_email}'
        return self.search_emails(query, max_results)
    
    def get_emails_with_subject(self, subject_keyword, max_results=10):
        """Get emails containing specific keywords in subject"""
        query = f'subject:{subject_keyword}'
        return self.search_emails(query, max_results)
    
    def get_unread_emails(self, max_results=10):
        """Get unread emails"""
        query = 'is:unread'
        return self.search_emails(query, max_results)

    def get_email_details(self, message_id):
        """Get detailed information about a specific email"""
        details = self.get_message_details(message_id)
        if details:
            return self.extract_message_data(details)
        return None
    
    def print_email_summary(self, emails):
        """Print a summary of emails"""
        print(f"\nFound {len(emails)} emails:")
        print("-" * 80)
        
        for i, email in enumerate(emails, 1):
            print(f"{i}. Subject: {email['subject']}")
            print(f"   From: {email['sender']}")
            print(f"   Date: {email['date']}")
            print(f"   Snippet: {email['snippet'][:100]}...")
            print("-" * 80)
    
    def get_email_stats(self):
        """Get basic statistics about the Gmail account"""
        try:
            profile = self.service.users().getProfile(userId='me').execute()
            return {
                'email_address': profile['emailAddress'],
                'messages_total': profile['messagesTotal'],
                'threads_total': profile['threadsTotal'],
                'history_id': profile['historyId']
            }
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None
