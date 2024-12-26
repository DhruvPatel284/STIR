# Twitter Trends Scraper

A web application that automatically scrapes and displays trending topics from Twitter/X using Selenium WebDriver and Flask. The application stores trends in MongoDB and provides a clean, Twitter-like interface for viewing them.

## 📚 Table of Contents
- [Project Overview](#-project-overview)
- [Project Demo](#-project-demo)
- [Key Features](#-key-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Features](#-features)
- [Contributing](#-contributing)

## 🚀 Project Overview

Twitter Trends Scraper is a full-stack web application that automatically logs into Twitter, scrapes the current trending topics, stores them in a MongoDB database, and displays them in a clean, Twitter-inspired interface. The application updates trends on demand and shows timestamps for each update.

## 🎥 Project Demo
<video controls src="Screen Recording 2024-12-26 173948.mp4" title="Title"></video>

### Key Features:
- **Automated Login**: Securely logs into Twitter using provided credentials
- **Real-time Scraping**: Fetches current trending topics from Twitter
- **Data Persistence**: Stores trends in MongoDB with timestamps
- **Clean UI**: Twitter-inspired interface for displaying trends
- **Refresh Capability**: On-demand trend updates

## 🛠️ Technologies Used

### Backend:
- **Python**: Core programming language
- **Flask**: Web framework for serving the application
- **Selenium**: For web scraping and browser automation
- **MongoDB**: Database for storing trend data
- **ChromeDriver**: WebDriver for Chrome browser automation

### Frontend:
- **HTML/CSS**: For structuring and styling the interface
- **Jinja2**: Template engine for dynamic content
- **JavaScript**: For interactive features

## 🏗️ Project Structure

```
twitter-trends-scraper/
├── app.py              # Flask application
├── scraper.py          # Twitter scraping logic
├── config.py           # Configuration and environment variables
├── requirements.txt    # Python dependencies
└── .env               # Environment variables file
```

## 🚀 Getting Started

### Prerequisites:
- Python 3.8+
- Chrome Browser
- MongoDB
- ChromeDriver

### Step-by-Step Setup:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DhruvPatel284/Twitter-Trends-Scraper.git
   cd Twitter-Trends-Scraper
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** in `.env` file:
   ```env
   TWITTER_USERNAME=your_twitter_username
   TWITTER_PASSWORD=your_twitter_password
   MONGODB_URI=your_mongodb_connection_string
   PROXYMESH_USERNAME=your_proxymesh_username
   PROXYMESH_PASSWORD=your_proxymesh_password
   PROXYMESH_HOST=your_proxymesh_host
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   - Open your browser and visit: `http://localhost:5000`

## 📂 Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
TWITTER_USERNAME=your_twitter_username
TWITTER_PASSWORD=your_twitter_password
MONGODB_URI=your_mongodb_connection_string
PROXYMESH_USERNAME=your_proxymesh_username
PROXYMESH_PASSWORD=your_proxymesh_password
PROXYMESH_HOST=your_proxymesh_host
```

## 📝 Features

1. **Automated Twitter Login**: 
   - Secure login using provided credentials
   - Handles login flow with proper timing and error handling

2. **Trend Scraping**:
   - Captures both hashtag and non-hashtag trends
   - Filters out promotional content
   - Handles various trend formats and structures

3. **Data Storage**:
   - Stores trends with unique IDs
   - Includes timestamps for each update
   - Maintains trend history in MongoDB

4. **User Interface**:
   - Clean, Twitter-inspired design
   - Responsive layout
   - One-click trend refresh
   - Timestamp display for each update

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request