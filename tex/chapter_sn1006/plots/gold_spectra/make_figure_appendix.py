from glob import glob

imagetemplate = r'\includegraphics[width=0.7\textwidth, trim=0 0mm 0 10mm, clip]{chapter_sn1006/plots/gold_spectra/%s}' 
footer = r"""
\captcont{Fit of SN1006 candidate spectra}
   \label{fig:sn1006_candfit}
\end{figure}"""
header=r"""\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering""" + '\n'
latex_string = ""
i=0   
for plot in sort(glob('*.pdf')):
    if i == 0:
        latex_string+=header
    elif i%3 == 0:
        latex_string+=footer
        latex_string+=header
    latex_string += imagetemplate % plot + '\n'
    i+=1

latex_string+=footer    


file('images.tex', 'w').write(latex_string)