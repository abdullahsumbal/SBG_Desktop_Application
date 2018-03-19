from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import psycopg2
import matplotlib.pyplot as plt


class menu_1():

    def __init__(self, ui):

        # connect to database
        db = psycopg2.connect(dbname='cs421', user='cs421g29', host='comp421.cs.mcgill.ca', password='spinBike4!')
        cursor = db.cursor()

        # Perform select query on booking table
        title = ""
        if ui.Menu_1_radioButton.isChecked():

            cursor.execute("SELECT p.address, blh.serial_no, count(spu.duration) as Number_Of_Users FROM bike_location_history blh, spin_bike_usage spu, places p " \
                           "WHERE blh.serial_no=spu.serial_no AND blh.place_id=p.place_id " \
                           "GROUP BY p.address, blh.serial_no ORDER BY Number_Of_Users DESC")
            column_names = [('Building Name', 'serial_no', 'Total_Users')]
            title = " Number of user "
        else:
            cursor.execute("SELECT p.address, blh.serial_no, sum(spu.duration) as Duration FROM  bike_location_history blh, spin_bike_usage spu, places p " \
                           "WHERE blh.serial_no=spu.serial_no AND blh.place_id=p.place_id " \
                           "GROUP BY p.address, blh.serial_no ORDER BY Duration DESC")
            column_names = [('Building Name', 'serial_no', 'Total_Duration')]
            title = " Duration of Bike Use"

        # fetch all the data
        query_result = cursor.fetchall()

        # remove previous data from table
        ui.Menu_1_tableWidget.clear()

        # Add column information to the data
        query_result = column_names + query_result

        # insert data into column
        names_of_buidlings = []
        dur_no = []
        for row_number, row_data in enumerate(query_result):
            ui.Menu_1_tableWidget.insertRow(row_number)
            names_of_buidlings.append(str(row_data[0])+ " " +str(row_data[1]))
            dur_no.append(row_data[2])
            for column_number, data in enumerate(row_data):
                ui.Menu_1_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


        # Plotting
        x_axis = names_of_buidlings.pop(0)
        y_axis = dur_no.pop(0)
        plt.title(title)
        plt.ylabel(y_axis)
        plt.xlabel(x_axis)
        plt.bar(names_of_buidlings, dur_no)
        plt.show()

        # close connection
        db.close()












