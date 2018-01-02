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
	latexmk -pvc -pdf optimization.tex
