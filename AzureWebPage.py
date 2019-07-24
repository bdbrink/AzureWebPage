from flask import Flask
app = Flask(__name__)
#make sure to have flask installed, i had to define the interpeter of flask in Pycharm
@app.route("/")
def hello():
  return "Kyles and Naurto runners are welcome here !"
#it will print the return line on the page
if __name__ == "__main__":
    app.run()
    