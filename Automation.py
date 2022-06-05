# Применение функции к одному файлу Excel
automate_excel('sales_january.xlsx')
automate_excel('sales_february.xlsx')
automate_excel('sales_march.xlsx')
# сначала объединить эти три отчета с помощью pd.concat(), а затем применить функцию только один раз.
# читать эксель файлы
excel_file_1 = pd.read_excel('sales_january.xlsx')
excel_file_2 = pd.read_excel('sales_february.xlsx')
excel_file_3 = pd.read_excel('sales_march.xlsx')
# объединить файлы
new_file = pd.concat([excel_file_1,
                      excel_file_2,
                      excel_file_3], ignore_index=True)
# файл экспорта
new_file.to_excel('sales_2021.xlsx')
# применить функцию
automate_excel('sales_2021.xlsx')
