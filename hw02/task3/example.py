from slatgen import LatexDoc, LatexTable, LatexTableColBorderPreset, LatexTableRowBorderPreset, LatexTableJustificationPreset, LatexImage

doc = LatexDoc.article().use_package("graphicx")
doc = doc.into_env("center").as_paragraph(
    "This Is an example of paragraph generated with slatgen!").insert_content()

table_dataset = [["Col 1 shows Left Alignment", "Col 2", "ExtraExtraExtra Long Column", "Long Col", "Col 5"], 
                 [123, 1234567890, 0], 
                 ["H", "E", "L", "L", "O"]]

table = LatexTable.fixed("Table example").\
    with_col_preset(LatexTableColBorderPreset.separatedfirstcol).\
    with_row_preset(LatexTableRowBorderPreset.firstsingle).\
    with_jus_preset(LatexTableJustificationPreset.leftfirstcenterrest). \
    from_dataset(table_dataset)

doc = doc.as_table(table).insert_content()
image = LatexImage.fixed().with_caption("Image example").from_path("assets/example.jpeg")
doc = doc.as_image(image).insert_content()
doc.save_as("example.tex")
