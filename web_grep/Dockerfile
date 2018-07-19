FROM python:3
Add * /
ENV FILE_NAME=/product_total.xlsx
RUN pip3 install xlsxwriter
RUN pip3 install openpyxl
CMD [ "python3", "webgrep.py" ]
