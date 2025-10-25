"""
State management for Learning Guide Generator
Updated for Hugo structure support
"""

from typing import TypedDict, List, Dict, Any, Optional


class LearningGuideState(TypedDict, total=False):
    """State for learning guide generation workflow"""
    
    # User input
    user_query: str
    
    # Topic information
    topic: str
    level: str  # 'beginner', 'advanced', or 'complete'
    
    # Prompt selection
    selected_prompt: str
    
    # Hugo folder structure
    base_dir: str  # Base output directory with timestamp
    posts_dir: str  # content/posts/ directory for index file
    section_dir: str  # content/<subfolder>/ directory for chapters
    folder_path: str  # For backward compatibility (same as base_dir)
    suggested_subfolder: str  # Subfolder name from structure generation
    
    # File paths
    index_file_path: str
    
    # Content structure
    topics_structure: List[Dict[str, Any]]
    chapter_files: Dict[str, str]  # {chapter_title: file_path}
    
    # Generation progress
    current_chapter_index: int
    current_chapter: Optional[str]
    completed_chapters: List[str]
    progress: Dict[str, Any]
    
    # Search results
    search_results: List[Dict[str, Any]]
    search_context: str
    
    # Error handling
    error_messages: List[str]
    generation_status: str