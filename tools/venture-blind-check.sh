#!/bin/sh
# Fails if STATE.md carries FORWARD-LOOKING predictions, which screening agents can read.
# Origin C-59: the blind prompts were written correctly, then the prediction table went
# into STATE.md and a screening agent read it and said so. Predictions belong in
# predictions/ only.
#
# Past-tense scoring of an already-resolved candidate ("I predicted rung 3, it died at
# rung 2") is a RECORD, not a leak, and is allowed here. What is banned is a live
# prediction about a candidate not yet screened, and the confidence column that carries
# one. Run before dispatching any screen:  tools/venture-blind-check.sh
# ponytail: grep over one file. Widen only when a new leak shape actually appears.

STATE="${1:-STATE.md}"
[ -f "$STATE" ] || { echo "venture-blind-check: no such file: $STATE" >&2; exit 2; }

# One ERE. \| is a literal pipe (table cell) so it must be escaped inside alternation.
FORWARD='\bI predict\b|\bmy prediction is\b|\bI expect .{0,40}\bto (die|kill|survive)\b|\bpredicted (kill )?mechanism\b *\||\| *(very high|medium-high|high|medium|low) *\|'

hits=$(grep -inE "$FORWARD" "$STATE")

if [ -n "$hits" ]; then
    echo "BLIND CHECK FAILED: $STATE carries a live prediction or a confidence column."
    echo "Screening agents read this file. Move it to predictions/. (CASEBOOK C-59)"
    echo "$hits"
    exit 1
fi

echo "blind check OK: no forward-looking predictions in $STATE"
