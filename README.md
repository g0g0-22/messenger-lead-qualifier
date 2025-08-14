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


## 🚀 Future Improvements

- Add webhook verification logic
- Switch to PostgreSQL or Firebase for production
- Deploy on Render or Railway
- Add admin panel for managing leads

---

## 🧑‍💻 Author

Made by [Gorazd Nanevski](https://github.com/gorazdnanevski) 💻
