segunda: EcDif2.pdf
EcDif2.pdf: edo2.txt
	python grafica2.py
edo2.txt: edo2.cpp
	c++ edo2.cpp
	./a.out > edo2.txt
	rm a.out

primera: EcDif.pdf
EcDif.pdf: edo.txt
	python grafica.py
edo.txt: edo.cpp
	c++ edo.cpp
	./a.out > edo.txt
	rm a.out

