# Signal Insight Lab — ATSPM Engineering Diagnostics

An independent traffic-signal troubleshooting and high-resolution event-log analysis app, deployed as a static GitHub Pages site alongside Signal Atlas R1.

## Launch

`https://markrahmanph.github.io/signal-atlas-r1/signal-insight-lab/`

## Included analyses

- Browser-side direct SQLite `.db` / `.sqlite` / `.sqlite3`, CSV, and JSON imports.
- Phase green reconstruction, observed durations, short-green screening, phase utilization.
- Phase termination summaries (gap, max, force-off), detector activations and potential chatter.
- Pedestrian events, individual event-code frequency, and raw event explorer.
- Interactive high-resolution phase/detector event timeline, time zoom, PNG export.
- Editable detector-to-phase mapping and exploratory share of detector-on transitions coincident with phase green.
- Before/after descriptive comparison and non-optimizing timing budget sandbox.
- Data limitations guide and quality warnings for corrupted SQLite files.

## Data and privacy

The tool does not bundle operational event logs. Users upload files locally and computation runs in their browser. The SQLite engine is downloaded from a third-party CDN when first needed; do not use it where your agency's security policy prohibits external dependencies. Do not commit real controller logs or sensitive details to the public repository.

## Limitations

This application is a *diagnostic research prototype*, not a substitute for ATSPM validated detector mappings, controller configuration, field verification, or HCM/simulation. It cannot infer traffic volume or true arrivals on green from arbitrary detector channels alone. Its arrival-on-green proxy is limited to detector-on records coincident with reconstructed green intervals and does not model detector travel time or vehicle identities. Database corruption may result in incomplete or failed imports. Confirm high-resolution event-code meanings against controller firmware.

## Deploying changes

In the GitHub repository, the site lives in `/signal-insight-lab/index.html`. The parent repository's GitHub Pages configuration must publish from the branch/folder that contains this directory (typically `main` and `/root`). Existing Signal Atlas files need not be changed.