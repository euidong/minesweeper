copy app.py app.pyw
pyinstaller --onefile --icon imgs/bomb.png app.pyw
del app.pyw
mkdir dist\imgs
copy imgs\* dist\imgs\*