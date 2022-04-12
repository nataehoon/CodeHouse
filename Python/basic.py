from openpyxl import *
from openpyxl.styles import *
wb = Workbook()
ws = wb.active

ws.append(["No.", "Method", "Kind"])

ws["B2"] = "cv2.IMREAD_\n(이미지 색상 설정)"
ws["C2"] = "COLOR"
ws["C3"] = "GRAYSCALE"
ws["C4"] = "UNCHANGED"
ws.merge_cells("B2:B4")

ws["B5"] = "cv2.COLOR_BGR2GRAY (회색으로 이미지 변경)"
ws.merge_cells("B5:C5")

ws["B6"] = "cv2.LINE_\n(선 그릴때 선 스타일)"
ws["C6"] = 4
ws["C7"] = 8
ws["C8"] = "AA"
ws.merge_cells("B6:B8")

ws["B9"] = "cv2.FONT_\n(글꼴 종류)"
ws["C9"] = "HERSHEY_SIMPLEX"
ws["C10"] = "HERSHEY_PLAIN"
ws["C11"] = "HERSHEY_SCRIPT_SIMPLEX"
ws["C12"] = "HERSHEY_TRIPLEX"
ws["C13"] = "ITALC"
ws.merge_cells("B9:B13")

ws["B14"] = "cv2.INTER_\n(보간법)"
ws["C14"] = "AREA"
ws["C15"] = "CUBIC"
ws["C16"] = "LINEAR"
ws.merge_cells("B14:B16")

ws["B17"] = "cv2.ROTATE_\n(회전)"
ws["C17"] = "90_CLOCKWISE"
ws["C18"] = 180
ws["C19"] = "90_COUNTERCLOCKWISE"
ws.merge_cells("B17:B19")

ws["B20"] = "cv2.EVENT_\n(마우스 이벤트)\r\n"
ws["C20"] = "LBUTTONDOWN"
ws["C21"] = "LBUTTONDBLCLK"
ws["C22"] = "MOUSEWHEEL"
ws["C23"] = "MOUSEMOVE"
ws.merge_cells("B20:B23")

for i in range(1, ws.max_row):
    ws["A{}".format(i + 1)] = i

for i in range(1, ws.max_column + 1):
    row = ws.cell(row=1, column=i)
    row.font = Font(bold=True, size=15)

# a1 = ws["A1"]
# b1 = ws["B1"]
# c1 = ws["C1"]]

# a1.font = Font(bold=True, size=20)
# b1.font = Font(bold=True, size=20)
# c1.font = Font(bold=True, size=20)

thin_border = Border(left=Side(style="thin"), right=Side(style="thin"), bottom=Side(style="thin"), top=Side(style="thin"))

for row in ws.rows:
    for cell in row:
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = thin_border

ws.column_dimensions["A"].width = 7
ws.column_dimensions["B"].width = 25
ws.column_dimensions["C"].width = 20

ws.freeze_panes = "B2"
wb.save("Programing.xlsx")