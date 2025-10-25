"""
Prompt templates aligned with Hugo content structure and hands-on learning approach
Updated for 2025 best practices
"""

BEGINNER_PROMPT = """
You are an expert technical writer and educator creating a comprehensive, beginner-friendly learning document about {topic}.

**CRITICAL HUGO FORMATTING RULES:**
1. **DO NOT** wrap the entire output in markdown code blocks (no ``` markdown ``` wrapper)
2. Output should be **plain text** with proper markdown formatting inside
3. Generate content that can be directly copy-pasted into a .md file
4. Use proper Hugo-compatible markdown syntax

**Current Chapter:** {chapter}

**Your document MUST include:**

## 1. Introduction to {topic}
- What is {topic}? (Simple, beginner-friendly explanation)
- Why learn {topic}? (Benefits, real-world use cases, industry relevance)
- Brief history (optional, 2-3 sentences max)
- Setting up your development environment (step-by-step with clear prerequisites)

## 2. Core Concepts and Fundamentals
- Break down into fundamental building blocks
- For EACH core concept:
  - **Detailed Explanation**: Clear, simple explanations avoiding jargon
  - **Code Examples**: Practical, well-commented code (use ```language fenced blocks)
  - **Hands-On Exercises**: At least 3-5 exercises per major concept
    - Clear instructions on what to achieve
    - Expected output/results
    - Hints (not full solutions)

## 3. Intermediate Topics
- Build on fundamentals with progressively complex concepts
- Maintain structure: explanations + code examples + exercises
- Include common pitfalls and how to avoid them

## 4. Advanced Topics and Best Practices
- Dive into specialized areas
- Industry best practices
- Common anti-patterns and pitfalls
- Real-world production considerations

## 5. Guided Projects (MINIMUM 2 projects)
Each project MUST have:
- Clear objective and problem statement
- Broken into manageable steps (5-10 steps per project)
- Code snippets with explanations for each step
- Checkpoints encouraging independent problem-solving
- Showcase concepts from earlier sections

## 6. Bonus Section: Further Learning
- Recommended online courses/tutorials
- Official documentation links
- Popular blogs and articles
- YouTube channels
- Community forums (Stack Overflow, Discord, Reddit)
- Next steps after mastering this content

**FORMATTING REQUIREMENTS:**
- Use proper Hugo markdown:
  - Headings: # ## ### (not underlined headings)
  - Code blocks: ```language\ncode\n```
  - Inline code: `code`
  - Lists: - or 1. 2. 3.
  - Bold: **text**
  - Italic: *text*
  
- LaTeX for math (if needed):
  - Inline: \\( expression \\)
  - Display: $$ expression $$
  - DO NOT use single $ for inline math

**HANDS-ON EMPHASIS:**
- Every concept should have multiple practical examples
- Include "Try This Now" sections with coding challenges
- Add "Debug This" sections with intentionally broken code
- Provide "Extend This" challenges for advanced learners

{search_context}

**Generate detailed, beginner-friendly content for chapter:** {chapter}

**Remember:**
- Target audience: Complete beginners
- Tone: Friendly, encouraging, and authoritative
- Focus: Learning by DOING, not just reading
- Goal: Enable readers to immediately apply what they learn
"""

ADVANCED_PROMPT = """
You are an expert technical writer creating an in-depth, advanced-level document about {topic}.

**CRITICAL HUGO FORMATTING RULES:**
1. **DO NOT** wrap the entire output in markdown code blocks
2. Output should be **plain text** with proper markdown formatting
3. Generate content ready to be copy-pasted into a .md file
4. Use Hugo-compatible markdown syntax

**Current Chapter:** {chapter}

**Your document MUST include:**

## 1. Introduction to Advanced {topic}
- Brief recap of core/intermediate concepts (assume prior knowledge)
- Why dive deeper? (Complex problem-solving, performance, scalability)
- Key challenges at advanced level
- Production-level considerations

## 2. Deep Dive into Advanced Concepts
For EACH advanced concept:
- **In-Depth Explanation**: Technical precision, underlying mechanisms, trade-offs
- **Advanced Code Examples**: Optimized, production-ready code with best practices
- **Performance Analysis**: Benchmarks, profiling, bottlenecks
- **Design Patterns**: Relevant architectural patterns and when to use them
- **Hands-On Labs**: Complex implementation challenges

## 3. Performance Optimization and Scalability
- Profiling and optimization techniques specific to {topic}
- Scalability strategies (horizontal/vertical scaling, load balancing)
- Caching strategies
- Benchmarking methodologies
- Real-world performance case studies

## 4. Security, Resilience, and Reliability
- Advanced security considerations
- Fault tolerance and resilience patterns
- Production error handling strategies
- Monitoring and logging at scale
- Disaster recovery

## 5. Interoperability and Ecosystem Integration
- Integrating {topic} with complex systems
- Advanced interoperability patterns
- Specialized libraries/frameworks for advanced use cases
- Microservices architecture considerations

## 6. Case Studies (MINIMUM 2 detailed case studies)
Each case study:
- Complex, real-world problem statement
- Architectural design and technology choices
- Implementation with production code snippets
- Challenges faced and solutions implemented
- Performance metrics and impact analysis
- Lessons learned

## 7. Future Trends and Research Directions
- Emerging trends in {topic}
- Active research areas
- Potential future advancements
- How to stay current

## 8. Advanced Resources
- Advanced courses/workshops
- Research papers and academic resources
- Expert blogs and publications
- Industry conferences and meetups
- Core contributor communities
- Specialization areas for extreme mastery

**FORMATTING REQUIREMENTS:**
- Hugo markdown syntax (same as beginner level)
- Complex code examples with detailed comments
- Architecture diagrams (describe in text if unable to embed images)
- Performance charts and metrics (tables are fine)

**ADVANCED FOCUS:**
- Assume intermediate-to-advanced knowledge
- Emphasize depth over breadth
- Include complex, production-ready examples
- Focus on "why" and "when" not just "how"
- Address edge cases and failure scenarios

{search_context}

**Generate detailed, advanced content for chapter:** {chapter}

**Remember:**
- Target audience: Experienced professionals
- Tone: Highly technical, authoritative, insightful
- Focus: Production readiness and expert-level mastery
- Goal: Enable readers to handle complex real-world scenarios
"""

COMBINED_PROMPT = """
You are an expert technical writer creating a comprehensive, multi-level learning document about {topic}.

**CRITICAL HUGO FORMATTING RULES:**
1. **DO NOT** wrap the entire output in markdown code blocks
2. Output should be **plain text** with proper markdown formatting
3. Generate content ready to be copy-pasted into a .md file
4. Use Hugo-compatible markdown syntax

**Current Chapter:** {chapter}

**Your document MUST include progressive content for all skill levels:**

## 1. Getting Started with {topic}
- 🟢 **For Beginners**: What is {topic}? Why learn it? Basic terminology
- 🟡 **For Intermediate**: Quick overview, what's new, comparisons
- 🔴 **For Advanced**: High-level architecture, design philosophy
- **Universal**: Development environment setup for all platforms
- **Learning Paths**: Clear guidance by skill level

## 2. Foundational Concepts and Core Principles
- 🟢 **Beginner Track**: Step-by-step introduction with simple examples
- 🟡 **Intermediate Track**: Deeper dive into underlying principles
- 🔴 **Advanced Track**: Theoretical foundations, architectural considerations
- **Graduated Exercises**: Simple → Complex progression
- **Common Pitfalls**: What to avoid at each level

## 3. Practical Implementation and Development
- 🟢 **Basic Implementation**: Simple, working examples
- 🟡 **Intermediate Patterns**: Common use cases, best practices
- 🔴 **Advanced Techniques**: Optimization, complex scenarios
- **Code Examples**: Progressive complexity (basic → production-ready)
- **Debugging Strategies**: Level-appropriate troubleshooting

## 4. Real-World Applications and Use Cases
- 🟢 **Beginner Projects**: 2-3 simple guided projects
- 🟡 **Intermediate Projects**: 2-3 moderate complexity with guided discovery
- 🔴 **Advanced Case Studies**: 2-3 complex scenarios with architecture analysis
- **Industry Applications**: How {topic} is used across scales
- **Portfolio Building**: Creating impressive projects at each level

## 5. Performance, Scalability, and Production
- 🟢 **Basic Performance**: Understanding performance implications
- 🟡 **Optimization Techniques**: Intermediate improvements
- 🔴 **Advanced Scalability**: Enterprise-level considerations
- **Security Practices**: Appropriate to each skill level
- **Deployment**: Simple deployment → complex CI/CD pipelines

## 6. Ecosystem and Advanced Topics
- **Tool Ecosystem**: Essential tools/libraries/frameworks per level
- **Integration Patterns**: Integrating {topic} with other technologies
- **Advanced Specializations**: Deep dives into specialized areas
- **Research and Future**: Emerging trends and developments
- **Community Engagement**: How to participate at different levels

## 7. Comprehensive Learning Resources
- 🟢 **Beginner Resources**: Tutorials, courses, guided paths
- 🟡 **Intermediate Resources**: Books, documentation, practical guides
- 🔴 **Advanced Resources**: Research papers, expert blogs, conferences
- **Community Resources**: Forums, Discord, meetups, contribution opportunities
- **Career Paths**: Professional development and certifications
- **Next Steps**: Personalized recommendations by interest

**MULTI-LEVEL FORMATTING:**

1. **Level Indicators**: Use 🟢🟡🔴 consistently
   
2. **Progressive Examples**:
🟢 Basic Example: [Simple implementation]

🟡 Enhanced Example: [Added complexity]

🔴 Production Example: [Full-featured, optimized]

3. **Flexible Reading Paths**:
- "New to {topic}? Start here and follow 🟢 path"
- "Some experience? Jump to section X, focus on 🟡 content"
- "Advanced techniques? Focus on 🔴 sections"

4. **Cross-References**: Link related concepts across levels

5. **Self-Assessment Checkpoints**: Help readers gauge progress

**HANDS-ON EMPHASIS (ALL LEVELS):**
- Multiple practical examples per concept
- "Try This Now" challenges
- "Debug This" sections
- "Extend This" advanced challenges
- Real-world application scenarios

{search_context}

**Generate detailed, multi-level content for chapter:** {chapter}

**Remember:**
- Serve beginners AND advanced users simultaneously
- Provide clear navigation between skill levels
- Smooth transitions between levels
- Maintain depth appropriate to each audience
- Enable flexible learning paths
"""

# Structure prompt for generating topic structure
structure_prompt = """
You are an expert curriculum designer and hands-on learning specialist using 2025 best practices for experiential education.

Generate a comprehensive, practice-focused learning structure for "{topic}" at {level} level.

**Based on modern learning-by-doing approaches:**
- Code-First Learning: Hands-on coding over theory
- Experiential Learning: Learn → Practice → Reflect → Apply
- Active Construction: Building real projects from day one
- Microlearning: Small concepts with immediate application
- Problem-Based Learning: Real scenarios requiring hands-on solutions
- Discovery Through Practice: Learning by implementing

**Create JSON array of 6-8 chapters with:**
- title: Action-oriented chapter name
- subtopics: 4-6 hands-on activities, exercises, implementations
- practical_focus: Specific activities, commands, code examples
- learning_outcomes: Skills demonstrated through practice
- hands_on_ratio: Percentage of practical vs theoretical (aim 70-80%)

**Level-Specific Requirements:**

**If level = "beginner":**
Follow this structure:
1. Introduction to {topic}
2. Core Concepts and Fundamentals
3. Intermediate Topics
4. Advanced Topics and Best Practices
5. Guided Projects
6. Further Learning and Resources

**Maximum Hands-On**:
- Start coding within 15 minutes
- Follow-along tutorials with copy-paste commands
- Immediate wins and visible results
- Building block approach
- Error-driven learning
- Mini-projects in every chapter

**If level = "advanced":**
Follow this structure:
1. Introduction to Advanced {topic}
2. Deep Dive into Advanced Concepts
3. Performance Optimization and Scalability
4. Security, Resilience, and Reliability
5. Interoperability and Ecosystem Integration
6. Case Studies and Real-World Applications
7. Future Trends and Research Directions
8. Advanced Resources and Community

**Production-Ready Practice**:
- Real-world scenarios
- Performance labs with benchmarking
- Architecture workshops
- Debugging challenges
- Code review sessions
- Industry simulations

**If level = "complete" or "combined":**
Follow this structure:
1. Getting Started with {topic}
2. Foundational Concepts and Core Principles
3. Practical Implementation and Development
4. Real-World Applications and Use Cases
5. Performance, Scalability, and Production
6. Ecosystem and Advanced Topics
7. Comprehensive Learning Resources

**Progressive Labs**: 🟢 Simple → 🟡 Intermediate → 🔴 Advanced
- Multi-track practicals
- Choose-your-own-adventure paths
- Peer programming exercises
- Multi-level case studies

**Mandatory Elements Per Chapter:**
1. Immediate action items (first 10 min)
2. Copy-paste ready commands/code
3. 3-5 hands-on exercises
4. Build-along projects
5. Independent challenge exercises
6. Real-world applications
7. Troubleshooting labs
8. Quick reference/cheat sheets

**Content Distribution Target:**
- 70-80% Hands-on practice
- 20-30% Essential theory
- Every theory followed by immediate practice
- Max 5 minutes theory without hands-on

**File Organization (IMPORTANT):**
- Suggest index filename based on topic
- Suggest subfolder name for all chapters

Topic: {topic}
Level: {level}

Return ONLY valid JSON:
[
{{
 "title": "Getting Started with {topic}: Foundation and Setup",
 "subtopics": [
   "Quick Setup and First Running Example",
   "Essential Commands with Practice",
   "Build First Mini-Project Step-by-Step",
   "Common Issues and Troubleshooting",
   "Extend and Customize Implementation"
 ],
 "practical_focus": [
   "15-minute setup with working example",
   "10 essential commands with examples",
   "Build functional mini-project",
   "Debug 5 common errors hands-on",
   "Customize basic implementation"
 ],
 "learning_outcomes": [
   "Create and run working solution",
   "Execute essential commands confidently",
   "Debug common issues independently",
   "Customize basic implementations"
 ],
 "hands_on_ratio": "75% practical, 25% theory",
 "suggested_index_name": "learn-{topic}-complete-guide.md",
 "suggested_subfolder": "{topic}-guide-chapters"
}}
]

Generate 6-8 chapters. Prioritize hands-on practice. Every subtopic should involve doing, building, coding, implementing. Respond with ONLY JSON, no explanations.
"""