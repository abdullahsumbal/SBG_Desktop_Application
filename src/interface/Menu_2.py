from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import psycopg2


class menu_2():

    def __init__(self, ui):

        # I have no isea what this is, but you need for the changing label
        _translate = QtCore.QCoreApplication.translate

        # connect to database
        db = psycopg2.connect(dbname='cs421', user='cs421g29', host='comp421.cs.mcgill.ca', password='spinBike4!')
        cursor = db.cursor()

        # read text from the text editor
        user_email = ui.Menu_2_textEdit.toPlainText()

        # Get the column names
        cursor.execute("""select column_name from information_schema.columns where table_name = 'booking';""")
        # fetch column names
        column_names = cursor.fetchall()

        # Perform select query on booking table
        cursor.execute("""SELECT * FROM  booking  WHERE user_email=%(user_email)s;""",
                       {'user_email': user_email})

        # fetch all the data
        query_result = cursor.fetchall()

        # remove previous data from table
        ui.Menu_2_tableWidget.clear()

        # Error message
        if user_email == "":
            ui.Menu_2_label_2.setText(_translate("MainWindow", "Please type in the email"))
        elif query_result == []:
            ui.Menu_2_label_2.setText(_translate("MainWindow", "No Record found"))
        else:
            # No error
            ui.Menu_2_label_2.setText(_translate("MainWindow", ""))

            # Add column information to the data
            column_names = [tuple([column_name[0] for column_name in column_names])]
            query_result = column_names + query_result

            # insert data into column
            for row_number, row_data in enumerate(query_result):
                ui.Menu_2_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    ui.Menu_2_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))




