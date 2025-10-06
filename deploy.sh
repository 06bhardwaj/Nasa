#!/bin/bash

# NASA Space Biology Knowledge Engine - Deployment Script

echo "🚀 Deploying NASA Space Biology Knowledge Engine..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Download NLTK data
echo "🧠 Downloading NLTK data..."
python -c "
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
print('NLTK data downloaded successfully!')
"

# Process data if CSV file exists
if [ -f "SB_publication_PMC.csv" ]; then
    echo "📊 Processing NASA publications data..."
    python process_data.py
else
    echo "⚠️  CSV file not found. Using sample data."
fi

# Create necessary directories
mkdir -p templates static/css static/js static/images

# Copy HTML file to templates directory
if [ -f "index.html" ]; then
    cp index.html templates/
    echo "📄 HTML template copied to templates directory"
fi

# Start the application
echo "🌟 Starting NASA Space Biology Knowledge Engine..."
echo "🌐 Application will be available at: http://localhost:5000"
echo "📡 API endpoints available at: http://localhost:5000/api/"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python app.py
