# TikTok Trend Tracker

This is a complete system to track TikTok hashtag trends and trending audio, visualize the results in a Streamlit dashboard, and automate email + Google Sheets alerts.

## Features
- Scrape TikTok hashtags
- Track trending audio
- Email daily trend reports
- Sync with Google Sheets
- Streamlit dashboard for visualization
- Scheduler for automation

## Setup

1. `pip install -r requirements.txt`
2. `playwright install`
3. Add your `your_key.json` (Google Sheets API)
4. Run `scheduler.py` or any script individually
5. Deploy `dashboard.py` using Streamlit Cloud

> ⚠️ Do not upload `your_key.json` to GitHub. Use `.gitignore`.