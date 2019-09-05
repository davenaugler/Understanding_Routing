from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'

#have it say "Dojo!"
def hello_dojo():
    print('in the hello_name function')
    return "Dojo!"

#have it say "Hi Flask! // Hi Michael! // Hi John!"
@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello_say(name):
    print('in the hello_name function')
    print(name)
    return f"Hi {name}!"

#localhost:5000/repeat/35/hello - have it say "hello" 35 times
@app.route('/repeat/<num>/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello_mult(name, num):
    num = int(num)
    mutlNameString = ''
    for x in range(0, num, +1):
        mutlNameString = mutlNameString + name + ' '
        #For Loop goes here to print out the number of names it's given in the url
    # print(name)
    return mutlNameString


     
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

