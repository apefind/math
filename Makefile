all: update
new: clean update
install: update
	cp optimization.pdf ../docs
update: optimization.pdf
optimization.pdf: optimization.tex macros.tex frontpage.tex section-1.tex
	pdflatex optimization.tex
	makeindex optimization.idx
	pdflatex optimization.tex
	latex_count=5 ; \
	while egrep -s 'Rerun (LaTeX|to get cross-references right)' optimization.log && [ $$latex_count -gt 0 ]; do \
	      echo "Rerunning latex...." ;\
	      pdflatex optimization.tex;\
	      latex_count=`expr $$latex_count - 1`;\
	    done
clean:
	rm -f *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *.pdf *.fls *.fdb_latexmk
