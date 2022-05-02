from openpyxl import *
from openpyxl.styles import *

def border(ws, cell_range):
    thin_left = Side(style="thin")
    thin_right = Side(style="thin")
    thin_top = Side(style="thin")
    thin_bottom = Side(style="thin")
    thick_left = Side(style="thick")
    thick_right = Side(style="thick")
    thick_top = Side(style="thick")
    thick_bottom = Side(style="thick")
    last_row = (cell_range.split(':'))[1][1:]
    last_col = (cell_range.split(':'))[1][0]
    first_row = (cell_range.split(':'))[0][1:]
    first_col = (cell_range.split(':'))[0][0]
    for row in ws[cell_range]:
        for cell in row:
            str_cell = str(cell).replace("<Cell 'Sheet'.", "").replace(">", "")
            if first_row != last_row:
                if str_cell[1:] == first_row:
                    cell.border = Border(top=thick_top, bottom=thin_bottom, left=thin_left, right=thin_right)
                    if str_cell[0] == first_col:
                        cell.border = Border(top=thick_top, left=thick_left, right=thin_right, bottom=thin_bottom)
                    elif str_cell[0] == last_col:
                        cell.border = Border(top=thick_top, right=thick_right, left=thin_left, bottom=thin_bottom)
                if str_cell[1:] == last_row:
                    cell.border = Border(bottom=thick_bottom, left=thin_left, right=thin_right, top=thin_top)
                    if str_cell[0] == first_col:
                        cell.border = Border(bottom=thick_bottom, left=thick_left, right=thin_right, top=thin_top)
                    elif str_cell[0] == last_col:
                        cell.border = Border(bottom=thick_bottom, right=thick_right, top=thin_top, left=thin_left)
                
                if str_cell[1:] != first_row and str_cell[1:] != last_row and str_cell[0] == first_col:
                    cell.border = Border(left=thick_left, bottom=thin_bottom, top=thin_top, right=thin_right)
                if str_cell[1:] != first_row and str_cell[1:] != last_row and str_cell[0] == last_col:
                    cell.border = Border(right=thick_right, bottom=thin_bottom, left=thin_left, top=thin_top)
            else:
                if first_col != last_col:
                    cell.border = Border(bottom=thick_bottom, top=thick_top, left=thin_left, right=thin_right)
                    if str_cell[0] == first_col:
                        cell.border = Border(bottom=thick_bottom, top=thick_top, left=thick_left, right=thin_right)
                    elif str_cell[0] == last_col:
                        cell.border = Border(bottom=thick_bottom, top=thick_top, left=thin_left, right=thick_right)
                else:
                    cell.border = Border(bottom=thick_bottom, top=thick_top, left=thick_left, right=thick_right)