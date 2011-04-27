(TeX-add-style-hook "chapter1"
 (lambda ()
    (LaTeX-add-labels
     "chap:one"
     "sec:foo"
     "sec:foobar"
     "sec:widgets")))

