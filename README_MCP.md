# Gmail Data Extractor with MCP Support

**Enhanced Gmail extraction tool with Model Context Protocol (MCP) integration for Claude CLI compatibility and Hebrew CSV/Excel support.**

## 🚀 Features

- **MCP Protocol Integration**: Works seamlessly with Claude CLI via Model Context Protocol
- **Hebrew Language Support**: Full UTF-8 support for Hebrew characters in CSV and Excel files
- **Excel Export**: Professional Excel files with formatting, filtering, and frozen headers
- **Advanced Email Filtering**: Extract lesson/exercise emails with smart keyword detection
- **Response Tracking**: Built-in columns for tracking email responses
- **Authentication Management**: OAuth 2.0 with persistent token storage
- **Date Range Queries**: Flexible date-based email extraction
- **Thread Tracking**: Track email conversations and threads

## 📋 Requirements

- Python 3.8+
- Gmail API credentials
- UV virtual environment
- Required packages (installed automatically)

## 🔧 Setup

### 1. Install Dependencies with UV

```bash
cd /home/gal-t2/agents/ExtractLessonsFromGmail

# Create UV virtual environment (if not exists)
uv venv

# Install packages
source .venv/bin/activate
pip install -r environment.txt
```

### 2. Gmail API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Gmail API
4. Create OAuth 2.0 credentials (Desktop Application)
5. Download the JSON credentials file
6. Save it as `config/gmail_credentials.json`

### 3. MCP Configuration

The MCP server is configured in `mcp_config.json` for Claude CLI integration.

## 🎯 Usage

### Starting the MCP Server

```bash
# Using the startup script (recommended)
./start_gmail_extractor.sh

# Or manually
source .venv/bin/activate
python3 mcp_gmail_server.py
```

### Using with Claude CLI

Once the MCP server is running, Claude CLI can automatically discover and use the Gmail extraction tools:

1. **Authenticate Gmail Access**:
   ```
   Please use the gmail-data-extractor to authenticate with Gmail
   ```

2. **Extract Lesson Emails**:
   ```
   Extract all lesson emails from September 20-26, 2025 sent to segal@gal-tech.ai
   ```

3. **Create Hebrew CSV**:
   ```
   Create a Hebrew-compatible CSV file from the extracted emails
   ```

4. **Generate Excel Report**:
   ```
   Create an Excel file with proper Hebrew support from the extracted data
   ```

## 🛠️ Available MCP Tools

### 1. `authenticate_gmail`
Authenticate with Gmail API using OAuth authorization code.

**Parameters:**
- `auth_code` (string, required): OAuth authorization code from Google

### 2. `get_auth_url`
Generate Gmail OAuth authorization URL for first-time setup.

**Returns:** Authorization URL and setup instructions

### 3. `extract_lesson_emails`
Extract lesson/exercise emails from Gmail with advanced filtering.

**Parameters:**
- `start_date` (string, required): Start date in YYYY-MM-DD format
- `end_date` (string, required): End date in YYYY-MM-DD format
- `recipient` (string, optional): Target email (default: segal@gal-tech.ai)
- `keywords` (array, optional): Keywords to search for
- `max_results` (integer, optional): Maximum results (default: 100)

### 4. `create_hebrew_csv`
Create Hebrew-compatible CSV file with UTF-8 BOM for Excel compatibility.

**Parameters:**
- `email_data` (array, required): Extracted email data
- `filename` (string, optional): Output filename
- `include_response_tracking` (boolean, optional): Include response columns

### 5. `create_excel_file`
Create professional Excel file with Hebrew support and formatting.

**Parameters:**
- `email_data` (array, required): Extracted email data
- `filename` (string, optional): Output filename
- `sheet_name` (string, optional): Excel sheet name

### 6. `get_email_count`
Get count of emails matching specific criteria.

**Parameters:**
- `query` (string, optional): Gmail search query
- `start_date` (string, optional): Start date in YYYY-MM-DD
- `end_date` (string, optional): End date in YYYY-MM-DD

## 📊 Output Formats

### CSV Format (Hebrew Compatible)
- Uses UTF-8-sig encoding for proper Hebrew display in Excel
- Pipe-delimited fields with proper escaping
- Response tracking columns for follow-up management

### Excel Format
- Professional styling with headers
- Auto-adjusted column widths
- Frozen header row
- Filter functionality
- Border formatting
- Hebrew character support

## 🔄 Workflow Example

### Complete Gmail Extraction Workflow

1. **Start the MCP Server**:
   ```bash
   ./start_gmail_extractor.sh
   ```

2. **Get Authorization URL** (first time only):
   ```
   Use the gmail-data-extractor to get an authorization URL
   ```

3. **Authenticate**:
   ```
   Authenticate with Gmail using the authorization code I received
   ```

4. **Extract Emails**:
   ```
   Extract lesson emails from 2025-09-20 to 2025-09-26
   ```

5. **Generate Reports**:
   ```
   Create both Hebrew CSV and Excel files from the extracted emails
   ```

## 🎨 Features

### Hebrew Language Support
- Full UTF-8 support for Hebrew characters
- Smart keyword detection in Hebrew and English
- Proper RTL text handling in Excel
- CSV files with BOM for Excel compatibility

### Smart Email Detection
- Advanced pattern matching for lesson/exercise numbers
- Multi-language keyword support (Hebrew, English)
- Content-based filtering with subject and body analysis
- Thread and conversation tracking

### Professional Excel Output
- Formatted headers with company colors
- Auto-sized columns with optimal widths
- Data filtering and sorting
- Frozen header rows for easy navigation
- Professional styling and borders

## 📁 File Structure

```
/home/gal-t2/agents/ExtractLessonsFromGmail/
├── mcp_gmail_server.py          # Main MCP server
├── enhanced_hebrew_extractor.py # Enhanced extractor with Hebrew support
├── gmail_api_tool.py           # Core Gmail API functionality
├── start_gmail_extractor.sh    # Startup script
├── mcp_config.json            # MCP configuration
├── environment.txt            # Package requirements
├── config/
│   ├── gmail_credentials.json # Gmail API credentials
│   └── token.pickle          # Authentication token
└── csv/                      # Output directory
    ├── *.csv                # Generated CSV files
    └── *.xlsx               # Generated Excel files
```

## 🐛 Troubleshooting

### Common Issues

1. **Authentication Failed**:
   - Check Gmail credentials file location
   - Ensure OAuth consent screen is configured
   - Verify redirect URI is set to `urn:ietf:wg:oauth:2.0:oob`

2. **Package Import Errors**:
   - Ensure UV virtual environment is activated
   - Run `pip install -r environment.txt`
   - Check Python version compatibility

3. **Hebrew Character Issues**:
   - CSV files use UTF-8-sig encoding
   - Excel files have proper font settings
   - Check system locale settings

4. **MCP Server Connection**:
   - Ensure server is running before using Claude CLI
   - Check configuration in `mcp_config.json`
   - Verify Python paths are correct

### Debug Mode

Enable debug logging by setting environment variable:

```bash
export PYTHONPATH=/path/to/extractor:$PYTHONPATH
export DEBUG=1
./start_gmail_extractor.sh
```

## 📝 License

This Gmail data extractor is designed for educational and legitimate business purposes only. Users must comply with Gmail's Terms of Service and applicable privacy laws.

## 🤝 Support

For issues and support:
1. Check the troubleshooting section
2. Verify Gmail API credentials
3. Ensure all dependencies are installed
4. Check MCP server logs for error details

---

**Note**: This tool requires valid Gmail API credentials and user consent for accessing Gmail data. Always ensure you have proper authorization before extracting email data.