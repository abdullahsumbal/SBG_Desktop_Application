from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import psycopg2


class menu_3():

    def __init__(self, ui, tab_event):

        # connect to database
        db = psycopg2.connect(dbname='cs421', user='cs421g29', host='comp421.cs.mcgill.ca', password='spinBike4!')

        if tab_event:
            self.handle_tab(ui, db)
        else:
            self.handle_button(ui, db)


    def handle_tab(self, ui, db):
        cursor = db.cursor()
        # Perform select on the bike models
        cursor.execute("""SELECT  Distinct brand_model FROM  spinbike ;""")

        # fetch all the data
        query_result = cursor.fetchall()
        print(query_result)
        for model in query_result:
            ui.Menu_3_comboBox.addItem(model[0])

        # Get the column names
        cursor.execute("""select column_name from information_schema.columns where table_name = 'booking';""")
        # fetch column names
        column_names = cursor.fetchall()

        # get all bike data
        cursor.execute("""SELECT  * FROM  spinbike ;""")
        # fetch all the data
        query_result = cursor.fetchall()

        # Add column information to the data
        column_names = [tuple([column_name[0] for column_name in column_names])]
        query_result = column_names + query_result

        # insert data into column
        for row_number, row_data in enumerate(query_result):
            ui.Menu_3_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                ui.Menu_3_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        # Close connection
        db.close()

    def handle_button(self, ui, db):
        # I have no idea what this is, but you need for the changing label
        _translate = QtCore.QCoreApplication.translate
        # Errors
        errors = ["Serial Number is not in digits", "Serial_Number is already exists", ""]

        # read text from the text editor
        serial_number = ui.Menu_3_lineEdit.text()

        # get date time
        last_batter_change_time = ui.Menu_3_dateTimeEdit.dateTime().toPyDateTime()

        # get has collector data
        has_datacollector = "Yes"
        if ui.Menu_3_checkBox.checkState() == 0:
            has_datacollector = "No"
        else:
            has_datacollector = "Yes"

        # Get the Selected model of the bike
        brand_model = ui.Menu_3_comboBox.currentText()

        # insert query
        cursor = db.cursor()
        try:
            cursor.execute("""INSERT INTO spinbike (serial_no, brand_model, last_battery_charge_time, has_datacollector)
                 VALUES (%(serial_number)s, %(brand_model)s, %(date)s, %(has_datacollector)s);
                 """, {'serial_number': serial_number, 'brand_model': brand_model, 'date': last_batter_change_time,
                       'has_datacollector': has_datacollector})
            ui.Menu_3_label_error.setText(_translate("MainWindow", ""))
            db.commit()

            # remove previous data from table
            ui.Menu_3_tableWidget.clear()
            # Get the column names
            cursor.execute("""select column_name from information_schema.columns where table_name = 'booking';""")
            # fetch column names
            column_names = cursor.fetchall()

            # get all bike data
            cursor.execute("""SELECT  * FROM  spinbike ;""")
            # fetch all the data
            query_result = cursor.fetchall()

            # Add column information to the data
            column_names = [tuple([column_name[0] for column_name in column_names])]
            query_result = column_names + query_result

            # insert data into column
            for row_number, row_data in enumerate(query_result):
                ui.Menu_3_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    ui.Menu_3_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except psycopg2.DataError as err:
            ui.Menu_3_label_error.setText(_translate("MainWindow", str(err)))
        except Exception as e:
            ui.Menu_3_label_error.setText(_translate("MainWindow", str(e)))

        # Close connection
        db.close()












