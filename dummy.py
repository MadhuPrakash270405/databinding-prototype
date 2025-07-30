from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process the form data here
        group_name = request.form['groupName']
        member_count = request.form['memberCount']
        emails = request.form.getlist('emailSelect')
        message = request.form['message']

        # For now, we can print the submitted data or handle as needed
        print(f"Group Name: {group_name}")
        print(f"Member Count: {member_count}")
        print(f"Emails: {emails}")
        print(f"Message: {message}")

        # You can redirect to a new page or render a success message
        return f"Form submitted successfully. Emails: {emails}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)