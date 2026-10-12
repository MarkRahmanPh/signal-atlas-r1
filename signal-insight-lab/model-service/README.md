# Optional model-backed detector classification

This service calls Shawn Strasser's genuine `atspm_detector.predict`. It is **not hosted by GitHub Pages**. Deploy separately to your own Python host. Install from `requirements.txt`, set `MODEL_API_TOKEN` and `ALLOWED_ORIGINS=https://markrahmanph.github.io`, then run `uvicorn app:app --host 0.0.0.0 --port 8000`.

The browser accepts your HTTPS service URL and token at run time. **Do not save tokens in your public GitHub repository.** Controller event logs are sent to this backend only after you click Run model. Service does not write log data to disk, though your host, reverse proxy or network infrastructure may log requests. Use an authenticated, HTTPS-hosted private service. No claim of model-backed predictions is made until a real response is received.

Model returns phase, function, probabilities, review flags, health, lane and setback output when available. Review predictions before using in ATSPM.
