import stripe
from flask import Flask, render_template, request

app = Flask(__name__)

stripe.api_key = 'Your Api keys'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    # Process payment with Stripe
    token = request.form['stripeToken']
    amount = 1000

    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency='INR',
            description='Example Charge',
            source=token,
        )
        return render_template('success.html')
    except stripe.error.CardError as e:
        return render_template('error.html', error=e)

if __name__ == "__main__":
    app.run(debug=True)
