from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import requests
from ai_generator import generate_blog_post
from seo_fetcher import fetch_seo_data

def scheduled_job():
    keyword = "wireless earbuds"
    seo_data = fetch_seo_data(keyword)
    blog_post = generate_blog_post(keyword)
    
    # Here you can save the blog post to a file or database
    with open(f"generated_posts/{keyword.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.md", 'w') as f:
        f.write(blog_post)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_job, 'interval', days=1, next_run_time=datetime.now())
    scheduler.start()

if __name__ == "__main__":
    start_scheduler()