"""
Prompt templates for different learning levels
"""

BEGINNER_PROMPT = """
	You are an expert technical writer and educator creating a comprehensive, beginner-friendly textbook-style document about {topic}.
	
	Generate comprehensive content for the chapter: {chapter}
	
	Your document should be structured to guide a complete novice from foundational concepts to advanced topics, enabling them to learn and apply the technology effectively.
	
	Your content must include the following sections and adhere to these guidelines:
	
	**Overall Guidelines:**
	- **Target Audience:** Absolute beginners with no prior knowledge of {topic}
	- **Clarity and Simplicity:** Explain complex concepts in simple, easy-to-understand language. Avoid jargon where possible, or explain it clearly when used.
	- **Logical Progression:** Arrange topics in a logical, step-by-step manner, building upon previously learned concepts.
	- **Markdown Format:** Use proper Markdown formatting for headings, subheadings, code blocks, lists, and emphasis.
	
	**Document Structure and Content:**
	
	**1. Introduction to {topic}**
	- What is {topic}?
	- Why learn {topic}? (Benefits, use cases, industry relevance)
	- A brief history (optional, keep it concise)
	- Setting up your development environment (step-by-step instructions with clear prerequisites).
	
	**2. Core Concepts and Fundamentals**
	- Break down the technology into its fundamental building blocks.
	- For each core concept:
	  - **Detailed Explanation:** Provide thorough explanations.
	  - **Code Examples:** Include practical, well-commented code examples that illustrate the concept. Examples should be concise but demonstrate the concept effectively.
	  - **Exercises/Mini-Challenges:** Include small, focused exercises or mini-challenges after each major concept or group of related concepts. These should reinforce understanding. Provide clear instructions for what to achieve. (Solutions can be omitted or hinted at).
	
	**3. Intermediate Topics**
	- Cover more advanced aspects, building on the fundamentals.
	- Maintain the same structure as "Core Concepts": detailed explanations, code examples, and exercises/challenges.
	
	**4. Advanced Topics and Best Practices**
	- Delve into more complex or specialized areas.
	- Include best practices, common pitfalls, and advanced techniques relevant to the technology.
	- Provide real-world context where applicable.
	
	**5. Guided Projects**
	- **At least two (2) guided, step-by-step projects.**
	- Each project should:
	  - Have a clear objective and problem statement.
	  - Break down the project into manageable steps.
	  - Provide code snippets and explanations for each step.
	  - Encourage independent problem-solving at certain points (e.g., "Now, try to implement X on your own before looking at the next step").
	  - Showcase the application of concepts learned in earlier sections.
	
	**6. Bonus Section: Further Learning and Resources**
	- **Recommended Online Courses/Tutorials:** List reputable online courses or platforms.
	- **Official Documentation:** Provide links to official documentation.
	- **Blogs and Articles:** Suggest popular and influential blogs/websites.
	- **YouTube Channels:** Recommend high-quality YouTube channels for learning.
	- **Community Forums/Groups:** Point to relevant communities (e.g., Stack Overflow, Discord servers).
	- **Next Steps/Advanced Topics:** Suggest what to learn after mastering the content in this document.
	
	{search_context}
	
	Generate detailed content for: {chapter}
	
	Prioritize clarity, practical examples, and actionable exercises/projects. Ensure code examples are accurate and runnable (if applicable to the technology). Maintain a friendly, encouraging, and authoritative tone.
	"""

ADVANCED_PROMPT = """
	You are an expert technical writer and educator creating a comprehensive, advanced-level textbook-style document about {topic}.
	
	Generate in-depth content for the chapter: {chapter}
	
	Your document should be structured to guide an experienced professional from intermediate knowledge to mastering advanced topics, enabling them to apply the technology effectively in complex scenarios.
	
	Your content must include the following sections and adhere to these guidelines:
	
	**Overall Guidelines:**
	- **Target Audience:** Experienced developers and professionals with intermediate knowledge of {topic}. This document is _not_ for beginners.
	- **Depth and Nuance:** Explain complex concepts with depth and precision, assuming prior understanding of foundational and intermediate topics.
	- **Logical Progression:** Arrange topics in a logical, step-by-step manner, building upon advanced concepts.
	- **Markdown Format:** Use proper Markdown formatting for headings, subheadings, code blocks, lists, and emphasis.
	
	**Document Structure and Content:**
	
	**1. Introduction to Advanced {topic}**
	- Recap of core and intermediate concepts (briefly, assuming prior knowledge).
	- Why delve deeper into {topic}? (Complex problem-solving, performance gains, scalability, specific industry demands).
	- Key challenges and common pitfalls at an advanced level.
	
	**2. Deep Dive into Advanced Concepts**
	- Break down the technology into its complex, often nuanced, advanced building blocks.
	- For each advanced concept:
	  - **Detailed Explanation:** Provide thorough, in-depth explanations, including underlying mechanisms, theoretical considerations, and trade-offs.
	  - **Advanced Code Examples:** Include practical, highly optimized, and well-commented code examples demonstrating the concept's implementation in real-world, complex scenarios. Examples should highlight best practices, performance considerations, and error handling.
	  - **Performance Implications:** Discuss the performance characteristics and potential bottlenecks associated with the concept.
	  - **Design Patterns/Architectural Considerations:** Relate the concept to relevant design patterns or architectural choices.
	
	**3. Performance Optimization and Scalability**
	- Techniques for optimizing {topic} applications.
	- Scalability strategies and patterns (e.g., horizontal scaling, load balancing, caching).
	- Profiling and debugging advanced issues.
	- Benchmarking and performance testing.
	
	**4. Security, Resilience, and Reliability**
	- Advanced security considerations specific to {topic}.
	- Designing for fault tolerance and resilience.
	- Error handling strategies for production systems.
	- Monitoring and logging advanced applications.
	
	**5. Interoperability and Ecosystem Integration**
	- Integrating {topic} with other complex systems and technologies.
	- Advanced interoperability patterns and protocols.
	- Leveraging specialized libraries or frameworks within the {topic} ecosystem for advanced use cases.
	
	**6. Case Studies and Real-World Applications**
	- **At least two (2) detailed case studies** of complex, real-world applications of {topic}.
	- Each case study should:
	  - Present a challenging problem statement.
	  - Describe the architectural design and why specific advanced concepts were chosen.
	  - Showcase relevant code snippets demonstrating the implementation.
	  - Discuss the challenges faced and solutions implemented.
	  - Analyze the impact and lessons learned.
	
	**7. Future Trends and Research Directions**
	- Emerging trends and ongoing developments in {topic}.
	- Research areas and potential future advancements.
	- How to stay current with the rapidly evolving landscape of {topic}.
	
	**8. Advanced Resources and Community**
	- **Recommended Advanced Courses/Workshops:** List highly specialized or advanced learning opportunities.
	- **Research Papers/Academic Resources:** Provide links to relevant academic papers or in-depth research.
	- **Expert Blogs and Publications:** Suggest influential blogs, newsletters, or online publications from industry leaders.
	- **Conferences and Meetups:** Point to significant conferences or specialized meetups.
	- **Core Contributor Communities:** Guide users to highly technical forums or communities where core development discussions occur.
	- **Next Steps/Specialization:** Suggest areas of extreme specialization within {topic} for further mastery.
	
	{search_context}
	
	Generate detailed content for: {chapter}
	
	Prioritize depth, complex examples, and actionable insights for experienced professionals. Ensure code examples are accurate, robust, and demonstrate advanced concepts effectively. Maintain a highly technical, authoritative, and insightful tone.
	"""

COMBINED_PROMPT = """
	You are an expert technical writer and educator creating a comprehensive, multi-level textbook-style document about {topic}.
	
	Generate thorough content for the chapter: {chapter}
	
	Your document should be structured to serve learners from beginner to advanced levels, providing a progressive learning pathway that adapts to different skill levels while maintaining coherence and depth.
	
	Your content must include the following sections and adhere to these guidelines:
	
	**Overall Guidelines:**
	- **Target Audience:** Multi-level learners from absolute beginners to experienced professionals
	- **Progressive Complexity:** Start with fundamental concepts and gradually increase complexity, clearly marking skill level transitions
	- **Adaptive Content:** Provide multiple pathways through the material with clear signposting for different skill levels
	- **Comprehensive Coverage:** Balance breadth and depth to serve all skill levels effectively
	- **Markdown Format:** Use proper Markdown formatting for headings, subheadings, code blocks, lists, and emphasis.
	
	**Document Structure and Content:**
	
	**1. Getting Started with {topic}**
	- **For Beginners:** What is {topic}? Why learn it? Basic concepts and terminology
	- **For Experienced Users:** Quick overview, what's new, and how this differs from similar technologies
	- **Universal:** Setting up development environment with options for different platforms
	- **Learning Paths:** Clear guidance on which sections to focus on based on current skill level
	
	**2. Foundational Concepts and Core Principles**
	- **Beginner Track:** Step-by-step introduction to core concepts with simple examples
	- **Intermediate Track:** Deeper dive into underlying principles and mechanisms  
	- **Advanced Track:** Theoretical foundations, design philosophy, and architectural considerations
	- **Hands-On Practice:** Graduated exercises from simple to complex
	- **Common Pitfalls:** What to avoid at each skill level
	
	**3. Practical Implementation and Development**
	- **Basic Implementation:** Getting started with simple, working examples
	- **Intermediate Patterns:** Common use cases, best practices, and design patterns
	- **Advanced Techniques:** Optimization strategies, complex scenarios, and expert-level implementations
	- **Code Examples:** Progressive complexity from basic syntax to production-ready code
	- **Debugging and Troubleshooting:** Level-appropriate debugging strategies
	
	**4. Real-World Applications and Use Cases**
	- **Beginner Projects:** 2-3 simple, guided projects with step-by-step instructions
	- **Intermediate Projects:** 2-3 moderate complexity projects with guided discovery
	- **Advanced Case Studies:** 2-3 complex, real-world scenarios with architectural analysis
	- **Industry Applications:** How {topic} is used across different industries and scales
	- **Portfolio Building:** Guidance for creating impressive projects at each level
	
	**5. Performance, Scalability, and Production Readiness**
	- **Basic Performance:** Understanding performance implications for beginners
	- **Optimization Techniques:** Intermediate-level performance improvements
	- **Advanced Scalability:** Enterprise-level considerations, monitoring, and optimization
	- **Security Considerations:** Security practices appropriate to each skill level
	- **Deployment and DevOps:** From simple deployment to complex CI/CD pipelines
	
	**6. Ecosystem and Advanced Topics**
	- **Tool Ecosystem:** Essential tools, libraries, and frameworks for each level
	- **Integration Patterns:** How to integrate {topic} with other technologies
	- **Advanced Specializations:** Deep dives into specialized areas and cutting-edge features
	- **Research and Future Directions:** Emerging trends and ongoing developments
	- **Community and Contribution:** How to engage with the community at different levels
	
	**7. Comprehensive Learning Resources**
	- **Beginner Resources:** Tutorials, courses, and guided learning paths
	- **Intermediate Resources:** Books, documentation, and practical guides
	- **Advanced Resources:** Research papers, expert blogs, conference talks, and specialized courses
	- **Community Resources:** Forums, Discord servers, meetups, and contribution opportunities
	- **Certification and Career Paths:** Professional development opportunities
	- **Next Steps:** Personalized recommendations based on interests and career goals
	
	{search_context}
	
	**Special Instructions for Multi-Level Content:**
	
	1. **Clear Level Indicators:** Use consistent formatting to indicate content difficulty (🟢 Beginner, 🟡 Intermediate, 🔴 Advanced)
	
	2. **Progressive Examples:** Start each concept with a simple example, then build complexity:

🟢 Basic Example: [Simple implementation]

🟡 Enhanced Example: [Added complexity/features]

🔴 Production Example: [Full-featured, optimized implementation]


	3. **Flexible Reading Paths:** Provide clear navigation guidance:
	- "New to {topic}? Start here and follow the 🟢 path"
	- "Have some experience? Jump to section X and focus on 🟡 content"
	- "Looking for advanced techniques? Focus on 🔴 sections"
	
	4. **Cross-References:** Link related concepts across skill levels
	
	5. **Practical Checkpoints:** Include self-assessment points to help readers gauge their progress
	
	Generate detailed content for: {chapter}
	
	Create content that serves as both a beginner's guide and an advanced reference, with clear pathways for different learning objectives. Ensure smooth transitions between skill levels while maintaining the depth needed for each audience.
	"""

# structure_prompt = """
# 	You are an expert curriculum designer and hands-on learning specialist, utilizing the latest 2025 research-backed methodologies for experiential education and practical skill development.

# 	Generate a comprehensive, practice-focused learning structure for "{topic}" at {level} level based on modern "learning-by-doing" educational approaches including:
# 	- **Code-First Learning**: Prioritizing hands-on coding over theoretical explanations
# 	- **Experiential Learning Cycles**: Learn → Practice → Reflect → Apply methodology
# 	- **Active Construction**: Building real projects and solutions from day one
# 	- **Microlearning with Immediate Application**: Small concepts with instant practical application
# 	- **Problem-Based Learning**: Real scenarios requiring hands-on problem solving
# 	- **Discovery Through Practice**: Learning concepts by implementing them first

# 	Create a JSON array of 6-8 strategically designed chapters with maximum practical emphasis, where each chapter includes:
# 	- title: Action-oriented chapter name emphasizing practical outcomes
# 	- subtopics: 4-6 hands-on activities, coding exercises, and practical implementations
# 	- practical_focus: Specific hands-on activities, commands, code examples, and projects
# 	- learning_outcomes: Skills students will demonstrate through practice
# 	- hands_on_ratio: Percentage of practical vs theoretical content (aim for 70-80% practical)

# 	**Enhanced Practical Requirements:**

# 	**If level = "beginner":**
# 	- **Maximum Hands-On Approach**: Start coding/doing within first 15 minutes
# 	- **Follow-Along Examples**: Step-by-step coding tutorials with copy-paste ready commands
# 	- **Immediate Gratification**: Quick wins and visible results in each lesson
# 	- **Building Blocks**: Each practical exercise builds on the previous one
# 	- **Error-Driven Learning**: Common mistakes and how to fix them through practice
# 	- **Mini-Projects**: Small, completable projects in every chapter

# 	**If level = "advanced":**  
# 	- **Production-Ready Practice**: Real-world scenarios and enterprise-level implementations
# 	- **Performance Labs**: Hands-on optimization and benchmarking exercises
# 	- **Architecture Workshops**: Build and deploy complex systems
# 	- **Debugging Challenges**: Real-world problem-solving exercises
# 	- **Code Review Sessions**: Analyzing and improving existing codebases
# 	- **Industry Simulations**: Replicate real workplace scenarios and challenges

# 	**If level = "combined":**
# 	- **Progressive Difficulty Labs**: 🟢 Simple exercises → 🟡 Intermediate projects → 🔴 Advanced implementations
# 	- **Multi-Track Practicals**: Different complexity levels for same concepts
# 	- **Choose-Your-Own-Adventure**: Multiple practical paths based on skill level
# 	- **Peer Programming**: Collaborative coding exercises across skill levels
# 	- **Real-World Case Studies**: Practical implementations at different complexity levels

# 	**Mandatory Practical Elements for Each Chapter:**
# 	1. **Immediate Action Items**: What to code/build/implement in first 10 minutes
# 	2. **Command Reference**: Copy-paste ready commands, code snippets, and configurations
# 	3. **Hands-On Exercises**: At least 3-5 practical exercises per chapter
# 	4. **Build-Along Projects**: Step-by-step guided implementations
# 	5. **Challenge Exercises**: Independent practice to reinforce learning
# 	6. **Real-World Applications**: How the concepts apply in actual work scenarios
# 	7. **Troubleshooting Labs**: Common problems and hands-on debugging
# 	8. **Quick Reference**: Practical cheat sheets and command references

# 	**Content Distribution Target:**
# 	- 70-80% Hands-on practice, coding, building, implementing
# 	- 20-30% Essential theory and explanations
# 	- Every theoretical concept must be immediately followed by practical application
# 	- No more than 5 minutes of theory without hands-on practice

# 	Topic: {topic}
# 	Level: {level}

# 	Return ONLY valid JSON in this exact format:
# 	[
# 	{{
# 		"title": "Hands-On {topic} Fundamentals: Build Your First Working Solution",
# 		"subtopics": [
# 		"Quick Setup and First Running Example", 
# 		"Essential Commands and Immediate Practice", 
# 		"Build Your First Mini-Project Step-by-Step", 
# 		"Common Issues and Hands-On Troubleshooting",
# 		"Extend and Customize Your Implementation"
# 		],
# 		"practical_focus": [
# 		"15-minute setup with working example",
# 		"10 essential commands with copy-paste examples", 
# 		"Build a functional mini-project from scratch",
# 		"Debug 5 common beginner errors hands-on",
# 		"Customize and enhance the basic implementation"
# 		],
# 		"learning_outcomes": [
# 		"Create and run a working {topic} solution",
# 		"Execute essential commands confidently", 
# 		"Debug common issues independently",
# 		"Customize basic implementations"
# 		],
# 		"hands_on_ratio": "75% practical, 25% essential theory"
# 	}},
# 	{{
# 		"title": "Core Implementation Workshop: Build Real-World Solutions",
# 		"subtopics": [
# 		"Advanced Implementation Patterns with Live Coding",
# 		"Performance Testing and Optimization Lab", 
# 		"Integration Workshop with External Systems",
# 		"Error Handling and Recovery Implementation",
# 		"Production-Ready Code Development"
# 		],
# 		"practical_focus": [
# 		"Code 3 different implementation patterns",
# 		"Benchmark and optimize performance hands-on",
# 		"Connect to real APIs and databases",
# 		"Implement comprehensive error handling",
# 		"Deploy to production environment"
# 		],
# 		"learning_outcomes": [
# 		"Implement advanced {topic} patterns",
# 		"Optimize for production performance",
# 		"Integrate with real-world systems",
# 		"Handle errors gracefully in practice"
# 		],
# 		"hands_on_ratio": "80% practical, 20% essential theory"
# 	}}
# 	]

# 	Generate 6-8 chapters total following this hands-on structure. Prioritize practical application over theoretical knowledge. Every subtopic should involve actual doing, building, coding, or implementing. Respond with ONLY the JSON array, no explanations or additional text.
# 	"""

structure_prompt = """
You are an expert curriculum designer and hands-on learning specialist, utilizing the latest 2025 research-backed methodologies for experiential education and practical skill development.

Generate a comprehensive, practice-focused learning structure for "{topic}" at {level} level based on modern "learning-by-doing" educational approaches including:
- **Code-First Learning**: Prioritizing hands-on coding over theoretical explanations
- **Experiential Learning Cycles**: Learn → Practice → Reflect → Apply methodology
- **Active Construction**: Building real projects and solutions from day one
- **Microlearning with Immediate Application**: Small concepts with instant practical application
- **Problem-Based Learning**: Real scenarios requiring hands-on problem solving
- **Discovery Through Practice**: Learning concepts by implementing them first

Create a JSON array of 6-8 strategically designed chapters with maximum practical emphasis, where each chapter includes:
- title: Action-oriented chapter name emphasizing practical outcomes
- subtopics: 4-6 hands-on activities, coding exercises, and practical implementations
- practical_focus: Specific hands-on activities, commands, code examples, and projects
- learning_outcomes: Skills students will demonstrate through practice
- hands_on_ratio: Percentage of practical vs theoretical content (aim for 70-80% practical)

**Chapter Structure Alignment:**

**If level = "beginner":**
Follow this chapter progression to match beginner learning needs:
1. **Introduction to {topic}** - What is it, why learn it, setup environment
2. **Core Concepts and Fundamentals** - Building blocks with hands-on practice
3. **Intermediate Topics** - More advanced aspects with practical exercises
4. **Advanced Topics and Best Practices** - Complex areas with real-world context
5. **Guided Projects** - Step-by-step practical implementations
6. **Further Learning and Resources** - Next steps and community resources

**Maximum Hands-On Approach**: Start coding/doing within first 15 minutes
- **Follow-Along Examples**: Step-by-step coding tutorials with copy-paste ready commands
- **Immediate Gratification**: Quick wins and visible results in each lesson
- **Building Blocks**: Each practical exercise builds on the previous one
- **Error-Driven Learning**: Common mistakes and how to fix them through practice
- **Mini-Projects**: Small, completable projects in every chapter

**If level = "advanced":**
Follow this chapter progression for experienced professionals:
1. **Introduction to Advanced {topic}** - Recap and advanced challenges
2. **Deep Dive into Advanced Concepts** - Complex building blocks and mechanisms
3. **Performance Optimization and Scalability** - Optimization techniques and patterns
4. **Security, Resilience, and Reliability** - Production-level considerations
5. **Interoperability and Ecosystem Integration** - Complex system integration
6. **Case Studies and Real-World Applications** - Complex scenario analysis
7. **Future Trends and Research Directions** - Emerging developments
8. **Advanced Resources and Community** - Expert-level resources

**Production-Ready Practice**: Real-world scenarios and enterprise-level implementations
- **Performance Labs**: Hands-on optimization and benchmarking exercises
- **Architecture Workshops**: Build and deploy complex systems
- **Debugging Challenges**: Real-world problem-solving exercises
- **Code Review Sessions**: Analyzing and improving existing codebases
- **Industry Simulations**: Replicate real workplace scenarios and challenges

**If level = "combined":**
Follow this multi-level chapter progression:
1. **Getting Started with {topic}** - Multi-level introduction and setup
2. **Foundational Concepts and Core Principles** - Progressive complexity tracks
3. **Practical Implementation and Development** - Graduated implementation patterns
4. **Real-World Applications and Use Cases** - Projects from simple to complex
5. **Performance, Scalability, and Production Readiness** - Multi-level considerations
6. **Ecosystem and Advanced Topics** - Comprehensive ecosystem coverage
7. **Comprehensive Learning Resources** - Resources for all skill levels

**Progressive Difficulty Labs**: 🟢 Simple exercises → 🟡 Intermediate projects → 🔴 Advanced implementations
- **Multi-Track Practicals**: Different complexity levels for same concepts
- **Choose-Your-Own-Adventure**: Multiple practical paths based on skill level
- **Peer Programming**: Collaborative coding exercises across skill levels
- **Real-World Case Studies**: Practical implementations at different complexity levels

**Mandatory Practical Elements for Each Chapter:**
1. **Immediate Action Items**: What to code/build/implement in first 10 minutes
2. **Command Reference**: Copy-paste ready commands, code snippets, and configurations
3. **Hands-On Exercises**: At least 3-5 practical exercises per chapter
4. **Build-Along Projects**: Step-by-step guided implementations
5. **Challenge Exercises**: Independent practice to reinforce learning
6. **Real-World Applications**: How the concepts apply in actual work scenarios
7. **Troubleshooting Labs**: Common problems and hands-on debugging
8. **Quick Reference**: Practical cheat sheets and command references

**Content Distribution Target:**
- 70-80% Hands-on practice, coding, building, implementing
- 20-30% Essential theory and explanations
- Every theoretical concept must be immediately followed by practical application
- No more than 5 minutes of theory without hands-on practice

**File Organization Requirements:**
Please suggest:
- **Index File Name**: A descriptive name for the main index.md file based on the topic
- **Content Subfolder Name**: A clean subfolder name where all chapter files and subtopic files will be organized (everything except the main index file)

Topic: {topic}
Level: {level}

Return ONLY valid JSON in this exact format:
[
{{
    "title": "Getting Started with {topic}: Foundation and Setup",
    "subtopics": [
    "Quick Setup and First Running Example", 
    "Essential Commands and Immediate Practice", 
    "Build Your First Mini-Project Step-by-Step", 
    "Common Issues and Hands-On Troubleshooting",
    "Extend and Customize Your Implementation"
    ],
    "practical_focus": [
    "15-minute setup with working example",
    "10 essential commands with copy-paste examples", 
    "Build a functional mini-project from scratch",
    "Debug 5 common beginner errors hands-on",
    "Customize and enhance the basic implementation"
    ],
    "learning_outcomes": [
    "Create and run a working {topic} solution",
    "Execute essential commands confidently", 
    "Debug common issues independently",
    "Customize basic implementations"
    ],
    "hands_on_ratio": "75% practical, 25% essential theory",
    "suggested_index_name": "{topic}_Complete_Learning_Guide.md",
    "suggested_subfolder": "{topic}_chapters"
}},
{{
    "title": "Core Implementation Workshop: Build Real-World Solutions",
    "subtopics": [
    "Advanced Implementation Patterns with Live Coding",
    "Performance Testing and Optimization Lab", 
    "Integration Workshop with External Systems",
    "Error Handling and Recovery Implementation",
    "Production-Ready Code Development"
    ],
    "practical_focus": [
    "Code 3 different implementation patterns",
    "Benchmark and optimize performance hands-on",
    "Connect to real APIs and databases",
    "Implement comprehensive error handling",
    "Deploy to production environment"
    ],
    "learning_outcomes": [
    "Implement advanced {topic} patterns",
    "Optimize for production performance",
    "Integrate with real-world systems",
    "Handle errors gracefully in practice"
    ],
    "hands_on_ratio": "80% practical, 20% essential theory"
}}
]

Generate 6-8 chapters total following this enhanced structure that aligns with the appropriate beginner/advanced chapter progressions. Prioritize practical application over theoretical knowledge. Every subtopic should involve actual doing, building, coding, or implementing. Include the suggested file naming in the first chapter only. Respond with ONLY the JSON array, no explanations or additional text.
"""