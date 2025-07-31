#!/bin/bash

# Script to convert all .md files to PDFs using pandoc
# with file exceptions

set -e  # Exit on any error

echo "Starting markdown to PDF conversion..."

# Define files to exclude (you can modify this array)
EXCLUDE_FILES=(
    "README.md"
    "to_do_list.md"
    "Useful_links.md"
    "model_comparison_by_task.md"
    "Ppai6_creative_use_cases.md"
    "matlab_example.md"
)

# Define patterns to exclude (you can modify this array)
EXCLUDE_PATTERNS=(
    "*Excel*"
    "*excel*"
    "*WIP*"
    ".*"  # Hidden files starting with dot
)

# Function to check if a file should be excluded
should_exclude() {
    local file="$1"
    local basename_file=$(basename "$file")
    
    # Check exact filename matches
    for exclude in "${EXCLUDE_FILES[@]}"; do
        if [ "$basename_file" = "$exclude" ]; then
            echo "Excluding (exact match): $file"
            return 0
        fi
    done
    
    # Check pattern matches
    for pattern in "${EXCLUDE_PATTERNS[@]}"; do
        if [[ "$basename_file" == $pattern ]]; then
            echo "Excluding (pattern match): $file"
            return 0
        fi
    done
    
    return 1
}

# Function to convert a single markdown file
convert_md_to_pdf() {
    local md_file="$1"
    local pdf_file="$2"
    
    echo "Converting: $md_file -> $pdf_file"
    
    pandoc "$md_file" \
        --lua-filter=include-files.lua \
        --number-sections \
        --filter pandoc-xnos \
        -V colorlinks=true \
        -V linkcolor=blue \
        --toc \
        --highlight-style=tango \
        --pdf-engine=pdflatex \
        -o "$pdf_file"
}

# Create main pdfs directory
mkdir -p pdfs

# Convert .md files in root directory
for md_file in *.md; do
    if [ -f "$md_file" ] && ! should_exclude "$md_file"; then
        base_name=$(basename "$md_file" .md)
        convert_md_to_pdf "$md_file" "pdfs/${base_name}.pdf"
    fi
done

# Process all docs directories (including nested ones)
find . -type d -name "docs" | while read -r docs_dir; do
    echo "Processing docs directory: $docs_dir"
    
    # Use find to get all .md files in this docs directory and its subdirectories
    find "$docs_dir" -name "*.md" -type f | while read -r md_file; do
        # Skip excluded files
        if should_exclude "$md_file"; then
            continue
        fi
        
        # Get relative path from the docs directory
        rel_path="${md_file#$docs_dir/}"
        
        # Get directory part and filename
        dir_part=$(dirname "$rel_path")
        base_name=$(basename "$rel_path" .md)
        
        # Create target directory structure
        # Map docs path to pdfs path
        if [ "$docs_dir" = "./docs" ]; then
            # Main docs directory -> pdfs
            if [ "$dir_part" = "." ]; then
                target_dir="pdfs"
            else
                target_dir="pdfs/$dir_part"
            fi
        else
            # Nested docs directory -> pdfs/path/to/parent
            parent_path="${docs_dir#./}"
            parent_path="${parent_path%/docs}"
            if [ "$dir_part" = "." ]; then
                target_dir="pdfs/$parent_path"
            else
                target_dir="pdfs/$parent_path/$dir_part"
            fi
        fi
        
        mkdir -p "$target_dir"
        
        # Convert file
        convert_md_to_pdf "$md_file" "$target_dir/${base_name}.pdf"
    done
done

echo "Conversion complete!"