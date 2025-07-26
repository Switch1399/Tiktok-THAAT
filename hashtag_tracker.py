from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import datetime
import os

def track_hashtags(hashtags, max_posts=10):
    results = []
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for tag in hashtags:
            url = f"https://www.tiktok.com/tag/{tag}"
            try:
                page.goto(url, timeout=60000)
                page.wait_for_timeout(5000)

                posts = page.query_selector_all("div[data-e2e='video-feed-item']")
                post_count = 0
                like_total = 0

                for post in posts[:max_posts]:
                    try:
                        likes = post.query_selector("strong[data-e2e='like-count']").inner_text()
                        likes = int(likes.replace('K', '000').replace('M', '000000').replace('.', ''))
                        like_total += likes
                        post_count += 1
                    except:
                        continue

                results.append({
                    "Hashtag": tag,
                    "Time": date,
                    "Posts": post_count,
                    "Total Likes": like_total
                })

            except Exception as e:
                print(f"Error with #{tag}: {e}")
                continue

        browser.close()

    return pd.DataFrame(results)

if __name__ == "__main__":
    hashtags = ["aiart", "foryou", "summerfit", "barbiecore"]
    df = track_hashtags(hashtags)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/hashtag_trends_log.csv", mode='a', header=not os.path.exists("data/hashtag_trends_log.csv"), index=False)
    print(df)