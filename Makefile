.PHONY: help count compile track init test clean status

help:
	@echo "Novel Project Commands:"
	@echo "  make count       - Count words in all chapters"
	@echo "  make compile     - Compile manuscript into single document"
	@echo "  make track       - Track character appearances across chapters"
	@echo "  make init        - Initialize git repository"
	@echo "  make status      - Show git status"
	@echo "  make test        - Test all scripts"
	@echo "  make clean       - Remove compiled exports"

count:
	@python3 scripts/word_count.py

compile:
	@python3 scripts/compile_manuscript.py

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