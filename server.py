from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '1234'  # Change this to a secure random key

# Dummy user data (for demonstration purposes)
users = {
    'user1': 'password1',
    'user2': 'password2',
}

# Main PIPBOI page
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        button_clicked = request.form['button']
        if button_clicked == 'login-button':
            return redirect(url_for('login'))
    return render_template('index.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password match
        if users.get(username) == password:
            flash('Login successful!', 'success')
            return redirect(url_for('welcome'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    
    return render_template('login.html')

# Route for the welcome page (accessed after successful login)
@app.route('/welcome')
def welcome():
    return 'Welcome to the protected area!'

# Logout route (optional)
@app.route('/logout')
def logout():
    # Implement your logout logic here (e.g., clearing session data)
    return 'Logged out successfully'

if __name__ == '__main__':
    app.run(debug=True)