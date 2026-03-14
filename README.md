# Course Scraper

Small Python scraper plus a static browser UI for course catalogs.

Current scope:

- CNM course scraping and local browsing
- UNM support planned next

The current scraper pulls course data from CNM's Banner endpoints and writes three outputs:

- `cnm_courses_<term>.csv`
- `cnm_courses_<term>.xlsx`
- `cnm_courses_data.js`

The browser UI in `index.html` reads `cnm_courses_data.js`, so you can open the page directly from disk without running a local web server.

## What's In This Repo

- `cnm_course_scraper.py`: Scrapes Banner, flattens section data, and writes CSV, Excel, and browser bundle outputs.
- `index.html`: Static catalog viewer with filtering, sorting, and CSV export.
- `cnm_courses_data.js`: Bundled course snapshot used by `index.html`.
- `test_cnm_scraper.py`: Unit tests for the scraper and bundle generation.

## Quick Start

If you already have the shared virtualenv:

```zsh
source ~/bin/venv/bin/activate
```

Open the included snapshot in your browser:

```zsh
open index.html
```

No server is required for the default flow. The page uses the local `cnm_courses_data.js` bundle instead of making live cross-origin requests.

## Refresh The Data Snapshot

List available terms:

```zsh
source ~/bin/venv/bin/activate
python cnm_course_scraper.py --list-terms
```

Scrape the default current term:

```zsh
source ~/bin/venv/bin/activate
python cnm_course_scraper.py
```

Scrape a specific term:

```zsh
source ~/bin/venv/bin/activate
python cnm_course_scraper.py --term 202580
```

By default the scraper writes output files into the current directory. You can change that with `--output-dir`.

## Testing

Run the test suite:

```zsh
source ~/bin/venv/bin/activate
python -m pytest test_cnm_scraper.py -q
```

The scraper module can also be syntax-checked with:

```zsh
source ~/bin/venv/bin/activate
python -m py_compile cnm_course_scraper.py
```

## Dependencies

Runtime dependencies:

- `requests`
- `openpyxl` for Excel output

Dev/test dependency:

- `pytest`

See `requirements.txt` and `requirements-dev.txt`.

## How The Browser UI Avoids CORS

`index.html` now prefers the bundled local snapshot in `cnm_courses_data.js`. That means:

- Opening the file directly with `file://` works.
- GitHub Pages or other static hosting can work from the bundled snapshot.
- A local proxy is only needed if you intentionally switch back to live Banner requests.

If you do want live mode, the page still supports the old proxy flow:

```zsh
npx local-cors-proxy --proxyUrl https://banner.cnm.edu --port 8010
```

Then enable the proxy checkbox in the UI.
