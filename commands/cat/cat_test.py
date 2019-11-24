# Purpose
# Test for GNU/cat comparability

# Lessons learned
# * splitlines(keepends=True) mimics a filehandle line read

# TODO: write stdin test
# TODO: write file open test (sys.argvs)

import tempfile

import cat


def test_cat_basic_1line():
    filehandle_text = b"""This is a crazy file"""
    with tempfile.TemporaryFile() as filehandle:
        filehandle.write(filehandle_text)
        assert cat.basic(filehandle) == filehandle_text.splitlines(
            keepends=True
        )


def test_basic_newline():
    filehandle_text = b"""This is a crazy file\nanother line"""
    with tempfile.TemporaryFile() as filehandle:
        filehandle.write(filehandle_text)
        assert cat.basic(filehandle) == filehandle_text.splitlines(
            keepends=True
        )


def test_basic_newline_with_carriage_return():
    filehandle_text = b"""This is a crazy file\r\nanother line with \\r"""
    with tempfile.TemporaryFile() as filehandle:
        filehandle.write(filehandle_text)
        assert cat.basic(filehandle) == filehandle_text.splitlines(
            keepends=True
        )
