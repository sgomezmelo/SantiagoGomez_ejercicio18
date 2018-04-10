EcDif.pdf: edo.txt
	python grafica.py
edo.txt: a.out
	./a.out > edo.txt
	rm a.out
a.out: edo.cpp
	c++ edo.cpp
