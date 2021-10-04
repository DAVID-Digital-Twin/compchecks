## setup	: get and possibly install dependencies
.PHONY : setup
setup : venv rmlmapper tbox

## compcheck	: transform, simplify and check
.PHONY : compcheck
compcheck : transform simplify check

## rmlmapper	: fetch rmlmapper jar + function files from github
rmlmapper:
	TDIR="./src/transformation/";\
	if [ ! -d "$$TDIR" ]; then\
		echo "warning: no dir $$TDIR";\
		mkdir $$TDIR;\
	fi;\
	FDIR="./src/transformation/functions/";\
	if [ ! -d "$$FDIR" ]; then\
		echo "warning: no dir $$FDIR";\
		mkdir $$FDIR;\
	fi;\
	cd $$TDIR && { curl -LJO https://github.com/RMLio/rmlmapper-java/releases/download/v4.11.0/rmlmapper.jar ; cd -; };\
	cd $$FDIR && { curl -LJO https://raw.githubusercontent.com/FnOio/grel-functions-java/master/src/main/resources/grel_java_mapping.ttl ; };\
	{ curl -LJO https://github.com/RMLio/rmlmapper-java/raw/master/src/main/resources/GrelFunctions.jar ; };\
	{ curl -LJO https://raw.githubusercontent.com/RMLio/rmlmapper-java/master/src/main/resources/functions_grel.ttl ; cd -; }

## venv		: setup python venv and install dependencies
venv:
	python3 -m venv .venv;\
	.venv/bin/python -m pip install -r requirements.txt

## tbox		: get tbox from aas repo
tbox:
	ODIR="./src/specs/";\
	if [ ! -d "$$ODIR" ]; then\
		mkdir $$ODIR;\
	fi;\
	cd $$ODIR && { curl -LJO https://raw.githubusercontent.com/admin-shell-io/aas-specs/master/schemas/rdf/rdf-ontology.ttl ; } && { cat ontology-supplement.ttl >> rdf-ontology.ttl ; cd -; }

## transform	: transform example aas files
transform:
	cd src/ && bash xml2ttl.sh pump_directref.aas.xml friction_bearing.aas.xml && mv ../data/output.ttl ../data/_direct.ttl ;\
	bash xml2ttl.sh pump_eclassref.aas.xml friction_bearing.aas.xml && mv ../data/output.ttl ../data/_eclass.ttl

## simplify	: simplify example graphs
simplify:
	cd src/simplification && cp ../../data/*.ttl . && ../../.venv/bin/python rdflib_query_exec.py _direct.ttl _eclass.ttl && rm _direct.ttl _eclass.ttl && mv *.ttl ../../data

## check	: run compatibility checks
check:
	cd src/compatibility && bash check.sh


.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<

