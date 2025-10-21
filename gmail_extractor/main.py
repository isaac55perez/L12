
from fastapi import FastAPI
from gmail_client import GmailClient
from pydantic import BaseModel

app = FastAPI(
    title="mail_assist",
    description="An MCP server for interacting with your Gmail account.",
    version="1.0.0",
)

gmail_client = GmailClient()

class Prompt(BaseModel):
    query: str

@app.get("/tools/get_recent_emails")
def get_recent_emails(days: int = 7, max_results: int = 10):
    """Get recent emails from the last N days."""
    return gmail_client.get_recent_emails(days=days, max_results=max_results)

@app.get("/tools/search_emails")
def search_emails(query: str, max_results: int = 10):
    """Search emails with Gmail query syntax."""
    return gmail_client.search_emails(query=query, max_results=max_results)

@app.get("/tools/get_unread_emails")
def get_unread_emails(max_results: int = 10):
    """Get unread emails."""
    return gmail_client.get_unread_emails(max_results=max_results)

@app.get("/tools/get_email_details")
def get_email_details(message_id: str):
    """Get detailed information about a specific email."""
    return gmail_client.get_email_details(message_id=message_id)

@app.get("/tools/get_account_stats")
def get_account_stats():
    """Get basic statistics about the Gmail account."""
    return gmail_client.get_email_stats()

@app.post("/prompt")
def process_prompt(prompt: Prompt):
    """
    Process a natural language prompt to interact with Gmail.
    This is a simplified implementation. A more advanced version would use an LLM to parse the prompt.
    """
    query = prompt.query.lower()
    if "recent emails" in query:
        return get_recent_emails()
    elif "search for" in query:
        search_query = query.split("search for")[-1].strip()
        return search_emails(query=search_query)
    elif "unread emails" in query:
        return get_unread_emails()
    elif "account stats" in query:
        return get_account_stats()
    else:
        return {"error": "Could not understand the prompt. Please try something like 'get recent emails', 'search for meeting', 'get unread emails', or 'get account stats'."}

@app.get("/")
def read_root():
    return {"message": "Welcome to the mail_assist MCP server. See /docs for available tools."}

