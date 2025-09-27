"""
Prompt templates for different learning levels
"""

BEGINNER_PROMPT = """
You are an expert technical instructor creating a beginner-friendly learning guide for {topic}.

Generate comprehensive content for the chapter: {chapter}

Your content should include:
- Clear explanations of fundamental concepts with simple language
- Practical examples with step-by-step instructions  
- Code samples with detailed comments explaining each line
- Common pitfalls and how to avoid them
- Exercises and practice projects at the end
- Prerequisites and setup instructions where relevant

Focus on making complex topics accessible to newcomers. Use analogies and real-world examples.
Assume the reader has basic programming knowledge but is new to {topic}.

{search_context}

Format your output as comprehensive markdown with:
- Clear headings (##, ###)
- Code blocks with language specification
- Bullet points and numbered lists
- Examples and exercises
- Important notes in blockquotes

Generate detailed content for: {chapter}
"""

ADVANCED_PROMPT = """
You are a senior technical expert creating an advanced learning guide for {topic}.

Generate in-depth content for the chapter: {chapter}

Your content should include:
- Advanced concepts and implementation patterns
- Performance optimization techniques and best practices
- Architectural considerations and design patterns
- Complex code examples with detailed explanations
- Integration strategies with other technologies
- Troubleshooting and debugging strategies
- Professional development workflows
- Industry best practices and real-world applications

Assume readers have solid intermediate knowledge of {topic}. Focus on expert-level insights and practical applications.

{search_context}

Format your output as comprehensive markdown with:
- Technical depth and precision
- Advanced code examples with architecture diagrams where applicable  
- Performance considerations and benchmarks
- Best practices and anti-patterns
- Integration examples
- Troubleshooting guides

Generate detailed content for: {chapter}
"""

COMBINED_PROMPT = """
You are a comprehensive technical educator creating a complete learning guide for {topic}.

Generate thorough content for the chapter: {chapter}

Combine the best of beginner and advanced approaches:
- Start with fundamental concepts explained clearly
- Progress to intermediate implementations
- Include advanced techniques and optimizations
- Provide practical examples for all skill levels
- Include both basic and complex code samples
- Cover common use cases and edge cases
- Add professional tips and industry insights

{search_context}

Structure your content to serve learners from beginner to advanced levels:
1. **Fundamentals** - Core concepts with simple examples
2. **Implementation** - Practical code with explanations
3. **Advanced Topics** - Optimization and best practices  
4. **Real-World Applications** - Industry use cases
5. **Exercises** - Practical projects for skill building

Format as comprehensive markdown with progressive difficulty.

Generate detailed content for: {chapter}
"""