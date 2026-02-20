@app.route('/submit_form', methods=['POST'])
def submit_form():
   
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    with open('form.txt', 'a', encoding='utf-8') as f:
        f.write(f"İsim: {name}\n")
        f.write(f"E-posta: {email}\n")
        f.write(f"Adres: {address}\n")
        f.write(f"Tarih: {date}\n")
        f.write("-" * 20 + "\n") 

    return render_template('form_result.html', 
                           name=name, 
                           email=email, 
                           address=address, 
                           date=date)
