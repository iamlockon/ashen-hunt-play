# Ashen Hunt — playable browser release

This repository contains the compiled desktop-browser player and a manual
GitHub Pages publishing workflow. The Unity authoring project is kept separately.

Controls: WASD movement, Shift sprint, Space evade, J/left mouse attack,
hold K/right mouse for a charged strike, Q heal, Tab lock-on, Escape pause.

`release.json` records the authoring revision and exact static payload hashes.
The workflow validates that inventory before publication. Pushes do not deploy
automatically; use `Publish playable game` on the `uat` branch.
