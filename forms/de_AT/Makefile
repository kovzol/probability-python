all: 0.pdf 1.pdf

0.pdf: 0.tex
	pdflatex 0.tex

1.pdf: 1.tex
	pdflatex 1.tex

clean:
	rm -f 0.log 0.aux 1.log 1.aux 1.out

fullclean: clean
	rm -f 0.pdf 1.pdf

.PHONY: clean fullclean all
