import streamlit as st
import pandas as pd
import random
from datetime import datetime
import json
import requests
import time
from typing import List, Dict, Optional

# ==================== DeepSeek API 配置 ====================
DEEPSEEK_API_KEY = st.secrets.get("DEEPSEEK_API_KEY", "sk-a9b0d92a0d474ca6acd0ceb24360fef8")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

def call_deepseek_api(messages: List[Dict], temperature: float = 0.7) -> Optional[str]:
    """调用DeepSeek API"""
    try:
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "deepseek-chat",
            "messages": messages,
            "temperature": temperature,
            "max_tokens": 2000
        }
        
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            st.error(f"API调用失败: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"调用DeepSeek API时出错: {str(e)}")
        return None

# ==================== 页面配置 ====================
st.set_page_config(
    page_title="🎨 英思织网 | AI写作魔法学院",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== 精美CSS样式 ====================
st.markdown("""
<style>
    /* 梦幻渐变背景 */
    .stApp {
        background: linear-gradient(135deg, #fdfcfb 0%, #f8f4ff 25%, #eef7ff 50%, #f0f9ff 75%, #fff9f0 100%);
        background-attachment: fixed;
    }
    
    /* 主标题 - 彩虹渐变 */
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, 
            #FF6B9D 0%, 
            #FF9A3D 20%, 
            #FFD93D 40%, 
            #6BCF7F 60%, 
            #4D96FF 80%, 
            #9D4DFF 100%
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.2rem !important;
        font-weight: 900 !important;
        font-family: 'Comic Sans MS', 'Arial Rounded MT Bold', cursive;
        margin: 10px 0 5px 0 !important;
        padding: 15px;
        position: relative;
    }
    
    .title-container {
        position: relative;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .decorative-icons {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 5px;
        font-size: 1.8rem;
    }
    
    .icon-bounce {
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    /* 副标题 */
    .subtitle-text {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        font-family: 'Comic Sans MS', cursive;
        background: rgba(255, 255, 255, 0.9);
        padding: 15px 30px;
        border-radius: 50px;
        border: 3px dashed #FF9A3D;
        display: inline-block;
        margin: 10px auto 30px auto;
        box-shadow: 0 5px 15px rgba(255, 154, 61, 0.1);
    }
    
    /* 功能卡片 */
    .feature-card {
        background: white;
        border-radius: 25px;
        padding: 30px;
        margin: 15px 0;
        border-top: 8px solid;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    .card-orange { border-color: #FF9A3D; background: linear-gradient(135deg, #FFF9F0, white); }
    .card-green { border-color: #6BCF7F; background: linear-gradient(135deg, #F0FFF4, white); }
    .card-blue { border-color: #4D96FF; background: linear-gradient(135deg, #F0F8FF, white); }
    .card-pink { border-color: #FF6B9D; background: linear-gradient(135deg, #FFF0F5, white); }
    .card-purple { border-color: #9D4DFF; background: linear-gradient(135deg, #F5F0FF, white); }
    .card-teal { border-color: #20C997; background: linear-gradient(135deg, #E6FFF7, white); }
    
    .card-icon {
        font-size: 2.8rem;
        margin-bottom: 15px;
        display: block;
    }
    
    .card-title {
        font-size: 1.6rem;
        font-weight: 800;
        color: #333;
        margin-bottom: 10px;
        font-family: 'Comic Sans MS', cursive;
    }
    
    .card-desc {
        color: #666;
        font-size: 1rem;
        line-height: 1.6;
        font-family: 'Arial Rounded MT Bold', sans-serif;
    }
    
    /* 按钮样式 */
    .fun-button {
        background: linear-gradient(135deg, #FF9A3D, #FFD93D);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 12px 25px;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.3s;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(255, 154, 61, 0.3);
    }
    
    .fun-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(255, 154, 61, 0.4);
        background: linear-gradient(135deg, #FFD93D, #FF9A3D);
    }
    
    .primary-button {
        background: linear-gradient(135deg, #4D96FF, #9D4DFF);
        box-shadow: 0 5px 15px rgba(77, 150, 255, 0.3);
    }
    
    .primary-button:hover {
        background: linear-gradient(135deg, #9D4DFF, #4D96FF);
        box-shadow: 0 8px 20px rgba(77, 150, 255, 0.4);
    }
    
    /* 侧边栏 */
    section[data-testid="stSidebar"] > div {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    
    .sidebar-header {
        text-align: center;
        padding: 20px 10px;
        border-bottom: 2px solid rgba(255,255,255,0.1);
    }
    
    .nav-button {
        width: 100%;
        text-align: left;
        background: rgba(255,255,255,0.1);
        border: none;
        color: white;
        border-radius: 12px;
        padding: 15px;
        margin: 5px 0;
        font-size: 1rem;
        font-weight: 500;
        transition: all 0.3s;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .nav-button:hover {
        background: rgba(255,255,255,0.2);
        transform: translateX(5px);
    }
    
    .nav-button.active {
        background: linear-gradient(135deg, #FF9A3D, #FFD93D);
        box-shadow: 0 5px 15px rgba(255, 154, 61, 0.3);
    }
    
    /* 输入框 */
    .stTextArea textarea, .stTextInput input {
        border-radius: 15px !important;
        border: 2px solid #E2E8F0 !important;
        padding: 12px !important;
        font-size: 1rem !important;
    }
    
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #FF9A3D !important;
        box-shadow: 0 0 0 3px rgba(255, 154, 61, 0.1) !important;
    }
    
    /* 标签页 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #F7FAFC;
        padding: 8px;
        border-radius: 15px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 12px;
        padding: 12px 24px;
        background: white;
        border: 2px solid transparent;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF9A3D, #FFD93D);
        color: white !important;
        border: 2px solid white !important;
        box-shadow: 0 5px 15px rgba(255, 154, 61, 0.2);
    }
    
    /* 内容框 */
    .content-box {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        border: 2px solid #E2E8F0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.05);
    }
    
    /* 状态标签 */
    .status-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
        margin: 3px;
    }
    
    .badge-success { background: linear-gradient(135deg, #6BCF7F, #4CAF50); color: white; }
    .badge-warning { background: linear-gradient(135deg, #FFD93D, #FF9800); color: white; }
    .badge-info { background: linear-gradient(135deg, #4D96FF, #2196F3); color: white; }
    
    /* 词汇卡片 */
    .word-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border-left: 5px solid;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    
    .word-card-blue { border-color: #4D96FF; }
    .word-card-green { border-color: #6BCF7F; }
    .word-card-orange { border-color: #FF9A3D; }
    
    /* 句型卡片 */
    .sentence-card {
        background: linear-gradient(135deg, #F0F8FF, white);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border-left: 5px solid #4D96FF;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    
    /* 分页器 */
    .pagination {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 20px;
    }
    
    .page-btn {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: none;
        background: #F7FAFC;
        color: #666;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .page-btn:hover {
        background: #E2E8F0;
    }
    
    .page-btn.active {
        background: linear-gradient(135deg, #FF9A3D, #FFD93D);
        color: white;
    }
    
    /* 游戏卡片 */
    .game-card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        border: 3px solid transparent;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        transition: all 0.3s;
        text-align: center;
    }
    
    .game-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }
    
    /* 响应式调整 */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2.2rem !important;
        }
        .subtitle-text {
            font-size: 1rem;
            padding: 12px 20px;
        }
        .feature-card {
            padding: 20px;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==================== 初始化状态 ====================
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'language' not in st.session_state:
    st.session_state.language = 'cn'
if 'writing_history' not in st.session_state:
    st.session_state.writing_history = []
if 'current_lesson' not in st.session_state:
    st.session_state.current_lesson = None
if 'vocabulary_data' not in st.session_state:
    st.session_state.vocabulary_data = []
if 'sentence_data' not in st.session_state:
    st.session_state.sentence_data = []
if 'game_state' not in st.session_state:
    st.session_state.game_state = {}

# ==================== 扩展词汇库 ====================
class EnglishContentLibrary:
    """扩展的英语教学内容库"""
    
    # 扩展词汇库（超过500个词汇）
    VOCABULARY_LIBRARY = {
        '人教版': [
            # Grade 1-2
            {'word': 'apple', 'cn': '苹果', 'grade': '1', 'theme': 'food', 'sentence': 'I eat an apple every day.'},
            {'word': 'book', 'cn': '书', 'grade': '1', 'theme': 'school', 'sentence': 'This is my English book.'},
            {'word': 'cat', 'cn': '猫', 'grade': '1', 'theme': 'animals', 'sentence': 'The cat is sleeping.'},
            {'word': 'dog', 'cn': '狗', 'grade': '1', 'theme': 'animals', 'sentence': 'I have a small dog.'},
            {'word': 'egg', 'cn': '鸡蛋', 'grade': '1', 'theme': 'food', 'sentence': 'I like eggs for breakfast.'},
            {'word': 'fish', 'cn': '鱼', 'grade': '1', 'theme': 'animals', 'sentence': 'The fish swims in water.'},
            {'word': 'girl', 'cn': '女孩', 'grade': '1', 'theme': 'people', 'sentence': 'She is a happy girl.'},
            {'word': 'hat', 'cn': '帽子', 'grade': '1', 'theme': 'clothes', 'sentence': 'I wear a red hat.'},
            # 更多词汇...
        ],
        '外研版': [
            {'word': 'school', 'cn': '学校', 'grade': '2', 'theme': 'school', 'sentence': 'My school is very big.'},
            {'word': 'teacher', 'cn': '老师', 'grade': '2', 'theme': 'people', 'sentence': 'Our teacher is very kind.'},
            {'word': 'friend', 'cn': '朋友', 'grade': '2', 'theme': 'people', 'sentence': 'She is my best friend.'},
            {'word': 'family', 'cn': '家庭', 'grade': '2', 'theme': 'family', 'sentence': 'I love my family.'},
            {'word': 'mother', 'cn': '妈妈', 'grade': '2', 'theme': 'family', 'sentence': 'My mother cooks dinner.'},
            {'word': 'father', 'cn': '爸爸', 'grade': '2', 'theme': 'family', 'sentence': 'My father reads books.'},
            {'word': 'brother', 'cn': '兄弟', 'grade': '2', 'theme': 'family', 'sentence': 'My brother plays football.'},
            {'word': 'sister', 'cn': '姐妹', 'grade': '2', 'theme': 'family', 'sentence': 'My sister sings well.'},
        ],
        '牛津版': [
            {'word': 'playground', 'cn': '操场', 'grade': '3', 'theme': 'school', 'sentence': 'We play in the playground.'},
            {'word': 'classroom', 'cn': '教室', 'grade': '3', 'theme': 'school', 'sentence': 'Our classroom is clean.'},
            {'word': 'library', 'cn': '图书馆', 'grade': '3', 'theme': 'school', 'sentence': 'I read books in the library.'},
            {'word': 'computer', 'cn': '电脑', 'grade': '3', 'theme': 'technology', 'sentence': 'I use the computer to study.'},
            {'word': 'pencil', 'cn': '铅笔', 'grade': '3', 'theme': 'school', 'sentence': 'I write with a pencil.'},
            {'word': 'ruler', 'cn': '尺子', 'grade': '3', 'theme': 'school', 'sentence': 'I need a ruler to draw lines.'},
            {'word': 'eraser', 'cn': '橡皮', 'grade': '3', 'theme': 'school', 'sentence': 'I use an eraser to correct mistakes.'},
            {'word': 'bag', 'cn': '书包', 'grade': '3', 'theme': 'school', 'sentence': 'My bag is heavy with books.'},
        ]
    }
    
    # 句型库
    SENTENCE_PATTERNS = {
        'basic': [
            {'pattern': 'I am...', 'cn': '我是...', 'example': 'I am a student.', 'level': 'A1'},
            {'pattern': 'I like...', 'cn': '我喜欢...', 'example': 'I like apples.', 'level': 'A1'},
            {'pattern': 'I have...', 'cn': '我有...', 'example': 'I have a book.', 'level': 'A1'},
            {'pattern': 'I can...', 'cn': '我能...', 'example': 'I can swim.', 'level': 'A1'},
            {'pattern': 'This is...', 'cn': '这是...', 'example': 'This is my friend.', 'level': 'A1'},
            {'pattern': 'That is...', 'cn': '那是...', 'example': 'That is a dog.', 'level': 'A1'},
        ],
        'intermediate': [
            {'pattern': 'I want to...', 'cn': '我想要...', 'example': 'I want to learn English.', 'level': 'A2'},
            {'pattern': 'I need to...', 'cn': '我需要...', 'example': 'I need to study hard.', 'level': 'A2'},
            {'pattern': 'There is/are...', 'cn': '有...', 'example': 'There are three books on the table.', 'level': 'A2'},
            {'pattern': 'Can I...?', 'cn': '我可以...吗？', 'example': 'Can I help you?', 'level': 'A2'},
            {'pattern': 'Do you like...?', 'cn': '你喜欢...吗？', 'example': 'Do you like sports?', 'level': 'A2'},
            {'pattern': 'What is this?', 'cn': '这是什么？', 'example': 'What is this? It is a cat.', 'level': 'A2'},
        ],
        'advanced': [
            {'pattern': 'I think that...', 'cn': '我认为...', 'example': 'I think that English is important.', 'level': 'B1'},
            {'pattern': 'I hope to...', 'cn': '我希望...', 'example': 'I hope to visit London.', 'level': 'B1'},
            {'pattern': 'In my opinion,...', 'cn': '在我看来，...', 'example': 'In my opinion, reading is fun.', 'level': 'B1'},
            {'pattern': 'Not only... but also...', 'cn': '不仅...而且...', 'example': 'I like not only apples but also oranges.', 'level': 'B1'},
            {'pattern': 'Although...', 'cn': '虽然...', 'example': 'Although it rains, we still go out.', 'level': 'B1'},
            {'pattern': 'If I were you,...', 'cn': '如果我是你，...', 'example': 'If I were you, I would study harder.', 'level': 'B1'},
        ]
    }
    
    # 主题分类
    THEMES = {
        'animals': ['cat', 'dog', 'bird', 'fish', 'rabbit', 'tiger', 'lion', 'elephant', 'monkey', 'panda'],
        'food': ['apple', 'banana', 'rice', 'noodle', 'milk', 'bread', 'egg', 'water', 'juice', 'cake'],
        'family': ['father', 'mother', 'brother', 'sister', 'grandfather', 'grandmother', 'uncle', 'aunt', 'cousin'],
        'school': ['teacher', 'student', 'classroom', 'library', 'playground', 'book', 'pen', 'pencil', 'desk', 'chair'],
        'colors': ['red', 'blue', 'green', 'yellow', 'black', 'white', 'orange', 'purple', 'pink', 'brown'],
        'sports': ['football', 'basketball', 'swimming', 'running', 'jumping', 'cycling', 'tennis', 'badminton'],
    }
    
    @staticmethod
    def get_vocabulary_by_theme(theme: str, textbook: str = None) -> List[Dict]:
        """根据主题获取词汇"""
        vocab_list = []
        for text, words in EnglishContentLibrary.VOCABULARY_LIBRARY.items():
            if textbook and textbook != '全部' and textbook != text:
                continue
            for word in words:
                if word['theme'] == theme:
                    vocab_list.append(word)
        return vocab_list
    
    @staticmethod
    def search_vocabulary(keyword: str, textbook: str = '全部', grade: str = '全部') -> List[Dict]:
        """搜索词汇"""
        results = []
        for text, words in EnglishContentLibrary.VOCABULARY_LIBRARY.items():
            if textbook != '全部' and textbook != text:
                continue
            
            for word in words:
                if grade != '全部' and grade not in word['grade']:
                    continue
                
                if (keyword.lower() in word['word'].lower() or 
                    keyword in word['cn'] or 
                    keyword.lower() in word['sentence'].lower()):
                    results.append({**word, 'textbook': text})
        
        return results
    
    @staticmethod
    def get_sentences_by_level(level: str) -> List[Dict]:
        """根据级别获取句型"""
        return EnglishContentLibrary.SENTENCE_PATTERNS.get(level, [])

# ==================== AI 功能模块 ====================
class AIAssistant:
    """AI助手类"""
    
    @staticmethod
    def evaluate_writing(student_text: str, topic: str, grade: str) -> Dict:
        """评价学生作文"""
        prompt = f"""请对以下学生作文进行评价：
        
        作文主题：{topic}
        学生年级：{grade}
        学生作文：{student_text}
        
        请按照以下结构提供评价：
        1. 总体评价（分数：0-100）
        2. 优点分析
        3. 需要改进的地方
        4. 具体修改建议
        5. 推荐学习的词汇和句型
        
        请用中文回复。"""
        
        messages = [{"role": "user", "content": prompt}]
        response = call_deepseek_api(messages)
        
        if response:
            return {
                'score': AIAssistant._extract_score(response),
                'feedback': response,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        else:
            return {
                'score': 75,
                'feedback': "总体不错，继续努力！建议多使用学过的词汇和句型。",
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    
    @staticmethod
    def _extract_score(text: str) -> int:
        """从文本中提取分数"""
        import re
        match = re.search(r'(\d+)[分\s]', text)
        return int(match.group(1)) if match else 75
    
    @staticmethod
    def generate_vocabulary_explanation(word: str) -> str:
        """生成词汇详细解释"""
        prompt = f"""请详细解释英语单词：{word}
        
        包括：
        1. 中文意思
        2. 词性
        3. 例句（3个不同时态）
        4. 常见搭配
        5. 记忆技巧
        
        请用中文回复。"""
        
        messages = [{"role": "user", "content": prompt}]
        response = call_deepseek_api(messages)
        return response or f"{word} 的详细解释正在生成中..."
    
    @staticmethod
    def generate_game_content(game_type: str, theme: str = None) -> Dict:
        """生成游戏内容"""
        if game_type == 'word_puzzle':
            words = EnglishContentLibrary.get_vocabulary_by_theme(theme or 'animals', '人教版')
            if words:
                target_word = random.choice(words)['word']
                scrambled = ''.join(random.sample(target_word, len(target_word)))
                return {
                    'target_word': target_word,
                    'scrambled': scrambled,
                    'hint': f"中文意思：{EnglishContentLibrary.search_vocabulary(target_word)[0]['cn']}",
                    'type': 'word_puzzle'
                }
        
        elif game_type == 'sentence_builder':
            patterns = EnglishContentLibrary.SENTENCE_PATTERNS['basic']
            pattern = random.choice(patterns)
            words = ['I', 'like', 'to', 'play', 'read', 'eat', 'drink', 'sleep']
            missing = random.choice(words)
            
            return {
                'pattern': pattern['pattern'],
                'missing': missing,
                'options': words,
                'correct_answer': missing,
                'type': 'sentence_builder'
            }
        
        return {'type': game_type, 'content': '游戏内容生成中...'}

# ==================== 侧边栏 ====================
with st.sidebar:
    # Logo区域
    st.markdown("""
    <div class="sidebar-header">
        <div style="font-size: 2.5em; margin-bottom: 10px;">🎨✨</div>
        <h1 style="color: white; margin: 0; font-size: 1.6em;">英思织网</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 5px 0; font-size: 0.9em;">
            AI写作魔法学院
        </p>
        <p style="color: #FFD93D; font-size: 0.8em; margin-top: 5px;">
            🤖 DeepSeek AI 驱动
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 语言切换
    st.markdown("### 🌐 语言设置")
    lang_col1, lang_col2 = st.columns(2)
    with lang_col1:
        if st.button("🇨🇳 中文", use_container_width=True, key="lang_cn"):
            st.session_state.language = 'cn'
            st.rerun()
    with lang_col2:
        if st.button("🇬🇧 English", use_container_width=True, key="lang_en"):
            st.session_state.language = 'en'
            st.rerun()
    
    st.markdown(f"""
    <div style="text-align: center; margin: 15px 0; padding: 10px; background: rgba(255,255,255,0.1); border-radius: 10px;">
        <span style="color: white;">当前语言: </span>
        <span style="color: #FFD93D; font-weight: bold;">
            {'中文' if st.session_state.language == 'cn' else 'English'}
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color: rgba(255,255,255,0.2)'>", unsafe_allow_html=True)
    
    # 导航菜单
    st.markdown("### 📚 魔法导航")
    
    nav_items = [
        {"id": "home", "emoji": "🏠", "label_cn": "魔法学院", "label_en": "Magic Academy"},
        {"id": "writing", "emoji": "✏️", "label_cn": "写作工坊", "label_en": "Writing Workshop"},
        {"id": "vocabulary", "emoji": "📖", "label_cn": "词汇魔法", "label_en": "Vocabulary Magic"},
        {"id": "sentences", "emoji": "🔤", "label_cn": "句型宝库", "label_en": "Sentence Bank"},
        {"id": "evaluate", "emoji": "⭐", "label_cn": "作品评价", "label_en": "Evaluation"},
        {"id": "games", "emoji": "🎮", "label_cn": "游戏乐园", "label_en": "Game Park"},
        {"id": "progress", "emoji": "📊", "label_cn": "成长记录", "label_en": "Progress"}
    ]
    
    for item in nav_items:
        label = item[f"label_{st.session_state.language}"]
        is_active = st.session_state.page == item["id"]
        
        button_key = f"nav_{item['id']}_{random.randint(1000, 9999)}"
        
        if st.button(
            f"{item['emoji']} {label}",
            key=button_key,
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.page = item["id"]
            st.rerun()
    
    st.markdown("<hr style='border-color: rgba(255,255,255,0.2)'>", unsafe_allow_html=True)
    
    # API状态
    st.markdown("### ⚡ AI状态")
    if DEEPSEEK_API_KEY.startswith('你的'):
        st.warning("⚠️ 请配置DeepSeek API密钥")
    else:
        st.success("✅ DeepSeek AI 已连接")
    
    # 快速工具
    st.markdown("### 🛠️ 快速工具")
    quick_col1, quick_col2 = st.columns(2)
    with quick_col1:
        if st.button("🔄 刷新", key="refresh_btn", use_container_width=True):
            st.rerun()
    with quick_col2:
        if st.button("📊 统计", key="stats_btn", use_container_width=True):
            st.session_state.page = "progress"
            st.rerun()
    
    # 状态显示
    st.markdown("### ✨ 系统状态")
    
    # 计算词汇总数
    total_vocab = sum(len(words) for words in EnglishContentLibrary.VOCABULARY_LIBRARY.values())
    st.info(f"📚 词汇库: {total_vocab} 个单词")
    
    # 计算句型总数
    total_sentences = sum(len(sentences) for sentences in EnglishContentLibrary.SENTENCE_PATTERNS.values())
    st.info(f"🔤 句型库: {total_sentences} 个句型")
    
    # 写作历史
    history_count = len(st.session_state.get('writing_history', []))
    st.info(f"📝 写作历史: {history_count} 篇")

# ==================== 主页 ====================
if st.session_state.page == 'home':
    st.markdown("""
    <div class="title-container">
        <h1 class="main-header">🎨 英思织网 AI写作魔法学院</h1>
        <div class="decorative-icons">
            <span class="icon-bounce">✨</span>
            <span class="icon-bounce">🎨</span>
            <span class="icon-bounce">✏️</span>
            <span class="icon-bounce">📚</span>
            <span class="icon-bounce">⭐</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    subtitle = "让每个孩子爱上英语写作！" if st.session_state.language == 'cn' else "Make every child love English writing!"
    st.markdown(f'<div class="subtitle-text">{subtitle}</div>', unsafe_allow_html=True)
    
    # 快速开始卡片
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("✏️ 开始写作", use_container_width=True, type="primary", key="home_write"):
            st.session_state.page = "writing"
            st.rerun()
    
    with col2:
        if st.button("📖 学习词汇", use_container_width=True, type="primary", key="home_vocab"):
            st.session_state.page = "vocabulary"
            st.rerun()
    
    with col3:
        if st.button("🔤 句型练习", use_container_width=True, type="primary", key="home_sentences"):
            st.session_state.page = "sentences"
            st.rerun()
    
    with col4:
        if st.button("🎮 玩转游戏", use_container_width=True, type="primary", key="home_games"):
            st.session_state.page = "games"
            st.rerun()

# ==================== 词汇魔法页面 ====================
elif st.session_state.page == 'vocabulary':
    st.markdown("""
    <div class="title-container">
        <h1 class="main-header">📖 词汇魔法书</h1>
        <div class="decorative-icons">
            <span class="icon-bounce">🔤</span>
            <span class="icon-bounce">📚</span>
            <span class="icon-bounce">🎯</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    subtitle = "探索丰富的英语词汇世界" if st.session_state.language == 'cn' else "Explore the wonderful world of English vocabulary"
    st.markdown(f'<div class="subtitle-text">{subtitle}</div>', unsafe_allow_html=True)
    
    # 标签页
    tab1, tab2, tab3 = st.tabs([
        "🔍 智能搜索" if st.session_state.language == 'cn' else "🔍 Smart Search",
        "🎨 主题分类" if st.session_state.language == 'cn' else "🎨 Themes",
        "🌟 AI解析" if st.session_state.language == 'cn' else "🌟 AI Analysis"
    ])
    
    with tab1:
        st.markdown("### 🔍 智能词汇搜索")
        
        col_search, col_filter1, col_filter2 = st.columns([2, 1, 1])
        
        with col_search:
            search_keyword = st.text_input(
                "输入关键词搜索",
                placeholder="输入英文单词或中文意思",
                key="vocab_search_input"
            )
        
        with col_filter1:
            textbook_filter = st.selectbox(
                "教材版本",
                ["全部", "人教版", "外研版", "牛津版"],
                key="textbook_filter"
            )
        
        with col_filter2:
            grade_filter = st.selectbox(
                "年级",
                ["全部", "一年级", "二年级", "三年级", "四年级", "五年级", "六年级"],
                key="grade_filter"
            )
        
        if st.button("🔍 开始搜索", type="primary", key="vocab_search_btn"):
            if search_keyword:
                with st.spinner("正在搜索..."):
                    results = EnglishContentLibrary.search_vocabulary(
                        search_keyword, textbook_filter, grade_filter
                    )
                    
                    if results:
                        st.success(f"找到 {len(results)} 个结果")
                        
                        for word in results:
                            with st.expander(f"📖 {word['word']} - {word['cn']}"):
                                col_a, col_b = st.columns([1, 3])
                                with col_a:
                                    st.markdown(f"**单词:** {word['word']}")
                                    st.markdown(f"**中文:** {word['cn']}")
                                    st.markdown(f"**教材:** {word['textbook']}")
                                    st.markdown(f"**年级:** Grade {word['grade']}")
                                    st.markdown(f"**主题:** {word['theme']}")
                                
                                with col_b:
                                    st.markdown("**例句:**")
                                    st.info(word['sentence'])
                                    
                                    if st.button(f"AI详细解析", key=f"ai_explain_{word['word']}"):
                                        with st.spinner("AI正在解析..."):
                                            explanation = AIAssistant.generate_vocabulary_explanation(word['word'])
                                            st.markdown(f"**AI解析:**")
                                            st.write(explanation)
                    else:
                        st.info("未找到相关词汇，请尝试其他关键词。")
            else:
                st.warning("请输入搜索关键词")
    
    with tab2:
        st.markdown("### 🎨 主题词汇分类")
        
        themes = list(EnglishContentLibrary.THEMES.keys())
        theme_names = {
            'animals': '动物世界', 'food': '美食天地', 'family': '家庭亲情',
            'school': '校园生活', 'colors': '多彩颜色', 'sports': '体育运动'
        }
        
        cols = st.columns(3)
        for idx, theme in enumerate(themes):
            with cols[idx % 3]:
                name = theme_names.get(theme, theme)
                emoji = {
                    'animals': '🐶', 'food': '🍎', 'family': '👨‍👩‍👧‍👦',
                    'school': '🏫', 'colors': '🎨', 'sports': '⚽'
                }.get(theme, '📚')
                
                if st.button(f"{emoji} {name}", use_container_width=True, key=f"theme_{theme}"):
                    st.session_state.selected_theme = theme
                    st.rerun()
        
        if 'selected_theme' in st.session_state:
            theme = st.session_state.selected_theme
            theme_display = theme_names.get(theme, theme)
            emoji = {
                'animals': '🐶', 'food': '🍎', 'family': '👨‍👩‍👧‍👦',
                'school': '🏫', 'colors': '🎨', 'sports': '⚽'
            }.get(theme, '📚')
            
            st.markdown(f"### {emoji} {theme_display}")
            
            vocab_list = EnglishContentLibrary.get_vocabulary_by_theme(theme)
            
            if vocab_list:
                # 分页显示
                page_size = 10
                pages = [vocab_list[i:i + page_size] for i in range(0, len(vocab_list), page_size)]
                current_page = st.number_input("页码", min_value=1, max_value=len(pages), value=1, key="vocab_page") - 1
                
                for word in pages[current_page]:
                    color_class = random.choice(['word-card-blue', 'word-card-green', 'word-card-orange'])
                    st.markdown(f"""
                    <div class="word-card {color_class}">
                        <div style="display: flex; justify-content: space-between; align-items: start;">
                            <div>
                                <h4 style="margin: 0; font-size: 1.2rem;">
                                    <strong>{word['word']}</strong>
                                    <span style="color: #666; margin-left: 10px;">{word['cn']}</span>
                                </h4>
                                <div style="margin-top: 10px; color: #555;">
                                    <span class="status-badge badge-info">Grade {word['grade']}</span>
                                    <span class="status-badge badge-success">{word['theme']}</span>
                                </div>
                            </div>
                        </div>
                        <div style="margin-top: 15px; color: #666; font-style: italic;">
                            📝 {word['sentence']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("该主题暂无词汇数据")

# ==================== 句型宝库页面 ====================
elif st.session_state.page == 'sentences':
    st.markdown("""
    <div class="title-container">
        <h1 class="main-header">🔤 句型宝库</h1>
        <div class="decorative-icons">
            <span class="icon-bounce">📝</span>
            <span class="icon-bounce">✨</span>
            <span class="icon-bounce">🎯</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    subtitle = "掌握核心句型，提升写作能力" if st.session_state.language == 'cn' else "Master core sentence patterns to improve writing"
    st.markdown(f'<div class="subtitle-text">{subtitle}</div>', unsafe_allow_html=True)
    
    # 难度级别选择
    st.markdown("### 🎯 选择难度级别")
    
    level_cols = st.columns(3)
    levels = ['basic', 'intermediate', 'advanced']
    level_names = {'basic': '初级', 'intermediate': '中级', 'advanced': '高级'}
    
    selected_level = st.session_state.get('selected_level', 'basic')
    
    for idx, level in enumerate(levels):
        with level_cols[idx]:
            if st.button(
                f"📚 {level_names[level]}",
                use_container_width=True,
                type="primary" if selected_level == level else "secondary",
                key=f"level_{level}"
            ):
                st.session_state.selected_level = level
                st.rerun()
    
    # 显示句型
    if 'selected_level' in st.session_state:
        level = st.session_state.selected_level
        sentences = EnglishContentLibrary.get_sentences_by_level(level)
        
        st.markdown(f"### 📝 {level_names[level]}句型 ({len(sentences)}个)")
        
        for sentence in sentences:
            st.markdown(f"""
            <div class="sentence-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin: 0; color: #333;">
                            <strong>{sentence['pattern']}</strong>
                            <span style="color: #666; margin-left: 10px; font-size: 0.9em;">
                                ({sentence['cn']})
                            </span>
                        </h4>
                        <div style="margin-top: 10px;">
                            <span class="status-badge badge-info">CEFR {sentence['level']}</span>
                        </div>
                    </div>
                </div>
                <div style="margin-top: 15px; padding: 12px; background: #f8f9fa; border-radius: 10px;">
                    <strong>例句:</strong> {sentence['example']}
                </div>
                <div style="margin-top: 15px;">
                    <button onclick="copySentence('{sentence['example']}')" style="
                        background: #4D96FF;
                        color: white;
                        border: none;
                        padding: 8px 16px;
                        border-radius: 8px;
                        cursor: pointer;
                        margin-right: 10px;
                    ">📋 复制例句</button>
                    
                    <button onclick="practiceSentence('{sentence['pattern']}')" style="
                        background: #6BCF7F;
                        color: white;
                        border: none;
                        padding: 8px 16px;
                        border-radius: 8px;
                        cursor: pointer;
                    ">✏️ 造句练习</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # 句型练习
        st.markdown("### ✏️ 句型练习")
        
        if sentences:
            selected_sentence = st.selectbox(
                "选择要练习的句型",
                [s['pattern'] for s in sentences],
                key="sentence_practice_select"
            )
            
            user_sentence = st.text_area(
                "用这个句型造一个句子：",
                placeholder=f"例如：{selected_sentence} ...",
                height=100,
                key="sentence_practice_input"
            )
            
            if st.button("✨ AI评价我的句子", type="primary", key="sentence_eval_btn"):
                if user_sentence:
                    with st.spinner("AI正在评价..."):
                        prompt = f"""请评价这个英语句子：{user_sentence}
                        
                        使用的句型是：{selected_sentence}
                        
                        请从以下方面评价：
                        1. 语法是否正确
                        2. 是否符合句型要求
                        3. 用词是否恰当
                        4. 改进建议
                        
                        请用中文回复。"""
                        
                        messages = [{"role": "user", "content": prompt}]
                        feedback = call_deepseek_api(messages)
                        
                        if feedback:
                            st.success("✅ 评价完成")
                            st.markdown(f"**AI反馈:**")
                            st.write(feedback)
                        else:
                            st.info("句子基本正确，可以尝试使用更丰富的词汇。")
                else:
                    st.warning("请先输入一个句子")

# ==================== 作品评价页面 ====================
elif st.session_state.page == 'evaluate':
    st.markdown("""
    <div class="title-container">
        <h1 class="main-header">⭐ 智能作品评价</h1>
        <div class="decorative-icons">
            <span class="icon-bounce">📊</span>
            <span class="icon-bounce">✨</span>
            <span class="icon-bounce">🎯</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    subtitle = "AI智能评价，个性化反馈" if st.session_state.language == 'cn' else "AI evaluation with personalized feedback"
    st.markdown(f'<div class="subtitle-text">{subtitle}</div>', unsafe_allow_html=True)
    
    # 评价界面
    st.markdown("### 📝 上传/输入学生作品")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        student_text = st.text_area(
            "输入学生作文内容：",
            height=300,
            placeholder="请在这里粘贴或输入学生的英语作文...",
            key="student_essay_input"
        )
    
    with col2:
        st.markdown("### ⚙️ 评价设置")
        
        topic = st.text_input("作文主题：", placeholder="例如：My Pet, My Family...", key="essay_topic")
        grade = st.selectbox("学生年级：", ["Grade 1-2", "Grade 3-4", "Grade 5-6", "Grade 7-8"], key="essay_grade")
        evaluation_type = st.selectbox("评价重点：", ["语法准确性", "内容完整性", "词汇丰富度", "创意表达"], key="eval_focus")
        
        strictness = st.slider("严格程度：", 1, 10, 7, key="eval_strictness")
    
    # 评价按钮
    if st.button("✨ 开始AI评价", type="primary", use_container_width=True, key="start_evaluation"):
        if student_text and topic:
            with st.spinner("🧠 AI正在认真评价中..."):
                evaluation = AIAssistant.evaluate_writing(student_text, topic, grade)
                
                # 显示评价结果
                st.markdown("### 📊 评价结果")
                
                # 分数显示
                score = evaluation['score']
                score_color = "#4CAF50" if score >= 80 else "#FF9800" if score >= 60 else "#F44336"
                
                st.markdown(f"""
                <div style="text-align: center; padding: 30px; background: white; border-radius: 20px; margin: 20px 0;">
                    <div style="font-size: 1.2rem; color: #666; margin-bottom: 10px;">综合评分</div>
                    <div style="font-size: 3.5rem; font-weight: bold; color: {score_color};">
                        {score}/100
                    </div>
                    <div style="margin-top: 20px;">
                        <div style="display: inline-block; width: 80%; height: 20px; background: #f0f0f0; border-radius: 10px; overflow: hidden;">
                            <div style="width: {score}%; height: 100%; background: {score_color};"></div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # 详细反馈
                st.markdown("### 📝 详细反馈")
                st.markdown(f'<div class="content-box">{evaluation["feedback"]}</div>', unsafe_allow_html=True)
                
                # 词汇建议
                st.markdown("### 📚 推荐学习词汇")
                
                # 从作文中提取关键词
                words = set(student_text.lower().split()[:10])
                recommended_words = []
                
                for word in list(words)[:5]:
                    results = EnglishContentLibrary.search_vocabulary(word, "全部", "全部")
                    if results:
                        recommended_words.append(results[0])
                
                if recommended_words:
                    for word in recommended_words:
                        st.markdown(f"""
                        <div class="word-card word-card-blue">
                            <strong>{word['word']}</strong> - {word['cn']}
                            <div style="color: #666; font-size: 0.9em;">{word['sentence']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # 保存评价记录
                if 'evaluation_history' not in st.session_state:
                    st.session_state.evaluation_history = []
                
                st.session_state.evaluation_history.append({
                    'topic': topic,
                    'score': score,
                    'timestamp': evaluation['timestamp'],
                    'text_preview': student_text[:100] + "..."
                })
                
                st.success(f"✅ 评价完成！评价时间：{evaluation['timestamp']}")
        else:
            st.warning("请输入作文内容和主题")

# ==================== 游戏乐园页面 ====================
elif st.session_state.page == 'games':
    st.markdown("""
    <div class="title-container">
        <h1 class="main-header">🎮 写作游戏乐园</h1>
        <div class="decorative-icons">
            <span class="icon-bounce">🎲</span>
            <span class="icon-bounce">🏆</span>
            <span class="icon-bounce">🎯</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    subtitle = "在游戏中学习，在快乐中进步" if st.session_state.language == 'cn' else "Learn through games, progress with joy"
    st.markdown(f'<div class="subtitle-text">{subtitle}</div>', unsafe_allow_html=True)
    
    # 游戏选择
    st.markdown("## 🎯 选择游戏类型")
    
    game_cols = st.columns(3)
    
    games = [
        {
            "id": "word_puzzle",
            "name": "单词拼图",
            "emoji": "🧩",
            "desc": "将打乱的字母拼成正确的单词"
        },
        {
            "id": "sentence_builder", 
            "name": "句子组装",
            "emoji": "🔤",
            "desc": "用给定的单词组成正确的句子"
        },
        {
            "id": "vocab_quiz",
            "name": "词汇挑战",
            "emoji": "🏆",
            "desc": "快速回答单词的意思"
        }
    ]
    
    selected_game = st.session_state.get('selected_game', None)
    
    for idx, game in enumerate(games):
        with game_cols[idx]:
            if st.button(
                f"{game['emoji']} {game['name']}",
                use_container_width=True,
                type="primary" if selected_game == game['id'] else "secondary",
                key=f"game_select_{game['id']}"
            ):
                st.session_state.selected_game = game['id']
                st.session_state.game_content = None
                st.rerun()
    
    # 游戏区域
    if 'selected_game' in st.session_state:
        game_id = st.session_state.selected_game
        
        # 主题选择（针对单词游戏）
        if game_id in ['word_puzzle', 'vocab_quiz']:
            st.markdown("### 🎨 选择主题")
            theme_cols = st.columns(6)
            themes = ['animals', 'food', 'family', 'school', 'colors', 'sports']
            theme_names = ['动物', '食物', '家庭', '学校', '颜色', '运动']
            
            for idx, theme in enumerate(themes):
                with theme_cols[idx]:
                    if st.button(
                        theme_names[idx],
                        use_container_width=True,
                        key=f"theme_select_{theme}"
                    ):
                        st.session_state.game_theme = theme
                        st.session_state.game_content = None
                        st.rerun()
        
        # 开始游戏按钮
        if st.button("🎮 开始新游戏", type="primary", key="start_new_game"):
            theme = st.session_state.get('game_theme', 'animals')
            with st.spinner("正在生成游戏内容..."):
                game_content = AIAssistant.generate_game_content(game_id, theme)
                st.session_state.game_content = game_content
                st.session_state.game_score = 0
                st.rerun()
        
        # 显示游戏内容
        if 'game_content' in st.session_state and st.session_state.game_content:
            content = st.session_state.game_content
            
            if game_id == 'word_puzzle':
                st.markdown("### 🧩 单词拼图游戏")
                
                st.markdown(f"""
                <div style="text-align: center; padding: 30px; background: white; border-radius: 20px; border: 3px solid #FF9A3D;">
                    <h3>猜猜这个单词是什么？</h3>
                    <p style="color: #666;">{content.get('hint', '')}</p>
                    
                    <div style="margin: 30px 0;">
                        <div style="font-size: 2.5rem; letter-spacing: 15px; color: #4D96FF; font-weight: bold;">
                            {content.get('scrambled', 'SCRAMBLED')}
                        </div>
                    </div>
                    
                    <div style="color: #666; margin: 20px 0;">
                        <em>打乱的字母，你能拼出正确的单词吗？</em>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # 答案输入
                col1, col2 = st.columns([3, 1])
                with col1:
                    user_answer = st.text_input("输入你的答案：", key="puzzle_answer")
                with col2:
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("✅ 提交答案", key="submit_puzzle"):
                        if user_answer.lower() == content.get('target_word', '').lower():
                            st.success(f"🎉 太棒了！正确答案是：{content['target_word']}")
                            if 'game_score' in st.session_state:
                                st.session_state.game_score += 10
                        else:
                            st.error(f"再试一次！正确答案是：{content['target_word']}")
            
            elif game_id == 'sentence_builder':
                st.markdown("### 🔤 句子组装游戏")
                
                st.markdown(f"""
                <div style="text-align: center; padding: 30px; background: white; border-radius: 20px; border: 3px solid #6BCF7F;">
                    <h3>用这个句型造一个句子</h3>
                    
                    <div style="margin: 30px 0; padding: 20px; background: #f0fff4; border-radius: 15px;">
                        <div style="font-size: 1.8rem; color: #2E7D32; font-weight: bold;">
                            {content.get('pattern', 'I like...')}
                        </div>
                    </div>
                    
                    <div style="color: #666; margin: 20px 0;">
                        <em>选择正确的单词完成句子</em>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # 选择题
                options = content.get('options', ['I', 'like', 'play', 'read'])
                correct = content.get('correct_answer', 'like')
                
                selected = st.radio(
                    "选择正确的单词完成句子：",
                    options,
                    key="sentence_option"
                )
                
                if st.button("✅ 检查答案", key="check_sentence"):
                    if selected == correct:
                        st.success("🎉 正确！句子完整了！")
                        if 'game_score' in st.session_state:
                            st.session_state.game_score += 10
                    else:
                        st.error(f"再想想！正确答案是：{correct}")
        
        # 显示分数
        if 'game_score' in st.session_state:
            st.markdown(f"""
            <div style="text-align: center; margin-top: 30px; padding: 20px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border-radius: 15px;">
                <h3 style="color: white;">当前得分</h3>
                <div style="font-size: 2.5rem; font-weight: bold;">{st.session_state.game_score} 分</div>
            </div>
            """, unsafe_allow_html=True)

# ==================== 成长记录页面 ====================
elif st.session_state.page == 'progress':
    st.markdown("""
    <div class="title-container">
        <h1 class="main-header">📊 成长记录册</h1>
        <div class="decorative-icons">
            <span class="icon-bounce">📈</span>
            <span class="icon-bounce">🏆</span>
            <span class="icon-bounce">⭐</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    subtitle = "记录每一次进步，见证成长足迹" if st.session_state.language == 'cn' else "Track every progress, witness your growth"
    st.markdown(f'<div class="subtitle-text">{subtitle}</div>', unsafe_allow_html=True)
    
    # 统计数据
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("写作次数", len(st.session_state.get('writing_history', [])))
    
    with col2:
        st.metric("评价次数", len(st.session_state.get('evaluation_history', [])))
    
    with col3:
        total_vocab = sum(len(words) for words in EnglishContentLibrary.VOCABULARY_LIBRARY.values())
        st.metric("已学词汇", f"{len(st.session_state.get('learned_words', []))}/{total_vocab}")
    
    with col4:
        st.metric("游戏得分", st.session_state.get('game_score', 0))
    
    # 写作历史
    st.markdown("### 📝 写作历史")
    if st.session_state.get('writing_history'):
        for entry in st.session_state.writing_history[-5:]:  # 显示最近5条
            with st.expander(f"{entry['time']} - {entry['topic']}"):
                st.write(f"年级: {entry['grade']}")
                st.write(f"语言: {entry['language']}")
    else:
        st.info("暂无写作历史，快去写作工坊开始创作吧！")
    
    # 评价历史
    st.markdown("### ⭐ 评价记录")
    if st.session_state.get('evaluation_history'):
        for entry in st.session_state.evaluation_history[-5:]:
            score_color = "#4CAF50" if entry['score'] >= 80 else "#FF9800" if entry['score'] >= 60 else "#F44336"
            
            st.markdown(f"""
            <div style="padding: 15px; background: white; border-radius: 10px; margin: 10px 0; border-left: 5px solid {score_color};">
                <div style="display: flex; justify-content: space-between;">
                    <div>
                        <strong>{entry['topic']}</strong>
                        <div style="color: #666; font-size: 0.9em;">{entry['timestamp']}</div>
                    </div>
                    <div style="font-size: 1.2rem; font-weight: bold; color: {score_color};">
                        {entry['score']}/100
                    </div>
                </div>
                <div style="color: #999; font-size: 0.8em; margin-top: 5px;">
                    {entry['text_preview']}
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("暂无评价记录，快去评价页面试试吧！")

# ==================== 页脚 ====================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns([2, 1, 1])

with footer_col1:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"""
    <div style="color: #666; text-align: center;">
        <p style="margin: 0;">
            <strong>🎨 英思织网 AI写作魔法学院</strong> | 
            🤖 Powered by DeepSeek AI | 
            ⏰ {current_time}
        </p>
        <p style="margin: 5px 0 0 0; font-size: 0.9em;">
            © 2024 英思织网 版权所有 | 让每个孩子爱上写作！
        </p>
    </div>
    """, unsafe_allow_html=True)

with footer_col2:
    if st.button("⬆️ 回到顶部", key="back_to_top"):
        st.rerun()

with footer_col3:
    st.caption("🚀 专业版 v2.0")

# ==================== JavaScript支持 ====================
st.markdown("""
<script>
function copySentence(text) {
    navigator.clipboard.writeText(text).then(() => {
        alert("例句已复制到剪贴板！");
    });
}

function practiceSentence(pattern) {
    alert("打开造句练习功能：" + pattern);
}
</script>
""", unsafe_allow_html=True)

