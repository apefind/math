LATEX = pdflatex
LATEXOPT = --shell-escape
NONSTOP = --interaction=nonstopmode
LATEXMK = latexmk
LATEXMKOPT = -pdf -quiet
CONTINUOUS = -pvc
MAIN = optimization
SOURCES = $(MAIN).tex Makefile macros.tex section-1.tex section-2.tex section-3.tex
FIGURES := $(shell find figures/* images/* -type f)

all: $(MAIN).pdf
.refresh:
	touch .refresh
$(MAIN).pdf: $(MAIN).tex .refresh $(SOURCES) $(FIGURES)
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) -pdflatex="$(LATEX) $(LATEXOPT) $(NONSTOP) %O %S" $(MAIN)
force:
	touch .refresh
	rm $(MAIN).pdf
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) -pdflatex="$(LATEX) $(LATEXOPT) %O %S" $(MAIN)
clean:
	$(LATEXMK) -C $(MAIN)
	rm -f $(MAIN).pdfsync
	rm -rf *~ *.tmp
	rm -f *.bbl *.blg *.aux *.end *.fls *.log *.out *.fdb_latexmk *.dvi *.ind *.fls
once:
	$(LATEXMK) $(LATEXMKOPT) -pdflatex="$(LATEX) $(LATEXOPT) %O %S" $(MAIN)

	$(LATEX) $(LATEXOPT) $(MAIN)
.PHONY: clean force once all
