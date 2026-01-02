#!/usr/bin/env python3
"""
Manuscript Compilation Tool
Combines all chapters into a single document
"""

import os
import glob
from pathlib import Path
from datetime import datetime

def compile_manuscript(novel_name=None, output_format='md'):
    """Compile all chapters into a single manuscript"""
    
    import sys
    
    base_dir = Path(__file__).parent.parent
    novels_dir = base_dir / 'novels'
    output_dir = base_dir / 'exports' / 'compiled'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Determine which novel(s) to compile
    if novel_name or len(sys.argv) > 1:
        target_novel = novel_name or sys.argv[1]
        novels_to_compile = {target_novel: novels_dir / target_novel}
    else:
        # Compile all novels
        novel_dirs = [d for d in novels_dir.iterdir() if d.is_dir() and d.name.startswith('novel_')]
        novels_to_compile = {d.name: d for d in novel_dirs}
    
    if not novels_to_compile:
        print("No novel directories found!")
        return
    
    for novel_name, novel_dir in novels_to_compile.items():
        manuscript_dir = novel_dir / 'manuscript' / 'chapters'
        
        if not manuscript_dir.exists():
            print(f"No chapters found for {novel_name}")
            continue
        
        # Get all chapter files in order
        chapter_files = sorted(glob.glob(str(manuscript_dir / 'chapter_*.md')))
        
        if not chapter_files:
            print(f"No chapter files found in {novel_name}!")
            continue
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = output_dir / f'{novel_name}_{timestamp}.{output_format}'
        
        print(f"Compiling {novel_name}: {len(chapter_files)} chapters...")
        
        with open(output_file, 'w', encoding='utf-8') as outf:
            # Add title page
            novel_title = novel_name.replace('_', ' ').title().replace('Novel ', '')
            outf.write(f"# {novel_title}\n\n")
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
        
        print(f"✓ {novel_name} compiled successfully!")
        print(f"  Output: {output_file}")
    
    print(f"\nTotal novels compiled: {len(novels_to_compile)}")

if __name__ == '__main__':
    compile_manuscript()