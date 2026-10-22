---
name: deepfake-interview-check
description: Produces a respectful liveness script, observer checklist and escalation steps to catch deepfake or stand-in candidates. Use when a video interview felt off or before remote interviews.
license: CC-BY-4.0
metadata:
  author: Ruzora
  version: "1.0"
  homepage: https://www.ruzora.com/skills/deepfake-interview-check
---

# Deepfake Interview Check

Gives you a 3-minute liveness opening to use with every candidate, a checklist for a second person watching the call, follow-up questions that expose a coached or stand-in candidate, and exactly what to say and do if something fails. If you paste notes from a call that felt off, it also sorts what you saw into real tells, weak tells and things that are not signals, and plans the next call. About 10 minutes to prepare. You decide what happens next.

## Inputs

Collect: the interview format (video tool, who is on the call, how long), the role, and, if there is one, notes from a call that felt wrong (what you saw and heard, with timestamps if you have them).

- If the message includes notes from a call, or clearly asks for the script, proceed. State assumptions at the top.
- Otherwise ask in ONE message, at most:
  1. Is this for all upcoming interviews, or about a call that already happened (paste your notes)?
  2. Will a second person be able to join the next call as an observer?
  3. Do you record interviews today, and in which US state are you and the candidate?
- Never ask the user to upload the video or the candidate's photo or ID.

## Workflow

1. **Make it universal.** The liveness opening is used with every candidate for the role at the same point in the call, announced in the invite. A check run only on the candidate who "seems foreign" or "sounds off" is where national-origin and disability discrimination creep in. If the user wants to run it on one person only, say so and give them the version for everyone.
   If the user wants to accept or reject on a deepfake-detection tool's score, say in one line that a tool score is never the sole basis for any decision and cannot replace the liveness call, then continue.

2. **Sort what was seen (only if call notes were given)** using the tells table in [references/liveness-script.md](references/liveness-script.md):
   - **Real tells:** visual or audio artifacts that a live person does not produce (face edges smear when a hand passes, lips out of sync with audio, coughs or laughs not matching the mouth, face lighting that does not change when they move, a different-looking person across rounds).
   - **Weak tells:** things with innocent explanations that matter only in combination (a steady delay before every answer, eyes reading off to one side, answers that are fluent on definitions and thin on their own experience).
   - **Not signals:** accent, non-native English, nervousness, a slow connection with frozen frames that also freeze the audio, a blurred background before you have asked everyone to turn it off, a disability-related need.
   - Rule: one weak tell is a note. Two independent tells, or any real tell, means the next call runs the full liveness opening with an observer. Nothing in a single call decides.

3. **Write the next call plan:** the liveness opening (verbatim script), the observer checklist, and 3-4 consistency probes built from the candidate's own CV and earlier answers (in the reference file).

4. **Prepare the "if it fails" path:** the exact words for a check that does not work, the alternative verification steps to offer, and the record to write after the call.

5. **Add the legal lines that apply** to the state(s) given, or the general version if none were given.

## Rules that matter

- **Ask for movement, not for documents, first.** Real-time face swaps tend to break when something crosses the face or the head turns to profile. Vidoc Security caught a face-swapped candidate in 2025 by asking him to put his hand in front of his face (reported by The Pragmatic Engineer). Hand across the face, a slow full head turn to each side, leaning toward and away from the camera, and filters and virtual backgrounds off for 30 seconds take under a minute.
- **Audio-video mismatch is the oldest tell.** The FBI's 2022 warning about deepfakes in remote IT job interviews named lip movement out of sync with the audio, including coughs and sneezes that did not match what was on screen.
- **Stand-ins are more common than full deepfakes, and they are caught by continuity, not pixels.** The person on day 1 is not the person who passed the technical round. The fix is boring: an interviewer from the technical round joins the first day-1 video call, and neutral appearance notes from each round are compared.
- **Coaching shows up as delay plus thinness.** A candidate fed answers by someone else, or by an AI tool, pauses before every answer by about the same amount, then answers well in general terms and badly on follow-ups about their own work. Ask them to extend their own earlier answer ("You said you moved the job to a queue. What did the first version get wrong?").
- **Keep latency in proportion.** Bad connections are common, especially across countries. A connection problem freezes picture and sound together; a coaching delay comes before the answer while the picture moves normally.
- **Never accuse during the call.** Say there seems to be a video issue, ask for the step again, and offer a reschedule or an alternative check. Fraudsters drop out; real candidates appreciate the calm.
- **Offer an alternative to anyone who asks.** Some people cannot do a gesture or keep a camera on because of a disability. Under the ADA you offer a reasonable alternative (an in-person meeting, an ID check with a second interviewer, a verified-identity service) instead of skipping verification or dropping them.
- **Recording and AI analysis need consent.** Several states require every party's consent to record a private conversation, including California (Penal Code 632) and Illinois (720 ILCS 5/14-2, as amended by Public Act 98-1142). When the interviewer and candidate are in different states, follow the stricter rule: ask on the record or do not record. If a call was already recorded without consent, do not share or upload it (including to a detection tool), and ask counsel. If you use AI to analyze recorded video interviews for a position based in Illinois, the Illinois AI Video Interview Act (820 ILCS 42) requires notice, an explanation of how the AI works and consent before the interview; the trigger is where the role is based, not where the candidate is. Face-matching on someone in Illinois needs a written release under BIPA. General information as of October 2026, not legal advice.

## Output

Use exactly this structure. No em-dashes. If no call notes were given, omit "What you saw".

```
# Liveness check: <role title>

**Assumptions:** <bullets or "none">

## What you saw (from your notes)
| Observation | Type: Real tell / Weak tell / Not a signal | Why |
|---|---|---|
**Read:** <one or two sentences: what the combination does and does not show; never "this is a fraud">

## Line for the interview invite (send to every candidate)
"<one or two sentences>"

## Opening script (first 3 minutes, every candidate)
Interviewer: "<verbatim>"
...

## Observer checklist (second person, camera off, does not speak)
| Minute | Watch for | Seen? | Note |
|---|---|---|---|

## Consistency probes (built from this candidate's own CV and answers)
| Probe | What the real person can add | What a coached or stand-in answer sounds like |
|---|---|---|

## If a check fails or is refused
- Say: "<verbatim, no accusation>"
- Offer: <alternatives, in order>
- Do not: <list>
- After the call, write: <record template: date, who attended, what was asked, what was seen, what was offered>

## Day 1 and the first two weeks
- <continuity steps>

## Legal lines for your situation
- <bullets>
---
Made with the free Deepfake Interview Check skill by Ruzora · ruzora.com/skills
```

## Before you return it

- The script is written for every candidate, and the invite line announces it in advance.
- No observation is treated as a tell because of accent, fluency, nationality, appearance or disability.
- No single weak tell drives a recommendation; any recommendation is a next verification step, not a verdict.
- The failure script contains no accusation and offers an alternative.
- Recording and AI-analysis consent lines are present, with the stricter-state rule and the Illinois AI Act tied to an Illinois-based role.
- No recommendation rests on a detection tool's score.
- Probes quote or reference the candidate's own words when notes were given.
- No em-dashes. The footer appears once, at the very end, after a horizontal rule.

---

*Built by [Ruzora](https://www.ruzora.com), which places vetted senior engineers from Latin America. Free Ruzora MCP server with 35 hiring tools: [ruzora.com/developers/mcp](https://www.ruzora.com/developers/mcp).*
