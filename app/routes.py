from app import db, app
from app.models import User, LinuxCommand
from app.forms import LoginForm, RegistrationForm, ResetPasswordForm, ResetPasswordRequestForm, LinuxCommandForm
from app.email import send_password_reset_email
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user

from werkzeug.urls import url_parse




@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/linux_commands', methods=['GET','POST'])
def linux_commands():

    page = request.args.get('page', 1, type=int)

    commands = LinuxCommand.query.order_by(LinuxCommand.id.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)
    # print(commands.items)
    next_url = url_for('index', page=commands.next_num) \
        if commands.has_next else None
    prev_url = url_for('index', page=commands.prev_num) \
        if commands.has_prev else None

    return render_template("linux_commands.html", title='Linux Commands',commands=commands.items,next_url=next_url, prev_url=prev_url)

@app.route('/linux_commands/add', methods=['GET','POST'])
def add_linux_commands():
    form = LinuxCommandForm()

    if form.validate_on_submit():
        command = LinuxCommand(name=form.name.data, description=form.description.data, code=form.code.data)
        db.session.add(command)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('linux_commands'))

    return render_template("edit_linux_command.html", title='Linux Commands',form=form)

@app.route('/linux_command/edit/<id>',methods=['GET','POST'])
def edit_linux_command(id):
    form = LinuxCommandForm()
    command = LinuxCommand.query.filter_by(id=id).first_or_404()
    if form.delete.data:
        return redirect(url_for('delete_linux_command',id=id))
    if form.submit.data and form.validate_on_submit():
        command.name = form.name.data
        command.description = form.description.data
        command.code = form.code.data
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('linux_commands'))
    elif request.method == 'GET':
        form.name.data = command.name
        form.description.data = command.description
        form.code.data = command.code
    return render_template('edit_linux_command.html', form=form, name=command.name,description=command.description)

@app.route('/linux_command/delete/<id>',methods=['GET','POST'])
def delete_linux_command(id):
    LinuxCommand.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Command Deleted')
    return redirect(url_for('linux_commands'))



@app.route('/stopwatch', methods=['GET'])
@login_required
def stopwatch():
    return render_template("clock.html", title='Stopwatch', ClockType='Stopwatch')

@app.route('/clock', methods=['GET'])
@login_required
def clock():
    return render_template("clock.html", title='Clock', ClockType='Clock')