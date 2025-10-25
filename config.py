"""
Configuration for Hugo-based Learning Guide Generator
Updated for 2025
"""

import os
from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Configuration(BaseModel):
    """Configuration settings for the learning guide generator"""
    
    # Ollama settings
    ollama_base_url: str = Field(
        default=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        description="Base URL for Ollama API"
    )
    mistral_model: str = Field(
        default=os.getenv("MISTRAL_MODEL", "mistral:latest"),
        description="Ollama model to use for content generation"
    )
    
    # Search settings
    searxng_url: str = Field(
        default=os.getenv("SEARXNG_URL", "http://localhost:8080"),
        description="Base URL for SearxNG search engine"
    )
    search_enabled: bool = Field(
        default=os.getenv("SEARCH_ENABLED", "true").lower() == "true",
        description="Enable web search for latest information"
    )
    max_search_results: int = Field(
        default=int(os.getenv("MAX_SEARCH_RESULTS", "5")),
        description="Maximum number of search results to fetch"
    )
    
    # Content generation settings
    content_max_tokens: int = Field(
        default=int(os.getenv("CONTENT_MAX_TOKENS", "32000")),
        description="Maximum tokens for content generation context"
    )
    max_retries: int = Field(
        default=int(os.getenv("MAX_RETRIES", "3")),
        description="Maximum retry attempts for failed operations"
    )
    timeout: int = Field(
        default=int(os.getenv("TIMEOUT", "3600")),
        description="Timeout in seconds for operations (1 hour default)"
    )
    
    # Output settings
    output_dir: str = Field(
        default=os.getenv("OUTPUT_DIR", str(Path.cwd() / "generated_guides")),
        description="Base directory for generated guides"
    )
    
    # Hugo-specific settings
    hugo_content_dir: str = Field(
        default="content",
        description="Hugo content directory name"
    )
    hugo_posts_dir: str = Field(
        default="posts",
        description="Hugo posts directory name (for index files)"
    )
    
    # Model configuration
    temperature: float = Field(
        default=float(os.getenv("TEMPERATURE", "0.7")),
        description="Temperature for content generation (0.0-1.0)"
    )
    top_p: float = Field(
        default=float(os.getenv("TOP_P", "0.9")),
        description="Top-p sampling parameter"
    )
    top_k: int = Field(
        default=int(os.getenv("TOP_K", "40")),
        description="Top-k sampling parameter"
    )
    repeat_penalty: float = Field(
        default=float(os.getenv("REPEAT_PENALTY", "1.1")),
        description="Repetition penalty"
    )
    
    class Config:
        """Pydantic config"""
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global configuration instance
config = Configuration()


# Helper function to validate configuration
def validate_config() -> bool:
    """Validate configuration settings"""
    import requests
    
    try:
        # Check Ollama connection
        response = requests.get(f"{config.ollama_base_url}/api/tags", timeout=5)
        if response.status_code != 200:
            print(f"⚠️  Warning: Cannot connect to Ollama at {config.ollama_base_url}")
            return False
        
        # Check if model exists
        models = response.json().get("models", [])
        model_names = [m.get("name") for m in models]
        if config.mistral_model not in model_names:
            print(f"⚠️  Warning: Model '{config.mistral_model}' not found in Ollama")
            print(f"   Available models: {', '.join(model_names)}")
            return False
        
        # Check output directory
        output_path = Path(config.output_dir)
        if not output_path.exists():
            output_path.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created output directory: {output_path}")
        
        # Check SearxNG if enabled
        if config.search_enabled:
            try:
                response = requests.get(f"{config.searxng_url}/search", 
                                       params={"q": "test", "format": "json"}, 
                                       timeout=5)
                if response.status_code != 200:
                    print(f"⚠️  Warning: Cannot connect to SearxNG at {config.searxng_url}")
                    print(f"   Search functionality will be disabled")
                    config.search_enabled = False
            except requests.exceptions.RequestException:
                print(f"⚠️  Warning: SearxNG not available. Search disabled.")
                config.search_enabled = False
        
        print("✅ Configuration validated successfully")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Configuration validation failed: {e}")
        return False


if __name__ == "__main__":
    # Test configuration
    print("Testing configuration...")
    print(f"Ollama URL: {config.ollama_base_url}")
    print(f"Model: {config.mistral_model}")
    print(f"Output Dir: {config.output_dir}")
    print(f"Search Enabled: {config.search_enabled}")
    validate_config()