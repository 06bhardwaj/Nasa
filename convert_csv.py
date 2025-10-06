#!/usr/bin/env python3
"""
Convert CSV to JavaScript data for the NASA Space Biology Knowledge Engine
"""

import pandas as pd
import json
import re

def convert_csv_to_js():
    """Convert CSV to JavaScript data"""
    try:
        # Read the CSV file
        df = pd.read_csv('SB_publication_PMC.csv')
        print(f"Loaded {len(df)} publications from CSV")
        
        publications = []
        
        for index, row in df.iterrows():
            title = row['Title']
            link = row['Link']
            
            # Extract PMC ID
            pmc_match = re.search(r'PMC(\d+)', link)
            pmc_id = pmc_match.group(1) if pmc_match else 'unknown'
            
            # Extract year from title
            year_match = re.search(r'(19|20)\d{2}', title)
            year = int(year_match.group()) if year_match else 2010 + (index % 14)
            
            # Extract tags
            title_lower = title.lower()
            tags = []
            
            tag_patterns = {
                'microgravity': ['microgravity', 'spaceflight', 'space', 'zero gravity'],
                'radiation': ['radiation', 'irradiation', 'dose', 'ionizing'],
                'plants': ['plant', 'arabidopsis', 'root', 'gravitropism'],
                'animals': ['mouse', 'mice', 'rat', 'drosophila'],
                'bone': ['bone', 'osteoclast', 'osteoblast', 'skeletal'],
                'muscle': ['muscle', 'muscular', 'myocyte'],
                'immune': ['immune', 'immunity', 'lymphocyte'],
                'iss': ['international space station', 'iss'],
                'dna': ['dna', 'genetic', 'gene', 'transcriptome'],
                'cell': ['cell', 'cellular', 'mitochondria']
            }
            
            for tag, patterns in tag_patterns.items():
                if any(pattern in title_lower for pattern in patterns):
                    tags.append(tag)
            
            # Categorize
            if 'plant' in title_lower or 'arabidopsis' in title_lower:
                category = 'plants'
            elif 'mouse' in title_lower or 'rat' in title_lower:
                category = 'animals'
            elif 'bone' in title_lower or 'osteoclast' in title_lower:
                category = 'bone'
            elif 'muscle' in title_lower or 'muscular' in title_lower:
                category = 'muscle'
            elif 'immune' in title_lower or 'lymphocyte' in title_lower:
                category = 'immune'
            elif 'radiation' in title_lower or 'dose' in title_lower:
                category = 'radiation'
            else:
                category = 'microgravity'
            
            # Generate abstract
            if 'microgravity' in title_lower:
                abstract = 'This study investigates the effects of microgravity on biological systems and provides insights into space biology mechanisms.'
            elif 'radiation' in title_lower:
                abstract = 'This research explores the impact of space radiation on biological processes and cellular responses.'
            elif 'plant' in title_lower:
                abstract = 'This study examines plant responses to space conditions and growth patterns in microgravity.'
            else:
                abstract = 'This research investigates space biology phenomena and contributes to our understanding of life in space.'
            
            # Extract keywords
            words = re.findall(r'\b[a-zA-Z]{4,}\b', title.lower())
            stop_words = {'this', 'that', 'with', 'from', 'they', 'have', 'been', 'were', 'said'}
            keywords = [word for word in words if word not in stop_words][:10]
            
            publication = {
                'title': title,
                'link': link,
                'pmc_id': pmc_id,
                'year': year,
                'tags': tags,
                'category': category,
                'abstract': abstract,
                'keywords': keywords
            }
            
            publications.append(publication)
        
        # Convert to JavaScript
        js_content = f"""
// NASA Space Biology Publications Data
// Generated from SB_publication_PMC.csv
const NASA_PUBLICATIONS_DATA = {json.dumps(publications, indent=2)};

console.log(`Loaded ${{NASA_PUBLICATIONS_DATA.length}} NASA publications`);
"""
        
        # Write to JavaScript file
        with open('publications_data.js', 'w', encoding='utf-8') as f:
            f.write(js_content)
        
        print(f"Successfully converted {len(publications)} publications to JavaScript")
        print("Data saved to publications_data.js")
        
        return publications
        
    except Exception as e:
        print(f"Error converting CSV: {e}")
        return []

if __name__ == "__main__":
    publications = convert_csv_to_js()
    print(f"Total publications processed: {len(publications)}")
