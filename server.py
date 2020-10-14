from flask import Flask, render_template,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
	return render_template('certificate.html')

#----------------Searching the Participant detail--------------------
def read_from_csv(data):
    with open('./static/files/participant_list.csv', mode='r') as db_list:     ##--------Change the file name accordingly--------##
        reader = csv.reader(db_list)
        for row in reader:  
            if data in row: #checks the email id in the list
                return row  # returns the whole detail of participant


#----------------Collecting the Participant details and certificate no.--------------------
@app.route('/download', methods=['POST', 'GET'])
def download():
    if request.method == 'POST':
        email = request.form['email_id']
        part_data = read_from_csv(email)   # getting the participant details

        if part_data != None:  # condition if the user inputs wrong email
            l = len(part_data)
            # name = part_data[1]     # Second column in the list is name   ##--------Change the column number for name accordingly--------##
            # parti_name = name.title()
            cert_no = part_data[l-1] # Last column in the list is certificate number
            return render_template('/download.html',certi=cert_no)   # redirecting to download the certificate
        else:
            return render_template('rf_certificate.html')  # redirecting to enter details again
        		


