import tempfile

from goattools_python import tac


def test_basic_1line():
    filehandle_text = b"""This is a crazy file"""
    with tempfile.TemporaryFile() as filehandle:
        filehandle.write(filehandle_text)
        assert tac.basic(filehandle) == filehandle_text.splitlines(keepends=True)[::-1]


def test_basic_newline():
    filehandle_text = b"""This is a crazy file\nanother line"""
    with tempfile.TemporaryFile() as filehandle:
        filehandle.write(filehandle_text)
        assert tac.basic(filehandle) == filehandle_text.splitlines(keepends=True)[::-1]


def test_basic_newline_with_carriage_return():
    filehandle_text = b"""This is a crazy file\r\nanother line with \\r"""
    with tempfile.TemporaryFile() as filehandle:
        filehandle.write(filehandle_text)
        assert tac.basic(filehandle) == filehandle_text.splitlines(keepends=True)[::-1]
