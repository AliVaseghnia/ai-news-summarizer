# News Aggregator with AI-Powered Summarization

A powerful news aggregation system that collects articles from various sources and generates AI-powered summaries using GPT-4. The project includes a streamlined pipeline for ingesting news articles, summarizing content, and presenting it through a clean web interface.

## Features

- 🔄 Automated news article collection using NewsAPI
- 🤖 AI-powered article summarization using GPT-4
- 💾 MongoDB integration for efficient data storage
- 🌐 Clean web interface built with Streamlit
- 🐳 Docker support for easy deployment

## Architecture

The project consists of three main components:

1. **Ingest System** (`ingest.py`): Collects articles from NewsAPI and stores them in MongoDB
2. **Summarization Engine** (`summarize.py`): Processes articles using LangChain and GPT-4 to generate concise summaries
3. **Web Interface** (`ui.py`): Presents the summarized articles through a Streamlit-based UI

## Prerequisites

- Python 3.8+
- MongoDB
- OpenAI API key
- NewsAPI key
- Docker and Docker Compose (optional)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd news-aggregator-ai-summarizer
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your configuration:
```
OPENAI_API_KEY=your_openai_api_key
NEWS_API_KEY=your_newsapi_key
MONGO_URI=your_mongodb_connection_string
```

## Usage

### Running with Python

1. Start the news ingestion:
```bash
python ingest.py
```

2. Generate summaries:
```bash
python summarize.py
```

3. Launch the web interface:
```bash
streamlit run ui.py
```

### Running with Docker

1. Build and start the services:
```bash
docker-compose up --build
```

## Project Structure

- `ingest.py`: News article collection script
- `summarize.py`: Article summarization using LangChain and GPT-4
- `ui.py`: Streamlit web interface
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container configuration
- `docker-compose.yml`: Multi-container Docker configuration
- `.env`: Environment variables configuration

## Dependencies

- requests==2.31.0
- pymongo==4.6.1
- openai==1.56.1
- langchain==0.1.9
- langchain-openai==0.0.8
- streamlit==1.32.0
- python-dotenv==1.0.7
- newsapi-python==0.2.7

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 