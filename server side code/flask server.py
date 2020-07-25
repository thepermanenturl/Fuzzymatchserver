from flask import Flask, request
import Fuzz

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def result():
    true=True
    false=False
    ans=Fuzz.Fuzzfun(request.json)
    #render_template('Ans.html', result=ans)
    return ans


if __name__ == '__main__':
    app.run(use_reloader=False,debug=True)