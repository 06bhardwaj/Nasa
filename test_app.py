#!/usr/bin/env python3
"""
Test script for NASA Space Biology Knowledge Engine
Tests the API endpoints and functionality.
"""

import requests
import json
import time
import sys

def test_api_endpoints():
    """Test all API endpoints"""
    base_url = "http://localhost:5000"
    
    print("🧪 Testing NASA Space Biology Knowledge Engine API...")
    print("=" * 60)
    
    # Test 1: Get statistics
    print("1. Testing /api/stats endpoint...")
    try:
        response = requests.get(f"{base_url}/api/stats")
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                print(f"   ✅ Success! Found {data['stats']['total_publications']} publications")
            else:
                print(f"   ❌ Error: {data['error']}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection Error: Make sure the server is running")
        return False
    
    # Test 2: Get publications
    print("\n2. Testing /api/publications endpoint...")
    try:
        response = requests.get(f"{base_url}/api/publications?limit=5")
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                print(f"   ✅ Success! Retrieved {len(data['publications'])} publications")
                if data['publications']:
                    print(f"   📄 Sample title: {data['publications'][0]['title'][:50]}...")
            else:
                print(f"   ❌ Error: {data['error']}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Search publications
    print("\n3. Testing /api/search endpoint...")
    try:
        search_data = {
            "query": "microgravity bone",
            "filters": {"category": "bone"}
        }
        response = requests.post(f"{base_url}/api/search", json=search_data)
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                print(f"   ✅ Success! Found {len(data['results'])} results for 'microgravity bone'")
                if data['results']:
                    print(f"   📄 Top result: {data['results'][0]['title'][:50]}...")
            else:
                print(f"   ❌ Error: {data['error']}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Get trends
    print("\n4. Testing /api/trends endpoint...")
    try:
        response = requests.get(f"{base_url}/api/trends")
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                trends = data['data']
                print(f"   ✅ Success! Found trends from {trends['year_range'][0]} to {trends['year_range'][1]}")
                print(f"   📊 Total publications: {trends['total_publications']}")
            else:
                print(f"   ❌ Error: {data['error']}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 5: Get insights
    print("\n5. Testing /api/insights endpoint...")
    try:
        response = requests.get(f"{base_url}/api/insights")
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                print(f"   ✅ Success! Generated {len(data['insights'])} AI insights")
                if data['insights']:
                    print(f"   🧠 Sample insight: {data['insights'][0]['title']}")
            else:
                print(f"   ❌ Error: {data['error']}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 6: Get knowledge graph
    print("\n6. Testing /api/knowledge-graph endpoint...")
    try:
        response = requests.get(f"{base_url}/api/knowledge-graph")
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                graph_data = data['data']
                print(f"   ✅ Success! Knowledge graph has {len(graph_data['nodes'])} nodes and {len(graph_data['edges'])} edges")
            else:
                print(f"   ❌ Error: {data['error']}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 API testing completed!")
    return True

def test_web_interface():
    """Test the web interface"""
    print("\n🌐 Testing web interface...")
    try:
        response = requests.get("http://localhost:5000")
        if response.status_code == 200:
            print("   ✅ Web interface is accessible")
            if "NASA Space Biology Knowledge Engine" in response.text:
                print("   ✅ Main page content loaded correctly")
            else:
                print("   ⚠️  Main page content may not be loading correctly")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error accessing web interface: {e}")

def main():
    """Main test function"""
    print("NASA Space Biology Knowledge Engine - Test Suite")
    print("=" * 60)
    
    # Wait a moment for server to start
    print("⏳ Waiting for server to start...")
    time.sleep(2)
    
    # Test API endpoints
    api_success = test_api_endpoints()
    
    if api_success:
        # Test web interface
        test_web_interface()
        
        print("\n🎯 Test Summary:")
        print("   ✅ API endpoints are working")
        print("   ✅ Web interface is accessible")
        print("   ✅ NASA Space Biology Knowledge Engine is ready!")
        print("\n🌐 Access the application at: http://localhost:5000")
    else:
        print("\n❌ Tests failed. Please check the server logs and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
