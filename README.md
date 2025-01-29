# News Aggregator with AI Summarization

A simple news aggregation tool that collects articles from NewsAPI and generates AI-powered summaries using OpenAI GPT-3.5 Turbo and LangChain. The project includes a streamlined pipeline for ingesting news articles, summarizing content, and presenting it through a clean web interface.

The ingestion system (`ingest.py`) fetches articles from NewsAPI's `/v2/everything` endpoint with configurable filters and implements URL-based deduplication before storing in MongoDB. The summarization engine (`summarize.py`) processes these articles using LangChain's MapReduce architecture, where articles are first split and summarized in chunks (map phase) before being combined into a final coherent summary (reduce phase). The system uses OpenAI's GPT-3.5 Turbo model for generating summaries and maintains separate MongoDB collections for raw articles and their summaries.

## Features

- 🔄 Automated news article collection using NewsAPI
- 🤖 AI-powered article summarization using GPT-3.5 Turbo
- 💾 MongoDB integration for efficient data storage
- 🌐 Clean web interface built with Streamlit
- 🐳 Docker support for easy deployment

## Architecture

The project consists of three main components:

1. **Ingest System** (`ingest.py`): Collects articles from NewsAPI and stores them in MongoDB
2. **Summarization Engine** (`summarize.py`): Processes articles using LangChain and GPT-3.5 Turbo to generate concise summaries
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