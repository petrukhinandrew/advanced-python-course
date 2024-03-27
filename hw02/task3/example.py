from slatgen import LatexDoc, LatexTable

doc = LatexDoc.article()
doc = doc.into_env("center").as_paragraph("hello, world!").insert_content()
doc.save_as("example.tex")