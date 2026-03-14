# Course Scraper

Small Python scraper plus a static browser UI for course catalogs.

## Live Site

- GitHub Pages: [pcleddy.github.io/course-scraper](https://pcleddy.github.io/course-scraper/)
- CNM view: [pcleddy.github.io/course-scraper](https://pcleddy.github.io/course-scraper/)
- UNM view: [pcleddy.github.io/course-scraper/?school=unm](https://pcleddy.github.io/course-scraper/?school=unm)

Current scope:

- CNM course scraping and local browsing
- UNM course scraping through the same Banner flow

The current scraper pulls course data from CNM's Banner endpoints and writes three outputs:

- `cnm_courses_<term>.csv`
- `cnm_courses_<term>.xlsx`
- `cnm_courses_data.js`

The browser UI in `index.html` reads `cnm_courses_data.js`, so you can open the page directly from disk without running a local web server.

## What's In This Repo

- `cnm_course_scraper.py`: CNM scraper plus shared Banner scraping logic.
- `unm_course_scraper.py`: UNM wrapper using the same Banner scraper flow.
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

For UNM after generating `unm_courses_data.js`:

```zsh
open 'index.html?school=unm'
```

No server is required for the default flow. The page uses the local bundle file for the selected school instead of making live cross-origin requests.

## Refresh The Data Snapshot

List CNM terms:

```zsh
source ~/bin/venv/bin/activate
python cnm_course_scraper.py --list-terms
```

Scrape the default current CNM term:

```zsh
source ~/bin/venv/bin/activate
python cnm_course_scraper.py
```

Scrape a specific CNM term:

```zsh
source ~/bin/venv/bin/activate
python cnm_course_scraper.py --term 202580
```

List UNM terms:

```zsh
source ~/bin/venv/bin/activate
python unm_course_scraper.py --list-terms
```

Scrape the default current UNM term:

```zsh
source ~/bin/venv/bin/activate
python unm_course_scraper.py
```

Scrape a specific UNM term:

```zsh
source ~/bin/venv/bin/activate
python unm_course_scraper.py --term 202610
```

By default the scraper writes output files into the current directory. You can change that with `--output-dir`.

Default output names:

- CNM: `cnm_courses_<term>.csv`, `cnm_courses_<term>.xlsx`, `cnm_courses_data.js`
- UNM: `unm_courses_<term>.csv`, `unm_courses_<term>.xlsx`, `unm_courses_data.js`

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

`index.html` now prefers the bundled local snapshot for the selected school. That means:

- Opening the file directly with `file://` works.
- GitHub Pages or other static hosting can work from the bundled snapshot.
- A local proxy is only needed if you intentionally switch back to live Banner requests.

If you do want live mode, the page still supports the old proxy flow:

```zsh
npx local-cors-proxy --proxyUrl https://banner.cnm.edu --port 8010
```

Then enable the proxy checkbox in the UI.
