from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import psycopg2


class menu_5():

    def __init__(self, ui, tab_event):

        # connect to database
        db = psycopg2.connect(dbname='cs421', user='cs421g29', host='comp421.cs.mcgill.ca', password='spinBike4!')

        if tab_event == 1:
            self.handle_tab(ui, db)
        elif tab_event == 2:
            self.handle_button(ui, db)
        elif tab_event == 0:
            self.handle_select(ui, db)



    def handle_tab(self, ui, db):
        cursor = db.cursor()
        # Perform select on the bike models
        cursor.execute("""SELECT  bmemail FROM  bikemanagers ;""")

        # fetch all the data
        query_result = cursor.fetchall()
        default = [('--SELECT EMAIL--',)]
        query_result = default + query_result

        # remove all items from the combobox before adding
        ui.Menu_5_comboBox.clear()
        # add item into combobox
        for email in query_result:
            ui.Menu_5_comboBox.addItem(email[0])

        # Get the column names
        cursor.execute("""select column_name from information_schema.columns where table_name = 'bikemanagers';""")
        # fetch column names
        column_names = cursor.fetchall()

        # get all bike data
        cursor.execute("""SELECT  * FROM  bikemanagers;""")
        # fetch all the data
        query_result = cursor.fetchall()

        # Add column information to the data
        column_names = [tuple([column_name[0] for column_name in column_names])]
        query_result = column_names + query_result

        # remove previous data from table
        ui.Menu_5_tableWidget.clear()

        # insert data into column
        for row_number, row_data in enumerate(query_result):
            ui.Menu_5_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                ui.Menu_5_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        # Close connection
        db.close()

    def handle_select(self, ui, db):

        # select query
        cursor = db.cursor()
        try:
            # I have no idea what this is, but you need for the changing label
            _translate = QtCore.QCoreApplication.translate
            # remove previous data from table
            ui.Menu_5_tableWidget.clear()
            # Get the column names
            cursor.execute("""select column_name from information_schema.columns where table_name = 'bikemanagers';""")
            # fetch column names
            column_names = cursor.fetchall()

            bm_email = str(ui.Menu_5_comboBox.currentText())
            if ui.Menu_5_comboBox.currentIndex():
                cursor.execute("""SELECT * FROM  bikemanagers  WHERE bmemail=%(bm_email)s ;""",
                               {'bm_email': bm_email})
            else:
                cursor.execute("""SELECT * FROM  bikemanagers;""")
            # fetch all the data
            query_result = cursor.fetchall()

            # Add column information to the data
            column_names = [tuple([column_name[0] for column_name in column_names])]
            query_result = column_names + query_result

            # insert data into column
            for row_number, row_data in enumerate(query_result):
                ui.Menu_5_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    ui.Menu_5_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        except Exception as err:
            ui.Menu_5_status_label_12.setText(_translate("MainWindow", str(err)))

        # Close connection
        db.close()

    def handle_button(self, ui, db):
        # I have no idea what this is, but you need for the changing label
        _translate = QtCore.QCoreApplication.translate
        # Errors
        errors = ["password can not be empty", ""]

        # read text from the text editor
        old_password = ui.Menu_5_lineEdit.text()
        new_password = ui.Menu_5_lineEdit_2.text()

        # get the selected value of the combobox
        bmemail = str(ui.Menu_5_comboBox.currentText())
        # alter/update query
        cursor = db.cursor()
        try:
            cursor.execute(""" UPDATE bikemanagers SET bmpassword = %(new_password)s WHERE bmemail = %(bmemail)s;;
                 """, {'new_password': new_password, 'bmemail': bmemail,})
            ui.Menu_5_status_label_12.setText(_translate("MainWindow", "Updated Successfully"))
            db.commit()

            # remove previous data from table
            ui.Menu_5_tableWidget.clear()
            # Get the column names
            cursor.execute("""select column_name from information_schema.columns where table_name = 'bikemanagers';""")
            # fetch column names
            column_names = cursor.fetchall()


            if ui.Menu_5_comboBox.currentIndex():
                cursor.execute("""SELECT * FROM  bikemanagers  WHERE bmemail=%(bm_email)s ;""",
                               {'bm_email': bmemail})
            # fetch all the data
            query_result = cursor.fetchall()

            # Add column information to the data
            column_names = [tuple([column_name[0] for column_name in column_names])]
            query_result = column_names + query_result

            # insert data into column
            for row_number, row_data in enumerate(query_result):
                ui.Menu_5_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    ui.Menu_5_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        except psycopg2.DataError as err:
            ui.Menu_5_status_label_12.setText(_translate("MainWindow", str(err)))
        except Exception as e:
            ui.Menu_5_status_label_12.setText(_translate("MainWindow", str(e)))

        # Close connection
        db.close()










