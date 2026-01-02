.PHONY: help count compile track init test clean status

help:
	@echo "LOTU - Multi-Novel Project Commands:"
	@echo "  make count           - Count words in all novels"
	@echo "  make count NOVEL=X   - Count words in specific novel"
	@echo "  make compile         - Compile all novels into single documents"
	@echo "  make compile NOVEL=X - Compile specific novel"
	@echo "  make track           - Track character appearances across chapters"
	@echo "  make init            - Initialize git repository"
	@echo "  make status          - Show git status"
	@echo "  make test            - Test all scripts"
	@echo "  make clean           - Remove compiled exports"

count:
	@if [ -n "$(NOVEL)" ]; then \
		python3 scripts/word_count.py $(NOVEL); \
	else \
		python3 scripts/word_count.py; \
	fi

compile:
	@if [ -n "$(NOVEL)" ]; then \
		python3 scripts/compile_manuscript.py $(NOVEL); \
	else \
		python3 scripts/compile_manuscript.py; \
	fi

track:
	@python3 scripts/character_tracker.py

init:
	@git init
	@git add .
	@git commit -m "Initial novel project structure"
	@echo "Git repository initialized!"

status:
	@git status

test: count
	@echo "All scripts tested successfully!"

clean:
	@rm -f exports/compiled/manuscript_*.md
	@echo "Compiled files removed."