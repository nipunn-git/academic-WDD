# CGPA Calculator

A simple browser-based CGPA calculator. Enter marks and credit values for your subjects to calculate a credit-weighted CGPA using the grade point scale below.

## Contributors

| Name | SAP ID | Roll number | GitHub |
| --- | --- | --- | --- |
| Nipun | 70572500365 | X050 | [nipunn-git](https://github.com/nipunn-git) |
| Parteek Garg | 70572500363 | X048 | [parteek1907](https://github.com/parteek1907) |
| Ojas Bali | 70572500250 | X034 | [OjasBali17](https://github.com/OjasBali17) |

## Features

- Add as many subjects as needed.
- Convert marks to grade points automatically.
- Calculate CGPA as a weighted average based on subject credits.
- Validate marks and credits and show the result to two decimal places.

## Grade Point Scale

| Marks | Grade | Grade points |
| --- | --- | ---: |
| 90–100 | O | 10 |
| 80–89 | A+ | 9 |
| 70–79 | A | 8 |
| 60–69 | B+ | 7 |
| 50–59 | B | 6 |
| 40–49 | C | 5 |
| Below 40 | F | 0 |

**Formula:** CGPA = Σ(grade points × credits) ÷ Σ(credits)

## Run the Project

1. Download or clone this repository.
2. Open `index.html` in a modern web browser.
3. Add subjects, enter marks (0–100) and positive credit values, then select **Calculate CGPA**.

No installation or build tools are required.

## Project Files

- `index.html` — calculator page and grade scale.
- `style.css` — page styling.
- `script.js` — subject rows, grade conversion, validation, and calculation logic.


## Technologies

HTML, CSS, and vanilla JavaScript.
