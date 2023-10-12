import pytest
from ETL import read_raw_data


def test_read_raw_data():
    with pytest.raises(FileExistsError):
        read_raw_data('wrongpath')
