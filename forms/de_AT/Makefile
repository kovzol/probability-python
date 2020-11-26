all: 0.pdf 1.pdf 2.pdf 3.pdf

0.pdf: 0.tex
	pdflatex 0.tex

1.pdf: 1.tex main-py-window.png ../../progs/de_AT/1.py
	pdflatex 1.tex

2.pdf: 2.tex ../../progs/de_AT/2.py
	pdflatex 2.tex

3.pdf: 3.tex ../../progs/de_AT/3.py
	pdflatex 3.tex

clean:
	rm -f 0.log 0.aux 1.log 1.aux 1.out 2.log 2.aux 2.out 3.log 3.aux 3.out

fullclean: clean
	rm -f 0.pdf 1.pdf 2.pdf 3.pdf

.PHONY: clean fullclean all
