#!/usr/bin/python
from flask import Flask, render_template,  request , flash , redirect, url_for , session
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField , validators , PasswordField

from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_security import UserMixin, RoleMixin



from Clinic import Clinic
from Disease import Disease

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('cred/oop-project-10172-firebase-adminsdk-mdj4v-50fe6e639c.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://oop-project-10172.firebaseio.com/ '
})

root = db.reference()


app = Flask(__name__)
app.config.update(
    DEBUG=False,
    SQLALCHEMY_DATABASE_URI='sqlite:///users.db',
    SECRET_KEY='James Bond',
    SECURITY_REGISTERABLE=True,
    SECURITY_PASSWORD_SALT = 'Some_salt',
)
db = SQLAlchemy(app)

Bootstrap(app)
Mail(app)
roles_users = db.Table('roles_users', db.Column('user_id', db.Integer(),
                                                db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
Security(app, user_datastore)

@app.route('/home')
def clinichome():
    return render_template('clinichome.html')

@app.route('/searchdisease')
def searchdisease():
    publications = root.child('publications').get()
    list = []  # create a list to store all the publication objects
    for pubid in publications:

        eachpublication = publications[pubid]

        if eachpublication['type'] == 'scli':
            print(eachpublication)
            clinic = Clinic(eachpublication['title'], eachpublication['type'],
                            eachpublication['address'], eachpublication['phone'],
                            eachpublication['openingHour'], eachpublication['busNo'], eachpublication['mrtStation'],
                            eachpublication['hospital'], eachpublication['created_by'], eachpublication['areaName'],
                            eachpublication['region'])
            print(eachpublication)
            clinic.set_pubid(pubid)
            print(clinic.get_pubid())
            list.append(clinic)

        else:
            print(eachpublication)
            disease = Disease(eachpublication['title'], eachpublication['type'], eachpublication['cause'],
                              eachpublication['symptom'],
                              eachpublication['treatment'], eachpublication['complication'],
                              eachpublication['specialist'],
                              eachpublication['created_by'])
            print(eachpublication['cause'])
            disease.set_pubid(pubid)
            list.append(disease)

    return render_template('searchdisease.html', publications=list)
@app.route('/searchclinic')
def searchclinic():
    publications = root.child('publications').get()
    list = []  # create a list to store all the publication objects
    for pubid in publications:

        eachpublication = publications[pubid]

        if eachpublication['type'] == 'scli':
            print(eachpublication)
            clinic = Clinic(eachpublication['title'], eachpublication['type'],
                            eachpublication['address'], eachpublication['phone'],
                            eachpublication['openingHour'], eachpublication['busNo'], eachpublication['mrtStation'],
                            eachpublication['hospital'], eachpublication['created_by'], eachpublication['areaName'],
                            eachpublication['region'])
            print(eachpublication)
            clinic.set_pubid(pubid)
            print(clinic.get_pubid())
            list.append(clinic)

        else:
            print(eachpublication)
            disease = Disease(eachpublication['title'], eachpublication['type'], eachpublication['cause'],
                              eachpublication['symptom'],
                              eachpublication['treatment'], eachpublication['complication'],
                              eachpublication['specialist'],
                              eachpublication['created_by'])
            print(eachpublication['cause'])
            disease.set_pubid(pubid)
            list.append(disease)

    return render_template('searchclinic.html', publications=list)







@app.route('/clinicinfo')
def clinicinfo():
    publications = root.child('publications').get()
    list = []  # create a list to store all the publication objects
    for pubid in publications:

        eachpublication = publications[pubid]

        if eachpublication['type'] == 'scli':
            print(eachpublication)
            clinic = Clinic(eachpublication['title'], eachpublication['type'],
                            eachpublication['address'], eachpublication['phone'],
                            eachpublication['openingHour'], eachpublication['busNo'], eachpublication['mrtStation'],
                            eachpublication['hospital'], eachpublication['created_by'], eachpublication['areaName'],
                            eachpublication['region'])
            print(eachpublication)
            clinic.set_pubid(pubid)
            print(clinic.get_pubid())
            list.append(clinic)

        else:
            print(eachpublication)
            disease = Disease(eachpublication['title'], eachpublication['type'], eachpublication['cause'],
                              eachpublication['symptom'],
                              eachpublication['treatment'], eachpublication['complication'],
                              eachpublication['specialist'],
                              eachpublication['created_by'])
            print(eachpublication['cause'])
            disease.set_pubid(pubid)
            list.append(disease)

    return render_template('clinicinfo.html', publications=list)

@app.route('/diseaseinfo')
def diseaseinfo():
    publications = root.child('publications').get()
    list = []  # create a list to store all the publication objects
    for pubid in publications:

        eachpublication = publications[pubid]

        if eachpublication['type'] == 'scli':
            print(eachpublication)
            clinic = Clinic(eachpublication['title'], eachpublication['type'],
                            eachpublication['address'], eachpublication['phone'],
                            eachpublication['openingHour'], eachpublication['busNo'], eachpublication['mrtStation'],
                            eachpublication['hospital'], eachpublication['created_by'], eachpublication['areaName'],
                            eachpublication['region'])
            print(eachpublication)
            clinic.set_pubid(pubid)
            print(clinic.get_pubid())
            list.append(clinic)

        else:
            print(eachpublication)
            disease = Disease(eachpublication['title'], eachpublication['type'], eachpublication['cause'],
                              eachpublication['symptom'],
                              eachpublication['treatment'], eachpublication['complication'],
                              eachpublication['specialist'],
                              eachpublication['created_by'])
            print(eachpublication['cause'])
            disease.set_pubid(pubid)
            list.append(disease)

    return render_template('diseaseinfo.html', publications=list)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Login')
def Login():
    return render_template('login_user.html')






@app.route('/viewpublications')
def viewpublications():
    publications = root.child('publications').get()
    list = []  # create a list to store all the publication objects
    for pubid in publications:

        eachpublication = publications[pubid]

        if eachpublication['type'] =='scli':
            print(eachpublication)
            clinic = Clinic(eachpublication['title'],eachpublication['type'],
                            eachpublication['address'],eachpublication['phone'],
                            eachpublication['openingHour'],eachpublication['busNo'],eachpublication['mrtStation'],
                            eachpublication['hospital'],eachpublication['created_by'],eachpublication['areaName'],
                            eachpublication['region'])
            print(eachpublication)
            clinic.set_pubid(pubid)
            print(clinic.get_pubid())
            list.append(clinic)

        else:
            print(eachpublication)
            disease = Disease(eachpublication['title'],eachpublication['type'],eachpublication['cause'],eachpublication['symptom'],
                              eachpublication['treatment'],eachpublication['complication'],eachpublication['specialist'],
                              eachpublication['created_by'])
            print(eachpublication['cause'])
            disease.set_pubid(pubid)
            list.append(disease)



    return render_template('view_all_publications.html', publications=list)


class RequiredIf(object):

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)



class PublicationForm(Form):
    title = StringField('Name', [
        validators.Length(min=1, max=150),
        validators.DataRequired()])

    pubtype = RadioField('Clinic or disease info', choices=[ ('scli', 'Clinic'), ('sdis','Disease')],default='scli')

    address = StringField('Address', [validators.Length(min=1, max=100),RequiredIf(pubtype='scli')] )
    phone = StringField('Phone No', [validators.Length(min=1, max=100), RequiredIf(pubtype='scli')])

    openingHour = StringField('Opening hours', [validators.Length(min=1, max=100), RequiredIf(pubtype='scli')])
    busNo = StringField('bus No', [validators.Length(min=1, max=100), RequiredIf(pubtype='scli')])
    mrtStation = StringField('Nearest mrt', [validators.Length(min=1, max=100), RequiredIf(pubtype='scli')])
    hospital = StringField('Nearest hospitals', [validators.Length(min=1, max=100), RequiredIf(pubtype='scli')])
    areaName = StringField('Area name(eg Tampines)',[validators.Length(min=1,max=100),RequiredIf(pubtype='scli') ])
    region = SelectField('Region',[RequiredIf(pubtype='scli')],
        choices=[('N','North') , ('C','Central'), ('E','East'),('W','West')])


    cause = StringField('Causes', [
        validators.Length(min=1, max=100),
        RequiredIf(pubtype='sdis')])
    symptom = StringField('Symptoms', [
        validators.Length(min=1, max=100),
        RequiredIf(pubtype='sdis')])
    treatment = StringField('Treatments', [
        validators.Length(min=1, max=100),
        RequiredIf(pubtype='sdis')])
    complication = StringField('Complications', [
        validators.Length(min=1, max=100),
        RequiredIf(pubtype='sdis')])
    specialist = StringField('Specialists', [
        validators.Length(min=1, max=100),
        RequiredIf(pubtype='sdis')])
    # isbn = StringField('ISBN No', [
    #     validators.Length(min=1, max=100),
    #     RequiredIf(pubtype='sbook')])
    # author = StringField('Author', [
    #     validators.Length(min=1, max=100),
    #     RequiredIf(pubtype='sbook')])
    # synopsis = TextAreaField('Synopsis', [
    #     RequiredIf(pubtype='sbook')])
    # frequency = RadioField('Frequency', [RequiredIf(pubtype='smag')],
    #                        choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')])


@app.route('/Register',methods=['GET','POST'])
def index():
    return render_template('register.html')



@app.route('/newpublication',methods=['GET','POST'])
def new():
    form = PublicationForm(request.form)
    if request.method == 'POST' and form.validate():
        if  form.pubtype.data == 'scli':
            title = form.title.data
            type = form.pubtype.data
            address = form.address.data
            phone = form.phone.data
            openingHour = form.openingHour.data
            busNo = form.busNo.data
            mrtStation = form.mrtStation.data
            hospital = form.hospital.data
            areaName = form.areaName.data
            region = form.region.data
            #status = form.status.data
            #frequency = form.frequency.data
            #publisher = form.publisher.data
            created_by = "U0001" # hardcoded value

            #mag = Magazine(title, publisher, status, created_by, category, type, frequency)
            cli = Clinic(title,type,address,phone,openingHour,busNo,mrtStation,hospital,created_by,areaName,region)
            cli_db = root.child('publications')
            cli_db.push({
                'title': cli.get_title(),
                'type': cli.get_type(),
                'address': cli.get_address(),
                'phone': cli.get_phone(),
                'openingHour': cli.get_openingHour(),
                'busNo': cli.get_busNo(),
                'mrtStation': cli.get_mrtStation(),
                'hospital': cli.get_hospital(),
                'areaName': cli.get_areaName(),
                'region': cli.get_region(),
                'created_by': cli.get_created_by(),
                'create_date': cli.get_created_date()
            })
            flash('Clinic Inserted Sucessfully.', 'success')

        elif form.pubtype.data == 'sdis':
            title = form.title.data
            type = form.pubtype.data
            cause = form.cause.data
            symptom = form.symptom.data
            treatment = form.treatment.data
            complication = form.complication.data
            specialist = form.specialist.data
            created_by = "U0001"  # hardcoded value

            dis = Disease(title,type,cause,symptom,created_by,treatment,complication,specialist)
            dis_db = root.child('publications')
            dis_db.push({
                'title': dis.get_title(),
                'type': dis.get_type(),
                'cause': dis.get_cause(),
                'symptom': dis.get_symptom(),
                'treatment': dis.get_treatment(),
                'complication': dis.get_complication(),
                'specialist': dis.get_specialist(),
                'created_by': dis.get_created_by(),
                'create_date': dis.get_created_date()
            })

            flash('Disease Inserted Sucessfully.', 'success')

        return redirect(url_for('viewpublications'))

    return render_template('create_publication.html', form=form)


@app.route('/update/<string:id>/', methods=['GET', 'POST'])
def update_publication(id):
    form = PublicationForm(request.form)
    if request.method == 'POST' and form.validate():
        if form.pubtype.data =='scli':

            title = form.title.data
            type = form.pubtype.data
            address = form.address.data
            phone = form.phone.data
            openingHour = form.openingHour.data
            busNo = form.busNo.data
            mrtStation = form.mrtStation.data
            hospital = form.hospital.data
            areaName = form.areaName.data
            region = form.region.data
            created_by = "U0001"  # hardcoded value
            cli = Clinic(title,type,address,phone,openingHour,busNo,mrtStation,hospital,created_by,areaName,region)
            # create the clinic object
            cli_db = root.child('publications/'+ id )
            cli_db.set({
                    'title': cli.get_title(),
                    'type': cli.get_type(),
                    'address': cli.get_address(),
                    'phone': cli.get_phone(),
                    'openingHour': cli.get_openingHour(),
                    'busNo': cli.get_busNo(),
                    'mrtStation': cli.get_mrtStation(),
                    'hospital': cli.get_hospital(),
                    'areaName': cli.get_areaName(),
                    'region': cli.get_region(),
                    'created_by': cli.get_created_by(),
                    'create_date':cli.get_created_date()
            })

            flash('Clinic Updated Sucessfully.', 'success')

        elif form.pubtype.data == 'sdis':
            title = form.title.data
            type = form.title.data
            cause = form.cause.data
            symptom = form.symptom.data
            treatment = form.treatment.data
            complication = form.complication.data
            specialist = form.specialist.data
            created_by = "U0001"  # hardcoded value

            dis = Disease(title,type,cause,symptom,treatment,complication,specialist,created_by)
            dis_db = root.child('publications/'+id)
            dis_db.set({
                'title': dis.get_title(),
                'type': dis.get_type(),
                'cause': dis.get_cause(),
                'symptom': dis.get_symptom(),
                'treatment': dis.get_treatment(),
                'complication': dis.get_complication(),
                'specialist': dis.get_specialist(),
                'created_by': dis.get_created_by(),
                'create_date': dis.get_created_date()
            })

            flash('Disease Updated Sucessfully.', 'success')

        return redirect(url_for('viewpublications'))

    else:
        url = 'publications/' + id
        eachpub = root.child(url).get()

        if eachpub['type']== 'scli':
            clinic = Clinic(eachpub['title'], eachpub['type'] , eachpub['address'],eachpub['phone'],
                            eachpub['openingHour'],eachpub['busNo'],eachpub['mrtStation'],eachpub['hospital'],
                            eachpub['created_by'],eachpub['areaName'], eachpub['region'])

            clinic.set_pubid(id)
            form.title.data = clinic.get_title()
            form.pubtype.data = clinic.get_type()
            form.address.data = clinic.get_address()
            form.phone.data = clinic.get_phone()
            form.openingHour.data = clinic.get_openingHour()
            form.busNo.data = clinic.get_busNo()
            form.mrtStation.data = clinic.get_mrtStation()
            form.hospital.data = clinic.get_hospital()
            form.areaName.data = clinic.get_areaName()
            form.region.data = clinic.get_region()

        elif eachpub['type'] == 'sdis':
            disease = Disease(eachpub['title'], eachpub['type'], eachpub['cause'], eachpub['symptom'], eachpub['treatment'],
                        eachpub['complication'], eachpub['specialist'],
                        eachpub['created_by'])
            disease.set_pubid(id)
            form.title.data = disease.get_title()
            form.cause.data = disease.get_cause()
            form.symptom.data = disease.get_symptom()
            form.treatment.data = disease.get_treatment()
            form.complication.data = disease.get_complication()
            form.specialist.data = disease.get_specialist()


        return render_template('update_publication.html', form=form)



@app.route('/delete_publication/<string:id>', methods=['POST'])
def delete_publication(id):
    cli_db = root.child('publications/' + id)
    cli_db.delete()

    dis_db = root.child('publications/'+id)
    dis_db.delete()
    flash('Publication Deleted','success')
    # mag_db = root.child('publications/' + id)
    # mag_db.delete()
    # flash('Publication Deleted', 'success')

    return redirect(url_for('viewpublications'))




class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

@app.before_first_request
def setupDatabase():
    db.create_all()





@app.route('/loin', methods=['GET', 'POST'])
def lgin():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        if username == 'admin' and password == 'P@ssw0rd':  # harcoded username and password
            session['logged_in'] = True  # this is to set a session to indicate the user is login into the system.
            return redirect(url_for('viewpublications'))

        else:
            error = 'Invalid login'
            flash(error, 'danger')
            return render_template('Login.html', form=form)

    return render_template('Login.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()
