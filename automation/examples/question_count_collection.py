"""Sanitised workflow excerpt adapted from a real PyTest data-collection test.

This example demonstrates collection, not reconciliation against expected values.
It requires an authorised browser session and an explicitly supplied test DB
connection; no credentials or private connection details are included.
"""

import re

from .practice_page import PracticePage


def extract_question_count(displayed_text):
    """Return the first integer found in the UI text, or None if absent."""
    match = re.search(r"(\d+)", displayed_text)
    return match.group(1) if match else None


def read_question_count(driver, subject_code, topics):
    """Open practice configuration, choose BGS and read the displayed count."""
    page = PracticePage(driver, subject_code, topics)
    page.open()

    page.question_source_dropdown.click()
    page.bgs_question_source.get_element()
    page.bgs_question_source.click()

    displayed_text = page.question_count.get_text()
    return extract_question_count(displayed_text)


def save_question_count(db_connection, subject_code, question_count):
    """Persist one collected count using a parameterised SQL statement."""
    if question_count is None:
        raise ValueError("Cannot store a question count when the UI value is missing")

    sql = (
        "INSERT INTO qb_summaries (air_subject, air_count) "
        "VALUES (%s, %s)"
    )
    with db_connection.cursor() as cursor:
        cursor.execute(sql, (subject_code, question_count))
    db_connection.commit()


def collect_subject_and_topic_counts(driver, db_connection, subjects):
    """Collect counts for each configured subject and each topic within it.

    subjects is an iterable of (subject_code, hyphen_delimited_topic_codes).
    """
    for subject_code, topic_codes in subjects:
        count = read_question_count(driver, subject_code, topic_codes)
        if count is not None:
            save_question_count(db_connection, subject_code, count)

        for topic_code in topic_codes.split("-"):
            topic_count = read_question_count(driver, subject_code, topic_code)
            if topic_count is not None:
                save_question_count(
                    db_connection,
                    f"{subject_code}_{topic_code}",
                    topic_count,
                )
