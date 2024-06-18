# I use this to write notes for PDFs in Obsidian
# PDF info
file_name = "Maarek - AWS Certified Cloud Practitioner" # don't add .pdf at the end
first_page = -1
last_page = -2
heading_level = "" # E.g., ### or ####

# print out file content
current_page = first_page
while current_page <= last_page:
    print(f"{heading_level} Page {current_page}")
    print(f"![[{file_name}.pdf#page={current_page}]]")
    print("- ")
    print("")
    print("")
    print("")
    print("")
    current_page = current_page + 1
