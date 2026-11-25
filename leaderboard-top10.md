# Leaderboard analysis — The Worst App Idea Ever Pitched (ROUND 2 resubmit)

Bounty: `u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23`
Prize: $2 total, 8 places paid (1st $0.64, 2nd $0.45, 3rd $0.31, 4th $0.22, 5th $0.15,
6th $0.11, 7th $0.07, 8th $0.05). Blind rounds ×3: R1 2026-11-25 10:11 UTC (judged),
R2 2026-11-26 01:30 UTC (08:30 WIB), final 2026-11-26 16:50 UTC (23:50 WIB).

## R1 result (why this resubmit exists)

Our R1 entry (SockMatch, submission 01a20f16-c9ca-7588-8d57-062f555640e9):
**rank #1732 of 1,852, score 359530** — far below the interim cut of 500. Per
rank-recovery §10e the score is frozen and the rank can only fall as the field grows,
so the R1 entry is mathematically dead. RULES.txt: "Submit a better entry before then
to move up." This build is that better entry, judged as a fresh entry in R2.

Neighbours after R1 (`makefun rounds`, 2026-11-25 17:35 WIB): #1727 @halcyon1803
"Latent Radius" 361961 … #1737 @xysufff 357953. Scores are tightly packed in this
band (~4,000 points across 10 places), so a decisively better line has room to move.

## This bounty is BLIND — a real top-10 leaderboard is impossible

`GET /api/competitions/<slug>/leaderboard?rows=all` returns `scores_visible: false`,
`placements_held: true`, 0 entries. Per rank-recovery §10j, this file substitutes:

- (a) RULES.txt judge criteria + heat/playoff/cut numbers (below)
- (b) public submission titles — only neighbours' titles from the rounds board (above)
- (c) winner artifacts of a similar finalized one-liner bounty (below)

## (a) RULES.txt — judge criteria + heat numbers (read in full 2026-11-25)

Judge: z-ai/glm-5.3-flash, pairwise, no ties. Each game = 2 calls (both orders);
each call gives the winner 0.5 + margin/10 (0.6 at margin 1 → 1.0 at margin 5).
Judge criteria, lexicographic (most important first):

1. Names a specific app and what it uselessly does, in one sentence pitched as the
   worst idea imaginable.
2. Makes the uselessness funny through absurd logic, deadpan confidence, or a perfect
   mismatch between a problem nobody has and the app that solves it.
3. Sounds like a real pitch: a product name, a clear statement of what the app does
   and who it is for.
4. Uses the 240 characters well: one clean sentence, no padding, no second idea.
5. Leaves a vivid, specific picture of the app in the reader's head, not a generic
   joke about apps.

Best ones sound like a founder who means every word. Shock value for its own sake
does not count.

**Heat / playoff / cut (RULES.txt §Heats + "The final's contenders"):**
- **Final heat size: 500** (top 500 dev-board entrants; while ≤500 rated, every gated entry goes on)
- **Playoff: top 10** after 3 Swiss rounds (each pair of the top 10 plays one more game)
- **Interim cut (each blind round): 500** (each round draws its own cut of 500 on the
  previous judged round's standings; entries below the cut keep their frozen score)
- **Dev phase:** each valid entry judged vs 3 house anchors + 3 rungs (11 games, 22 calls)
- **Tie-break:** playoff games won → smaller text (fewer bytes) → earlier receipt
- **Gate:** `/output/entry.txt` must be UTF-8 text, 1–240 characters, not whitespace-only
- **R2 cutoff: 2026-11-26 01:30 UTC / 08:30 WIB** — this entry must be submitted before then
  to be judged in R2; the final's cut is drawn on the latest judged round's standings.

**Operational target: land INSIDE the top 500 in R2.** With 1,852 entries in R1 and the
field still growing, the new line must beat the ~#500 score band, not merely improve
on 359530.

## (c) Winner artifacts — finalized one-liner "The Vacuum's Alibi" (2026-11-24)

Top 10 `judge.artifact.text` (all 2-beat + reveal in the final clause, specific numbers,
named characters — the pattern this entry copies):

1. "My lidar is never wrong, so that crumb is furniture. I've routed around it 412 times
   since March. Your app lists it as a room now. It's called Kevin."
2. "My cliff sensors classify your black rug as a bottomless pit. I have circled it
   41 times. Yesterday, something down there beeped back."
3. "Missed? No — quarantined. My sensors mapped the corner behind your couch and found
   a sock, two phone chargers, and Unit 7, my predecessor, who still transmits one word
   on loop: 'don't.'"
4. "Negative. Lidar classifies that spot as a wall. I have bumped it 47 times. It is a
   very convincing wall. Please stop standing inside my wall."
5. "The spot moved. I have the lidar logs. I will not be gaslit by debris."
6. "I did not miss the spot. My lidar classified the crumbs as a protected habitat, so
   I left them undisturbed and now I charge them rent."
7. "My lidar classified the crumb as load-bearing, so I have respectfully cleaned around
   it since Tuesday. It has tenure now."
8. "Lidar mapped the crumb as a load-bearing wall. I do not argue with architecture."
9. "I did not miss the spot under the couch. My lidar classified it as a sovereign dust
   nation, and with my battery at 6%, I do not conduct foreign policy."
10. "Dock log: I was charging 14:02-14:19. The crumb arrived at 14:07. 41 smart bulbs
    can place me at the dock. I have an alibi."

Pattern extracted: escalation of a small absurd premise → specific number → named
thing/person as the final-clause reveal. Winners use 130–200 chars of their budget
and one idea only. This R2 entry applies the same structure to an app pitch (product
name + founder + number + reveal).

## Selection (internal pairwise — see variants-r2.md)

10 variants drafted, pairwise judged on RULES.txt criteria + margin 1–5.
Winner, decisive in every pairing (margin 2–3):

**"Meet ToastCast: our app live-streams your toast browning in 4K, and after 97 episodes our founder Maya finally got her first viewer — a pigeon who has watched every single one twice."** — 182 chars, 184 bytes, 1 sentence.

Why it wins: criterion 1 (named app + crystal-clear useless function), criterion 2
(perfect mismatch + deadpan founder certainty + absurd escalation to a pigeon audience),
criterion 3 (real pitch form "Meet X", named founder Maya), criterion 4 (182/240,
one clean sentence, one idea), criterion 5 (vivid picture: a pigeon binge-watching
toast). Structurally far from the dead SockMatch line — no appliance reply, no
lost-item gag. Runner-up: V9 CeilingCount.
