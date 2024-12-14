import pytest
from unittest import mock
from unittest.mock import patch, mock_open
import sys
import requests
import openai
from project import validate, scan, scrape, count_tokens, trim_tokens, sentiment  # replace 'project' with your module name

# Mock data for testing
mock_stocks_csv = """Symbol,Security
AAPL,Apple Inc.
MSFT,Microsoft Corp
GOOGL,Alphabet Inc."""
import pytest
from unittest import mock
from unittest.mock import patch, mock_open
import sys
import requests
import openai
from project import validate, scan, scrape, count_tokens, trim_tokens, sentiment  # replace 'project' with your module name

# Mock data for testing
mock_stocks_csv = """Symbol,Security
AAPL,Apple Inc.
MSFT,Microsoft Corp
GOOGL,Alphabet Inc."""

mock_search_results = [
    "https://www.example.com/article1",
    "https://www.example.com/article2"
]

mock_html_content = """
<html>
    <body>
        <article>Main content about investing in Apple Inc.</article>
    </body>
</html>
"""

mock_trimmed_content = "Main content about investing in Apple Inc."

mock_sentiment_response = {
    "choices": [{
        "message": {
            "content": "Sentiment Analysis: Buy Apple Inc. because..."
        }
    }]
}

# Test for validate function
def test_validate(mocker):
    mocker.patch("builtins.open", mock_open(read_data=mock_stocks_csv))
    mocker.patch("sys.exit")
    validate("AAPL")
    sys.exit.assert_not_called()

    with pytest.raises(SystemExit):
        validate("XYZ")


# Test for scan function
@patch('project.search', return_value=mock_search_results)  # replace 'project' with your module name
def test_scan(mock_search):
    result = scan("Apple Inc.")
    assert len(mock_search_results) == 2
    assert isinstance(result, str)


# Test for scrape function
@patch("requests.get")
def test_scrape(mock_get):
    mock_response = mock.Mock()
    mock_response.text = mock_html_content
    mock_get.return_value = mock_response

    result = scrape(mock_search_results, "Apple Inc.")
    assert isinstance(result, str)
    assert "Sentiment Analysis" in result


# Test for count_tokens function
def test_count_tokens():
    assert count_tokens(mock_trimmed_content) > 0


# Test for trim_tokens function
def test_trim_tokens():import pytest
from unittest import mock
from unittest.mock import patch, mock_open
import sys
import requests
import openai
from project import validate, scan, scrape, count_tokens, trim_tokens, sentiment  # replace 'project' with your module name

# Mock data for testing
mock_stocks_csv = """Symbol,Security
AAPL,Apple Inc.
MSFT,Microsoft Corp
GOOGL,Alphabet Inc."""

mock_search_results = [
    "https://www.example.com/article1",
    "https://www.example.com/article2"
]

mock_html_content = """
<html>
    <body>
        <article>Main content about investing in Apple Inc.</article>
    </body>
</html>
"""

mock_trimmed_content = "Main content about investing in Apple Inc."

mock_sentiment_response = {
    "choices": [{
        "message": {
            "content": "Sentiment Analysis: Buy Apple Inc. because..."
        }
    }]
}

# Test for validate function
def test_validate(mocker):
    mocker.patch("builtins.open", mock_open(read_data=mock_stocks_csv))
    mocker.patch("sys.exit")
    validate("AAPL")
    sys.exit.assert_not_called()

    with pytest.raises(SystemExit):
        validate("XYZ")


# Test for scan function
@patch('project.search', return_value=mock_search_results)  # replace 'project' with your module name
def test_scan(mock_search):
    result = scan("Apple Inc.")
    assert len(mock_search_results) == 2
    assert isinstance(result, str)


# Test for scrape function
@patch("requests.get")
def test_scrape(mock_get):
    mock_response = mock.Mock()
    mock_response.text = mock_html_content
    mock_get.return_value = mock_response

    result = scrape(mock_search_results, "Apple Inc.")
    assert isinstance(result, str)
    assert "Sentiment Analysis" in result


# Test for count_tokens function
def test_count_tokens():
    assert count_tokens(mock_trimmed_content) > 0


# Test for trim_tokens function
def test_trim_tokens():
    trimmed_content = trim_tokens(mock_trimmed_content, 100)
    assert len(trimmed_content) <= 100


# Test for sentiment function
@patch('openai.ChatCompletion.create', return_value=mock_sentiment_response)
def test_sentiment(mock_openai):
    result = sentiment(mock_trimmed_content, "Apple Inc.")
    assert "Sentiment Analysis" in result

    trimmed_content = trim_tokens(mock_trimmed_content, 100)
    assert len(trimmed_content) <= 100


# Test for sentiment function
@patch('openai.ChatCompletion.create', return_value=mock_sentiment_response)
def test_sentiment(mock_openai):
    result = sentiment(mock_trimmed_content, "Apple Inc.")
    assert "Sentiment Analysis" in result

mock_search_results = [
    "https://www.example.com/article1",
    "https://www.example.com/article2"
]

mock_html_content = """
<html>
    <body>
        <article>Main content about investing in Apple Inc.</article>
    </body>
</html>
"""

mock_trimmed_content = "Main content about investing in Apple Inc."

mock_sentiment_response = {
    "choices": [{
        "message": {
            "content": "Sentiment Analysis: Buy Apple Inc. because..."
        }
    }]
}

# Test for validate function
def test_validate(mocker):
    mocker.patch("builtins.open", mock_open(read_data=mock_stocks_csv))
    mocker.patch("sys.exit")
    validate("AAPL")
    sys.exit.assert_not_called()

    with pytest.raises(SystemExit):
        validate("XYZ")


# Test for scan function
@patch('project.search', return_value=mock_search_results)  # replace 'project' with your module name
def test_scan(mock_search):
    result = scan("Apple Inc.")
    assert len(mock_search_results) == 2
    assert isinstance(result, str)


# Test for scrape function
@patch("requests.get")
def test_scrape(mock_get):
    mock_response = mock.Mock()
    mock_response.text = mock_html_content
    mock_get.return_value = mock_response

    result = scrape(mock_search_results, "Apple Inc.")
    assert isinstance(result, str)
    assert "Sentiment Analysis" in result


# Test for count_tokens function
def test_count_tokens():
    assert count_tokens(mock_trimmed_content) > 0


# Test for trim_tokens function
def test_trim_tokens():
    trimmed_content = trim_tokens(mock_trimmed_content, 100)
    assert len(trimmed_content) <= 100


mock_sentiment_response = {
    "choices": [{
        "message": {
            "content": "Sentiment Analysis: Buy Apple Inc. because..."
        }
    }]
}

@patch('openai.ChatCompletion.create', return_value=mock_sentiment_response)
def test_sentiment(mock_openai):
    result = sentiment(mock_trimmed_content, "Apple Inc.")
    assert "Sentiment Analysis" in result
