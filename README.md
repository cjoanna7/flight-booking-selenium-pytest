# Flight Booking Selenium Pytest

End-to-end UI test automation for a flight booking workflow, built with **Python**, **Selenium** and **pytest**. The tests search for flights, select a flight, enter passenger and payment details, and verify the booking confirmation.

## Highlights

- **Page Object Model:** each page of the booking flow has its own class, which keeps tests readable and easy to maintain
- **Data-driven tests:** test data is kept in a JSON file, separate from the test code
- **Cross-browser:** run on Chrome or Firefox with a command-line option
- **Parallel execution** with pytest-xdist
- **HTML reports** with pytest-html

## Tech Stack

- Python 3.13
- Selenium
- pytest
- pytest-xdist
- pytest-html

## Project Structure

```
flight-booking-selenium-pytest/
├── Data/
│   └── flightBookingData.json      # Test data (fake data only)
├── pageObjects/
│   ├── searchFlightsPage.py
│   ├── selectFlightsPage.py
│   ├── personalDetailsPage.py
│   └── bookingConfirmationPage.py
├── pytests/
│   ├── conftest.py                 # Fixtures and command-line options
│   ├── test_flightBooking.py       # Test cases
│   └── reports/                    # Generated HTML reports
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/cjoanna7/flight-booking-selenium-pytest.git
   cd flight-booking-selenium-pytest
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # macOS / Linux
   .venv\Scripts\activate           # Windows
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

You also need Chrome and/or Firefox installed. Selenium 4 downloads the matching browser driver automatically.

## Running the Tests

Run all commands from the `pytests` folder:

```bash
cd pytests
```

Run on Chrome (the default):

```bash
pytest
```

Run on Firefox:

```bash
pytest --browser_name firefox
```

Run in parallel on 2 workers and generate an HTML report:

```bash
pytest -n 2 --browser_name firefox --html=reports/report.html
```

The report is saved to `pytests/reports/report.html`. Open it in any browser.

## Command-Line Options

| Option | Values | Default | Description |
|---|---|---|---|
| `--browser_name` | `chrome`, `firefox` | `chrome` | Browser to run the tests on |

## Test Data

Test data lives in `Data/flightBookingData.json`. Each entry holds the route, airline, passenger details and payment details for one test run. All values are fake and used for testing only. To add a scenario, add another entry to the `data` list.
