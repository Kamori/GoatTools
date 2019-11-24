alltests:
	$(MAKE) pythontests
	$(MAKE) gotests

pythontests:
	venv/bin/pytest 

gotests:
	go test ./...

readme:
	bash utilities/make_readme.bash