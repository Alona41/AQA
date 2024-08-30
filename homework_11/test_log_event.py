import logging
from homework_11.log_event import log_event


def test_log_success(caplog):
    with caplog.at_level(logging.INFO):
        log_event("user1", "success")

    assert "Login event - Username: user1, Status: success" in caplog.text


def test_log_expired(caplog):
    with caplog.at_level(logging.WARNING):
        log_event("user1", "expired")

    assert "Login event - Username: user1, Status: expired" in caplog.text


def test_log_failed(caplog):
    with caplog.at_level(logging.ERROR):
        log_event("user1", "failed")

    assert "Login event - Username: user1, Status: failed" in caplog.text

