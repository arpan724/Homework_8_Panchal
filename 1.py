from flask import Flask, jsonify
import yaml

app = Flask(__name__)

@app.route('/config_info')
def display_config_info():
    with open('config.yaml', 'r') as file:
        config_data = yaml.safe_load(file)
    
    return jsonify(config_data)

if __name__ == '__main__':
    app.run(debug=True)

