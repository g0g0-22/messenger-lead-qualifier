# Messenger Lead Qualifier 🧠📩

A smart AI-powered lead qualification assistant for Facebook Messenger, built using Flask, OpenAI, and SQLite — with automatic lead summarization into Google Sheets.

## 🧐 What It Does

When a user messages your Facebook Page:

1. Their conversation is tracked and stored in a local SQLite database.
2. Context-aware responses are generated using OpenAI's GPT-4o.
3. Once the AI detects that the lead is qualified (destination, dates, guests, etc.), it:

   - Summarizes the conversation.
   - Stores the lead summary in a Google Sheet.
   - Ends the conversation politely.

## 🛡️ Stack

- **Backend**: Python + Flask + Flask-RESTX
- **Database**: SQLite (for development)
- **AI**: OpenAI (GPT-4o)
- **Messenger**: Meta Graph API
- **Sheets Integration**: gspread + Google Sheets API

## 📁 Folder Structure

```
app/
├── ai/               # AI client + response logic
├── db/               # SQLite logic and init
├── facebook/         # Facebook webhook + send message
├── __init__.py       # Flask app factory
├── resources.py      # API routes
.env                  # API keys and secrets
chatbot.db            # SQLite database
```

## ⚙️ Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/messenger-lead-qualifier.git
   cd messenger-lead-qualifier
   ```

2. **Install dependencies**

   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**

   ```env
   PAGE_ACCESS_TOKEN=your_facebook_page_token
   OPENAI_API_KEY=your_openai_key
   GOOGLE_SHEETS_CREDENTIALS=your_json_key_path_or_env
   SHEET_ID=your_google_sheet_id
   ```

4. **Initialize the database**

   ```bash
   flask --app app run  # Will auto-create `chatbot.db` if missing
   ```

5. **Expose webhook (for dev)**
   Use [ngrok](https://ngrok.com/) or similar:

   ```bash
   ngrok http 5000
   ```

## 📝 Google Sheets Integration

Make sure:

- You enabled both **Google Sheets API** and **Google Drive API**.
- You've shared your Google Sheet with the service account email.

---

## 🚀 Example Use Case

> User: "Hi, I’m planning a trip to Zakynthos from July 21st to 29th for 4 people."
>
> ✅ AI qualifies lead.
>
> 📅 Lead gets logged to the sheet:

```
UID        | Name        | Summary
-----------|-------------|----------------------------------------
1234567890 | John Smith  | Trip to Zakynthos, July 21-29, 4 guests
```

---

## 🚀 Future Improvements

- Add webhook verification logic
- Switch to PostgreSQL or Firebase for production
- Deploy on Render or Railway
- Add admin panel for managing leads

---

## 🧑‍💻 Author

Made by [Gorazd Nanevski](https://github.com/gorazdnanevski) 💻
