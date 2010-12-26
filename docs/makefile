spec/specification.pdf: spec/specification.tex
	pdflatex spec/specification.tex
	mv specification.* spec

view: spec/specification.pdf
	evince spec/specification.pdf

clean:
	rm spec/specification.pdf spec/specification.aux spec/specification.log
