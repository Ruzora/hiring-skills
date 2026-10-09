---
title: "Deepfake Interview Detection: Free AI Skill and Script"
description: A free AI skill that gives you a respectful liveness script, an observer checklist and next steps to catch deepfake or stand-in candidates on video calls.
target_query: deepfake interview detection
category: screen
related_blog: how-to-spot-a-fake-senior-developer
cta: /how-we-vet
author: Roberto Espinoza
updated: 2026-10-04
---

# Deepfake interview detection: a liveness script you can run on every call

Deepfake Interview Check is a free AI skill that helps hiring managers catch face-swapped or stand-in candidates on video interviews without accusing real people. It writes a 3-minute liveness opening for every candidate, an observer checklist, probes built from the candidate's own CV, and the exact words to use if a check fails.

The FBI warned in 2022 that deepfakes and stolen identities were being used to apply for remote IT jobs. The fix is cheap: a few movements at the top of every call.

## What you get

- **An invite line** announcing the camera check to every candidate, so nobody is singled out.
- **A verbatim opening script:** filters off for 30 seconds, head turn to profile, hand across the face, lean in and out, hold up an object.
- **An observer checklist** for a second person, minute by minute.
- **A sorted read of call notes** you paste: real tells, weak tells, and things that are not signals.
- **Consistency probes** that ask the candidate to extend their own earlier answers.
- **A failure path:** what to say, which alternatives to offer, and a neutral record to keep.
- **Legal lines for your state**, including recording consent.

## Sample output

From a real run. The input: a California CTO's notes on a call with a senior Go candidate whose mouth did not move when he coughed, whose jaw "smeared" when he turned, who paused 3 seconds before every answer and had a strong accent. The CTO records interviews by default.

> | Observation | Type: Real tell / Weak tell / Not a signal | Why |
> |---|---|---|
> | Around min 12, coughed and the mouth did not move; the face stayed in its talking position while the video kept running | Real tell | A cough that does not match the mouth is the audio-video mismatch the FBI named in its 2022 warning. Your Wi-Fi is unlikely to explain it: a bad connection freezes picture and sound together, and the picture did not freeze. |
> | Strong accent (you guess Eastern European), very formal English | Not a signal | Accent and formal second-language English say nothing about identity. Do not write them in any record as a tell. |

> **Read:** Two real tells (cough not matching the mouth, jaw smear on a head turn) plus several independent weak ones mean Thursday should run the full liveness opening with an observer. That is the next verification step, not a finding: a bad setup, a heavy blur effect and a nervous candidate could still account for much of what you saw, and nothing from Tuesday decides anything on its own.

> - Tuesday's recording: check whether Zoom showed him its recording notice and whether he clearly agreed. If you are not sure he consented, do not share it, do not upload it to any tool (detection or otherwise), and ask counsel what to do with it.

## How it works

**The check is for everyone.** A liveness step run only on the candidate who "seems off" is where national-origin and disability bias get in. So it is a standard opening, announced in the invite.

**Movement beats documents.** Real-time face swaps tend to break when something crosses the face or the head turns. Vidoc Security caught a face-swapped candidate in 2025 by asking him to put a hand in front of his face (reported by The Pragmatic Engineer).

**One tell is a note.** Two independent tells, or one real artifact, means the next call runs the full check with an observer. Nothing in a single call decides anything.

**Stand-ins are caught by continuity.** Sometimes the person on day 1 is not the one who passed the technical round. An interviewer joins the first day-1 call, and neutral notes from each round get compared.

**Never accuse on the call.** The script blames the video, asks again, then offers alternatives: meeting in person, a second call with two interviewers and a photo ID held to the camera, or a verification service. Under the ADA, anyone who cannot do a gesture for a disability-related reason gets an alternative.

**Consent first.** Several states, including California and Illinois, require every party's consent to record; across state lines, follow the stricter rule. Illinois also requires notice and consent before AI analyzes recorded interviews for Illinois-based roles. A detection tool's score never decides anything alone. General information, not legal advice.

### How this compares

A static deepfake checklist lists artifacts and stops. Asking a chatbot cold tends to produce a list of detection tools, or advice that treats an accent or a slow connection as suspicious. This skill gives you words to say, a way to tell signal from noise, and a failure path that keeps a real candidate's dignity intact.

## How to install and use

**Claude.ai:** download the skill's .zip from this page and upload it under Customize > Skills in Claude (any plan, including Free; code execution must be on). Then paste your call notes, or ask for the script.

**Claude Code:** run `/plugin marketplace add Remutopia/ruzora-skills`, then `/plugin install hire-screen@ruzora-hiring`. Describe the interview and the skill loads on its own.

**Any other AI (ChatGPT, Gemini, Copilot):** copy the prompt version from this page, paste it as your first message, then add your notes.

Never upload the video or an ID. Notes are enough.

## Frequently asked questions

### How can you tell if a job candidate is using a deepfake?
Ask everyone to turn off filters and backgrounds briefly, turn their head to profile and pass a hand in front of their face. Watch for face edges that smear, a face that renders over the hand, and lips or coughs that do not match the audio while the picture keeps moving.

### Is it legal to ask a candidate to do a liveness check?
Generally yes, when you ask every candidate the same way, announce it in advance and offer an alternative to anyone who needs one. Recording needs consent in some states. This is not legal advice.

### What do I do if a candidate fails the check?
Do not accuse them. Say the video seems to be struggling, try once more, then offer an in-person meeting or a verified ID call with two interviewers. Write down what you saw, without interpretation.

### Does it cost anything?
No. No signup and no email gate. Use it, change it and share it under CC-BY-4.0.

---

**Want identity and liveness checks done before a candidate ever reaches you?** See [how we vet engineers](/how-we-vet): 5-stage vetting, including live coding, system design and AI-tool proficiency. Or [request a shortlist](/request-shortlist) and get a vetted shortlist within 72 hours. For more on the warning signs, read [how to spot a fake senior developer](/blog/how-to-spot-a-fake-senior-developer).
