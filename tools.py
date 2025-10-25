"""
Enhanced tools for Hugo-based learning guide generation
Updated for 2025 best practices
"""

import os
import json
import requests
import ollama
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Optional
from config import config
import logging
from prompts import structure_prompt

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LearningGuideTools:
    def __init__(self):
        try:
            self.ollama_client = ollama.Client(host=config.ollama_base_url)
            # Test connection
            self.ollama_client.list()
            logger.info("Successfully connected to Ollama")
        except Exception as e:
            logger.error(f"Failed to connect to Ollama: {e}")
            raise

    def prompt_selector_tool(self, user_query: str) -> str:
        """Analyze user query and return appropriate prompt level"""
        query_lower = user_query.lower()

        beginner_keywords = [
            "beginner",
            "basics",
            "intro",
            "getting started",
            "basic",
            "simple",
            "learn",
            "tutorial",
        ]
        advanced_keywords = [
            "advanced",
            "expert",
            "professional",
            "deep dive",
            "complex",
            "production",
        ]
        complete_keywords = [
            "zero to advance",
            "complete",
            "comprehensive",
            "full",
            "end to end",
            "beginner to advanced",
        ]

        if any(term in query_lower for term in complete_keywords):
            return "complete"
        elif any(term in query_lower for term in advanced_keywords):
            return "advanced"
        elif any(term in query_lower for term in beginner_keywords):
            return "beginner"
        else:
            return "complete"  # Default

    def create_folder_structure_tool(self, topic: str) -> Dict[str, str]:
        """
        Create Hugo-compatible folder structure:
        - content/posts/<index_file>.md  (main index)
        - content/<subfolder>/<chapter_files>.md  (all chapters)
        - content/<subfolder>/_index.md  (section index)
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_topic = "".join(
                c for c in topic if c.isalnum() or c in (" ", "-", "_")
            ).rstrip()
            safe_topic = safe_topic.replace(" ", "_")[:50]

            # Create base output directory
            base_dir = Path(config.output_dir) / f"{safe_topic}_{timestamp}"
            base_dir.mkdir(parents=True, exist_ok=True)

            # Hugo structure:
            # content/posts/ - for index file
            # content/<subfolder>/ - for all chapters
            posts_dir = base_dir / "content" / "posts"
            posts_dir.mkdir(parents=True, exist_ok=True)

            # Subfolder will be determined from JSON response
            # We'll create it later when we know the name

            logger.info(f"Created Hugo folder structure: {base_dir}")
            
            return {
                "base_dir": str(base_dir),
                "posts_dir": str(posts_dir),
            }
        except Exception as e:
            logger.error(f"Error creating folder structure: {e}")
            raise

    def create_index_file_tool(
        self,
        posts_dir: str,
        topic: str,
        topics_list: List[Dict],
        index_filename: str,
        subfolder_name: str,
    ) -> str:
        """Create main index.md file with Hugo TOML front matter and TOC"""
        try:
            current_date = datetime.now().strftime("%Y-%m-%d")
            slug = self._create_slug(index_filename)

            # Create TOML front matter
            front_matter = f"""+++
title = "{topic} - Complete Learning Guide"
date = {current_date}
draft = false
description = "Comprehensive learning guide for {topic} from beginner to advanced. Hands-on, practical approach with exercises and projects."
slug = "{slug}"
keywords = ["{topic.lower()}", "tutorial", "learning guide", "hands-on", "practical", "beginner", "advanced"]
tags = ["{topic}", "Tutorial", "Learning Guide", "Programming"]
categories = ["Learning Guides", "{topic}"]
author = "AI Learning Guide Generator"
showReadingTime = true
showTableOfContents = true
showComments = false
toc = false
+++

# {topic} - Complete Learning Guide

Welcome to the comprehensive **{topic}** learning guide! This guide takes you from beginner concepts to advanced implementations with a **hands-on, learning-by-doing approach**.

## 📚 Table of Contents

"""

            # Add chapter links in Hugo format: /subfolder/chapter-slug/
            for i, topic_item in enumerate(topics_list, 1):
                chapter_title = topic_item["title"]
                chapter_slug = self._create_slug(chapter_title)
                
                # Hugo link format: /subfolder/chapter-slug/
                front_matter += f"{i}. [{chapter_title}](/{subfolder_name}/{chapter_slug}/)\n"
                
                # Add subtopics if they exist
                if "subtopics" in topic_item and topic_item["subtopics"]:
                    for subtopic in topic_item["subtopics"]:
                        front_matter += f"   - {subtopic}\n"
                    front_matter += "\n"

            front_matter += f"""
## 🎯 How to Use This Guide

1. **Start with the Index** - You're here! Overview of all topics
2. **Follow Sequential Order** - Each chapter builds upon previous ones
3. **Practice Along** - Every chapter includes hands-on examples and exercises
4. **Learn by Doing** - 70-80% practical exercises, 20-30% theory
5. **Take Your Time** - Understanding > Speed

## 🔥 What You'll Learn

By completing this guide, you'll have solid understanding of {topic} from fundamentals to advanced implementations, ready to apply in real-world projects.

## 📊 Course Stats

- **Total Chapters**: {len(topics_list)}
- **Estimated Time**: {len(topics_list) * 2} hours
- **Difficulty**: Progressive (🟢 Beginner → 🟡 Intermediate → 🔴 Advanced)
- **Hands-On Focus**: 70-80% practical exercises

---

**Generated**: {datetime.now().strftime("%Y-%m-%d")} | **Version**: 1.0
"""

            # Write to posts directory
            index_path = Path(posts_dir) / index_filename
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(front_matter)

            logger.info(f"Created index file: {index_path}")
            return str(index_path)
        except Exception as e:
            logger.error(f"Error creating index file: {e}")
            raise

    def create_section_index_tool(
        self, base_dir: str, subfolder_name: str, topic: str
    ) -> str:
        """Create _index.md for the chapter section"""
        try:
            # Create subfolder in content directory
            section_dir = Path(base_dir) / "content" / subfolder_name
            section_dir.mkdir(parents=True, exist_ok=True)

            current_date = datetime.now().strftime("%Y-%m-%d")
            
            front_matter = f"""+++
title = "{topic} Chapters"
date = {current_date}
draft = false
description = "All chapters for the {topic} learning guide"
toc = false
showTableOfContents = false
+++

# {topic} Learning Chapters

This section contains all the chapters for the {topic} learning guide. Navigate using the links below or from the main index.
"""

            section_index_path = section_dir / "_index.md"
            with open(section_index_path, "w", encoding="utf-8") as f:
                f.write(front_matter)

            logger.info(f"Created section _index.md: {section_index_path}")
            return str(section_dir)
        except Exception as e:
            logger.error(f"Error creating section index: {e}")
            raise

    def create_chapter_files_tool(
        self, section_dir: str, chapters: List[Dict]
    ) -> Dict[str, str]:
        """Create empty markdown files for each chapter with TOML front matter"""
        try:
            chapter_files = {}

            for i, chapter in enumerate(chapters, 1):
                chapter_title = chapter["title"]
                chapter_slug = self._create_slug(chapter_title)
                filename = f"{chapter_slug}.md"
                file_path = Path(section_dir) / filename

                current_date = datetime.now().strftime("%Y-%m-%d")

                # Extract description from subtopics if available
                description = chapter.get("subtopics", [chapter_title])[0] if chapter.get("subtopics") else chapter_title

                front_matter = f"""+++
title = "{chapter_title}"
date = {current_date}
draft = false
description = "{description}"
slug = "{chapter_slug}"
keywords = ["{chapter_title.lower()}", "tutorial", "hands-on", "practical"]
tags = ["Tutorial", "Learning", "Hands-On"]
categories = ["Learning Guides"]
author = "AI Learning Guide Generator"
showReadingTime = true
showTableOfContents = true
showComments = false
weight = {i}
+++

# {chapter_title}

*Content will be generated here...*
"""

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(front_matter)

                chapter_files[chapter_title] = str(file_path)

            logger.info(f"Created {len(chapter_files)} chapter files")
            return chapter_files
        except Exception as e:
            logger.error(f"Error creating chapter files: {e}")
            raise

    def save_chapter_content_tool(
        self, file_path: str, content: str, title: str, chapter_index: int = 1
    ) -> str:
        """Save generated content to chapter file with TOML front matter"""
        try:
            current_date = datetime.now().strftime("%Y-%m-%d")
            chapter_slug = self._create_slug(title)

            # Extract first line of content as description
            content_lines = content.strip().split("\n")
            description = content_lines[0][:150] if content_lines else title

            front_matter = f"""+++
title = "{title}"
date = {current_date}
draft = false
description = "{description}"
slug = "{chapter_slug}"
keywords = ["{title.lower()}", "tutorial", "hands-on"]
tags = ["Tutorial", "Learning", "Hands-On"]
categories = ["Learning Guides"]
author = "AI Learning Guide Generator"
showReadingTime = true
showTableOfContents = true
showComments = false
weight = {chapter_index}
+++

"""

            full_content = front_matter + content

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(full_content)

            logger.info(f"Saved content to {file_path}")
            return f"Successfully saved content to {file_path}"
        except Exception as e:
            logger.error(f"Error saving content: {e}")
            raise

    def cleanup_index_progress_tool(self, index_path: str) -> str:
        """Remove progress section from index file after completion"""
        try:
            with open(index_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Remove any progress sections
            # Look for patterns like "## ✅ Generation Progress" and remove until next ##
            import re
            
            # Pattern to match progress section
            progress_pattern = r'##\s*✅\s*Generation Progress.*?(?=##|$)'
            cleaned_content = re.sub(progress_pattern, '', content, flags=re.DOTALL)
            
            # Also remove "Latest Update" lines if any
            update_pattern = r'\*\*Latest Update:\*\*.*?\n'
            cleaned_content = re.sub(update_pattern, '', cleaned_content)
            
            # Remove extra blank lines (more than 2 consecutive)
            cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)

            with open(index_path, "w", encoding="utf-8") as f:
                f.write(cleaned_content)

            logger.info(f"Cleaned up progress section from {index_path}")
            return f"Successfully cleaned up {index_path}"
        except Exception as e:
            logger.error(f"Error cleaning up index: {e}")
            return f"Error cleaning up index: {str(e)}"

    def update_index_tool(
        self, index_path: str, completed_chapter: str, progress: Dict
    ) -> str:
        """Update index file with completion status (temporary progress tracking)"""
        try:
            with open(index_path, "r", encoding="utf-8") as f:
                content = f.read()

            completed_count = len(progress.get("completed_chapters", []))
            total_count = progress.get("total_chapters", 0)
            progress_percentage = (
                (completed_count / total_count * 100) if total_count > 0 else 0
            )

            # Add or update progress section
            progress_section = f"""

## ✅ Generation Progress

**Latest Update:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

**Progress:** {completed_count}/{total_count} chapters completed ({progress_percentage:.1f}%)

**Last Completed:** {completed_chapter}

**Status:** {'🎉 Complete!' if completed_count == total_count else '🔄 In Progress...'}

---

"""

            # Remove old progress section if exists
            import re
            progress_pattern = r'##\s*✅\s*Generation Progress.*?(?=##|$)'
            content = re.sub(progress_pattern, '', content, flags=re.DOTALL)

            # Add new progress before the last line
            if "**Generated**" in content:
                content = content.replace("**Generated**", progress_section + "**Generated**")
            else:
                content += progress_section

            with open(index_path, "w", encoding="utf-8") as f:
                f.write(content)

            logger.info(f"Updated index with progress for {completed_chapter}")
            return f"Updated index with progress for {completed_chapter}"
        except Exception as e:
            logger.error(f"Error updating index: {e}")
            return f"Error updating index: {str(e)}"

    def searxng_search_tool(
        self, query: str, max_results: int = 5
    ) -> List[Dict[str, Any]]:
        """Search using SearxNG for latest information"""
        if not config.search_enabled:
            logger.info("Search is disabled")
            return []

        try:
            params = {
                "q": query,
                "format": "json",
                "safesearch": 0,
                "pageno": 1,
                "engines": "google,duckduckgo,bing",
            }

            response = requests.get(
                f"{config.searxng_url}/search",
                params=params,
                timeout=10,
                headers={"User-Agent": "Learning-Guide-Generator/2.0"},
            )
            response.raise_for_status()

            results = response.json().get("results", [])

            formatted_results = []
            for result in results[:max_results]:
                formatted_results.append(
                    {
                        "title": result.get("title", ""),
                        "url": result.get("url", ""),
                        "snippet": result.get("content", result.get("snippet", "")),
                    }
                )

            logger.info(f"Found {len(formatted_results)} search results")
            return formatted_results

        except requests.exceptions.RequestException as e:
            logger.warning(f"Search request failed: {e}")
            return []
        except Exception as e:
            logger.error(f"Search error: {e}")
            return []

    def generate_content_with_ollama(self, prompt: str, model: str = None) -> str:
        """Generate content using Ollama with retries"""
        if model is None:
            model = config.mistral_model

        max_retries = 3
        for attempt in range(max_retries):
            try:
                logger.info(
                    f"Generating content with {model} (attempt {attempt + 1}/{max_retries})"
                )

                response = self.ollama_client.chat(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    options={
                        "temperature": 0.7,
                        "num_ctx": 32000,  # Increased for longer content
                        "repeat_penalty": 1.1,
                        "top_k": 40,
                        "top_p": 0.9,
                    },
                )

                content = response["message"]["content"]
                
                # Clean up any markdown wrapper if mistakenly added
                if content.strip().startswith("```markdown"):
                    content = content.replace("```markdown", "", 1)
                if content.strip().endswith("```"):
                    content = content.rsplit("```", 1)[0]
                
                logger.info(
                    f"Successfully generated {len(content)} characters of content"
                )
                return content.strip()

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    logger.error(f"All attempts failed. Last error: {e}")
                    return f"Error generating content: {str(e)}"

        return "Error: Failed to generate content after multiple attempts"

    def parse_query_extract_topic(self, user_query: str) -> str:
        """Extract topic from user query"""
        query_lower = user_query.lower()

        common_phrases = [
            "generate a learning guide for me topic:",
            "generate a learning guide for",
            "create a learning guide for",
            "learning guide for",
            "create a guide for",
            "guide for",
            "tutorial for",
            "learn about",
            "generate guide for",
            "create guide for",
            "make a guide for",
        ]

        topic = user_query.strip()
        for phrase in common_phrases:
            if phrase in query_lower:
                topic = user_query[query_lower.find(phrase) + len(phrase) :].strip()
                break

        # Clean and capitalize
        topic = " ".join(word.capitalize() for word in topic.split() if word.isalnum())

        return topic if topic else "General Programming"

    def generate_topics_structure(self, topic: str, level: str) -> Dict[str, Any]:
        """Generate topic structure with file naming suggestions"""
        structure_prompt_filled = structure_prompt.format(topic=topic, level=level)

        try:
            logger.info(f"Generating topic structure for {topic} at {level} level")
            response = self.generate_content_with_ollama(structure_prompt_filled)

            # Extract JSON
            json_start = response.find("[")
            json_end = response.rfind("]") + 1

            if json_start != -1 and json_end > json_start:
                json_str = response[json_start:json_end]
                structure = json.loads(json_str)
                
                # Extract file naming suggestions from first chapter
                suggested_index = structure[0].get("suggested_index_name", f"learn-{topic.lower().replace(' ', '-')}-guide.md")
                suggested_subfolder = structure[0].get("suggested_subfolder", f"{topic.lower().replace(' ', '-')}-chapters")
                
                logger.info(
                    f"Successfully generated structure with {len(structure)} chapters"
                )
                
                return {
                    "chapters": structure,
                    "suggested_index_name": suggested_index,
                    "suggested_subfolder": suggested_subfolder,
                }
            else:
                logger.warning("Could not parse JSON, using fallback")
                return self._get_fallback_structure(topic, level)

        except json.JSONDecodeError as e:
            logger.warning(f"JSON parsing error: {e}, using fallback")
            return self._get_fallback_structure(topic, level)
        except Exception as e:
            logger.error(f"Error generating structure: {e}")
            return self._get_fallback_structure(topic, level)

    def _get_fallback_structure(self, topic: str, level: str) -> Dict[str, Any]:
        """Enhanced fallback topic structure"""
        base_structure = [
            {
                "title": f"Introduction to {topic}",
                "subtopics": [
                    "Overview and History",
                    "Key Concepts",
                    "Benefits and Use Cases",
                    "Getting Started",
                ],
            },
            {
                "title": "Setting Up Your Environment",
                "subtopics": [
                    "Installation Guide",
                    "Configuration",
                    "Development Tools",
                    "First Setup",
                ],
            },
            {
                "title": "Fundamental Concepts",
                "subtopics": [
                    "Core Principles",
                    "Architecture Overview",
                    "Key Components",
                    "Basic Workflow",
                ],
            },
            {
                "title": "Hands-On Practice",
                "subtopics": [
                    "Basic Examples",
                    "Step-by-Step Tutorials",
                    "Common Patterns",
                    "Code Walkthrough",
                ],
            },
            {
                "title": "Intermediate Topics",
                "subtopics": [
                    "Advanced Features",
                    "Best Practices",
                    "Optimization Techniques",
                    "Error Handling",
                ],
            },
            {
                "title": "Real-World Applications",
                "subtopics": [
                    "Project Planning",
                    "Implementation Strategies",
                    "Case Studies",
                    "Production Considerations",
                ],
            },
        ]

        if level == "advanced":
            base_structure.extend(
                [
                    {
                        "title": "Advanced Techniques",
                        "subtopics": [
                            "Performance Optimization",
                            "Scaling Strategies",
                            "Advanced Patterns",
                            "Expert Tips",
                        ],
                    },
                    {
                        "title": "Production Deployment",
                        "subtopics": [
                            "Deployment Strategies",
                            "Monitoring",
                            "Maintenance",
                            "Troubleshooting",
                        ],
                    },
                ]
            )

        return {
            "chapters": base_structure,
            "suggested_index_name": f"learn-{topic.lower().replace(' ', '-')}-guide.md",
            "suggested_subfolder": f"{topic.lower().replace(' ', '-')}-chapters",
        }

    def _create_slug(self, text: str) -> str:
        """Create URL-safe slug from text"""
        slug = text.lower()
        slug = slug.replace(" ", "-")
        slug = "".join(c for c in slug if c.isalnum() or c == "-")
        slug = slug.strip("-")
        return slug[:100]  # Limit length