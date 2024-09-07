import openpyxl


workbook = openpyxl.load_workbook('alunosSAB11H.xlsx')



sheet_alunos =  workbook ['Alunos']
ff

for linha in sheet_alunos.iter_rows(min_row=2):
  print(linha[0].value)