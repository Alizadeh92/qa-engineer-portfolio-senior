# UI Automation — Real Project Code Samples

These examples are adapted from UI test code I wrote for an ATPL question-bank workflow. They show supporting automation skills alongside my primary focus on manual QA.

## What the original workflow did

- Used **Python, Selenium WebDriver and PyTest**.
- Organised UI access through page objects and a reusable element wrapper.
- Signed in to the application and opened practice-test configuration for a subject and its topics.
- Selected the question source, read the displayed question count and extracted the numeric value.
- Repeated the collection across 13 subjects and their individual topics.
- Stored collected values in MySQL for later inspection.

## Examples

1. [Reusable Selenium element wrapper](examples/web_element_wrapper.py) — locator handling, explicit waits, interaction and element checks.
2. [Practice page object](examples/practice_page.py) — page object structure and parameterised navigation.
3. [Question-count collection flow](examples/question_count_collection.py) — extracting a number from UI text and iterating over subject/topic inputs.

## Engineering notes and limitations

- These are **sanitised, portfolio-ready excerpts adapted from my own project**, not a turnkey runnable suite.
- Private application addresses, credentials, database connection details and environment-specific configuration are intentionally omitted.
- Running the original end-to-end flow requires authorised access to the application, matching test data, a configured WebDriver and a test database.
- The workflow collected and stored displayed counts. It did **not** compare them against an independently defined expected-count dataset, so I do not describe it as an automated reconciliation test.
- The source project used fixed sleeps in several places. In a production-quality follow-up, I would replace these with explicit waits for meaningful UI states, add stronger assertions, and ensure database writes are isolated and repeatable.

These samples are intended to make the implementation approach reviewable without exposing private systems or data.
