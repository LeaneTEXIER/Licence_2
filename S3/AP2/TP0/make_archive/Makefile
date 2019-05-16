# AP2 
# Makefile pour créer un projet

# Adaptez la variable en y portant votre ou vos noms
AUTHOR=Léane Texier


.PHONY: project clean

prj_%:
	mkdir $*
	sed -e 's/<PROJECT_NAME>/$*/g' \
	    -e 's/<AUTHOR>/$(AUTHOR)/g' conf.py.model > $*/conf.py
	sed -e 's/<PROJECT_NAME>/$*/g' Makefile.model > $*/Makefile
	cp -r images $*/
	mkdir $*/src
	mkdir $*/sourcedoc
	sed -e 's/<PROJECT_NAME>/$*/g' index.rst.model > $*/sourcedoc/index.rst

clean:
	rm -f *~ 
	rm -rf __pycache__

