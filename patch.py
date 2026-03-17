import sys

def patch_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We will replace the copy block.
    # We want to change the slow cell-by-cell copy with a faster one that skips style copy for data rows
    
    old_code = """
            # Copiar dados com estilo
            for i, row in enumerate(linhas, start=2):
                for cell in row:
                    try:
                        col_idx = cell.column if isinstance(cell.column, int) else cell.col_idx
                        nova_cell = novo_ws.cell(row=i, column=col_idx, value=cell.value)
                        
                        # Otimização: Só copiar estilo se for estritamente necessário
                        if cell.has_style and cell.value is not None:
                            nova_cell.font = get_cached_style(cell, 'font')
                            nova_cell.border = get_cached_style(cell, 'border')
                            nova_cell.fill = get_cached_style(cell, 'fill')
                            nova_cell.number_format = cell.number_format
                            nova_cell.alignment = get_cached_style(cell, 'alignment')
                    except Exception as e_style:
                        pass
"""

    new_code = """
            # Copiar dados sem estilo para máxima performance de CPU e Memória
            for row in linhas:
                values = [cell.value for cell in row]
                novo_ws.append(values)
"""
    
    # We also need to fix the filter since append moves the max row down.
    old_filter = """
            # Ativar filtro na primeira linha
            ultima_coluna = novo_ws.max_column
            ultima_linha = novo_ws.max_row
            letra_ultima_coluna = get_column_letter(ultima_coluna)
            novo_ws.auto_filter.ref = f"A1:{letra_ultima_coluna}{ultima_linha}"
"""

    new_filter = """
            # Ativar filtro na primeira linha
            ultima_coluna = novo_ws.max_column
            ultima_linha = novo_ws.max_row
            if ultima_coluna > 0 and ultima_linha > 0:
                letra_ultima_coluna = get_column_letter(ultima_coluna)
                novo_ws.auto_filter.ref = f"A1:{letra_ultima_coluna}{ultima_linha}"
"""

    if old_code in content:
        content = content.replace(old_code, new_code)
        content = content.replace(old_filter, new_filter)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Patched successfully")
    else:
        print("Could not find block to patch")

if __name__ == '__main__':
    patch_file('processor.py')
