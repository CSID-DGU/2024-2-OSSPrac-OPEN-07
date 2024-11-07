from flask import Flask, render_template, request

app = Flask(__name__)

# 메인 입력 페이지 경로
@app.route('/')
def input():
    return render_template('input.html')

# 결과 페이지 경로 - 입력한 팀원 정보를 출력
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = dict()
        result['TeamName'] = request.form.get('TeamName')
        
        # 팀장 정보
        leader = {
            'Name': request.form.get('leader_name'),
            'Role': 'Team Leader',
            'Department': request.form.get('leader_department'),
            'Phone': request.form.get('leader_phone'),
            'Email': request.form.get('leader_email')
        }
        
        # 팀원 1 정보
        member1 = {
            'Name': request.form.get('member1_name'),
            'Role': 'Gender Specialist',
            'Department': request.form.get('member1_department'),
            'Phone': request.form.get('member1_phone'),
            'Email': request.form.get('member1_email')
        }
        
        # 팀원 2 정보
        member2 = {
            'Name': request.form.get('member2_name'),
            'Role': 'Programming Languages Specialist',
            'Department': request.form.get('member2_department'),
            'Phone': request.form.get('member2_phone'),
            'Email': request.form.get('member2_email')
        }
        
        result['Leader'] = leader
        result['Members'] = [member1, member2]
        
        return render_template('result.html', result=result)

# 새로운 경로 추가 - 인덱스 페이지 (메인 페이지)
@app.route('/index')
def index():
    return render_template('index.html')

# 새로운 경로 추가 - 연락처 페이지
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
