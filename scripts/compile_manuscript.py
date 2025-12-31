#!/usr/bin/env python3
"""
Manuscript Compilation Tool
Combines all chapters into a single document
"""

import os
import glob
from pathlib import Path
from datetime import datetime

def compile_manuscript(output_format='md'):
    """Compile all chapters into a single manuscript"""
    
    manuscript_dir = Path(__file__).parent.parent / 'manuscript' / 'chapters'
    output_dir = Path(__file__).parent.parent / 'exports' / 'compiled'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get all chapter files in order
    chapter_files = sorted(glob.glob(str(manuscript_dir / 'chapter_*.md')))
    
    if not chapter_files:
        print("No chapter files found!")
        return
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = output_dir / f'manuscript_{timestamp}.{output_format}'
    
    print(f"Compiling {len(chapter_files)} chapters...")
    
    with open(output_file, 'w', encoding='utf-8') as outf:
        # Add title page
        outf.write("# [YOUR NOVEL TITLE]\n\n")
        outf.write("by [Your Name]\n\n")
        outf.write(f"Compiled: {datetime.now().strftime('%B %d, %Y')}\n\n")
        outf.write("---\n\n")
        outf.write("\n\n")
        
        # Compile chapters
        for i, chapter_file in enumerate(chapter_files, 1):
            print(f"  Adding Chapter {i}...")
            with open(chapter_file, 'r', encoding='utf-8') as inf:
                content = inf.read()
                # Remove metadata section if present
                if '---' in content:
                    parts = content.split('---')
                    if len(parts) > 2:
                        content = '---'.join(parts[2:])
                
                outf.write(content)
                outf.write("\n\n")
                # Add page break for next chapter
                outf.write("\n---\n\n")
    
    print(f"\nManuscript compiled successfully!")
    print(f"Output: {output_file}")
    print(f"Total chapters: {len(chapter_files)}")

if __name__ == '__main__':
    compile_manuscript()