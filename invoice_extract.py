import tabula

pdf_path = 'sample.pdf'
# pdf_path = 'https://sedl.org/afterschool/toolkits/science/pdf/ast_sci_data_tables_sample.pdf'
# pdf_path = 'ast_sci_data_tables_sample.pdf'
dfs = tabula.read_pdf(pdf_path,pages ='all')

print(len(dfs))