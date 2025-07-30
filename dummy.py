from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # Receive JSON data from frontend
    group_name = data.get('groupName')
    member_count = data.get('memberCount')
    emails = data.get('emails')
    message = data.get('message')

    print(f"Group Name: {group_name}")
    print(f"Member Count: {member_count}")
    print(f"Emails: {emails}")
    print(f"Message: {message}")

    return jsonify({'status': 'success', 'message': 'Form submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)