# Experiment Log

One row per explored path. This is what makes returning to a rejected option real.

| topic | option | hypothesis | result (oracle/score/perf) | decision | recover ref (tag/branch) | resume command | revisit trigger |
|---|---|---|---|---|---|---|---|

Decisions: chosen, rejected, parked.
Recover ref example: experiment/<topic>/<option>.
Resume command example: git checkout -b explore/<topic>-<option>-resume experiment/<topic>/<option> && git rebase main.
