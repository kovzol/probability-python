all: 0.pdf 1.pdf 2.pdf 3.pdf 4.pdf 5.pdf 6.pdf 7.pdf

0.pdf: 0.tex
	pdflatex 0.tex

1.pdf: 1.tex main-py-window.png ../../progs/de_AT/1.py
	pdflatex 1.tex

2.pdf: 2.tex ../../progs/de_AT/2.py
	pdflatex 2.tex

3.pdf: 3.tex ../../progs/de_AT/3.py
	pdflatex 3.tex

4.pdf: 4.tex ../../progs/de_AT/4.py
	pdflatex 4.tex

5.pdf: 5.tex ../../progs/de_AT/5a.py ../../progs/de_AT/5b.py
	pdflatex 5.tex

6.pdf: 6.tex ../../progs/de_AT/6a.py ../../progs/de_AT/6b.py ../../progs/de_AT/6c.py
	pdflatex 6.tex

7.pdf: 7.tex ../../progs/de_AT/7a.py ../../progs/de_AT/7b.py
	pdflatex 7.tex

clean:
	rm -f 0.log 0.aux 1.log 1.aux 1.out 2.log 2.aux 2.out 3.log 3.aux 3.out \
	    4.log 4.aux 4.out 5.log 5.aux 5.out 6.log 6.aux 6.out 7.log 7.aux 7.out

fullclean: clean
	rm -f 0.pdf 1.pdf 2.pdf 3.pdf 4.pdf 5.pdf 6.pdf 7.pdf

.PHONY: clean fullclean all
