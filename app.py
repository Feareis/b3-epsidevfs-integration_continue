# app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Currency conversion function
def convert_currency(amount, source_currency, target_currency):
    """
    Converts an amount from a source currency to a target currency using current exchange rates.

    :param amount: Amount to convert (float).
    :param source_currency: Source currency code (str).
    :param target_currency: Target currency code (str).
    :return: Converted amount (float) or None if conversion rate is unavailable.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{source_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for a successful response
        rate = response.json().get("rates", {}).get(target_currency)
        return amount * rate if rate else None
    except requests.RequestException as e:
        print(f"Error retrieving exchange rates: {e}")
        return None


@app.route('/convert', methods=['POST'])
def convert():
    """
    Currency conversion endpoint. Receives an amount, source currency, and target currency in JSON format,
    then returns the converted amount.

    :return: JSON containing the converted amount or an error message.
    """
    data = request.get_json()
    amount = data.get('amount')
    source_currency = data.get('source_currency')
    target_currency = data.get('target_currency')

    if not all([amount, source_currency, target_currency]):
        return jsonify({"error": "Amount, source currency, and target currency are required"}), 400

    result = convert_currency(amount, source_currency, target_currency)

    if result is None:
        return jsonify({"error": "Conversion failed. Check the currencies and try again."}), 400

    return jsonify({"converted_amount": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
