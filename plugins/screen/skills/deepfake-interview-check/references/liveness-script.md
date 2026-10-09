# Liveness script, tells and probes

## Invite line (adapt, send to everyone for the role)

"Like every candidate for this role, we'll start with a quick two-minute camera check at the top of the call: filters and virtual backgrounds off for a moment and a couple of simple movements. If anything about that doesn't work for you, just tell us and we'll arrange an alternative."

## Opening script (3 minutes, interviewer reads it)

1. "Thanks for joining. As mentioned in the invite, we do a quick camera check with everyone before we start."
2. "Could you switch off any filters, touch-up effects and virtual or blurred background for about thirty seconds? You can turn them back on right after."
3. "Could you slowly turn your head to the left until we see your profile, then to the right?"
4. "Now pass your hand slowly in front of your face, from one side to the other."
5. "Lean in toward the camera, then sit back."
6. "Last one: could you hold up whatever is closest on your desk, a mug or a pen is fine?"
7. "Thanks, that's it. Background back on if you like. Let's talk about your work."

Order matters: filters off first, so the movements are tested without a filter covering artifacts.

## What each step tests

| Step | A live face | A real-time face swap often |
|---|---|---|
| Filters and background off | Room appears, same face | Cannot turn off; makes an excuse; face texture looks smoother than the room |
| Head to profile | Ears, jaw and hair line stay consistent | Face flattens, slides, or snaps back to the front view; edges smear |
| Hand across face | Hand covers the face cleanly | Face renders on top of the hand, or the face flickers and distorts |
| Lean in and out | Focus and lighting change naturally | Face scale lags the head; edges shimmer |
| Hold up an object | Object occludes naturally | Object near the face causes glitches |

## Tells table (for sorting call notes)

| Observation | Type | Notes |
|---|---|---|
| Lips out of sync with audio while the picture is otherwise smooth | Real tell | FBI 2022 warning. Rule out a known lag by asking them to say a short sentence after a pause. |
| Cough, sneeze or laugh that does not match the mouth | Real tell | Same FBI warning. |
| Face edges smear, blur or flicker when the head turns or a hand passes | Real tell | Classic face-swap artifact. |
| Lighting on the face does not change when they move or the room light changes | Real tell | |
| Looks like a different person from an earlier round (face shape, glasses, hairline, voice) | Real tell for continuity | Could be a stand-in. Compare against notes from the earlier round, not memory. |
| Will not turn off filter or virtual background, with no reason given | Weak tell | Becomes real only with another tell. Offer an alternative check. |
| Steady 2-5 second pause before nearly every answer while the picture moves normally | Weak tell | Possible relay or coaching. A bad connection freezes the picture too. |
| Eyes repeatedly reading from one fixed point off-screen | Weak tell | Many people glance at notes; matters with thin follow-up answers. |
| Strong on definitions, weak on their own past work | Weak tell | Use the consistency probes. |
| Typed messages much more fluent than speech | Not a signal alone | Many people write better than they speak in a second language, and many use grammar tools. |
| Accent, non-native English, nervousness | Not a signal | Never record these as tells. |
| Frozen frames with audio dropping at the same moment | Not a signal | A connection problem. Offer a reschedule if it is bad. |
| Blurred background before anyone asked to turn it off | Not a signal | Very common for privacy. |
| Asks for an alternative to a gesture or camera use for a disability-related reason | Not a signal | Offer the alternative. |

## Consistency probes (build from the candidate's own words)

Pick 3-4. The point is detail only the person who did the work would have, and the ability to extend their own earlier answer.

| Probe pattern | Real person adds | Coached or stand-in |
|---|---|---|
| "In the last round you described <X>. What did the first version of that get wrong?" | A specific mistake, a date or a person, a fix | Repeats the earlier answer in new words; gives a textbook mistake |
| "Walk me through the folder structure of <project on CV> from memory." | Names folders, a file they hated, why it is structured that way | Vague; generic "controllers, services, models" |
| "Who reviewed your code at <company>? What did they usually push back on?" | A role or a habit ("she always asked for tests on the parsers") | "Senior engineers reviewed it" |
| "Draw/describe how a request flows through <system on CV>, then: what happens if <component> is down?" | Answers the failure case quickly from experience | Pauses, then a general answer about redundancy |
| "What did you work on the week before you left <company>?" | Something small and specific | Something big and generic |

## Alternatives to offer (same for anyone)

1. An in-person meeting if practical.
2. A second short video call with two interviewers and a government photo ID held next to the face (viewed, not recorded or copied).
3. An identity-verification service applied to every finalist (Illinois: BIPA written notice and release first).

## After-call record (neutral, factual)

Date and time · role · interviewers present · steps asked · what each step showed (describe, do not interpret) · what was offered · candidate's response · next step agreed. Keep it with the hiring file; share only with people involved in the decision.

## Sources

- FBI IC3 PSA, June 28, 2022 (deepfakes and stolen PII in remote IT job applications): https://www.ic3.gov/PSA/2022/psa220628
- The Pragmatic Engineer, "AI fakers exposed" (Vidoc Security case), Mar 11, 2025: https://newsletter.pragmaticengineer.com/p/ai-fakers
- California Penal Code 632: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=632
- Illinois BIPA, 740 ILCS 14/15: https://www.ilga.gov/documents/legislation/ilcs/documents/074000140K15.htm
- Illinois eavesdropping statute, 720 ILCS 5/14-2: https://www.ilga.gov/documents/legislation/ilcs/documents/072000050K14-2.htm
- Illinois AI Video Interview Act, 820 ILCS 42/5: https://www.ilga.gov/legislation/ilcs/documents/082000420K5.htm
