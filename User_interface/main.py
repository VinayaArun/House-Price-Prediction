# main.py
from flask import Flask, render_template, request


import pickle

# Load data from a file
with open('rf_model.pkl', 'rb') as file:
    loaded_data = pickle.load(file)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')



@app.route('/get_data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        # Access form data using request.form
        property_details = {
            'area': int(request.form['area']),  # Assuming 'area' is provided in the form
            'bedrooms': int(request.form['Number_of_Rooms']),  # Mapping 'Number_of_Rooms' to 'bedrooms'
            'bathrooms': int(request.form['Number_of_Bathroom']),  # Mapping 'Number_of_Bathroom' to 'bathrooms'
            'stories': int(request.form['stories']),  # Assuming 'stories' is provided in the form
            'parking': 1,  # Total parking spaces
            'mainroad_encoded': request.form['mainroad'],  # Encoding example function
            'guestroom_encoded': request.form['guestroom'],  # Encoding example function
            'basement_encoded': request.form['basement'],  # Encoding example function
            'hotwaterheating_encoded': request.form['hotwaterheating'],  # Encoding example function
            'airconditioning_encoded': request.form['airconditioning'],  # Encoding example function
            'prefarea_encoded': request.form['prefarea'],  # Encoding example function
            'furnishingstatus_encoded': request.form['furnishing_status']  # Encoding furnishing status
        }

        
        import pandas as pd
        new_test_df = pd.DataFrame([property_details])

        new_test_array = new_test_df.to_numpy().reshape(1, -1)
 

        result=loaded_data.predict(new_test_array)

        # Process the form data as needed (e.g., store in a database)

        print(f"{property_details}")
        print(f" {result}")
        result=int(result[0])

        return render_template('index.html',data=result)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('your_template.html')

