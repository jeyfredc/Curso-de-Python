from flask import Flask, render_template, request, flash, redirect
from contact_model import Contact
from google.cloud import ndb

app = Flask(__name__)
app.secret_key = 'some_secret'
app.debug = True


@app.route(r'/', methods=['GET'])
def contact_book():
    client = ndb.Client()
    with client.context():
        contacts = Contact.query().fetch()
    return render_template('contact_book.html', contacts=contacts)


@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():
    
    if request.form:
        client = ndb.Client()
with client.context():
	    contact = Contact(name=request.form.get('name'), phone=request.form.get('phone'), email=request.form.get('email'))
	    contact.put()
	    flash('¡Se añadió el contacto!')

        return render_template('add_contact.html')


@app.route(r'/contacts/<uid>', methods=['GET'])
def contact_details(uid):
    client = ndb.Client()
    with client.context():
        contact = Contact.get_by_id(int(uid))

if not contact:
        return redirect('/', code=301)

return render_template('contact.html', contact=contact)

@app.route(r'/delete', methods=['POST'])
def delete_contact():
    client = ndb.Client()
    with client.context():
	    contact = Contact.get_by_id(int(request.form.get('uid')))
	    contact.key.delete()
    return redirect('/contacts/{}'.format(contact.key.id()))

if __name__ == '__main__':
    app.run()