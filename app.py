from flask import Flask, render_template, request

def Invol(num1,num2):
    a = int(num1)
    n = int(num2)
    a1 = 1

    binstr = (bin(n)[2:])
    binstr = (binstr[::-1])
    l = len(binstr)


    for i in range(l):
        a1 = a1*pow(a,int(binstr[i]))
        a = a*a
    return a1


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sum_numbers():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        if num1 and num2:
            result = Invol(num1,num2)
            return render_template('result.html', result=result)
    return render_template('enter.html')

if __name__ == '__main__':
    app.run(debug=True)

