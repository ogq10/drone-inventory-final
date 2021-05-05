from flask import Blueprint, render_template, request,flash, redirect, url_for
from drone_inventory.forms import UserLoginForm
from drone_inventory.models import User, db

auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()
    
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)
            #insatantiate a new User class here with email/pw
            user = User(email, password = password)
            #equivalent to committing or staging this db change
            db.session.add(user)
            #equivalent to 'pushing' to our database
            db.session.commit()

            #Showing a message to the user
            flash(f'You have successfully created a user account for {email}', 'user-created')
            
            return redirect(url_for('site.home'))



    except:
        raise Exception('Invalid form Data: Please check your form')

    return render_template('signup.html', form = form)


@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    return render_template('signin.html')