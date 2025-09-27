# main.py
from workflow import create_learning_guide_workflow
from state import LearningGuideState
import logging
import sys
from datetime import datetime

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
    """Main function to run the learning guide generator"""
    
    start_time = datetime.now()
    logger.info("=" * 80)
    logger.info(f"🚀 Starting Learning Guide Generation")
    logger.info(f"📝 Query: {user_query}")
    logger.info(f"⏰ Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 80)
    
    try:
        # Create workflow
        app = create_learning_guide_workflow()
        
        # Initial state
        initial_state: LearningGuideState = {
            "user_query": user_query,
            "topic": "",
            "level": "",
            "selected_prompt": "",
            "folder_path": "",
            "index_file_path": "",
            "topics_structure": [],
            "chapter_files": {},
            "current_chapter_index": 0,
            "completed_chapters": [],
            "progress": {},
            "error_messages": [],
            "generation_status": "initialized"
        }
        
        # Run the workflow with progress tracking
        logger.info("🔄 Executing workflow...")
        final_state = app.invoke(initial_state)
        
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
        
        logger.info(f"📁 Generated in folder: {final_state.get('folder_path', 'Unknown')}")
        logger.info(f"📚 Topic: {final_state.get('topic', 'Unknown')}")
        logger.info(f"📖 Level: {final_state.get('level', 'Unknown')}")
        logger.info(f"✅ Completed chapters: {len(final_state.get('completed_chapters', []))}")
        logger.info(f"⏱️  Total duration: {duration}")
        logger.info(f"📊 Final status: {final_state.get('generation_status', 'Unknown')}")
        
        if final_state.get('folder_path'):
            logger.info(f"\n🎉 Your learning guide is ready!")
            logger.info(f"📂 Location: {final_state['folder_path']}")
            logger.info(f"📖 Start with: index.md")
            logger.info("=" * 80)
        
        return final_state
        
    except Exception as e:
        logger.error(f"❌ Critical error in workflow execution: {str(e)}")
        logger.exception("Full traceback:")
        return None

def main():
    """Interactive main function"""
    sample_queries = [
        "Generate a learning guide for Redis",
        "Create a complete guide for Docker from beginner to advanced", 
        "Generate an advanced learning guide for TypeScript",
        "Learning guide for Python web development with FastAPI",
        "Comprehensive Kubernetes tutorial from basics to production",
        "Complete React.js learning path with hooks and state management"
    ]
    
    print("🤖 Learning Guide PDF Generation Agent v2.0")
    print("=" * 60)
    print("\n📝 Sample queries you can try:")
    for i, query in enumerate(sample_queries, 1):
        print(f"   {i}. {query}")
    
    print(f"\n💡 Or enter your own query:")
    print("   Format: 'Generate a learning guide for [TOPIC]'")
    print("   Level keywords: beginner, advanced, complete, comprehensive")
    
    user_input = input("\n🔍 Query: ").strip()
    
    if not user_input:
        print("📋 Using sample query...")
        user_input = sample_queries[0]
        
    print(f"\n🎯 Processing: {user_input}")
    
    # Run the generator
    result = run_learning_guide_generator(user_input)
    
    if result:
        print("\n✨ Generation completed! Check the logs above for details.")
    else:
        print("\n💥 Generation failed! Check the error logs for details.")

if __name__ == "__main__":
    main()