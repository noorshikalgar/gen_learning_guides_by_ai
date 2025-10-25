"""
Enhanced workflow for Hugo-based learning guide generation
Updated for 2025 with proper cleanup and Hugo structure
"""

from typing import Literal
from langgraph.graph import StateGraph, END, START
from prompts import BEGINNER_PROMPT, ADVANCED_PROMPT, COMBINED_PROMPT
from tools import LearningGuideTools
from state import LearningGuideState
import logging

logger = logging.getLogger(__name__)
tools = LearningGuideTools()


def parse_query_node(state: LearningGuideState) -> LearningGuideState:
    """Parse user query and extract topic and level"""
    try:
        user_query = state["user_query"]

        topic = tools.parse_query_extract_topic(user_query)
        level = tools.prompt_selector_tool(user_query)

        logger.info(f"Parsed query - Topic: {topic}, Level: {level}")

        return {
            **state,
            "topic": topic,
            "level": level,
            "error_messages": [],
            "generation_status": "parsed",
        }
    except Exception as e:
        logger.error(f"Parse query error: {e}")
        return {
            **state,
            "error_messages": [f"Parse query error: {str(e)}"],
            "generation_status": "error",
        }


def select_prompt_node(state: LearningGuideState) -> LearningGuideState:
    """Select appropriate prompt based on level"""
    try:
        level = state["level"]

        prompt_mapping = {
            "beginner": BEGINNER_PROMPT,
            "advanced": ADVANCED_PROMPT,
            "complete": COMBINED_PROMPT,
        }

        selected_prompt = prompt_mapping.get(level, COMBINED_PROMPT)
        logger.info(f"Selected prompt for level: {level}")

        return {
            **state,
            "selected_prompt": selected_prompt,
            "generation_status": "prompt_selected",
        }
    except Exception as e:
        logger.error(f"Prompt selection error: {e}")
        return {
            **state,
            "error_messages": state.get("error_messages", [])
            + [f"Prompt selection error: {str(e)}"],
            "generation_status": "error",
        }


def generate_index_node(state: LearningGuideState) -> LearningGuideState:
    """Generate topics structure and create Hugo folder structure"""
    try:
        topic = state["topic"]
        level = state["level"]

        logger.info(f"Generating index for {topic}")

        # Create Hugo folder structure
        folder_structure = tools.create_folder_structure_tool(topic)
        base_dir = folder_structure["base_dir"]
        posts_dir = folder_structure["posts_dir"]

        # Generate topics structure (returns dict with chapters and file suggestions)
        topics_data = tools.generate_topics_structure(topic, level)
        topics_structure = topics_data["chapters"]
        suggested_index_name = topics_data.get("suggested_index_name", f"learn-{topic.lower().replace(' ', '-')}-guide.md")
        suggested_subfolder = topics_data.get("suggested_subfolder", f"{topic.lower().replace(' ', '-')}-chapters")

        # Create section directory and _index.md
        section_dir = tools.create_section_index_tool(
            base_dir, suggested_subfolder, topic
        )

        # Create index file in posts directory
        index_file_path = tools.create_index_file_tool(
            posts_dir, topic, topics_structure, suggested_index_name, suggested_subfolder
        )

        return {
            **state,
            "base_dir": base_dir,
            "posts_dir": posts_dir,
            "section_dir": section_dir,
            "folder_path": base_dir,  # For backward compatibility
            "topics_structure": topics_structure,
            "index_file_path": index_file_path,
            "suggested_subfolder": suggested_subfolder,
            "progress": {
                "completed_chapters": [],
                "total_chapters": len(topics_structure),
            },
            "current_chapter_index": 0,
            "generation_status": "index_created",
        }
    except Exception as e:
        logger.error(f"Index generation error: {e}")
        return {
            **state,
            "error_messages": state.get("error_messages", [])
            + [f"Index generation error: {str(e)}"],
            "generation_status": "error",
        }


def create_structure_node(state: LearningGuideState) -> LearningGuideState:
    """Create chapter files in section directory"""
    try:
        section_dir = state["section_dir"]
        topics_structure = state["topics_structure"]

        logger.info("Creating chapter file structure")
        chapter_files = tools.create_chapter_files_tool(section_dir, topics_structure)

        return {
            **state,
            "chapter_files": chapter_files,
            "generation_status": "structure_created",
        }
    except Exception as e:
        logger.error(f"Structure creation error: {e}")
        return {
            **state,
            "error_messages": state.get("error_messages", [])
            + [f"Structure creation error: {str(e)}"],
            "generation_status": "error",
        }


def generate_content_node(state: LearningGuideState) -> LearningGuideState:
    """Generate content for current chapter"""
    try:
        topics_structure = state["topics_structure"]
        current_index = state.get("current_chapter_index", 0)

        if current_index >= len(topics_structure):
            return {**state, "generation_status": "completed"}

        current_chapter = topics_structure[current_index]
        chapter_title = current_chapter["title"]

        logger.info(
            f"Generating content for chapter {current_index + 1}: {chapter_title}"
        )

        # Search for latest information if enabled
        search_context = ""
        search_results = []

        if hasattr(tools, "searxng_search_tool"):
            search_query = f"{state['topic']} {chapter_title} 2025 tutorial guide"
            search_results = tools.searxng_search_tool(search_query, max_results=5)

            if search_results:
                search_context = "Recent information from web search:\n"
                for result in search_results:
                    search_context += (
                        f"- {result['title']}: {result['snippet'][:200]}...\n"
                    )
                search_context += "\n"

        # Prepare prompt with subtopics
        subtopics_text = ""
        if current_chapter.get("subtopics"):
            subtopics_text = f"\nSpecific subtopics to cover:\n" + "\n".join(
                [f"- {subtopic}" for subtopic in current_chapter["subtopics"]]
            )

        return {
            **state,
            "current_chapter": chapter_title,
            "search_results": search_results,
            "search_context": search_context,
            "generation_status": f"generating_content_{current_index + 1}",
        }
    except Exception as e:
        logger.error(f"Content generation error: {e}")
        return {
            **state,
            "error_messages": state.get("error_messages", [])
            + [f"Content generation error: {str(e)}"],
            "generation_status": "error",
        }


def save_content_node(state: LearningGuideState) -> LearningGuideState:
    """Save generated content to file"""
    try:
        current_chapter = state.get("current_chapter")
        if not current_chapter:
            return state

        current_index = state.get("current_chapter_index", 0)
        chapter_files = state["chapter_files"]
        file_path = chapter_files[current_chapter]

        logger.info(f"Saving content for: {current_chapter}")

        # Get search context
        search_context = state.get("search_context", "")

        # Get chapter details
        topics_structure = state["topics_structure"]
        current_chapter_data = topics_structure[current_index]

        subtopics_text = ""
        if current_chapter_data.get("subtopics"):
            subtopics_text = f"\nSpecific subtopics to cover:\n" + "\n".join(
                [f"- {subtopic}" for subtopic in current_chapter_data["subtopics"]]
            )

        # Generate content
        selected_prompt = state["selected_prompt"]
        prompt = selected_prompt.format(
            topic=state["topic"],
            chapter=current_chapter + subtopics_text,
            search_context=search_context,
        )

        content = tools.generate_content_with_ollama(prompt)

        # Save content
        tools.save_chapter_content_tool(
            file_path, content, current_chapter, current_index
        )

        return {
            **state,
            "completed_chapters": state.get("completed_chapters", [])
            + [current_chapter],
            "generation_status": f"saved_content_{current_index + 1}",
        }
    except Exception as e:
        logger.error(f"Save content error: {e}")
        return {
            **state,
            "error_messages": state.get("error_messages", [])
            + [f"Save content error: {str(e)}"],
            "generation_status": "error",
        }


def update_progress_node(state: LearningGuideState) -> LearningGuideState:
    """Update progress and prepare for next chapter"""
    try:
        current_chapter = state.get("current_chapter")
        current_index = state.get("current_chapter_index", 0)

        # Update index file with progress
        if current_chapter:
            progress = state.get("progress", {})
            progress["completed_chapters"] = state.get("completed_chapters", [])

            tools.update_index_tool(state["index_file_path"], current_chapter, progress)

        return {
            **state,
            "current_chapter_index": current_index + 1,
            "progress": {
                "completed_chapters": state.get("completed_chapters", []),
                "total_chapters": len(state.get("topics_structure", [])),
            },
            "generation_status": f"updated_progress_{current_index + 1}",
        }
    except Exception as e:
        logger.error(f"Progress update error: {e}")
        return {
            **state,
            "error_messages": state.get("error_messages", [])
            + [f"Progress update error: {str(e)}"],
            "generation_status": "error",
        }


def cleanup_index_node(state: LearningGuideState) -> LearningGuideState:
    """Clean up progress section from index file after completion"""
    try:
        index_file_path = state.get("index_file_path")
        
        if index_file_path:
            logger.info("Cleaning up progress section from index file")
            result = tools.cleanup_index_progress_tool(index_file_path)
            logger.info(result)

        return {
            **state,
            "generation_status": "cleanup_completed",
        }
    except Exception as e:
        logger.error(f"Cleanup error: {e}")
        return {
            **state,
            "error_messages": state.get("error_messages", [])
            + [f"Cleanup error: {str(e)}"],
            "generation_status": "error",
        }


def should_continue(state: LearningGuideState) -> Literal["continue", "cleanup", "end"]:
    """Determine if we should continue generating chapters or move to cleanup"""
    try:
        # Check for errors
        if state.get("generation_status") == "error":
            logger.error("Stopping due to errors")
            return "end"

        current_index = state.get("current_chapter_index", 0)
        total_chapters = len(state.get("topics_structure", []))

        if current_index < total_chapters:
            logger.info(f"Continuing with chapter {current_index + 1}/{total_chapters}")
            return "continue"
        else:
            logger.info("All chapters completed! Moving to cleanup...")
            return "cleanup"
    except Exception as e:
        logger.error(f"Error in should_continue: {e}")
        return "end"


def create_learning_guide_workflow():
    """Create the main workflow with cleanup step"""
    workflow = StateGraph(LearningGuideState)

    # Add nodes
    workflow.add_node("parse_query", parse_query_node)
    workflow.add_node("select_prompt", select_prompt_node)
    workflow.add_node("generate_index", generate_index_node)
    workflow.add_node("create_structure", create_structure_node)
    workflow.add_node("generate_content", generate_content_node)
    workflow.add_node("save_content", save_content_node)
    workflow.add_node("update_progress", update_progress_node)
    workflow.add_node("cleanup_index", cleanup_index_node)

    # Define edges
    workflow.add_edge(START, "parse_query")
    workflow.add_edge("parse_query", "select_prompt")
    workflow.add_edge("select_prompt", "generate_index")
    workflow.add_edge("generate_index", "create_structure")
    workflow.add_edge("create_structure", "generate_content")
    workflow.add_edge("generate_content", "save_content")
    workflow.add_edge("save_content", "update_progress")

    # Conditional edge for looping or cleanup
    workflow.add_conditional_edges(
        "update_progress",
        should_continue,
        {
            "continue": "generate_content",
            "cleanup": "cleanup_index",
            "end": END,
        },
    )

    # After cleanup, end the workflow
    workflow.add_edge("cleanup_index", END)

    return workflow.compile()