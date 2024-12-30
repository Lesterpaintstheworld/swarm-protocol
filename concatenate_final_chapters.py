import os
import glob

def concatenate_chapters():
    # Directory containing the chapters
    final_text_dir = "final_text"
    
    # Get all markdown files in the directory and sort them naturally
    chapter_files = sorted(glob.glob(os.path.join(final_text_dir, "chapter_*.md")), 
                         key=lambda x: int(x.split('chapter_')[1].split('.')[0]))
    
    # Create or overwrite the output file
    with open("combined_chapters.md", "w", encoding="utf-8") as outfile:
        # Iterate through each chapter file
        for chapter_file in chapter_files:
            print(f"Processing {chapter_file}...")
            
            # Read and write each chapter with a separator
            with open(chapter_file, "r", encoding="utf-8") as infile:
                content = infile.read()
                outfile.write(f"\n\n{'='*80}\n\n")  # Separator between chapters
                outfile.write(content)
                outfile.write("\n")  # Add newline at end of chapter

    print("Chapters have been combined into 'combined_chapters.md'")

if __name__ == "__main__":
    concatenate_chapters()
