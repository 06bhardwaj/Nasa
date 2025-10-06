i# NASA Space Biology Knowledge Engine Configuration

# Application Settings
DEBUG = True
HOST = '0.0.0.0'
PORT = 5000

# Data Processing Settings
MAX_PUBLICATIONS_DISPLAY = 100
SEARCH_RESULTS_LIMIT = 50
KNOWLEDGE_GRAPH_NODES_LIMIT = 50

# AI/ML Settings
TFIDF_MAX_FEATURES = 1000
TFIDF_NGRAM_RANGE = (1, 2)
MIN_SIMILARITY_THRESHOLD = 0.1

# Knowledge Graph Settings
MIN_COMMON_TAGS = 2
GRAPH_LAYOUT_ITERATIONS = 100

# API Settings
CORS_ORIGINS = ['http://localhost:3000', 'http://localhost:5000']
API_RATE_LIMIT = '100 per minute'

# Logging Settings
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# File Paths
CSV_FILE_PATH = 'SB_publication_PMC.csv'
PROCESSED_DATA_PATH = 'processed_publications.json'
TEMPLATES_PATH = 'templates'
STATIC_PATH = 'static'

# External APIs
NASA_OSDR_API_URL = 'https://science.nasa.gov/biological-physical/data/'
NASA_TASK_BOOK_URL = 'https://taskbook.nasaprs.com/tbp/welcome.cfm'
NASA_NSLSL_URL = 'https://public.ksc.nasa.gov/nslsl/'
