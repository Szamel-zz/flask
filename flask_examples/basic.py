from flask import Flask, render_template

app = Flask(__name__)

'''
Folder name are mandatory:
static
templates
'''

@app.route('/')
def index():
    greetings = "Lok'tar Ogar!"
    my_list = [1, 2, 3, 4]
    sum_of_my_list = sum(my_list)
    my_dict = {'race': 'orc'}
    user_loged_in = True
    return render_template('basic.html',
                           my_variable=greetings,
                           my_list=my_list,
                           my_sum=sum_of_my_list,
                           my_dict=my_dict,
                           user_loged_in=user_loged_in)


if __name__ == '__main__':
    app.run(debug=True)
