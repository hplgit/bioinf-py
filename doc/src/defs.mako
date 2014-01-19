## Attempts to use mako functions (instead of python functions)
## but it did not work out

<%def name="primer_book_comment(text)">
% if PRIMER_BOOK:
${text}
% endif
</%def>

<%def name="primer_pbook_comment(text)">
% if PRIMER_BOOK and not EBOOK:
${text}
% endif
</%def>

<%def name="primer_ebook_comment(text)">
% if PRIMER_BOOK and EBOOK:
${text}
% endif
</%def>

<%def name="not_primer_book_comment(text)">
% if not PRIMER_BOOK:
${text}
% endif
</%def>
## Generate text for link to a source code file.
## Primer book: filename. (primer_src_dir is given early in the chapter.)
## Primer ebook: link to _static/filename and info on filename.
## Else: link to _static/filename.
## typical text: "...can be found in the file ${link('file', 'dir')}.

<%def name="link(filename)">
<%
urlbase = 'http://hplgit.github.com/bioinf-py/doc/tutorial/html/_static'
%>
## We use a backslash to swallow newline so that a period in the calling
## code can follow.
"${filename}": "${urlbase}/${filename}"\
% if PRIMER_BOOK and not EBOOK:
${filename}\
% elif PRIMER_BOOK and EBOOK:
"${filename}": "${urlbase}/${filename}"\
% elif not PRIMER_BOOK and FORMAT =='sphinx':
"${filename}": "_static/${filename}"\
% else:
% endif
</%def>
