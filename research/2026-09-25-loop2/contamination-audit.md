# Loop 2 contamination audit (2026-09-25)

Veer asked whether the shaper gamed the evaluation by knowing the bar. To find out, I scanned every loop 2 agent's transcript for tool calls that touched the repo.

## What each agent read

| Agent | Local files read |
|---|---|
| Generators 1-3 | None |
| Shaper | METHOD.md, STATE.md, merged.md (it was given this path), **controls.md** (the three control paragraphs), **scores.csv and `tools/scores.py` output** (the bar), loop 1 RESULT.md, loop 1 shaper and dealer-warranty reports, and all three loop 2 generator reports |
| Control judges | Forward 2 (grep of METHOD) and 3, Vorelios 2: METHOD.md and the file list of the loop 2 folder (which then held only `controls.md`, by name). The other six read nothing. |
| Commissioning judges | 1, 2, 4, 5: METHOD.md. Judge 4 also read STATE.md, which then showed loop 1 standings and the old 10.78 bar. Judge 3 read nothing. |
| Truck judges | 2 and 3: the first 3,000-6,000 characters of METHOD.md. Judge 1 read nothing. Judge 3 also listed the shared scratchpad, which held the YC batch file and the agent ID map. |
| Team fit | METHOD.md, STATE.md, README.md |

No judge read `candidates.md`, `controls.md` or `scores.csv`.

**Root cause:** AGENTS.md is loaded into every subagent and tells it to read METHOD.md and STATE.md. Only the generator prompt told agents not to. Loop 1's transcripts are gone, so it can't be audited the same way. Loop 1's shaper report mentions STATE.md and the judge-versus-controls step, so it probably read them too. At that point no scores existed yet.

## Did it move the scores?

Judge totals in loop 2, split by whether the judge read METHOD or STATE first:

| Paragraph | Read METHOD | Clean |
|---|---|---|
| Perit.AI (control) | none | 11, 11, 13 |
| Forward (control) | 12, 12 | 11 |
| Vorelios (control) | 12 | 10, 11 |
| Commissioning | 12, 11, 12, 12 | 11 |
| Truck warranty | 11, 10 | 9 |
| **Mean** | **11.56 (n=9)** | **10.88 (n=8)** |

- On every paragraph with both kinds of judge, the METHOD readers scored higher, by 0.75 to 1.5 points.
- The samples are tiny. The direction is still consistent, and METHOD itself says the judge passes nearly everything, which a reader could take as a hint to be generous.
- The readers were not spread evenly. Commissioning had 4 of 5, the controls 3 of 9. That tilts commissioning upward against the bar.
- Clean judges only: commissioning is 11.0 (n=1) against a clean loop 2 control mean of 11.17 (n=6). If each reader score is cut by about 1 point, commissioning lands near 11.0 against a bar near 10.85.

**Conclusion:** commissioning's 11.6 is not a clean pass. The honest reading is that it sits at the bar, not clearly above it. Truck warranty stops either way.

## Did the shaper game it?

Mostly not, as far as the record shows:
- Commissioning was generator 3's best idea before the shaper saw anything. The shaper didn't invent it.
- The shaper's main change, from software to a service, followed from competitors it found: CxAlloy OTTO, Facility Grid/PingCx, Bluerithm, CxPlanner.
- Its report said neither idea "clearly clears the bar of 10.93." That understates the idea rather than selling it.
- The one inflated claim in its draft paragraph, "each agent covers several times the megawatts," was docked by every judge. So was its general-contractor channel.
- Knowing loop 1's judges docked market size may have tilted it toward the bigger market over truck warranty. The founder brief already names market size as a judging criterion.

The larger distortion came from the judges reading METHOD, not from the shaper.

## Fixes (METHOD and AGENTS.md, 2026-09-25)

- Shaper, judge and team-fit prompts now say "Use the web, and don't read local project files."
- The shaper gets the merged file pasted into its prompt, not a path.
- AGENTS.md now exempts agents started with a METHOD prompt from its reading list.
- The orchestrator keeps control-identifying files out of the shared scratchpad during judging.

Desk research only; none of this is customer validation.
