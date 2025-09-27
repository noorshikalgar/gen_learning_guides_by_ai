# state.py
from typing import TypedDict, List, Dict, Optional, Any
from typing_extensions import NotRequired

class LearningGuideState(TypedDict):
    user_query: str
    topic: str
    level: str  # 'beginner', 'advanced', 'complete'
    selected_prompt: str
    folder_path: str
    index_file_path: str
    topics_structure: List[Dict[str, Any]]
    chapter_files: Dict[str, str]
    current_chapter: NotRequired[Optional[str]]
    current_chapter_index: int
    completed_chapters: List[str]
    progress: Dict[str, Any]
    error_messages: List[str]
    search_results: NotRequired[List[Dict[str, Any]]]
    generation_status: NotRequired[str]