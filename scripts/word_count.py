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
    # Get all chapter files
    manuscript_dir = Path(__file__).parent.parent / 'manuscript' / 'chapters'
    chapter_files = sorted(glob.glob(str(manuscript_dir / 'chapter_*.md')))
    
    if not chapter_files:
        print("No chapter files found!")
        return
    
    print("=" * 60)
    print("WORD COUNT REPORT")
    print("=" * 60)
    print()
    
    total_words = 0
    chapter_counts = []
    
    for chapter_file in chapter_files:
        words = count_words_in_file(chapter_file)
        chapter_name = os.path.basename(chapter_file)
        chapter_counts.append((chapter_name, words))
        total_words += words
        print(f"{chapter_name:30} {words:>8,} words")
    
    print()
    print("-" * 60)
    print(f"{'TOTAL':30} {total_words:>8,} words")
    print("-" * 60)
    print()
    
    # Statistics
    if chapter_counts:
        avg_words = total_words / len(chapter_counts)
        print(f"Average chapter length: {avg_words:,.0f} words")
        print(f"Total chapters: {len(chapter_counts)}")
        print()
        
        # Progress toward common novel lengths
        targets = {
            "Novella (40k)": 40000,
            "Short Novel (60k)": 60000,
            "Standard Novel (80k)": 80000,
            "Long Novel (100k)": 100000
        }
        
        print("Progress toward targets:")
        for name, target in targets.items():
            percentage = (total_words / target) * 100
            print(f"  {name:25} {percentage:>6.1f}%")
    
    print()
    print("=" * 60)

if __name__ == '__main__':
    main()