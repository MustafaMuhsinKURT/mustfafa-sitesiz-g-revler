@app.route('/submit_form', methods=['POST'])
def submit_form():

    name = request.form['name']
    email = request.form['email']
  
    return render_template('form_result.html', name=name, email=email)
