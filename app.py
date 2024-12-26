from flask import Flask, render_template_string
from scraper import TwitterScraper
import json

app = Flask(__name__)
scraper = TwitterScraper()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Twitter Trends</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #000000;
            color: #ffffff;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 400px;
            margin: 0 auto;
            background-color: #16181c;
            border-radius: 16px;
            padding: 16px;
        }
        .header {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 1px solid #2f3336;
        }
        .trend-item {
            padding: 12px 16px;
            border-bottom: 1px solid #2f3336;
            font-size: 15px;
            font-weight: bold;
        }
        .run-button {
            background-color: #1d9bf0;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
            margin-top: 20px;
            font-size: 15px;
            width: 100%;
        }
        .run-button:hover {
            background-color: #1a8cd8;
        }
        .timestamp {
            font-size: 13px;
            color: #71767b;
            margin-top: 12px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">Trending Topics</div>
        {% if result %}
            {% for i in range(1, 6) %}
                {% set trend = result["nameoftrend" ~ i] %}
                {% if trend != "N/A" %}
                <div class="trend-item">{{ trend }}</div>
                {% endif %}
            {% endfor %}
            <button onclick="window.location.href='/scrape'" class="run-button">Refresh Trends</button>
            <div class="timestamp">Last updated: {{ result.timestamp.strftime('%Y-%m-%d %H:%M:%S') }}</div>
        {% else %}
            <button onclick="window.location.href='/scrape'" class="run-button">Get Trends</button>
        {% endif %}
    </div>
</body>
</html>
"""
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/scrape')
def scrape():
    result = scraper.get_trending_topics()
    json_data = json.dumps(result, default=str, indent=2)
    return render_template_string(HTML_TEMPLATE, result=result, json_data=json_data)

if __name__ == '__main__':
    app.run(debug=True)






# from flask import Flask, render_template_string
# from scraper import TwitterScraper
# import json

# app = Flask(__name__)
# scraper = TwitterScraper()

# HTML_TEMPLATE = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Twitter Trends Scraper</title>
#     <style>
#         body {
#             font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
#             background-color: #000000;
#             color: #ffffff;
#             margin: 0;
#             padding: 20px;
#         }
#         .container {
#             max-width: 400px;
#             margin: 0 auto;
#             background-color: #16181c;
#             border-radius: 16px;
#             padding: 16px;
#         }
#         .header {
#             font-size: 20px;
#             font-weight: bold;
#             margin-bottom: 20px;
#             padding-bottom: 12px;
#             border-bottom: 1px solid #2f3336;
#         }
#         .trend-item {
#             padding: 12px 0;
#             border-bottom: 1px solid #2f3336;
#         }
#         .trend-category {
#             font-size: 13px;
#             color: #71767b;
#             margin-bottom: 4px;
#         }
#         .trend-title {
#             font-size: 15px;
#             font-weight: bold;
#             margin-bottom: 4px;
#         }
#         .trend-posts {
#             font-size: 13px;
#             color: #71767b;
#         }
#         .more-link {
#             color: #1d9bf0;
#             text-decoration: none;
#             font-size: 15px;
#             padding: 16px 0;
#             display: block;
#         }
#         .more-link:hover {
#             text-decoration: underline;
#         }
#         .run-button {
#             background-color: #1d9bf0;
#             color: white;
#             border: none;
#             padding: 12px 24px;
#             border-radius: 20px;
#             cursor: pointer;
#             font-weight: bold;
#             margin-top: 20px;
#             font-size: 15px;
#             width: 100%;
#         }
#         .run-button:hover {
#             background-color: #1a8cd8;
#         }
#         .timestamp {
#             font-size: 13px;
#             color: #71767b;
#             margin-top: 12px;
#             text-align: center;
#         }
#     </style>
# </head>
# <body>
#     <div class="container">
#         <div class="header">What's happening</div>
#         {% if result %}
#             {% for i in range(1, 6) %}
#                 {% set trend = result["nameoftrend" ~ i] %}
#                 {% if trend != "N/A" %}
#                 <div class="trend-item">
#                     <div class="trend-category">Trending in India</div>
#                     <div class="trend-title">{{ trend }}</div>
#                     <div class="trend-posts">10K posts</div>
#                 </div>
#                 {% endif %}
#             {% endfor %}
#             <a href="#" class="more-link">Show more</a>
#             <button onclick="window.location.href='/scrape'" class="run-button">Refresh Trends</button>
#             <div class="timestamp">Last updated: {{ result.timestamp.strftime('%Y-%m-%d %H:%M:%S') }}</div>
#         {% else %}
#             <button onclick="window.location.href='/scrape'" class="run-button">Get Trends</button>
#         {% endif %}
#     </div>
# </body>
# </html>
# """

# @app.route('/')
# def home():
#     return render_template_string(HTML_TEMPLATE)

# @app.route('/scrape')
# def scrape():
#     result = scraper.get_trending_topics()
#     json_data = json.dumps(result, default=str, indent=2)
#     return render_template_string(HTML_TEMPLATE, result=result, json_data=json_data)

# if __name__ == '__main__':
#     app.run(debug=True)

