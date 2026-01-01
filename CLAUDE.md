# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a novel writing project structured for collaborative fiction writing with Claude Code. The project uses Python automation scripts for manuscript management and word count tracking.

## Essential Commands

All commands use `make`:

- `make count` - Count words in all chapters and show progress toward novel length targets
- `make compile` - Compile all chapters into a single manuscript document (exports to `exports/compiled/`)
- `make track` - Track character appearances across all chapters (update character list in script)
- `make status` - Show git status
- `make test` - Test all scripts (runs word count)
- `make clean` - Remove compiled exports
- `make help` - Show all available commands

## Architecture

### Directory Structure

- **manuscript/chapters/** - Individual chapter markdown files (named `chapter_01.md`, `chapter_02.md`, etc.)
- **manuscript/outline.md** - Story structure and plot points
- **manuscript/scenes/drafts/** - Rough scene drafts before incorporation into chapters
- **worldbuilding/characters/** - Character profiles (protagonists.md, antagonists.md, supporting.md)
- **worldbuilding/locations/settings.md** - Setting descriptions
- **worldbuilding/timeline.md** - Chronological events
- **research/notes.md** - Research notes and references
- **scripts/** - Python automation tools for manuscript management
- **exports/compiled/** - Generated compiled manuscripts

### Python Scripts

1. **word_count.py** - Counts words in all chapters, filters out markdown headers, provides statistics and progress toward target word counts (40k-100k)
2. **compile_manuscript.py** - Combines all chapters in order into a single markdown document with title page and timestamps
3. **character_tracker.py** - Tracks character mentions across chapters (requires manual updates to character list in script)

### Chapter Format

Chapters are written in markdown. The compiler strips metadata sections between `---` delimiters if present.

## Development Workflow

1. **Update character list** in `scripts/character_tracker.py` when adding new characters
2. **Commit frequently** to save writing progress
3. **Use branches** for experimental rewrites
4. **Track progress** with `make count` to monitor word count goals
5. **Compile manuscript** regularly with `make compile` to review full story flow
6. **Check character consistency** using `make track` to ensure character appearances align with story needs

## Important Notes

- The character tracker requires manual updates to the `characters` list in the script
- Word counts exclude markdown headers and metadata
- Compiled manuscripts include timestamps for version tracking
- The project uses `python3` for all scripts