#!/usr/bin/env python3
"""
Word Count Analysis Tool
Counts words in all chapter files and provides statistics
"""

import os
import glob
from pathlib import Path

def count_words_in_file(filepath):
    """Count words in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove markdown headers and metadata
            lines = [line for line in content.split('\n') 
                    if not line.startswith('#') and not line.startswith('**')]
            words = sum(len(line.split()) for line in lines)
            return words
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return 0

def main():
    # Check if a specific novel is provided, otherwise scan all novels
    import sys
    
    base_dir = Path(__file__).parent.parent
    novels_dir = base_dir / 'novels'
    
    if len(sys.argv) > 1:
        # Specific novel provided
        novel_name = sys.argv[1]
        manuscript_dir = novels_dir / novel_name / 'manuscript' / 'chapters'
        novels_to_process = {novel_name: manuscript_dir}
    else:
        # Process all novels
        novel_dirs = [d for d in novels_dir.iterdir() if d.is_dir() and d.name.startswith('novel_')]
        novels_to_process = {d.name: d / 'manuscript' / 'chapters' for d in novel_dirs}
    
    if not novels_to_process:
        print("No novel directories found!")
        return
    
    print("=" * 60)
    print("WORD COUNT REPORT - MULTI-NOVEL SERIES")
    print("=" * 60)
    print()
    
    series_total = 0
    
    for novel_name, manuscript_dir in novels_to_process.items():
        if not manuscript_dir.exists():
            print(f"No chapters found for {novel_name}")
            continue
            
        chapter_files = sorted(glob.glob(str(manuscript_dir / 'chapter_*.md')))
        
        if not chapter_files:
            print(f"No chapter files found in {novel_name}!")
            continue
        
        print(f"📚 {novel_name.replace('_', ' ').title()}")
        print("-" * 60)
        
        novel_total = 0
        chapter_counts = []
        
        for chapter_file in chapter_files:
            words = count_words_in_file(chapter_file)
            chapter_name = os.path.basename(chapter_file)
            chapter_counts.append((chapter_name, words))
            novel_total += words
            print(f"  {chapter_name:30} {words:>8,} words")
        
        print(f"  {'NOVEL TOTAL':30} {novel_total:>8,} words")
        
        if chapter_counts:
            avg_words = novel_total / len(chapter_counts)
            print(f"  Average chapter: {avg_words:,.0f} words")
        
        series_total += novel_total
        print()
    
    print("=" * 60)
    print(f"SERIES TOTAL: {series_total:>8,} words")
    print("=" * 60)

if __name__ == '__main__':
    main()