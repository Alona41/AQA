import pytest
from unittest.mock import patch

@pytest.fixture
def mock_get_logger():
    with patch('homework_11.log_event.logging.getLogger') as mock_logger:
        yield mock_logger
