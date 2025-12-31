#!/usr/bin/env python3
"""
Character Tracker
Finds all character mentions across chapters
"""

import os
import glob
from pathlib import Path
from collections import defaultdict
import re

def extract_character_mentions(filepath, character_names):
    """Find mentions of characters in a file"""
    mentions = defaultdict(int)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            for name in character_names:
                # Count occurrences
                count = len(re.findall(r'\b' + re.escape(name.lower()) + r'\b', content))
                if count > 0:
                    mentions[name] = count
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    
    return mentions

def main():
    # Define your main characters (update this list!)
    characters = [
        "Elena",
        "Marcus", 
        "Dr. Chen",
        "Jason",
        "Rebecca"
    ]
    
    manuscript_dir = Path(__file__).parent.parent / 'manuscript' / 'chapters'
    chapter_files = sorted(glob.glob(str(manuscript_dir / 'chapter_*.md')))
    
    if not chapter_files:
        print("No chapter files found!")
        return
    
    print("=" * 70)
    print("CHARACTER APPEARANCE TRACKER")
    print("=" * 70)
    print()
    
    # Track appearances per chapter
    chapter_data = {}
    total_mentions = defaultdict(int)
    
    for chapter_file in chapter_files:
        chapter_name = os.path.basename(chapter_file)
        mentions = extract_character_mentions(chapter_file, characters)
        chapter_data[chapter_name] = mentions
        
        for char, count in mentions.items():
            total_mentions[char] += count
    
    # Display results
    print(f"{'Chapter':<30}", end='')
    for char in characters:
        print(f"{char:>12}", end='')
    print()
    print("-" * 70)
    
    for chapter, mentions in chapter_data.items():
        print(f"{chapter:<30}", end='')
        for char in characters:
            count = mentions.get(char, 0)
            if count > 0:
                print(f"{count:>12}", end='')
            else:
                print(f"{'—':>12}", end='')
        print()
    
    print("-" * 70)
    print(f"{'TOTAL':<30}", end='')
    for char in characters:
        print(f"{total_mentions[char]:>12}", end='')
    print()
    print()
    
    # Show character prominence
    print("Character prominence:")
    sorted_chars = sorted(total_mentions.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        print(f"  {char:15} {count:>5} mentions")
    
    print()
    print("=" * 70)

if __name__ == '__main__':
    main()