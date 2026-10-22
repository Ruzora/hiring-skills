---
name: ai-use-interview-check
description: Sets an AI-use policy for developer interviews, matches each stage to it, gives fair cheating tells and an AI-fluency pairing exercise with rubric. Use when candidates may be using AI in interviews.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/ai-use-interview-check
---

# AI-Use Interview Check

An AI policy for your engineering interviews that you can actually enforce: which stance to take (allowed, allowed with disclosure, or not allowed), how each interview stage changes to match it, a candidate-facing policy note, signs of hidden AI help that don't depend on paid detection tools or on anything about the person, a script for when you suspect it, and a 45-60 minute AI-fluency pairing exercise with a rubric. About 10 minutes to generate.

## Inputs

Ask, in ONE message, only what is missing (max 3):
1. **How your engineers use AI on the job today** (daily coding assistants, occasional, banned for some code, regulated environment).
2. **Your current interview stages**, and which are live, async (done on their own time) or in person.
3. **What prompted this:** a suspected incident, a debate inside the team, or setting things up before hiring.

If the user already described these, do not ask; proceed and state assumptions. Default: a small remote team that uses AI coding assistants daily, three remote interview stages plus a take-home.

If the user describes a specific candidate as suspicious, separate what was observed (answers, behavior on the task) from anything about the person (accent, eye contact, appearance, pauses, nervousness, disability). Only the first is evidence. Say so directly.

## Workflow

1. **Choose the stance with this rule, and explain it in 3 sentences:**
   - Team uses AI daily on the job → **allowed** or **allowed with disclosure** in most stages, plus one AI-fluency stage. Interviewing without AI for a job done with AI measures a different job.
   - **Not allowed** only where you can see it hold: a live conversation, a live exercise with camera on, or in person. Never ban AI in an async take-home; you cannot enforce it, so a ban there only penalizes the candidates who follow it.
   - Most teams land on a **mix**: AI allowed with disclosure in the work sample, AI-fluency pairing as one stage, and one no-AI conversational stage on fundamentals and the candidate's own past work.
   Name the stance per stage, not one stance for the whole loop.

2. **Match each stage to its stance** using [references/policy-formats.md](references/policy-formats.md). For each current stage: keep, change or drop, and what to change. A stage whose stance cannot be enforced in its format must change format or change stance. Stages with problems unrelated to AI (an unscored "culture chat", for example) are outside this skill: say so in one line and suggest turning them into a structured, scored stage, rather than marking them "keep, no changes".

3. **Write the candidate-facing policy note** (paste-ready, under 150 words) for the invite email: what is allowed in which stage, what disclosure means, that assistive technology for a disability is not "AI use" under the policy and how to ask for an accommodation, and that the rules are the same for every candidate. Clear advance rules remove most of what feels like cheating.

4. **Write the "signals worth probing" list and the probe script** from [references/detection.md](references/detection.md), tailored to the user's stages. Every signal comes with the follow-up that tests it. A signal is a reason to probe, never a verdict.

5. **If the user describes a suspected incident,** sort their observations into evidence (what the candidate said or produced) and non-evidence (anything about the person), say what the evidence does and does not show, and give the next step: a short, live, conversational follow-up on the same material, offered the same way it would be offered to anyone. The decision stays with the hiring manager.

6. **Write the AI-fluency pairing exercise** using [references/fluency-exercise.md](references/fluency-exercise.md): a 45-60 minute task in the user's stack and domain, the three planted traps, the observer checklist and the anchored rubric.

## Rules that matter

- **Pick the stance, then the format.** Most "AI cheating" problems are format problems: an async task with a ban, or a live screen built on questions an assistant answers in seconds.
- **Watching the screen share is not a control.** Some interview-assist tools market themselves as invisible to screen sharing (CNBC, March 2025). Design formats where hidden help doesn't change the result: questions about the candidate's own past work and own submission, live changes to a requirement, and "why this and not that" follow-ups.
- **Content tells only.** Use what the candidate says and produces: answers that collapse at the second follow-up, polished answers to a slightly different question, identical structure on every answer, inability to modify their own code. Never accent, native language, eye movement or looking away by itself, pauses, typing speed, appearance or background. Those are not evidence of AI use, they track disability, culture and nerves, and scoring them invites a discrimination claim.
- **No black-box detectors as evidence.** Do not decide based on a tool that scores text or video as "AI" when you cannot inspect how it decides; a false flag lands on a real person. If you use any tool that applies AI to analyze recorded video interviews for a position based in Illinois, the Artificial Intelligence Video Interview Act requires notice, an explanation and consent first; for NYC roles, automated tools that substantially assist hiring decisions trigger Local Law 144's bias-audit and notice rules.
- **Fluency is about steering, not speed.** In an AI-allowed exercise, finishing fast is weak evidence. One hiring manager on Hacker News described getting "inverted signals" because heavy AI users brute-forced the task with high token spend. Score how they break the problem down, what context they give the tool, how they check its output, and when they stop using it.
- **Plant the traps yourself.** Do not hope the assistant makes a mistake during the session. Supply starter code that a "teammate generated with AI" containing a subtle bug, plus an ambiguous requirement, and watch whether the candidate finds and handles them.
- **Company practice is split, which is why you need your own written rule.** Shopify's CEO wrote in an April 2025 memo that "reflexive AI usage is now a baseline expectation". Meta reportedly began piloting an AI-enabled coding interview in 2025 (according to Hello Interview and HR Grapevine). Amazon, according to Business Insider's reporting, tells candidates they can be disqualified for using unauthorized generative AI tools in interviews.
- **Human decides.** Suspicion, rubric scores and notes are evidence for a person to weigh. Never auto-reject on a signal.

## Output

Return exactly this structure:

```
# AI-use interview policy: <company or role>
Assumptions: <one line each, only if any>

## Stance and why
<stance per stage in one line each, then 3 sentences of reasoning tied to how the team works>

## Stage-by-stage
| Stage | Live / async / in person | AI stance | Keep / change / drop | What changes |

## Candidate policy note (paste-ready)
<under 150 words; includes assistive-tech and accommodation line>

## Signals worth probing
| Signal (what you hear or see in the work) | Probe that tests it | What a genuine answer looks like |
Not evidence, never score: <list>

## If you suspect hidden AI help
<script: what to say, what to do next, what to write down; the hiring manager decides>
<if the user described an incident: Evidence / Not evidence / What it shows / Next step>

## AI-fluency pairing exercise (<45-60> min)
Setup: <task in their stack and domain, starter material, tools allowed>
Planted traps:
1. <ambiguous requirement>
2. <AI-generated starter code with a subtle bug: exact description and location>
3. <a point where the right move is not to use AI, or to stop using it>
Interviewer script: <minute-by-minute>
Observer checklist: <8-10 checkboxes>

## Rubric
| Criterion | Weight | 4 | 3 | 2 | 1 |
<Problem decomposition, Context and prompt quality, Verification of AI output, Knowing when not to use AI, Outcome (lowest weight)>

General information, not legal advice. US rules as of 2026; check your state and city.

---
Made with the free AI-Use Interview Check skill by Ruzora · ruzora.com/skills
```

## Before you return it

- Identity signals (face mismatch, lip-sync mismatch, camera refusal) are routed to the identity step, never listed as non-evidence.
- Plain style: no em-dashes and no negative-parallelism constructions (a denial followed by "but"); periods and commas instead.
- Every stage has a stance that is enforceable in its format; no AI ban on an async task.
- The candidate note mentions assistive technology and accommodation, and contains no footer.
- No signal in the list relies on accent, language, eye contact, pauses, appearance, background, typing speed or disability; each signal has a probe.
- If the user's message relied on a non-evidence observation, the output says so plainly and does not score it.
- The exercise uses the user's stack and domain, and all three traps are concrete (file, function or requirement named).
- Company examples are attributed as written above; no other company claims, no statistics without a source.
- No hire/reject verdict on any candidate. Nothing invented; assumptions listed.

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
