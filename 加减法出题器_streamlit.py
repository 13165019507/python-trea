
# pip install streamlit
import streamlit as st
import random

# 初始化 session_state
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = []
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0
if 'results' not in st.session_state:
    st.session_state.results = []
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'generated' not in st.session_state:
    st.session_state.generated = False
if 'operation' not in st.session_state:
    st.session_state.operation = '+'
if 'range' not in st.session_state:
    st.session_state.range = 10
if 'question_count' not in st.session_state:
    st.session_state.question_count = 5
if 'grading_mode' not in st.session_state:
    st.session_state.grading_mode = '每题批改'
if 'answer_submitted' not in st.session_state:
    st.session_state.answer_submitted = False

st.title('加减法出题器')

# 用户选择区域
st.session_state.operation = st.selectbox('选择运算类型', ['+', '-'])
st.session_state.range = st.selectbox('选择数值范围', [10, 100])
st.session_state.question_count = st.number_input('输入出题数量', min_value=1, value=5)
st.session_state.grading_mode = st.selectbox('选择批改模式', ['每题批改', '全部批改'])

if st.button('生成题目'):
    st.session_state.questions = []
    st.session_state.answers = []
    st.session_state.user_answers = [None] * st.session_state.question_count
    st.session_state.current_question_index = 0
    st.session_state.results = []
    st.session_state.score = 0
    st.session_state.generated = True
    st.session_state.answer_submitted = False

    # 生成题目
    while len(st.session_state.questions) < st.session_state.question_count:
        a = random.randint(0, st.session_state.range)
        b = random.randint(0, st.session_state.range)
        if st.session_state.operation == '+':
            question = f'{a} + {b} = '
            answer = a + b
        else:
            if a < b:
                a, b = b, a
            question = f'{a} - {b} = '
            answer = a - b

        if question not in st.session_state.questions:
            st.session_state.questions.append(question)
            st.session_state.answers.append(answer)

if st.session_state.generated:
    if st.session_state.grading_mode == '每题批改':
        # 每题批改模式，逐题显示
        if st.session_state.current_question_index < st.session_state.question_count:
            question = st.session_state.questions[st.session_state.current_question_index]
            answer = st.session_state.answers[st.session_state.current_question_index]
            
            st.subheader(f'第 {st.session_state.current_question_index + 1} 题: {question}')
            user_answer = st.number_input('', step=1, value=None, placeholder='请输入答案', key=f'answer_{st.session_state.current_question_index}')
            
            button_text = '下一题' if st.session_state.answer_submitted else '提交答案'
            if st.button(button_text):
                if not st.session_state.answer_submitted and user_answer is not None:
                    st.session_state.user_answers[st.session_state.current_question_index] = user_answer
                    is_correct = user_answer == answer
                    if is_correct:
                        st.session_state.score += 1
                    st.session_state.results.append((question, user_answer, answer, is_correct))
                    st.session_state.answer_submitted = True
                else:
                    st.session_state.current_question_index += 1
                    st.session_state.answer_submitted = False
    else:
        # 全部批改模式，一次性显示所有题目
        st.subheader('全部题目')
        for i in range(st.session_state.question_count):
            question = st.session_state.questions[i]
            st.write(f'第 {i + 1} 题: {question}')
            st.session_state.user_answers[i] = st.number_input('', step=1, value=None, placeholder='请输入答案', key=f'answer_all_{i}')

    # 显示批改历史
    if st.session_state.results:
        st.subheader('批改历史')
        for i, (q, u_a, a, correct) in enumerate(st.session_state.results):
            status = '正确' if correct else '错误'
            color = 'green' if correct else 'red'
            st.markdown(f'第 {i+1} 题: {q} 你的答案: {u_a}, 正确答案: {a} - <span style="color:{color};">{status}</span>', unsafe_allow_html=True)

    # 全部批改模式下显示提交按钮
    if st.session_state.grading_mode == '全部批改' and all(ans is not None for ans in st.session_state.user_answers):
        if st.button('全部提交'):
            st.session_state.results = []
            st.session_state.score = 0
            for i in range(st.session_state.question_count):
                is_correct = st.session_state.user_answers[i] == st.session_state.answers[i]
                if is_correct:
                    st.session_state.score += 1
                st.session_state.results.append((st.session_state.questions[i], st.session_state.user_answers[i], st.session_state.answers[i], is_correct))

    # 显示总分
    if st.session_state.results:
        st.subheader(f'当前得分: {st.session_state.score}/{st.session_state.question_count}')