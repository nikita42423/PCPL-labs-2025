import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    pytest.main(["-v"])
