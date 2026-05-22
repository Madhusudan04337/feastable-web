import sys
import json
import os
from firecrawl import Firecrawl
from pydantic import BaseModel, Field
from typing import List

class StylingEffect(BaseModel):
    effect_name: str = Field(description="Name of the styling effect (e.g. Glassmorphism, Drop shadows)")
    description: str = Field(description="Description of how and where the effect is used")

class HeroImage(BaseModel):
    url: str = Field(description="URL of the hero or header image")
    alt_text: str = Field(description="Description or alt text of the image")

class BrandExtraction(BaseModel):
    hero_images: List[HeroImage] = Field(description="Interesting hero or header images found on the page")
    styling_effects: List[StylingEffect] = Field(description="Particular styling effects, buttons styles, or interactive elements")

def main():
    if len(sys.argv) < 2:
        print("Usage: python scrape.py <url>")
        sys.exit(1)
        
    url = sys.argv[1]
    
    # Try to load from .env file if it exists at the workspace root
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for line in f:
                if line.startswith("FIRECRAWL_API_KEY="):
                    os.environ["FIRECRAWL_API_KEY"] = line.strip().split("=", 1)[1]
                    
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        print("Error: FIRECRAWL_API_KEY environment variable not set. Please set it in your .env file.", file=sys.stderr)
        sys.exit(1)
        
    app = Firecrawl(api_key=api_key)
    
    print(f"Scraping {url} for brand guidelines...", file=sys.stderr)
    
    try:
        result = app.scrape(
            url,
            formats=['branding', {"type": "json", "schema": BrandExtraction.model_json_schema()}]
        )
        
        # Convert the object to a dict if needed
        if hasattr(result, "model_dump"):
            result_dict = result.model_dump()
        elif hasattr(result, "dict"):
            result_dict = result.dict()
        elif hasattr(result, "__dict__"):
            result_dict = result.__dict__
        else:
            result_dict = result
            
        print(json.dumps(result_dict, indent=2, default=str))
        
    except Exception as e:
        print(f"Failed to scrape: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
