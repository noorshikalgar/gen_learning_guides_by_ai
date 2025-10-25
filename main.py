"""
Main entry point for Hugo-based Learning Guide Generator
Updated for 2025 with Hugo content structure support
Version: 3.0
"""

from workflow import create_learning_guide_workflow
from state import LearningGuideState
from langchain_core.runnables.config import RunnableConfig
import logging
import sys
from datetime import datetime
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('learning_guide_generator.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def run_learning_guide_generator(user_query: str):
    """Main function to run the learning guide generator with proper recursion limit"""
    
    start_time = datetime.now()
    logger.info("=" * 80)
    logger.info(f"🚀 Starting Hugo Learning Guide Generation")
    logger.info(f"📝 Query: {user_query}")
    logger.info(f"⏰ Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 80)
    
    try:
        # Create workflow
        app = create_learning_guide_workflow()
        
        # Initial state with Hugo-specific fields
        initial_state: LearningGuideState = {
            "user_query": user_query,
            "topic": "",
            "level": "",
            "selected_prompt": "",
            "base_dir": "",
            "posts_dir": "",
            "section_dir": "",
            "folder_path": "",  # Backward compatibility
            "index_file_path": "",
            "suggested_subfolder": "",
            "topics_structure": [],
            "chapter_files": {},
            "current_chapter_index": 0,
            "current_chapter": None,
            "completed_chapters": [],
            "progress": {},
            "search_results": [],
            "search_context": "",
            "error_messages": [],
            "generation_status": "initialized"
        }
        
        # 🔧 Create RunnableConfig with increased recursion limit
        config = RunnableConfig(
            recursion_limit=150,  # Increased to handle cleanup step
            max_execution_time=3600,  # 1 hour timeout
            tags=["hugo_learning_guide_generator"],
        )
        
        logger.info(f"🔧 Using recursion limit: {config['recursion_limit']}")
        
        # Run the workflow with the config
        logger.info("🔄 Executing Hugo-compatible workflow...")
        final_state = app.invoke(initial_state, config)
        
        # Calculate duration
        end_time = datetime.now()
        duration = end_time - start_time
        
        # Print results
        logger.info("=" * 80)
        if final_state.get('error_messages'):
            logger.error("❌ Learning Guide Generation Completed with Errors!")
            for error in final_state['error_messages']:
                logger.error(f"   🔴 {error}")
        else:
            logger.info("✅ Learning Guide Generation Completed Successfully!")
            logger.info("🧹 Index file cleaned up (progress section removed)")
        
        # Display Hugo-specific paths
        base_dir = final_state.get('base_dir', 'Unknown')
        posts_dir = final_state.get('posts_dir', 'Unknown')
        section_dir = final_state.get('section_dir', 'Unknown')
        suggested_subfolder = final_state.get('suggested_subfolder', 'Unknown')
        
        logger.info(f"📁 Base directory: {base_dir}")
        logger.info(f"📄 Index location: {posts_dir}")
        logger.info(f"📂 Chapters location: {section_dir}")
        logger.info(f"🏷️  Subfolder name: {suggested_subfolder}")
        logger.info(f"📚 Topic: {final_state.get('topic', 'Unknown')}")
        logger.info(f"📖 Level: {final_state.get('level', 'Unknown')}")
        logger.info(f"✅ Completed chapters: {len(final_state.get('completed_chapters', []))}")
        logger.info(f"⏱️  Total duration: {duration}")
        logger.info(f"📊 Final status: {final_state.get('generation_status', 'Unknown')}")
        
        if base_dir != 'Unknown':
            logger.info("\n" + "=" * 80)
            logger.info("🎉 Your Hugo-compatible learning guide is ready!")
            logger.info("=" * 80)
            logger.info(f"\n📂 Hugo Content Structure:")
            logger.info(f"   {base_dir}/")
            logger.info(f"   ├── content/")
            logger.info(f"   │   ├── posts/")
            logger.info(f"   │   │   └── {Path(final_state.get('index_file_path', '')).name}")
            logger.info(f"   │   └── {suggested_subfolder}/")
            logger.info(f"   │       ├── _index.md")
            logger.info(f"   │       └── [chapter files].md")
            logger.info(f"\n📋 Next Steps:")
            logger.info(f"   1. Copy content/posts/*.md to your Hugo project's content/posts/")
            logger.info(f"   2. Copy content/{suggested_subfolder}/ to your Hugo project's content/")
            logger.info(f"   3. Run 'hugo server' to preview")
            logger.info(f"   4. Navigate to the index page to start learning!")
            logger.info("=" * 80)
        
        return final_state
        
    except Exception as e:
        logger.error(f"❌ Critical error in workflow execution: {str(e)}")
        logger.exception("Full traceback:")
        return None


def display_banner():
    """Display application banner"""
    banner = """
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║        🤖 Hugo Learning Guide Generator v3.0                        ║
║        Powered by AI • Hugo-Compatible • Hands-On Learning         ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
    print(banner)


def main():
    """Interactive main function with enhanced UX"""
    display_banner()
    
    sample_queries = [
        "Generate a learning guide for Redis",
        "Create a complete guide for Docker from beginner to advanced",
        "Generate an advanced learning guide for TypeScript",
        "Learning guide for Python web development with FastAPI",
        "Comprehensive Kubernetes tutorial from basics to production",
        "Complete React.js learning path with hooks and state management",
        "Learn PostgreSQL database administration",
        "Advanced Go programming patterns and best practices",
    ]
    
    print("\n📝 Sample queries you can try:")
    print("=" * 70)
    for i, query in enumerate(sample_queries, 1):
        print(f"   {i}. {query}")
    
    print("\n" + "=" * 70)
    print("💡 Or enter your own query:")
    print("   Format: 'Generate a learning guide for [TOPIC]'")
    print("   Level keywords: beginner, advanced, complete, comprehensive")
    print("=" * 70)
    
    user_input = input("\n🔍 Your Query: ").strip()
    
    if not user_input:
        print("\n📋 No input provided. Using default sample query...")
        user_input = sample_queries[0]
    
    # Confirmation
    print(f"\n🎯 Processing Query: '{user_input}'")
    confirm = input("   Proceed? (Y/n): ").strip().lower()
    
    if confirm and confirm != 'y':
        print("\n❌ Cancelled by user.")
        return
    
    print("\n" + "=" * 70)
    print("⏳ Starting generation process...")
    print("   This may take 10-30 minutes depending on topic complexity")
    print("=" * 70 + "\n")
    
    # Run the generator
    result = run_learning_guide_generator(user_input)
    
    if result and not result.get('error_messages'):
        print("\n✨ Generation completed successfully!")
        print("📖 Check the logs above for the exact file locations.")
        
        # Ask if user wants to generate another guide
        another = input("\n🔄 Generate another guide? (y/N): ").strip().lower()
        if another == 'y':
            print("\n" + "=" * 70 + "\n")
            main()  # Recursive call for another generation
    else:
        print("\n💥 Generation failed or completed with errors!")
        print("📋 Check 'learning_guide_generator.log' for detailed error information.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user. Exiting gracefully...")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unhandled exception in main: {e}")
        logger.exception("Full traceback:")
        sys.exit(1)