# Signal Atlas Pro — Region 1 Signal Management

A browser-based traffic signal cabinet map with searchable inventory, manager filters, Google Maps and Street View shortcuts.

## Publish with GitHub Pages

1. Sign in to https://github.com/new and create a repository (for example `signal-atlas-r1`). Select **Public** if you want anyone with the URL to access it.
2. Upload `index.html` to the repository root (and optionally this README and `.nojekyll`). Commit the changes.
3. Go to **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, select **main** and **/(root)**, then **Save**.
4. Your link will be `https://YOUR-USERNAME.github.io/signal-atlas-r1/` (adjust for your actual GitHub username and repository name). GitHub may take a few minutes to publish.

## Notes

- No server or Google Maps API key required: Google Maps / Street View shortcuts open in a new tab using cabinet coordinates.
- The page needs an internet connection for the Leaflet library and map tiles.
- Inventory is included within `index.html`; it is visible to anyone who can load the site. **Review and remove any sensitive or nonpublic information before publishing a public repository.**
- Changes to your local file do not automatically update GitHub; commit the updated `index.html` to republish.
- If you want access limited to authorized ODOT personnel, public GitHub Pages is not an appropriate access control solution.
