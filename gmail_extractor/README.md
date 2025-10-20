# Gmail Email Extractor

A Python application to access and extract emails from your Gmail account using the Gmail API.

## Features

- Authenticate with Gmail using OAuth2
- Retrieve recent emails
- Search emails by keywords, sender, or subject
- Get unread emails
- Extract email content (subject, sender, date, body)
- Export emails to JSON format
- Account statistics

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Google API Setup

You already have the OAuth credentials file in the `secrets` directory. Make sure:

1. Gmail API is enabled in your Google Cloud Console
2. The OAuth consent screen is configured
3. Your application has the necessary scopes

### 3. Run the Application

```bash
cd gmail_extractor
python example_usage.py
```

On first run, it will:
1. Open a browser window for Google authentication
2. Ask you to sign in to your Google account
3. Request permission to read your Gmail
4. Save authentication tokens for future use

## Usage Examples

### Basic Usage

```python
from gmail_client import GmailClient

# Initialize client (handles authentication)
gmail = GmailClient()

# Get recent emails
recent_emails = gmail.get_recent_emails(days=7, max_results=10)

# Print email summaries
gmail.print_email_summary(recent_emails)
```

### Search Emails

```python
# Search by keyword
emails = gmail.search_emails('meeting', max_results=5)

# Get emails from specific sender
emails = gmail.get_emails_from_sender('sender@example.com', max_results=5)

# Get emails with specific subject
emails = gmail.get_emails_with_subject('invoice', max_results=5)

# Get unread emails
unread = gmail.get_unread_emails(max_results=10)
```

### Account Information

```python
# Get account statistics
stats = gmail.get_email_stats()
print(f"Total messages: {stats['messages_total']}")
print(f"Email address: {stats['email_address']}")
```

## File Structure

- `gmail_client.py` - Main Gmail API client class
- `example_usage.py` - Example script demonstrating usage
- `requirements.txt` - Python dependencies
- `token.pickle` - Authentication tokens (created after first run)
- `recent_emails.json` - Sample output file with email data

## Security Notes

- The `token.pickle` file contains your authentication tokens - keep it secure
- The application only requests read-only access to your Gmail
- Your credentials are stored locally and not shared

## Troubleshooting

1. **Authentication Error**: Delete `token.pickle` and run again
2. **API Not Enabled**: Enable Gmail API in Google Cloud Console
3. **Permission Denied**: Check OAuth consent screen configuration
4. **Import Error**: Install dependencies with `pip install -r requirements.txt`

## Available Methods

### GmailClient Methods

- `get_recent_emails(days=7, max_results=20)` - Get recent emails
- `search_emails(query='', max_results=10)` - Search with Gmail query syntax
- `get_emails_from_sender(sender_email, max_results=10)` - Filter by sender
- `get_emails_with_subject(subject_keyword, max_results=10)` - Filter by subject
- `get_unread_emails(max_results=10)` - Get unread emails only
- `get_email_stats()` - Get account statistics
- `print_email_summary(emails)` - Print formatted email list

### Gmail Query Syntax

You can use Gmail's advanced search syntax:

- `from:sender@example.com` - Emails from specific sender
- `subject:meeting` - Emails with "meeting" in subject
- `after:2023/01/01` - Emails after specific date
- `before:2023/12/31` - Emails before specific date
- `has:attachment` - Emails with attachments
- `is:unread` - Unread emails
- `label:important` - Emails with specific label

## Example Output

The application will display:
- Account statistics (email address, total messages)
- Recent emails summary
- Unread emails
- Search results
- Exported JSON file with detailed email data
