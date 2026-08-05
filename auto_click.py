import sys
from PySide6.QtWidgets import (
    QApplication,
    QTextEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QMessageBox
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 輸入範例")
        
        layout = QHBoxLayout()
        layout1 = QHBoxLayout()
        
        # 建立單行輸入框
        self.input_box = QTextEdit(self)
        self.input_box.setPlaceholderText("請在此輸入文字...")
        self.input_box.setFixedSize(150, 300)  # 設定固定大小
        layout.addWidget(self.input_box)
        
        # 建立按鈕
        self.button = QPushButton("開始報工", self)
        self.button.clicked.connect(self.get_input_text)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
    def get_input_text(self):
        text = self.input_box.toPlainText()
        lines = text.splitlines()

        data_list = []
        error_list = []

        for line_number, line in enumerate(lines, start=1):
            item = line.strip()  # 去除前後空白
            if not item: 
                continue  # 忽略空行

            if len(item) == 11:
                data_list.append(item)
            else:
                error_list.append({
                    "line": line_number,
                    "value": item,
                    "length": len(item)
                })

        # 偵測格式錯誤，若有錯誤則顯示警告訊息
        if error_list:
            error_messages = []

            for error in error_list:
                message = (
                    f"第 {error['line']} 行: "
                    f"{error['value']}"
                    f"({error['length']} 個字元)"
                )
                error_messages.append(message)

            warning_text = "\n".join(error_messages)

            QMessageBox.warning(
                self,
                "生管號輸入錯誤",
                f"以下生管號格式錯誤，請檢查輸入：\n\n{warning_text}"
            )

            return  # 停止執行，等待使用者修正輸入

        if not data_list:
            QMessageBox.information(
                self,
                "無符合條件的資料",
                "沒有符合條件的資料，請檢查輸入。"
            )
            return
        
        # 等待後續程序銜接
        # self.run_automation(data_list)

    def run_automation(self, data_list):
        failed_items = []
        warning_records = []

        # 執行期間避免重複按下按鈕或修改原始資料
        self.button.setEnabled(False)
        self.input_box.setReadOnly(True)

        try:
            try:
                # TODO（pywinauto）：連接公司程式，只需要連接一次
                company_window = ...

                # TODO（pywinauto）：等待公司程式視窗可見且可以操作
                # company_window.wait("visible enabled ready", timeout=10)
            except Exception as error:
                QMessageBox.critical(
                    self,
                    "無法連接公司程式",
                    (
                        "無法連接公司程式，請確認程式已開啟，"
                        "且 Python 與公司程式的權限一致。\n\n"
                        f"錯誤內容：{error}"
                    )
                )
                return

            for index, item in enumerate(data_list):
                warning_appeared = False
                warning_message = ""

                try:
                    # TODO（pywinauto）：取得公司程式的輸入欄位
                    company_input = ...

                    # TODO（pywinauto）：輸入目前這筆資料
                    company_input.set_edit_text(item)

                    # TODO（pywinauto）：第一次 Enter
                    company_input.type_keys("{ENTER}")

                    # TODO（pywinauto）：在限定時間內判斷是否出現警告視窗
                    warning_appeared = ...

                    if warning_appeared:
                        # TODO（pywinauto）：取得公司警告視窗
                        warning_window = ...

                        # TODO（pywinauto）：擷取公司警告視窗的訊息
                        warning_message = ...

                        # TODO（pywinauto）：按 Enter 關閉公司警告視窗
                        warning_window.type_keys("{ENTER}")

                        # TODO（pywinauto）：等待公司警告視窗完全消失
                        # warning_window.wait_not("visible", timeout=5)

                        # TODO（pywinauto）：警告關閉後重新取得輸入欄位
                        company_input = ...

                        # TODO（pywinauto）：清空公司程式中報錯的資料
                        company_input.set_edit_text("")

                        # TODO（pywinauto）：確認輸入欄位已經清空
                        input_is_empty = ...
                        if not input_is_empty:
                            raise RuntimeError("公司程式的輸入欄位無法清空")
                    else:
                        # TODO（pywinauto）：沒有警告才按第二次 Enter
                        company_window.type_keys("{ENTER}")

                        # TODO（pywinauto）：等待公司程式處理完成，
                        # 並確認已回到可以輸入下一筆資料的狀態
                        next_item_ready = ...
                        if not next_item_ready:
                            raise TimeoutError("等待公司程式處理完成逾時")

                except Exception as error:
                    # 技術性錯誤時，公司程式狀態不確定，因此停止整批。
                    # 保留先前的業務失敗資料、目前資料及尚未執行資料。
                    remaining_items = failed_items + data_list[index:]
                    self.input_box.setPlainText("\n".join(remaining_items))

                    QMessageBox.critical(
                        self,
                        "自動化執行錯誤",
                        (
                            f"處理以下資料時發生技術性錯誤：\n"
                            f"{item}\n\n"
                            f"錯誤內容：{error}\n\n"
                            "目前資料與尚未執行的資料已保留。"
                        )
                    )
                    return

                if warning_appeared:
                    # 公司業務警告已安全關閉並清空輸入欄，記錄後繼續下一筆
                    failed_items.append(item)
                    warning_records.append({
                        "value": item,
                        "message": str(warning_message)
                    })

                # TextEdit 保留已失敗資料與尚未執行資料；成功資料會被移除
                remaining_items = failed_items + data_list[index + 1:]
                self.input_box.setPlainText("\n".join(remaining_items))

                # 讓同步執行期間的 TextEdit 更新能顯示出來
                QApplication.processEvents()

            if warning_records:
                warning_lines = []

                for record in warning_records:
                    warning_lines.append(
                        f"{record['value']}：{record['message']}"
                    )

                warning_summary = "\n".join(warning_lines)
                success_count = len(data_list) - len(failed_items)

                QMessageBox.warning(
                    self,
                    "執行完成，但部分資料失敗",
                    (
                        f"成功：{success_count} 筆\n"
                        f"失敗：{len(failed_items)} 筆\n\n"
                        f"失敗明細：\n{warning_summary}"
                    )
                )
            else:
                # 全部成功時，TextEdit 會保持清空狀態
                QMessageBox.information(
                    self,
                    "執行完成",
                    f"全部 {len(data_list)} 筆資料執行成功。"
                )
        finally:
            self.input_box.setReadOnly(False)
            self.button.setEnabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
