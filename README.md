# CNM & UNM Course Catalog Browser

A faster, friendlier way to browse the CNM and UNM class schedules. Replaces Ellucian Banner's clunky search-one-subject-at-a-time interface with a single-page app you can browse offline or host on GitHub Pages.

Browse by subject, see what's open at a glance, click into any section for full details — instructor, schedule, building, seat availability, waitlist status.

## Live Site

- **CNM:** [pcleddy.github.io/course-scraper](https://pcleddy.github.io/course-scraper/)
- **UNM:** [pcleddy.github.io/course-scraper/?school=unm](https://pcleddy.github.io/course-scraper/?school=unm)

## Schools & Terms

- **Central New Mexico Community College (CNM)** — Albuquerque, NM
- **University of New Mexico (UNM)** — Albuquerque, NM
- Supports any term available in Banner (Spring 2026, Summer 2026, Fall 2025, etc.)

## What This Does

A Python scraper pulls every course section from Banner's class search API and writes three outputs per school: a CSV, an Excel workbook, and a JavaScript data bundle. The browser UI (`index.html`) reads the JS bundle so it works offline — no server, no CORS headaches, just open the file.

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

## What Is Ellucian Banner?

Ellucian Banner is the student information system used by hundreds of colleges and universities, including CNM and UNM. Its built-in class search interface (Banner Self-Service / StudentRegistrationSsb) only lets you search one subject at a time with no way to see the full catalog at once. This project works around that limitation by querying every subject programmatically and presenting the results in a browsable UI.

## Topics

`cnm` `unm` `central-new-mexico` `university-of-new-mexico` `albuquerque` `new-mexico` `course-catalog` `class-schedule` `class-search` `ellucian-banner` `banner-scraper` `student-registration` `open-sections` `seat-availability` `course-browser` `community-college` `higher-education` `spring-2026`
