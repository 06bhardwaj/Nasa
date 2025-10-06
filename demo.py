#!/usr/bin/env python3
"""
NASA Space Biology Knowledge Engine - Demo Script
Demonstrates the key features and capabilities of the knowledge engine.
"""

import requests
import json
import time
from typing import List, Dict, Any

class SpaceBiologyDemo:
    """Demo class for the NASA Space Biology Knowledge Engine"""
    
    def __init__(self, base_url: str = "http://localhost:5000"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def demo_search_functionality(self):
        """Demonstrate search functionality"""
        print("🔍 DEMO: Search Functionality")
        print("=" * 50)
        
        # Search queries to demonstrate
        search_queries = [
            "microgravity bone loss",
            "plant growth space",
            "immune system spaceflight",
            "radiation DNA damage",
            "muscle atrophy space"
        ]
        
        for query in search_queries:
            print(f"\n📝 Searching for: '{query}'")
            try:
                response = self.session.post(f"{self.base_url}/api/search", 
                                          json={"query": query})
                if response.status_code == 200:
                    data = response.json()
                    if data['success']:
                        results = data['results']
                        print(f"   ✅ Found {len(results)} results")
                        if results:
                            top_result = results[0]
                            print(f"   📄 Top result: {top_result['title'][:60]}...")
                            print(f"   🏷️  Category: {top_result['category']}")
                            print(f"   📅 Year: {top_result['year']}")
                    else:
                        print(f"   ❌ Error: {data['error']}")
                else:
                    print(f"   ❌ HTTP Error: {response.status_code}")
            except Exception as e:
                print(f"   ❌ Error: {e}")
            
            time.sleep(1)  # Rate limiting
    
    def demo_filtering(self):
        """Demonstrate filtering capabilities"""
        print("\n🎯 DEMO: Filtering Capabilities")
        print("=" * 50)
        
        categories = ['bone', 'plants', 'animals', 'immune', 'radiation']
        
        for category in categories:
            print(f"\n🔍 Filtering by category: '{category}'")
            try:
                response = self.session.post(f"{self.base_url}/api/search", 
                                          json={
                                              "query": "",
                                              "filters": {"category": category}
                                          })
                if response.status_code == 200:
                    data = response.json()
                    if data['success']:
                        results = data['results']
                        print(f"   ✅ Found {len(results)} publications in {category} category")
                        if results:
                            sample_titles = [r['title'][:40] + '...' for r in results[:3]]
                            for i, title in enumerate(sample_titles, 1):
                                print(f"   {i}. {title}")
                    else:
                        print(f"   ❌ Error: {data['error']}")
                else:
                    print(f"   ❌ HTTP Error: {response.status_code}")
            except Exception as e:
                print(f"   ❌ Error: {e}")
            
            time.sleep(1)
    
    def demo_ai_insights(self):
        """Demonstrate AI insights generation"""
        print("\n🧠 DEMO: AI-Powered Insights")
        print("=" * 50)
        
        try:
            response = self.session.get(f"{self.base_url}/api/insights")
            if response.status_code == 200:
                data = response.json()
                if data['success']:
                    insights = data['insights']
                    print(f"   ✅ Generated {len(insights)} AI insights")
                    
                    for i, insight in enumerate(insights, 1):
                        print(f"\n   📊 Insight {i}: {insight['title']}")
                        print(f"   📝 {insight['content']}")
                else:
                    print(f"   ❌ Error: {data['error']}")
            else:
                print(f"   ❌ HTTP Error: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    def demo_research_trends(self):
        """Demonstrate research trends analysis"""
        print("\n📈 DEMO: Research Trends Analysis")
        print("=" * 50)
        
        try:
            response = self.session.get(f"{self.base_url}/api/trends")
            if response.status_code == 200:
                data = response.json()
                if data['success']:
                    trends = data['data']
                    print(f"   ✅ Analyzed research trends")
                    print(f"   📊 Total publications: {trends['total_publications']}")
                    print(f"   📅 Year range: {trends['year_range'][0]} - {trends['year_range'][1]}")
                    print(f"   🏷️  Categories: {len(trends['categories'])}")
                    
                    print(f"\n   📋 Top research categories:")
                    sorted_categories = sorted(trends['categories'].items(), 
                                             key=lambda x: x[1], reverse=True)
                    for category, count in sorted_categories[:5]:
                        print(f"      • {category.title()}: {count} publications")
                else:
                    print(f"   ❌ Error: {data['error']}")
            else:
                print(f"   ❌ HTTP Error: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    def demo_knowledge_graph(self):
        """Demonstrate knowledge graph functionality"""
        print("\n🕸️ DEMO: Knowledge Graph")
        print("=" * 50)
        
        try:
            response = self.session.get(f"{self.base_url}/api/knowledge-graph")
            if response.status_code == 200:
                data = response.json()
                if data['success']:
                    graph_data = data['data']
                    nodes = graph_data['nodes']
                    edges = graph_data['edges']
                    
                    print(f"   ✅ Knowledge graph generated")
                    print(f"   🔗 Nodes: {len(nodes)}")
                    print(f"   🔗 Edges: {len(edges)}")
                    
                    # Show sample nodes
                    print(f"\n   📋 Sample nodes:")
                    for node in nodes[:5]:
                        if node['id'].startswith('pub_'):
                            print(f"      • Publication: {node['label']}")
                        else:
                            print(f"      • Category: {node['label']}")
                else:
                    print(f"   ❌ Error: {data['error']}")
            else:
                print(f"   ❌ HTTP Error: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    def demo_statistics(self):
        """Demonstrate statistics endpoint"""
        print("\n📊 DEMO: Application Statistics")
        print("=" * 50)
        
        try:
            response = self.session.get(f"{self.base_url}/api/stats")
            if response.status_code == 200:
                data = response.json()
                if data['success']:
                    stats = data['stats']
                    print(f"   ✅ Application statistics:")
                    print(f"   📚 Total publications: {stats['total_publications']}")
                    print(f"   🏷️  Categories: {stats['categories']}")
                    print(f"   📅 Years covered: {stats['years_covered']}")
                    print(f"   🕸️  Knowledge graph nodes: {stats['knowledge_graph_nodes']}")
                    print(f"   🔗 Knowledge graph edges: {stats['knowledge_graph_edges']}")
                else:
                    print(f"   ❌ Error: {data['error']}")
            else:
                print(f"   ❌ HTTP Error: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    def demo_publication_browsing(self):
        """Demonstrate publication browsing"""
        print("\n📚 DEMO: Publication Browsing")
        print("=" * 50)
        
        try:
            response = self.session.get(f"{self.base_url}/api/publications?limit=5")
            if response.status_code == 200:
                data = response.json()
                if data['success']:
                    publications = data['publications']
                    print(f"   ✅ Retrieved {len(publications)} publications")
                    
                    for i, pub in enumerate(publications, 1):
                        print(f"\n   📄 Publication {i}:")
                        print(f"      Title: {pub['title'][:60]}...")
                        print(f"      Category: {pub['category']}")
                        print(f"      Year: {pub['year']}")
                        print(f"      Tags: {', '.join(pub['tags'][:3])}")
                        print(f"      PMC ID: {pub['pmc_id']}")
                else:
                    print(f"   ❌ Error: {data['error']}")
            else:
                print(f"   ❌ HTTP Error: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    def run_full_demo(self):
        """Run the complete demo"""
        print("🚀 NASA Space Biology Knowledge Engine - Full Demo")
        print("=" * 60)
        print("This demo showcases the key features of the knowledge engine:")
        print("• AI-powered search and filtering")
        print("• Research trends analysis")
        print("• Knowledge graph visualization")
        print("• AI-generated insights")
        print("• Publication browsing and statistics")
        print("=" * 60)
        
        # Check if server is running
        try:
            response = self.session.get(f"{self.base_url}/api/stats")
            if response.status_code != 200:
                print("❌ Server is not running. Please start the server first:")
                print("   python app.py")
                return
        except requests.exceptions.ConnectionError:
            print("❌ Cannot connect to server. Please start the server first:")
            print("   python app.py")
            return
        
        # Run all demos
        self.demo_statistics()
        self.demo_publication_browsing()
        self.demo_search_functionality()
        self.demo_filtering()
        self.demo_research_trends()
        self.demo_ai_insights()
        self.demo_knowledge_graph()
        
        print("\n" + "=" * 60)
        print("🎉 Demo completed successfully!")
        print("🌐 Access the web interface at: http://localhost:5000")
        print("📡 API documentation available at: http://localhost:5000/api/")

def main():
    """Main demo function"""
    demo = SpaceBiologyDemo()
    demo.run_full_demo()

if __name__ == "__main__":
    main()
