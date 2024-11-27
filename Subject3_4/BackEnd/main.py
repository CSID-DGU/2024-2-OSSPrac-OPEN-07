from flask import Flask, request, render_template, url_for, jsonify
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # 사진 파일 저장 경로
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 메인 페이지
@app.route('/')
def index():
    return render_template('app_index.html')

# 학생 정보 입력 페이지
@app.route('/input')
def input_page():
    return render_template('app_input.html')

# 학생 정보 제출 처리 및 출력
@app.route('/result', methods=['POST'])
def result():
    # 폼 데이터 수집
    names = request.form.getlist('name[]')
    roles = request.form.getlist('role[]')
    student_numbers = request.form.getlist('StudentNumber[]')
    student_emails = request.form.getlist('email[]')
    majors = request.form.getlist('major[]')
    githubs = request.form.getlist('git[]')

    # 데이터 저장 형식 구성
    students = [
        {
            'name': n,
            'role': r,
            'student_number': sn,
            'email': em,
            'major': mj,
            'github': g
        }
        for n, r, sn, em, mj, g in zip(names, roles, student_numbers, student_emails, majors, githubs)
    ]

    # JSON 파일에 저장
    with open('student_data.json', 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

    # HTML 페이지로 렌더링
    return render_template('app_result.html', students=students)

# 학생 정보 JSON 반환 API
@app.route('/students', methods=['GET'])
def get_students():
    try:
        # JSON 파일 읽기
        with open('student_data.json', 'r', encoding='utf-8') as f:
            students = json.load(f)
    except FileNotFoundError:
        students = []  # 데이터가 없으면 빈 리스트 반환

    return jsonify(students)

# 연락처 페이지
@app.route('/contact')
def contact_info():
    return render_template('app_contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
