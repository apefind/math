all: update
new: clean update
install: update
	cp optimization.pdf ../doc
update: optimization.pdf
optimization.pdf:
	latexmk optimization.tex
clean:
	latexmk -c
run:
	#latexmk -pvc -e '$pdflatex=q/pdflatex %O -shell-escape %S/' -pdf
	latexmk -pvc -pdf optimization.tex
