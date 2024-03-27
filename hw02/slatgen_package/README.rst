# slatgen - Simplified LaTeX Generator

*Remark:* even though it had to be just a couple of functions to generate tables and images by provided data or file path, now it is a couple of classes with way more functions to let user customize result

## Usage

*Essential:* module provides LINQ-like syntax. It means that user may "chain" method calls (see example). Also, there are public constructors for all main classes, but we do not suggest using it.

### LatexDoc class

Currently, the only supported `\documentclass` is `article`. It can be created with `LatexDoc.article()`.

Here, we assume that `doc` is an instance of `LatexDoc` class

Extra packages may be added with `doc.use_package("package_name")`

You may add paragraph with `doc.as_paragraph("some text")` or add raw latex text with `doc.as_raw("latex text")`

If you want to wrap your input with environment such as `center`, use `doc.into_env("env_name")`. Arguments for the env can be put with `doc.into_env("env_name").with_args("args")`. Only one string of arguments currently supported.


Add `doc.insert_content()` to insert the content and environmetns you added into latex body.

The only method that does not return `LatexDoc` instance is `.save_as("output_path")`. This method wont create new dir's whilst may create a new file

### LatexTable class

Table may be created with `LatexTable.fixed()` or `LatexTable.floating()`: floating may stick to the top of the page no matter where it was put in LaTeX output 

Table may be inserted into doc with `doc.as_table(table).insert_content()`

See the example to find all the methods of class

### LatexImage class