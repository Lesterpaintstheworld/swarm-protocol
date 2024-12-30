#!/bin/bash

# Create/overwrite final_text.md
> final_text.md

# Add chapters from root directory in order
if [ -f chapter_1.md ]; then
    cat chapter_1.md >> final_text.md
    echo -e "\n\n" >> final_text.md
fi

if [ -f chapter_2.md ]; then
    cat chapter_2.md >> final_text.md
    echo -e "\n\n" >> final_text.md
fi

# Add chapters from final_text directory in order
for i in {3..10}; do
    if [ -f "final_text/chapter_$i.md" ]; then
        cat "final_text/chapter_$i.md" >> final_text.md
        echo -e "\n\n" >> final_text.md
    fi
done
