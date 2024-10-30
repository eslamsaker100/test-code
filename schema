pip install requests beautifulsoup4
import streamlit as st
import requests
from bs4 import BeautifulSoup
import json

# Schema types to validate
SCHEMA_TYPES = ["Organization", "BreadcrumbList", "Article", "Product"]

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch URL: {e}")
        return None

def validate_schema(html):
    soup = BeautifulSoup(html, "html.parser")
    schemas = soup.find_all("script", type="application/ld+json")
    schema_results = []
    
    for schema in schemas:
        try:
            schema_json = json.loads(schema.string)
            schema_type = schema_json.get("@type", None)
            if schema_type in SCHEMA_TYPES:
                schema_results.append({"type": schema_type, "data": schema_json})
        except json.JSONDecodeError:
            st.warning("Invalid JSON in schema markup")
    
    return schema_results

# Streamlit App Interface
st.title("Schema Markup Validator")

# User inputs URL
url = st.text_input("Enter the URL to validate schema markup")

if st.button("Validate"):
    if url:
        html = fetch_html(url)
        if html:
            schema_results = validate_schema(html)
            
            if schema_results:
                st.success("Schema Markup Found!")
                for schema in schema_results:
                    st.write(f"**Type:** {schema['type']}")
                    st.json(schema["data"])
            else:
                st.warning("No matching schema markup found.")
    else:
        st.error("Please enter a valid URL.")
