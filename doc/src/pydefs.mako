## This file is not in current use.
## defs.mako defines similar functions and is include via
## the namespace tag.

<%
# This is Python code block.
# If this is copied into bioinf.do.txt it works as the functions
# in defs.mako, but those below are pure Python. I didn't get
# these Python functions to work when using namespace for "import"
# of functions.

# primer_book_comment allows easy insertion of comments when this
# text is used in the book A Primer for Scientific Programming with Python.
# Inserting ${primer_book_comment('(see Chapter~\ref{foo:bar})')} will
# result in text if PRIMER_BOOK is true, otherwise no text comes out.
#
# A companion function, not_primer_book_comment(text) can be used
# for printing text that will occur when parts of this document
# is not included in the Primer book.


def primer_book_comment(text):
    """A comment to appear in the Primer book only."""
    return text if PRIMER_BOOK else ''

def primer_pbook_comment(text):
    """A comment to appear in the Primer book only."""
    return text if PRIMER_BOOK and not EBOOK else ''

def primer_ebook_comment(text):
    """A comment to appear in the Primer book only."""
    return text if PRIMER_BOOK and EBOOK else ''

def not_primer_book_comment(text):
    """A comment to appear when the text is not included in the Primer book."""
    return text if not PRIMER_BOOK else ''


def link(filename, primer_src_dir=None):
    """
    Generate text for link to a source code file.
    Primer book: filename. (primer_src_dir is given early in the chapter.)
    Primer ebook: link to _static/filename and info on filename.
    Else: link to _static/filename.
    """
    # typical text: "...can be found in the file ${link('file', 'dir')}.
    urlbase = 'http://hplgit.github.com/bioinf-py/doc/tutorial/html/_static/'
    #s = not_primer_book_comment('"%s": "%s"' % (filename, '_static/' + filename))
    #s = not_primer_book_comment('"%s": "%s"' % (filename, urlbase + filename))
    s = not_primer_book_comment('`%s` ("download": "%s" or "online viewing": "%s")' % (filename, urlbase + filename, urlbase + filename + '.html'))
    s += primer_pbook_comment(filename)
    s += primer_ebook_comment('"%s": "%s"' % (filename, urlbase + filename))
    return s

%>
