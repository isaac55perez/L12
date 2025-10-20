#!/usr/bin/env python3
"""
Example usage of the Gmail Client
This script demonstrates how to access and retrieve Gmail emails
"""

from gmail_client import GmailClient
import json

def main():
    print("Gmail Email Extractor")
    print("=" * 50)
    
    try:
        # Initialize Gmail client (will handle authentication)
        gmail = GmailClient()
        
        # Get account statistics
        print("\n1. Account Statistics:")
        stats = gmail.get_email_stats()
        if stats:
            print(f"   Email Address: {stats['email_address']}")
            print(f"   Total Messages: {stats['messages_total']}")
            print(f"   Total Threads: {stats['threads_total']}")
        
        # Get recent emails (last 7 days)
        print("\n2. Recent Emails (Last 7 days):")
        recent_emails = gmail.get_recent_emails(days=7, max_results=5)
        gmail.print_email_summary(recent_emails)
        
        # Get unread emails
        print("\n3. Unread Emails:")
        unread_emails = gmail.get_unread_emails(max_results=5)
        gmail.print_email_summary(unread_emails)
        
        # Example: Search for emails with specific keywords
        print("\n4. Search Example - Emails containing 'meeting':")
        meeting_emails = gmail.search_emails('meeting', max_results=3)
        gmail.print_email_summary(meeting_emails)
        
        # Example: Get emails from a specific sender
        print("\n5. Example - Get emails from Gmail (replace with actual sender):")
        # gmail_emails = gmail.get_emails_from_sender('noreply@gmail.com', max_results=3)
        # gmail.print_email_summary(gmail_emails)
        print("   (Uncomment and modify the sender email above to test)")
        
        # Save detailed email data to JSON file
        if recent_emails:
            print("\n6. Saving recent emails to 'recent_emails.json'...")
            with open('recent_emails.json', 'w', encoding='utf-8') as f:
                json.dump(recent_emails, f, indent=2, ensure_ascii=False)
            print("   Emails saved successfully!")
        
        print("\nDone! Check the generated files for detailed email data.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure you have:")
        print("1. Installed required packages: pip install google-auth google-auth-oauthlib google-api-python-client")
        print("2. Set up Google API credentials properly")
        print("3. Enabled Gmail API in your Google Cloud Console")

if __name__ == "__main__":
    main()
