# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a multi-novel fiction writing project structured for collaborative fiction writing with Claude Code. The project features interconnected stories across multiple worlds with shared cosmology, using Python automation scripts for manuscript management and word count tracking.

## Essential Commands

All commands use `make`:

- `make count` - Count words in all novels
- `make count NOVEL=novel_01_fantasy_tech` - Count words in specific novel
- `make compile` - Compile all novels into single documents
- `make compile NOVEL=novel_01_fantasy_tech` - Compile specific novel
- `make track` - Track character appearances across all chapters (update character list in script)
- `make status` - Show git status
- `make test` - Test all scripts (runs word count)
- `make clean` - Remove compiled exports
- `make help` - Show all available commands

## Architecture

### Directory Structure

- **novels/novel_*/manuscript/chapters/** - Individual chapter markdown files per novel
- **novels/novel_*/manuscript/outline.md** - Story structure and plot points per novel
- **novels/novel_*/manuscript/scenes/drafts/** - Rough scene drafts before incorporation into chapters
- **worldbuilding/characters/** - Character profiles shared across novels (protagonists.md, antagonists.md, supporting.md)
- **worldbuilding/locations/settings.md** - Setting descriptions shared across novels
- **worldbuilding/timeline.md** - Chronological events across all worlds
- **worldbuilding/cosmology.md** - Multi-world setup and ethereal being concept
- **research/notes.md** - Research notes and references
- **scripts/** - Python automation tools for manuscript management
- **exports/compiled/** - Generated compiled manuscripts

### Python Scripts

1. **word_count.py** - Counts words across all novels or specific novel, filters out markdown headers, provides statistics and series-wide word count tracking
2. **compile_manuscript.py** - Compiles each novel's chapters into separate markdown documents with title pages and timestamps
3. **character_tracker.py** - Tracks character mentions across all novels (requires manual updates to character list in script)

### Chapter Format

Chapters are written in markdown. The compiler strips metadata sections between `---` delimiters if present.

## Development Workflow

1. **Choose current novel** to work on from the `novels/` directory
2. **Update character list** in `scripts/character_tracker.py` when adding new characters
3. **Maintain cosmology consistency** in `worldbuilding/cosmology.md` across all novels
4. **Commit frequently** to save writing progress
5. **Use branches** for experimental rewrites of specific novels
6. **Track progress** with `make count` to monitor word count goals across all novels
7. **Compile manuscripts** regularly with `make compile` to review individual story flows
8. **Check character consistency** using `make track` to ensure character appearances align with story needs

## Important Notes

- The character tracker requires manual updates to the `characters` list in the script
- Word counts exclude markdown headers and metadata
- Each novel compiles into its own manuscript file with timestamps
- Worldbuilding files are shared across all novels for consistency
- The cosmology.md file defines the multi-world rules and ethereal being concept
- The project uses `python3` for all scripts