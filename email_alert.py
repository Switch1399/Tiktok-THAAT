import smtplib
import pandas as pd
from email.mime.text import MIMEText
from datetime import datetime

def send_email_alert():
    df = pd.read_csv("data/hashtag_trends_log.csv")
    latest = df[df["Time"] == df["Time"].max()]
    top = latest.sort_values(by="Total Likes", ascending=False).head(5)

    body = "🔥 Top 5 Trending TikTok Hashtags:\n\n"
    for _, row in top.iterrows():
        body += f"#{row['Hashtag']}: {row['Total Likes']} likes ({row['Posts']} posts)\n"

    msg = MIMEText(body)
    msg['Subject'] = f"TikTok Trend Alert – {datetime.now().strftime('%Y-%m-%d')}"
    msg['From'] = "your-email@gmail.com"
    msg['To'] = "your-email@gmail.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("your-email@gmail.com", "your-app-password")
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

if __name__ == "__main__":
    send_email_alert()