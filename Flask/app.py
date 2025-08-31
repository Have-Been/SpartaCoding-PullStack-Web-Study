from flask import Flask, render_template, request
import random
import requests
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

@app.route('/movie')
def movie():
    query = request.args.get('query')
    res = requests.get(
	f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=6b3423156bb0fe131e9d7242b01d0234&movieNm={query}"
    )
    rjson = res.json()
    movie_list = rjson["movieListResult"]["movieList"]
    return render_template('movie.html', data=movie_list)

@app.route("/answer")
def answer():
    if request.args.get('query'):
        query = request.args.get('query')
    else:
        query = '20230601'    

    URL = f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=6b3423156bb0fe131e9d7242b01d0234&targetDt={query}"

    res = requests.get(URL)
    rjson = res.json()
    print(rjson)
    boxoffice_list = rjson["boxOfficeResult"]["weeklyBoxOfficeList"]
    return render_template("answer.html", data=boxoffice_list)

if __name__ == '__main__':  
    app.run(debug=True)