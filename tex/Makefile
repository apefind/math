latex = pdflatex
latexopt = --shell-escape
nonstop = --interaction=nonstopmode
latexmk = latexmk
latexmkopt = -pdf -quiet
#latexmkopt = -pdf
continuous = -pvc
main = notes
sources = $(main).tex macros.tex frontpage.tex section-1.tex section-2.tex section-3.tex section-4.tex section-5.tex

all: doc
new: clean doc
doc: $(main).pdf
run:
	$(latexmk) $(latexmkopt) $(continuous) -pdflatex="$(latex) $(latexopt) $(nonstop) %O %S" $(main)
clean:
	$(latexmk) -c $(main)
	rm -f $(main).pdf $(main).pdfsync
	rm -rf *~ *.tmp _minted-build _minted-notes __latexindent_temp.tex
	rm -f *.pdf *.bbl *.blg *.aux *.end *.fls *.log *.out *.fdb_latexmk *.dvi *.ind *.fls *.md5
	rm -f *.idv *.4tc *.xref *.lg *.css *.idx *.auxlock *.dpth
$(main).pdf: $(main).tex $(sources)
	$(latexmk) $(latexmkopt) -pdflatex="$(latex) $(latexopt) %O %S" $(nonstop) $(main)
	$(latex) $(latexopt) $(main)
