import tkinter as tk
from tkinter import ttk
import requests

# API Key
API_KEY = "57f68e8031dd4dd4a8256f13d8e9db93"

# Fetch the currency list
url = f"https://openexchangerates.org/api/currencies.json"
response = requests.get(url)
currency_data = response.json()
currencies = sorted(currency_data.keys())

# Function to fetch conversion rates
def fetch_conversion_rates(base_currency):
    url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base={base_currency}"
    response = requests.get(url)
    if response.status_code != 200:

        # API call failed, return None
        print(f"Error fetching conversion rates: {response.status_code} - {response.text}")
        return None
    data = response.json()

    if 'rates' not in data:
        # response does not contain rates, return None
        print("Error fetching conversion rates: response does not contain rates")
        return None
    return data['rates']

#function for conversion form one conversion to other
def perform_conversion():
    amount = float(amount_entry.get())
    from_currency = from_currency_dropdown.get()
    to_currency = to_currency_dropdown.get()
    if conversion_rates is None:
        output_label.config(text="Error fetching conversion rates")
        return
    converted_amount = amount * conversion_rates[from_currency] / conversion_rates[to_currency]
    output_label.config(text=f"Converted Amount: {converted_amount:.2f} {from_currency}")

# Function to reset the input and output fields
def reset():
    amount_entry.delete(0, tk.END)
    output_label.config(text="")

# Create main window
root = tk.Tk()
root.title("Daniyal's Currency Converter")
root.configure(bg="#C1CDCD")
intro_label = ttk.Label(root, text='Welcome to Daniyal & Co Currency Convertor', relief=tk.RAISED, borderwidth=5)
intro_label.config(font=('Courier', 15, 'bold'))
intro_label.pack(pady=10)
intro_label.configure(background='#C1CDCD')

# Set the window size and position
root.geometry("650x600+50+50")
# Add a logo image
logo_image = tk.PhotoImage(file="img.png").subsample(5)
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(pady=10)
logo_label.configure(background='#C1CDCD')

# Create and place widgets
amount_label = ttk.Label(root, text="Enter Amount:", font=("Helvetica", 14))
amount_label.pack(pady=10)
amount_entry = ttk.Entry(root)
amount_entry.pack(pady=5)
amount_label.configure(background='#C1CDCD')

#taking input source or main currency
to_currency_label = ttk.Label(root, text="From Currency:")
to_currency_label.configure(background='#C1CDCD', font=("Arial", 14))
to_currency_label.pack(pady=10)
to_currency_dropdown = ttk.Combobox(root, values=currencies)
to_currency_dropdown.pack(pady=5)
to_currency_dropdown.set("USD")

#taking input desire currency in which want to convert
from_currency_label = ttk.Label(root, text="To Currency:")
from_currency_label.pack(pady=10)
from_currency_label.configure(background='#C1CDCD', font=("Arial", 14))
from_currency_dropdown = ttk.Combobox(root, values=currencies)
from_currency_dropdown.pack(pady=5)
from_currency_dropdown.set("PKR")

#button for calling perform conversion opertaion
convert_button = ttk.Button(root, text="Convert", command=perform_conversion, style="my.TButton")
convert_button.pack(pady=10)

# Define a custom style for the button
style = ttk.Style()
style.configure("my.TButton", font=("Helvetica", 12), background="#4CAF50")

#output displaying after conversion
output_label = ttk.Label(root, text="")
output_label.pack(pady=10)
output_label.configure(background='#C1CDCD', font=("Helvetica", 12))

#reset button
reset_button = ttk.Button(root, text="Reset", command=reset, style="my.TButton")
reset_button.pack(pady=10)

# Define a custom style for the button
style = ttk.Style()
style.configure("my.TButton", font=("Helvetica", 12), background="#4CAF50")
conversion_rates = fetch_conversion_rates("USD")

#for greetings
intro_label = ttk.Label(root, text="THANKS FOR VISITING US", relief=tk.RAISED, borderwidth=5)
intro_label.config(font=('Courier', 15, 'bold'))
intro_label.pack(pady=10)
intro_label.configure(background='#C1CDCD')

#calling mainloop to operate code
root.mainloop()