# NASA Space Biology Knowledge Engine

A comprehensive AI-powered knowledge engine for exploring NASA's space biology research publications. This tool leverages artificial intelligence, knowledge graphs, and interactive visualizations to help researchers, mission planners, and scientists discover insights from 608+ NASA bioscience publications.

## Features

### 🔍 **AI-Powered Search**
- Semantic search across publication titles and abstracts
- Filter by research areas, organisms, and space missions
- Relevance-based ranking using TF-IDF and cosine similarity

### 📊 **Interactive Dashboard**
- Research trends analysis over time
- Publication distribution by category
- Real-time statistics and metrics

### 🧠 **AI Insights**
- Automated analysis of research patterns
- Key findings extraction
- Trend identification and gap analysis

### 🕸️ **Knowledge Graph**
- Interactive network visualization
- Relationship mapping between publications
- Category and tag-based connections

### 📈 **Data Visualization**
- Publication trends over time
- Research area distribution
- Interactive charts and graphs

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript, D3.js, Plotly.js
- **Backend**: Python Flask, RESTful API
- **AI/ML**: scikit-learn, NLTK, TF-IDF, cosine similarity
- **Data Processing**: pandas, numpy
- **Knowledge Graph**: NetworkX
- **Visualization**: D3.js, Plotly.js

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd space-biology-knowledge-engine
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK data**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   ```

4. **Process the data**
   ```bash
   python process_data.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`
   - The API endpoints are available at `http://localhost:5000/api/`

## Usage

### Web Interface
1. Open the main dashboard at `http://localhost:5000`
2. Use the search bar to find publications by keywords
3. Apply filters to narrow down results by category, year, or tags
4. Explore AI insights and research trends
5. Interact with the knowledge graph to discover relationships

### API Endpoints

- `GET /api/publications` - Get all publications
- `POST /api/search` - Search publications with query and filters
- `GET /api/trends` - Get research trends analysis
- `GET /api/insights` - Get AI-generated insights
- `GET /api/knowledge-graph` - Get knowledge graph data
- `GET /api/stats` - Get application statistics

### Example API Usage

```python
import requests

# Search for microgravity research
response = requests.post('http://localhost:5000/api/search', 
                        json={'query': 'microgravity bone loss', 
                              'filters': {'category': 'bone'}})
results = response.json()

# Get AI insights
response = requests.get('http://localhost:5000/api/insights')
insights = response.json()
```

## Data Sources

The knowledge engine processes data from:
- **NASA Bioscience Publications**: 608 open-access publications from PubMed Central
- **NASA Open Science Data Repository (OSDR)**: Primary data and metadata
- **NASA Space Life Sciences Library**: Additional relevant publications
- **NASA Task Book**: Grant information and project details

## Research Areas Covered

- **Microgravity Effects**: Bone loss, muscle atrophy, cellular changes
- **Space Radiation**: DNA damage, repair mechanisms, protective measures
- **Plant Biology**: Growth patterns, gravitropism, space agriculture
- **Animal Studies**: Mouse, rat, Drosophila, C. elegans research
- **Human Research**: Astronaut health, immune system, cardiovascular
- **Space Missions**: ISS, Bion-M, Inspiration4, Space Shuttle

## Key Features for Different Users

### For Scientists
- Semantic search across research literature
- Trend analysis and gap identification
- Knowledge graph exploration
- AI-powered insights and summaries

### For Mission Planners
- Risk assessment based on research findings
- Countermeasure effectiveness analysis
- Long-duration mission planning insights
- Evidence-based decision support

### For Managers
- Research investment opportunities
- Progress tracking and metrics
- Resource allocation insights
- Strategic planning support

## Contributing

We welcome contributions to improve the NASA Space Biology Knowledge Engine:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- NASA Biological and Physical Sciences Division
- NASA Open Science Data Repository
- PubMed Central for open-access publications
- The space biology research community

## Contact

For questions, suggestions, or collaboration opportunities, please contact:
- Project Lead: [Your Name]
- Email: [your.email@example.com]
- GitHub: [your-github-username]

## Future Enhancements

- Integration with NASA OSDR API
- Real-time data updates
- Advanced NLP models for better text analysis
- Machine learning for predictive insights
- Mobile application development
- Multi-language support
- Collaborative features for research teams