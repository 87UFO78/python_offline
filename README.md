假設安裝檔放置在 D:\python_offline\whl
python.exe -m pip install --no-index --find-links=C:\python_offline\whl pandas numpy openpyxl PySide6 requests

驗證安裝
python.exe -c "import pandas, numpy, openpyxl, PySide6, requests; print('全部套件安装成功')"