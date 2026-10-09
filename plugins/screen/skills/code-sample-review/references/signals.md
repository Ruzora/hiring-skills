# Signals a non-engineer can check

Report what you saw and where. Each signal has a plain-English meaning and a matching interview question.

| Signal | Where to look | Good sign | Worrying sign | Question it leads to |
|---|---|---|---|---|
| README explains how to run it | README | Steps to install and start; what the project does; known limits | Empty, or only the template text of a framework ("This project was bootstrapped with...") | "If I joined your team tomorrow, how would I get this running?" |
| README explains choices | README | "I used X instead of Y because..."; trade-offs; what they would do next | Only a feature list | "Why <choice>? What did you give up?" |
| Tests exist | folders named test, tests, spec, __tests__; files ending in .test or _test | Tests for the important logic (money, dates, permissions), not only a sample test | No tests in a project that handles money or user data; one default test file untouched | "Which part of this would you test first if you had one hour? Why?" |
| Errors are handled | code files: try/catch, error returns, input checks | Bad input and failed network calls produce a clear message or a retry | Errors swallowed silently (empty catch blocks), or no checks on user input | "What happens if <external service> is down when this runs?" |
| Secrets kept out | files named .env, config, settings; strings like "key", "secret", "password" | Settings read from environment variables; a .env.example with placeholders | Real-looking API keys or passwords committed | "I noticed a key in <file>. What would you do about that now?" |
| Structure | file and folder list | Folders that match parts of the product (billing, users, notifications); files of reasonable size | One file with thousands of lines; folders named misc, stuff, new, final2 | "Walk me through where things live. Where would a new feature go?" |
| Dependencies | package.json, requirements.txt, go.mod, Gemfile | A short list of well-known libraries that fit the job | Dozens of libraries for a small app, or several that do the same thing | "Why did you add <library>? What would you do without it?" |
| Commit messages | commits page | Say what changed and why ("handle empty cart at checkout") | All "update", "fix", "wip"; or one giant commit (common, proves little either way) | "Tell me about the commit '<message>'. What was the bug?" |
| Consistency | code files | Same naming style and patterns throughout | Sections in very different styles (could mean copied pieces; ask, do not conclude) | "This part looks different from the rest. What's the story?" |
| Data safety | code that touches databases or user input | Uses parameters or an ORM (a library that builds database queries safely) | Builds database queries by gluing user text into strings (risk of SQL injection, a common attack) | "How does this stop someone from sending malicious input here?" |
| Comments | code files | Explain why something odd is done | Explain obvious lines ("increment i by 1") everywhere; weak hint only | "Why is <odd thing> done this way?" |
| Scope beyond the tutorial | README, commits | Features clearly added after the tutorial or template | Matches the tutorial exactly | "What did you add that the course didn't cover?" |

## Confidence guide

- **High:** you can see it directly and it does not need judgment (tests exist; a key is committed; README has run steps).
- **Medium:** visible but needs some interpretation (structure, commit message quality).
- **Low:** a hint that has innocent explanations (comment style, a style change in one file).

## Seniority calibration

- **Junior (0-2 years):** tutorial-based projects are normal. Look for what they added, whether they can explain it, and whether they wrote any tests at all.
- **Mid (2-5 years):** expect run instructions, some tests, error handling on the main paths.
- **Senior (5+ years):** a personal repo may still be small and messy; seniors often have little public code. When there is code, the useful signals are trade-offs explained, failure handling and tests on the risky parts. Most of the signal for a senior comes from the walkthrough conversation, not the repo.
