# minimal examples

A collection of small code examples, which can be used for learning syntax and idiosyncrasies.

## latex

Currently contains mainly TikZ examples

### Creating pdfs and images

Prerequisites: `pdflatex` and `imagemagick`
Optional: `pngquant` for smaller PNGs

You can compile all the examples to pdf and png by executing the following command:

```
./build_script/latex/make.sh
```

It creates a folder `output/pdf` for the pdf files and a folder `output/img` for png files.

### Creating Anki flash cards

Use the command

```
./build_script/latex/make-anki.sh ANKI_USER > output.tsv
```

It writes TSV to output.tsv with the following columns 
1. result picture
2. description
3. code

It can be imported into Anki as follows (assuming you have already created an appropriate note type):

- "File -> Import...". 
- choose "Text separated by tabs or semicolons" and select output.tsv
- click on "Fields separated by" and enter "\t"
- select "Allow HTML in fields"
- assign the fields as stated above

