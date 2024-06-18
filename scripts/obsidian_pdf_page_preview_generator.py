# I use this to write notes for PDFs in Obsidian
# PDF info
file_name = "" # don't add .pdf at the end
first_slide = -1
last_slide = -2

# print out file content
current_slide = first_slide
while current_slide <= last_slide:
    print(f"![[{file_name}.pdf#page={current_slide}]]")
    print("- ")
    print("")
    print("")
    print("")
    print("")
    current_slide = current_slide + 1
