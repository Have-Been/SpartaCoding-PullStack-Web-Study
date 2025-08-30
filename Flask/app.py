from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def home():
    name = '오유빈'
    lotto = [16, 18, 22, 43, 32, 11]

    def generate_lotto_numbers():
        numbers = random.sample(range(1, 46), 6)
        return sorted(numbers)

    random_lotto = generate_lotto_numbers()
    
    def count_common_elements(list1, list2):
        common_elements = set(list1) & set(list2)
        return len(common_elements)
    
    common_count = count_common_elements(lotto, random_lotto)

    context = {
        "name": name,
        "lotto": lotto,
        "random_lotto": random_lotto,
        "common_count": common_count
    }
    
    return render_template('index.html', data=context)

@app.route('/mypage')
def mypage():
    return 'This is Mypage!'

if __name__ == '__main__':  
    app.run(debug=True)