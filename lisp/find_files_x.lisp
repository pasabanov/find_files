#!/usr/bin/sbcl --script
(dolist(a(cdr *posix-argv*))(dolist(f(directory a))(format t"~a~%"f)))