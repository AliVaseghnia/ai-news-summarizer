# News Aggregator with AI Summarization

A simple news aggregation tool that collects articles from NewsAPI and generates AI-powered summaries using OpenAI GPT-4o and LangChain. The project includes a streamlined pipeline for ingesting news articles, summarizing content, and presenting it through a clean web interface.

The ingestion system (`ingest.py`) fetches articles from NewsAPI's `/v2/everything` endpoint with configurable filters and implements URL-based deduplication before storing in MongoDB. The summarization engine (`summarize.py`) processes these articles using LangChain's MapReduce architecture, where articles are first split and summarized in chunks (map phase) before being combined into a final coherent summary (reduce phase). The system uses OpenAI's GPT-4o model for generating summaries and maintains separate MongoDB collections for raw articles and their summaries.

## Features

- 🔄 Automated news article collection using NewsAPI
- 🤖 AI-powered article summarization using GPT-4o
- 💾 MongoDB integration for efficient data storage
- 🌐 Clean web interface built with Streamlit
- 🐳 Docker support for easy deployment

## Architecture

The project consists of three main components:

1. **Ingest System** (`ingest.py`): Collects articles from NewsAPI and stores them in MongoDB
2. **Summarization Engine** (`summarize.py`): Processes articles using LangChain and GPT-4o to generate concise summaries
3. **Web Interface** (`ui.py`): Presents the summarized articles through a Streamlit-based UI

## Prerequisites

- Docker and Docker Compose
- OpenAI API key
- NewsAPI key
- MongoDB connection string (if needed)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AliVaseghnia/ai-news-summarizer.git
cd ai-news-summarizer
```

2. Copy the example environment file and update it with your credentials:
```bash
cp .env.example .env
```
Then edit `.env` with your API keys. The default MongoDB URI will work with the Docker setup.

## Usage

Build and start the services:
```bash
docker-compose up --build
```

Once the services are running, access the web interface at:
```
http://localhost:8501
```

## Project Structure

- `ingest.py`: News article collection script
- `summarize.py`: Article summarization using LangChain and GPT-4
- `ui.py`: Streamlit web interface
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container configuration
- `docker-compose.yml`: Multi-container Docker configuration
- `.env`: Environment variables configuration