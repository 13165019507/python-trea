import streamlit as st
import random
import pandas as pd
from datetime import datetime

def generate_question(operator, max_num):
    """Generate a single arithmetic question"""
    num1 = random.randint(0, max_num)
    num2 = random.randint(0, max_num)

    if operator == '-':
        num1, num2 = max(num1, num2), min(num1, num2)

    question = f"{num1} {operator} {num2} = "
    answer = eval(f"{num1} {operator} {num2}")
    return question, answer

def generate_all_questions(operator, max_num, total_questions):
    """Generate all questions without duplicates"""
    used_questions = set()
    questions = []
    answers = []
    
    for i in range(total_questions):
        while True:
            question, answer = generate_question(operator, max_num)
            if question not in used_questions:
                used_questions.add(question)
                break
        questions.append(question)
        answers.append(answer)
    
    return questions, answers

def main():
    st.set_page_config(
        page_title="加减法出题器",
        page_icon="🧮",
        layout="wide"
    )
    
    st.title("🧮 加减法出题器")
    st.subheader("Made by ZhongYi")
    st.markdown("---")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ 设置")
        
        # Operator selection
        operator_choice = st.selectbox(
            "选择运算类型",
            ["+", "-"],
            format_func=lambda x: "加法" if x == "+" else "减法"
        )
        
        # Range selection
        range_choice = st.selectbox(
            "选择数值范围",
            [10, 100],
            format_func=lambda x: f"{x}以内"
        )
        
        # Number of questions
        max_possible_questions = (range_choice + 1) * (range_choice + 1)
        if operator_choice == '-':
            max_possible_questions = (range_choice + 1) * (range_choice + 2) // 2
        
        total_questions = st.slider(
            "出题数量",
            min_value=1,
            max_value=min(max_possible_questions, 50),  # Cap at 50 for web interface
            value=10
        )
        
        # Check mode
        check_mode = st.radio(
            "批改模式",
            ["1", "2"],
            format_func=lambda x: "每题批改" if x == "1" else "全部答完后批改"
        )
        
        st.markdown("---")
        st.info(f"最大可能题目数: {max_possible_questions}")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📝 开始答题")
        
        # Initialize session state
        if 'questions' not in st.session_state:
            st.session_state.questions = []
            st.session_state.answers = []
            st.session_state.user_answers = []
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.quiz_started = False
            st.session_state.quiz_finished = False
            st.session_state.show_result = False
            st.session_state.last_result = None
            st.session_state.show_detailed_review = False
        
        # Start quiz button
        if not st.session_state.quiz_started:
            if st.button("🚀 开始答题", type="primary", use_container_width=True):
                st.session_state.questions, st.session_state.answers = generate_all_questions(
                    operator_choice, range_choice, total_questions
                )
                st.session_state.quiz_started = True
                st.session_state.current_question = 0
                st.session_state.user_answers = []
                st.session_state.score = 0
                st.session_state.quiz_finished = False
                st.session_state.show_result = False
                st.session_state.last_result = None
                st.session_state.show_detailed_review = False
                st.rerun()
        
        # Quiz interface
        if st.session_state.quiz_started and not st.session_state.quiz_finished:
            if check_mode == "1":  # Per-question checking
                if st.session_state.current_question < len(st.session_state.questions):
                    current_q = st.session_state.current_question
                    question = st.session_state.questions[current_q]
                    answer = st.session_state.answers[current_q]
                    
                    st.subheader(f"第 {current_q + 1} 题")
                    st.markdown(f"### {question}")
                    
                    # Show result if available
                    if st.session_state.show_result and st.session_state.last_result:
                        if st.session_state.last_result == "correct":
                            st.success("✅ 回答正确！")
                        elif st.session_state.last_result == "wrong":
                            st.error(f"❌ 回答错误，正确答案是 {answer}。")
                        elif st.session_state.last_result == "skipped":
                            st.warning("⏭️ 已跳过此题")
                        
                        # Next question button
                        if st.button("⏭️ 下一题", type="primary", use_container_width=True):
                            st.session_state.show_result = False
                            st.session_state.last_result = None
                            st.session_state.current_question += 1
                            st.rerun()
                    
                    # Answer input (only show if not showing result)
                    if not st.session_state.show_result:
                        user_answer_input = st.text_input(
                            "请输入你的答案:",
                            key=f"answer_{current_q}",
                            placeholder="输入数字答案..."
                        )
                        
                        # Convert to number or None
                        user_answer = None
                        if user_answer_input.strip():
                            try:
                                user_answer = int(user_answer_input)
                            except ValueError:
                                st.error("请输入有效的数字！")
                                user_answer = None
                        
                        col_a, col_b = st.columns(2)
                        with col_a:
                            if st.button("✅ 提交答案", use_container_width=True):
                                if user_answer is None:
                                    st.warning("⚠️ 请先输入答案！")
                                elif user_answer == answer:
                                    st.session_state.score += 1
                                    st.session_state.user_answers.append(user_answer)
                                    st.session_state.show_result = True
                                    st.session_state.last_result = "correct"
                                    st.rerun()
                                else:
                                    st.session_state.user_answers.append(user_answer)
                                    st.session_state.show_result = True
                                    st.session_state.last_result = "wrong"
                                    st.rerun()
                        
                        with col_b:
                            if st.button("⏭️ 跳过", use_container_width=True):
                                st.session_state.user_answers.append(None)
                                st.session_state.show_result = True
                                st.session_state.last_result = "skipped"
                                st.rerun()
                
                else:
                    st.session_state.quiz_finished = True
                    st.rerun()
            
            else:  # Batch checking
                if st.session_state.current_question < len(st.session_state.questions):
                    current_q = st.session_state.current_question
                    question = st.session_state.questions[current_q]
                    
                    st.subheader(f"第 {current_q + 1} 题")
                    st.markdown(f"### {question}")
                    
                    user_answer_input = st.text_input(
                        "请输入你的答案:",
                        key=f"answer_{current_q}",
                        placeholder="输入数字答案..."
                    )
                    
                    # Convert to number or None
                    user_answer = None
                    if user_answer_input.strip():
                        try:
                            user_answer = int(user_answer_input)
                        except ValueError:
                            st.error("请输入有效的数字！")
                            user_answer = None
                    
                    if st.button("⏭️ 下一题", use_container_width=True):
                        if user_answer is None:
                            st.warning("⚠️ 请先输入答案！")
                        else:
                            st.session_state.user_answers.append(user_answer)
                            st.session_state.current_question += 1
                            st.rerun()
                
                else:
                    # Show all questions for review
                    if not st.session_state.show_detailed_review:
                        st.subheader("📋 题目回顾")
                        st.info("所有题目已完成，请查看详细作答情况：")
                        
                        # Create detailed review
                        review_data = []
                        for i, (question, user_ans, correct_ans) in enumerate(zip(
                            st.session_state.questions, 
                            st.session_state.user_answers, 
                            st.session_state.answers
                        )):
                            if user_ans is None:
                                status = "未作答"
                                result = "⚠️"
                                st.warning(f"第 {i+1} 题: {question} 未作答 ⚠️ (正确答案: {correct_ans})")
                            elif user_ans == correct_ans:
                                status = "正确"
                                result = "✅"
                                st.success(f"第 {i+1} 题: {question} 你的答案: {user_ans} ✅")
                                st.session_state.score += 1
                            else:
                                status = "错误"
                                result = "❌"
                                st.error(f"第 {i+1} 题: {question} 你的答案: {user_ans} ❌ (正确答案: {correct_ans})")
                            
                            review_data.append({
                                "题号": i+1,
                                "题目": question,
                                "你的答案": user_ans if user_ans is not None else "未作答",
                                "正确答案": correct_ans,
                                "结果": result,
                                "状态": status
                            })
                        
                        # Show summary table
                        st.subheader("📊 作答清单")
                        df = pd.DataFrame(review_data)
                        st.dataframe(df, use_container_width=True)
                        
                        # Summary statistics
                        total_answered = len([ans for ans in st.session_state.user_answers if ans is not None])
                        total_correct = st.session_state.score
                        total_wrong = total_answered - total_correct
                        total_skipped = len(st.session_state.user_answers) - total_answered
                        
                        col_sum1, col_sum2, col_sum3, col_sum4 = st.columns(4)
                        with col_sum1:
                            st.metric("总题数", total_questions)
                        with col_sum2:
                            st.metric("已作答", total_answered)
                        with col_sum3:
                            st.metric("答对", total_correct)
                        with col_sum4:
                            st.metric("答错", total_wrong)
                        
                        if total_skipped > 0:
                            st.warning(f"⚠️ 跳过题目数: {total_skipped}")
                        
                        # Button to proceed to final results
                        if st.button("📈 查看最终成绩", type="primary", use_container_width=True):
                            st.session_state.show_detailed_review = True
                            st.rerun()
                    else:
                        st.session_state.quiz_finished = True
                        st.rerun()
        
        # Results
        if st.session_state.quiz_finished:
            st.success("🎉 答题完成！")
            score_percentage = int(st.session_state.score / total_questions * 100)
            
            # Display results
            col_result1, col_result2, col_result3 = st.columns(3)
            with col_result1:
                st.metric("答对题数", f"{st.session_state.score}/{total_questions}")
            with col_result2:
                st.metric("得分", f"{score_percentage}分")
            with col_result3:
                st.metric("正确率", f"{score_percentage}%")
            
            # Performance indicator
            if score_percentage >= 90:
                st.success("🌟 优秀！继续保持！")
            elif score_percentage >= 70:
                st.info("👍 良好！继续努力！")
            elif score_percentage >= 50:
                st.warning("💪 及格！需要多加练习！")
            else:
                st.error("📚 需要更多练习！")
            
            # Restart button
            if st.button("🔄 重新开始", type="primary", use_container_width=True):
                st.session_state.questions = []
                st.session_state.answers = []
                st.session_state.user_answers = []
                st.session_state.current_question = 0
                st.session_state.score = 0
                st.session_state.quiz_started = False
                st.session_state.quiz_finished = False
                st.session_state.show_result = False
                st.session_state.last_result = None
                st.rerun()
    
    with col2:
        st.header("📊 统计信息")
        
        if st.session_state.quiz_started:
            # Progress bar
            if not st.session_state.quiz_finished:
                progress = st.session_state.current_question / total_questions
                st.progress(progress)
                st.write(f"进度: {st.session_state.current_question}/{total_questions}")
            
            # Current score
            if st.session_state.quiz_started:
                st.metric("当前得分", f"{st.session_state.score}分")
            
            # Question preview
            if st.session_state.questions:
                st.subheader("📝 题目预览")
                for i, question in enumerate(st.session_state.questions[:5]):
                    st.write(f"{i+1}. {question}")
                if len(st.session_state.questions) > 5:
                    st.write(f"... 还有 {len(st.session_state.questions) - 5} 题")
        
        # Instructions
        st.header("📖 使用说明")
        st.markdown("""
        1. 在左侧设置中选择运算类型和数值范围
        2. 选择出题数量和批改模式
        3. 点击"开始答题"开始练习
        4. 根据选择的批改模式进行答题
        5. 完成后查看成绩和错题分析
        """)

if __name__ == "__main__":
    main() 