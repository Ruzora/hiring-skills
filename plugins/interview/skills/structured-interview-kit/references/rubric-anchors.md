# Anchor library for engineering competencies

Starting anchors and question patterns. Rewrite them for the user's role and stack; never paste them unchanged. A good anchor names behavior two interviewers would both recognize.

## Writing anchors: the test

Read the anchor for 3 and the anchor for 2 side by side. If an interviewer could not tell which one a specific answer matches, rewrite them. Typical differences between levels:
- **4 vs 3:** did it unprompted; named trade-offs and alternatives; generalized a lesson.
- **3 vs 2:** got there, but needed probes; specific about what happened, thinner on why.
- **2 vs 1:** some specifics vs none; could separate own work from the team's vs could not.

## Library

### Technical depth in the role's core stack
- Question patterns: "Walk me through the hardest [stack] problem you solved in the last year." / Work-sample discussion: "Why did you structure it this way?"
- 4: Explains how the tool behaves under the hood where it mattered (for example why a query was slow, how a cache was invalidated); names limits of their solution before being asked.
- 3: Correct, specific explanation of what they built and why; needs a probe to get to limits.
- 2: Describes what the code does but not why; answers about internals are vague or partly wrong.
- 1: Cannot explain their own example beyond surface description, or explanations contradict each other.

### System and data design
- Patterns: "Design the data model for [real feature from the user's product]." / "Tell me about a design you had to change after launch."
- 4: Starts with questions about users, scale and change; proposes a design, states 2+ trade-offs, adjusts cleanly when a constraint changes.
- 3: Sensible design with one trade-off named; adapts to a changed constraint with help.
- 2: A design that works for the happy path; misses an obvious failure case (duplicates, concurrency, deletes) until pointed out.
- 1: No structure, or a design that would not work for the stated requirement, and does not see why when probed.

### Debugging and production ownership
- Patterns: "Tell me about the worst production incident you handled." / Seeded-bug exercise.
- 4: Methodical (reproduce, narrow down, confirm root cause), explains how they would prevent recurrence and how they'd detect it sooner.
- 3: Finds the cause with a sensible method; prevention ideas are generic.
- 2: Guesses before gathering evidence; finds it eventually with hints.
- 1: Changes things at random, or blames external factors without evidence.

### Shipping with ambiguity and judgment
- Patterns: "Tell me about a time requirements were unclear." / "We need X in 3 weeks; what do you ask first?"
- 4: Asks clarifying questions that change the plan, proposes a smaller first version, names what to cut and what never to cut (data, security).
- 3: Reasonable plan with some clarifying questions; scope cutting needs a prompt.
- 2: Plans to build everything as stated, or waits for a full spec.
- 1: Cannot describe a decision process; answers are generic principles with no example.

### Code quality and review
- Patterns: review a short pull request (a proposed code change) with problems seeded in it; "What do you look for when reviewing a teammate's code?"
- 4: Finds the important issues first (correctness, security, data loss) before style; suggests concrete fixes; tone is direct and kind.
- 3: Finds most important issues; mixes in style nits at the same priority.
- 2: Focuses on style and naming; misses a correctness or security issue.
- 1: Misses the main problems, or comments are unclear or dismissive.

### Communication and collaboration
- Patterns: "Explain [their past technical decision] to a non-engineer." / "Tell me about a disagreement with a teammate or manager."
- 4: Plain language, checks understanding, adapts on the fly; in conflict stories, argues with evidence, commits after a decision, credits the other side.
- 3: Clear with minor jargon; conflict handled well but story is thin on what they learned.
- 2: Jargon-heavy even when asked to simplify; conflict stories make them always right.
- 1: Cannot make the point understandable; contempt for colleagues.

### Remote and async work (remote roles)
- Patterns: "How did you keep others aware of your progress at your last job?" / "Tell me about a time you were blocked for a day."
- 4: Writes things down by default (design notes, status updates), asks for help early with a specific question, gives an example.
- 3: Good habits described, fewer concrete examples.
- 2: Relies on meetings or on others asking; waits long when blocked.
- 1: No working method beyond "I just work"; no example.

## Behavioral vs situational

- Behavioral ("Tell me about a time...") for anyone with 3+ years of relevant work. Probe for what *they* did.
- Situational ("Here's what happened to us last month. What would you do?") for juniors, career changers, or competencies their past roles did not exercise. Use a real situation from the user's company.
