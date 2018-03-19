from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import psycopg2


class menu_4():

    def __init__(self, ui, tab_event):

        # connect to database
        db = psycopg2.connect(dbname='cs421', user='cs421g29', host='comp421.cs.mcgill.ca', password='spinBike4!')

        if tab_event:
            self.handle_tab(ui, db)
        else:
            self.handle_select(ui, db)



    def handle_tab(self, ui, db):
        cursor = db.cursor()
        # Perform select on the bike models
        cursor.execute("""SELECT  Distinct bmemail FROM  tickets ;""")

        # fetch all the data
        query_result = cursor.fetchall()
        default = [('--SELECT EMAIL--',)]
        query_result = default + query_result

        # remove all items from the combobox before adding
        ui.Menu_4_comboBox.clear()
        # add item into combobox
        for email in query_result:
            ui.Menu_4_comboBox.addItem(email[0])

        # Get the column names
        cursor.execute("""select column_name from information_schema.columns where table_name = 'tickets';""")
        # fetch column names
        column_names = cursor.fetchall()

        # get all bike data
        cursor.execute("""SELECT  * FROM  tickets WHERE is_solved='No';""")
        # fetch all the data
        query_result = cursor.fetchall()

        # Add column information to the data
        column_names = [tuple([column_name[0] for column_name in column_names])]
        query_result = column_names + query_result

        # remove previous data from table
        ui.Menu_4_tableWidget.clear()

        # insert data into column
        for row_number, row_data in enumerate(query_result):
            ui.Menu_4_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                ui.Menu_4_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        # Close connection
        db.close()


    def handle_select(self, ui, db):

        # select query
        cursor = db.cursor()
        try:
            # I have no idea what this is, but you need for the changing label
            _translate = QtCore.QCoreApplication.translate
            # remove previous data from table
            ui.Menu_4_tableWidget.clear()
            # Get the column names
            cursor.execute("""select column_name from information_schema.columns where table_name = 'tickets';""")
            # fetch column names
            column_names = cursor.fetchall()

            bm_email = str(ui.Menu_4_comboBox.currentText())
            if ui.Menu_4_comboBox.currentIndex():
                cursor.execute("""SELECT * FROM  tickets  WHERE bmemail=%(bm_email)s AND  is_solved='No';""", {'bm_email': bm_email})
            else:
                cursor.execute("""SELECT * FROM  tickets WHERE is_solved='No';""")
            # fetch all the data
            query_result = cursor.fetchall()

            # Add column information to the data
            column_names = [tuple([column_name[0] for column_name in column_names])]
            query_result = column_names + query_result

            # insert data into column
            for row_number, row_data in enumerate(query_result):
                ui.Menu_4_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    ui.Menu_4_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        except Exception as e:
            print(str(e))

        # Close connection
        db.close()














