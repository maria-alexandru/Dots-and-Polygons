PYTHON = python3
SCRIPT = menu.py

run:
	$(PYTHON) $(SCRIPT)

clean:
	rm -f *.pyc
	rm -rf __pycache__
