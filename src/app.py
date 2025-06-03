from flask import Flask, request, jsonify
from ai_generator import generate_blog_post
from seo_fetcher import get_mock_seo_data
from apscheduler.schedulers.background import BackgroundScheduler
import os

app = Flask(__name__)

# Predefined keyword for daily generation
DAILY_KEYWORD = "wireless earbuds"

@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400

    seo_data = get_mock_seo_data(keyword)
    blog_post = generate_blog_post(keyword, seo_data)

    return jsonify({
        "keyword": keyword,
        "seo_data": seo_data,
        "blog_post": blog_post
    })

def daily_job():
    get_mock_seo_data(DAILY_KEYWORD)
    generate_blog_post(DAILY_KEYWORD, get_mock_seo_data(DAILY_KEYWORD))

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(daily_job, 'interval', days=1, next_run_time='2023-10-01 00:00:00')  # Set to your desired time
    scheduler.start()
    
    try:
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()