from pywinauto import Desktop

# 列出目前所有可見視窗
for window in Desktop(backend="uia").windows():
    try:
        print(repr(window.window_text()))
    except Exception:
        pass

"""
#-----------------------------------
# 列出特定視窗的所有可辨識控制項
from pywinauto import Desktop

window = Desktop(backend="uia").window(
    title_re=".*公司程式名稱.*"
)

window.wait("visible", timeout=10)
window.set_focus()

# 將所有可辨識的按鈕、輸入框、表格列出
window.print_control_identifiers()

#可能輸出項目
Button - '查詢'
Edit - '客戶編號'
DataGrid - '查詢結果'

#-----------------------------------
#輸入客戶編號並點擊查詢
from pywinauto import Desktop

window = Desktop(backend="uia").window(
    title_re=".*公司程式名稱.*"
)
window.wait("visible enabled ready", timeout=15)

# 輸入客戶編號
customer_field = window.child_window(
    title="客戶編號",
    control_type="Edit"
)
customer_field.set_edit_text("A123456")

# 點擊查詢
search_button = window.child_window(
    title="查詢",
    control_type="Button"
)
search_button.click_input()

#-----------------------------------
# 如果控制項有 auto_id
window.child_window(
    auto_id="txtCustomerNo",
    control_type="Edit"
).set_edit_text("A123456")

window.child_window(
    auto_id="btnSearch",
    control_type="Button"
).click_input()
#-------------------------------
# 如果 backend="uia" 看不到控制項，可以改用 backend="win32"
"""