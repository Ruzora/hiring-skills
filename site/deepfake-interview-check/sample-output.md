# Liveness check: Senior Backend Engineer (Go + Postgres), fully remote US

**Assumptions:**
- You (interviewer) are in Sacramento, California; the candidate says he is in Portland, Oregon. California requires every party's consent to record, so that is the rule for Thursday.
- The role is fully remote in the US and not based in Illinois, so the Illinois AI Video Interview Act and BIPA do not apply unless that changes.
- Thursday's call is 60 minutes on Zoom: you interview, Priyanka (staff engineer) observes with camera off.
- Ana kept some written notes from her 20-minute screen last week. If she did not, she writes down what she remembers today, before Thursday, so the comparison is not done from memory on the call.
- The camera check below becomes standard for every remaining candidate for this role, not only for this one. On Tuesday you asked only him to drop the background; from now on, everyone gets the same request at the same point.

## What you saw (from your notes)
| Observation | Type: Real tell / Weak tell / Not a signal | Why |
|---|---|---|
| Around min 12, coughed and the mouth did not move; the face stayed in its talking position while the video kept running | Real tell | A cough that does not match the mouth is the audio-video mismatch the FBI named in its 2022 warning. Your Wi-Fi is unlikely to explain it: a bad connection freezes picture and sound together, and the picture did not freeze. |
| Edge of the jaw smeared for a second when he turned to grab water | Real tell | Edges smearing on a head turn is a classic face-swap artifact. One caveat: background blur can also smear the outline of a moving head, so this needs a retest with the blur off. |
| Blurred office background the whole call; when asked, said his laptop "doesn't let him turn it off" | Weak tell | A blurred background on its own is very common for privacy. He gave a reason, but Zoom lets you switch blur off on almost any laptop. It only counts alongside the other tells, and only one candidate was asked, so Thursday's check has to be the same for everyone. |
| About a 3-second pause before nearly every answer, including "how's your day going," while the picture moved normally | Weak tell | Fits relaying or coaching. A connection problem would freeze the picture too. A pause even on small talk is worth noting, but nervousness and second-language processing also slow people down. |
| Kept looking to the lower left, as if reading | Weak tell | Lots of people glance at notes. It only matters together with the thin follow-up answers below. |
| Textbook-perfect answers on Go concurrency; on "what went wrong when you moved the job runner to NATS" he said "there were some challenges with message ordering which we resolved with best practices" | Weak tell | Strong on definitions, thin on his own work. The NATS project is his own headline CV item, so this is what the probes test. |
| Ana: looked "younger" and had a beard on the screen; no beard on Tuesday | Weak tell (continuity, unconfirmed) | Shaving explains a beard. "Younger" is a memory impression. This becomes a real continuity tell only if Ana's written notes describe a different face shape, glasses, hairline or voice. |
| Strong accent (you guess Eastern European), very formal English | Not a signal | Accent and formal second-language English say nothing about identity. Do not write them in any record as a tell. |

**Read:** Two real tells (cough not matching the mouth, jaw smear on a head turn) plus several independent weak ones mean Thursday should run the full liveness opening with an observer. That is the next verification step, not a finding: a bad setup, a heavy blur effect and a nervous candidate could still account for much of what you saw, and nothing from Tuesday decides anything on its own.

## Line for the interview invite (send to every candidate)
"Like every candidate for this role, we'll start with a quick two-minute camera check at the top of the call: filters and virtual or blurred backgrounds off for a moment and a couple of simple movements. If anything about that doesn't work for you, just tell us before Thursday and we'll arrange an alternative. We'd also like to record the call for our hiring team and will ask for your OK at the start; you're free to say no."

Send Sol the Thursday invite with this line today, and add the same line to every other interview invite for this role from now on. If his laptop really cannot drop the blur, this gives him time to tell you or switch devices, and you are not springing it on him live.

## Opening script (first 3 minutes, every candidate)
Interviewer: "Thanks for joining. Before anything else: we'd like to record this call for our hiring team. Is that OK with you? You can say no and we'll just take notes."
(Start the recording only after a clear yes. If no, do not record.)
Interviewer: "This is Priyanka, one of our staff engineers. She'll be listening with her camera off and taking notes."
Interviewer: "As mentioned in the invite, we do a quick camera check with everyone before we start."
Interviewer: "Could you switch off any filters, touch-up effects and the virtual or blurred background for about thirty seconds? You can turn them back on right after. In Zoom it's the little arrow next to Stop Video, then Blur or Virtual Background, then None."
Interviewer: "Could you slowly turn your head to the left until we see your profile, then to the right?"
Interviewer: "Now pass your hand slowly in front of your face, from one side to the other."
Interviewer: "Lean in toward the camera, then sit back."
Interviewer: "Last one: could you hold up whatever is closest on your desk, a mug or a pen is fine?"
Interviewer: "And just to check our audio sync: after a short pause, could you say 'I worked on the dispatch service'?"
Interviewer: "Thanks, that's it. Background back on if you like. Let's talk about your work."

## Observer checklist (second person, camera off, does not speak)
| Minute | Watch for | Seen? | Note |
|---|---|---|---|
| 0-1 | Blur actually turned off; real room visible; face texture similar to the room (not noticeably smoother) | | |
| 0-1 | If he says he cannot turn it off: the exact words used (write them down, do not interpret) | | |
| 1-2 | Head to profile both sides: ears, jaw and hairline stay consistent; no flattening, sliding or snapping back to front view; no edge smear | | |
| 1-2 | Hand across face: hand covers the face cleanly; face does not render on top of the hand or flicker | | |
| 2-3 | Lean in and out: face scale keeps up with the head; focus and lighting change naturally | | |
| 2-3 | Object held near the face: no glitching around it | | |
| 2-3 | Sync sentence after the pause: lips match the words | | |
| 0-60 | Any cough, laugh, sneeze or sigh: does the mouth match the sound? Note the minute | | |
| 0-60 | Pause length before answers: time 5 of them, including one small-talk answer. Does the picture keep moving during the pause? | | |
| 0-60 | Eye direction: repeatedly to one fixed off-screen point, timed with answers | | |
| 0-60 | Any frozen frames: did the audio drop at the same moment? (If yes, it is a connection issue, not a tell) | | |
| 3-50 | Probe answers: specific names, mistakes, files, dates vs general "best practices" language | | |
| 0-60 | Neutral appearance notes for continuity: face shape, glasses, hairline, facial hair, voice pitch. Compare with Ana's screen notes after the call, not during | | |

Do not note accent, fluency, formality of English or nervousness anywhere on this sheet.

## Consistency probes (built from this candidate's own CV and answers)
| Probe | What the real person can add | What a coached or stand-in answer sounds like |
|---|---|---|
| "On Tuesday you mentioned message ordering challenges when you moved the job runner to NATS. Which jobs actually broke when ordering went wrong, and what did the first version get wrong?" | A specific job type (for example, a cancel arriving before its create), how they noticed (an alert, a customer ticket), and the concrete fix: per-key subjects, JetStream with a sequence check, idempotent handlers, a dedupe table in Postgres | Repeats "message ordering challenges" in new words; "we followed best practices"; a textbook answer about ordering with no incident in it |
| "When you switched off the old cron-based runner, what happened to jobs that were mid-run or scheduled for that night? How did you cut over?" | A real cutover story: ran both in parallel, a feature flag, a job that ran twice or not at all, a date or weekend it happened | General talk about "zero-downtime migration" with no moment, person or problem in it |
| "Walk me through the folder structure of the dispatch service from memory. Which package did you most want to rewrite?" | Names packages or directories, a file everyone hated, why it is laid out that way, something they would change | Vague; generic "handlers, services, models, repository" with no opinion |
| "Who reviewed your Go code at the logistics company, and what did they usually push back on?" | A role or a habit ("our principal always made us pass context through and add a test for the retry path") | "Senior engineers reviewed it"; "they checked for best practices" |
| (If time allows) "What did you work on the week before you left?" | Something small and specific: a bug, a migration step, a handover doc | Something big and generic |

Ask each probe, then extend it once from whatever he says ("You said X. What happened next?"). That follow-up matters more than the first answer.

## If a check fails or is refused
- Say: "Looks like we've got a video issue on our side of things, the step didn't come through clearly. Could we try that one again?" If it still does not work: "No problem. We do this check with everyone, so let's set up another way to do it. Here are a couple of options."
- Offer, in order:
  1. A short second video call from a different device (phone is fine) with the blur off, with two of you on the call.
  2. A second short video call with two interviewers where he holds a government photo ID next to his face (you look at it; you do not record, screenshot or copy it).
  3. If he is near you or you can arrange it, an in-person meeting. Portland to Sacramento is far, so this is realistic only if you were planning a finalist visit anyway.
  4. An identity-verification service that you apply to every finalist for this role, not only to him.
  If he says a gesture or keeping the camera on is hard for a disability-related reason, offer one of the alternatives above without asking for details.
- Do not:
  - Use the words fake, deepfake, fraud, AI or "is this really you" on the call.
  - Mention his accent, his English or where he is from, then or later.
  - Mention Tuesday's cough, jaw or Ana's beard comment to him.
  - Drop him or reject him on the spot, or because he asked for an alternative.
  - Upload Tuesday's or Thursday's recording to a deepfake-detection tool, or make any decision on a tool's score.
  - Discuss what you saw with anyone outside the hiring decision (you, Priyanka, Ana).
- After the call, write: Date and time · role (Senior Backend Engineer) · attendees (you, Priyanka, Ana if she joined) · whether recording was consented to · each liveness step asked and what it showed (describe, do not interpret: "head turn to left: jaw edge stayed sharp" or "hand across face: face visible over the hand for about one second") · probes asked and a short summary of each answer · what was offered if a step did not work · the candidate's response · next step agreed. Then compare the neutral appearance notes with Ana's screen notes and Tuesday's notes, and add one line on whether they match. Keep it in the hiring file, shared only with people involved in the decision.

How to read Thursday: if all steps pass cleanly with the blur off and the probes get specific, first-hand answers, treat Tuesday as a bad setup and evaluate him on the work like anyone else. If a step fails, or he cannot turn the blur off and also cannot take any of the alternatives, the next step is alternative verification, not a rejection on this call.

## Day 1 and the first two weeks
- If you hire him, you or Priyanka (someone who saw him on Thursday) join his first day-1 video call, and compare against the neutral appearance notes from the screen, Tuesday and Thursday.
- Do the I-9 document review with a person who has seen him on an interview call, live on video, with the documents held up next to his face. If you use an authorized representative or E-Verify, do it the same way for every new hire.
- Ship his laptop to the Portland address on his I-9 and offer letter. A last-minute request to send equipment to a different address or a forwarding service is a reason to pause and verify, not to proceed.
- Check that the name on the payroll bank account matches the name on the offer.
- Camera on for standups in the first two weeks, as the norm for every new hire, him included.
- In week 1, have him walk Priyanka through his first PR live on a call, explaining the choices in his own words.
- If anything does not line up in the first two weeks, go back to the "Offer" list above and talk to counsel before acting on it.

## Legal lines for your situation
- Recording: California requires every party's consent to record a private conversation (Penal Code 632). Oregon has its own consent rules, and the stricter one applies across state lines, so ask on the record at the start of Thursday's call and do not record if he says no. Make "ask first" the default for every interview, not "record by default."
- Tuesday's recording: check whether Zoom showed him its recording notice and whether he clearly agreed. If you are not sure he consented, do not share it, do not upload it to any tool (detection or otherwise), and ask counsel what to do with it.
- AI analysis: the Illinois AI Video Interview Act (820 ILCS 42) applies when the role is based in Illinois. Yours is not, so it does not apply here. If you ever run AI analysis on interview video, tell every candidate in advance and get their consent anyway.
- Biometrics: BIPA's written release applies to face-matching on someone in Illinois. He says he is in Oregon. If you use an identity-verification service for finalists, use its notice and consent flow for everyone.
- A deepfake-detection tool score is never the sole basis for a decision and cannot replace the liveness call.
- Discrimination: accent, national origin and disability can play no part in this process. The same check, the same invite line and the same alternatives go to every candidate for the role, and any disability-related request gets a reasonable alternative under the ADA (and California's FEHA).
- General information as of October 2026, not legal advice.
---
Made with the free Deepfake Interview Check skill by Ruzora · ruzora.com/skills
