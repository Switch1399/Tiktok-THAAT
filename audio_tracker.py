from playwright.sync_api import sync_playwright
import pandas as pd

def get_trending_audio(limit=10):
    trending_url = "https://www.tiktok.com/music/trending"
    audio_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(trending_url, timeout=60000)
        page.wait_for_timeout(6000)

        items = page.query_selector_all("div[data-e2e='music-item']")

        for item in items[:limit]:
            try:
                title = item.query_selector("h4").inner_text()
                uses = item.query_selector("span[data-e2e='music-uses']").inner_text()
                link = item.query_selector("a").get_attribute("href")

                audio_data.append({
                    "Title": title,
                    "Uses": uses,
                    "URL": link
                })
            except:
                continue

        browser.close()

    df = pd.DataFrame(audio_data)
    df.to_csv("data/trending_audio.csv", index=False)
    print(df)

if __name__ == "__main__":
    get_trending_audio()