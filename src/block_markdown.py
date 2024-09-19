def markdown_to_blocks(markdown):
    blocks = []

    split_text = markdown.split("\n\n")

    for block in split_text:
        if block != "":
            
            blocks.append(block.strip())

    return blocks