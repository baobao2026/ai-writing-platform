import streamlit as st
import pandas as pd
import random
from datetime import datetime
import json

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

# ==================== 内置教学内容库 ====================
class EnglishContentLibrary:
    """内置英语教学内容库（完全免API）"""
    
    WRITING_LESSONS = {
        'animals': {
            'title_cn': '我的宠物朋友',
            'title_en': 'My Pet Friend',
            'content_cn': """
# 🐶 我的宠物朋友 - 写作教案

## 📝 学习目标
1. 学习描述动物的外貌特征
2. 掌握表达情感的词汇
3. 能够写一篇关于宠物的短文

## 🎯 重点词汇
- **外貌**: fluffy (毛茸茸的), furry (毛绒的), cute (可爱的), tiny (小小的)
- **动作**: run (跑), jump (跳), play (玩), sleep (睡觉)
- **情感**: happy (开心的), friendly (友好的), lovely (可爱的)

## ✍️ 写作结构
1. **开头**: 介绍你的宠物
   - I have a pet. It is a...
   - My pet's name is...

2. **中间**: 描述宠物特点
   - It is... (颜色/大小)
   - It has... (外貌特征)
   - It likes to... (喜好)

3. **结尾**: 表达感情
   - I love my pet.
   - My pet makes me happy.

## 📖 范文示例
My pet is a small dog. His name is Coco. He is brown and white. Coco has big eyes and a long tail. He likes to play with balls. Every day, I play with him in the park. Coco is my best friend. I love him very much.

## 🎮 写作练习
1. 画一张你的宠物图片
2. 写出5个描述宠物的词
3. 写一篇关于宠物的短文（5句话）

## 🏆 评价标准
✅ 使用正确单词（15分）
✅ 句子通顺（15分）
✅ 情感表达（10分）
✅ 创意加分（10分）
            """,
            'content_en': """
# 🐶 My Pet Friend - Writing Lesson

## 📝 Learning Objectives
1. Learn to describe animals' appearance
2. Master vocabulary for expressing emotions
3. Write a short paragraph about a pet

## 🎯 Key Vocabulary
- **Appearance**: fluffy, furry, cute, tiny
- **Actions**: run, jump, play, sleep
- **Emotions**: happy, friendly, lovely

## ✍️ Writing Structure
1. **Introduction**: Introduce your pet
   - I have a pet. It is a...
   - My pet's name is...

2. **Body**: Describe pet's features
   - It is... (color/size)
   - It has... (appearance)
   - It likes to... (likes)

3. **Conclusion**: Express feelings
   - I love my pet.
   - My pet makes me happy.

## 📖 Example
My pet is a small dog. His name is Coco. He is brown and white. Coco has big eyes and a long tail. He likes to play with balls. Every day, I play with him in the park. Coco is my best friend. I love him very much.

## 🎮 Writing Practice
1. Draw a picture of your pet
2. Write 5 words to describe pets
3. Write a paragraph about a pet (5 sentences)

## 🏆 Evaluation Criteria
✅ Correct vocabulary (15 points)
✅ Clear sentences (15 points)
✅ Emotional expression (10 points)
✅ Creativity bonus (10 points)
            """
        },
        'family': {
            'title_cn': '我的家人',
            'title_en': 'My Family',
            'content_cn': """
# 👨‍👩‍👧‍👦 我的家人 - 写作教案

## 📝 学习目标
1. 学习家庭成员的称呼
2. 能够描述家人的外貌和性格
3. 学会表达对家人的爱

## 🎯 重点词汇
- **家庭成员**: father (爸爸), mother (妈妈), brother (兄弟), sister (姐妹)
- **外貌**: tall (高的), short (矮的), kind (和蔼的), smart (聪明的)
- **职业**: teacher (老师), doctor (医生), worker (工人)

## ✍️ 写作结构
1. **开头**: 介绍你的家庭
   - There are... people in my family.
   - I have a... family.

2. **中间**: 描述每个家人
   - My father is...
   - He works as a...
   - My mother likes to...

3. **结尾**: 表达家庭的爱
   - I love my family.
   - We are happy together.

## 📖 范文示例
There are four people in my family. My father is a teacher. He is tall and kind. My mother is a doctor. She works in a hospital. I have a little sister. She is five years old. We play together every day. My family is warm and happy. I love them very much.

## 🎮 写作练习
1. 画一张家庭树
2. 写3句描述家人的话
3. 写一篇关于家庭的短文

## 🏆 评价标准
✅ 家庭成员介绍完整（15分）
✅ 描述准确生动（15分）
✅ 情感表达真实（10分）
            """,
            'content_en': """
# 👨‍👩‍👧‍👦 My Family - Writing Lesson

## 📝 Learning Objectives
1. Learn family member names
2. Describe family appearance and personality
3. Express love for family

## 🎯 Key Vocabulary
- **Family**: father, mother, brother, sister
- **Appearance**: tall, short, kind, smart
- **Jobs**: teacher, doctor, worker

## ✍️ Writing Structure
1. **Introduction**: Introduce your family
   - There are... people in my family.
   - I have a... family.

2. **Body**: Describe each family member
   - My father is...
   - He works as a...
   - My mother likes to...

3. **Conclusion**: Express family love
   - I love my family.
   - We are happy together.

## 📖 Example
There are four people in my family. My father is a teacher. He is tall and kind. My mother is a doctor. She works in a hospital. I have a little sister. She is five years old. We play together every day. My family is warm and happy. I love them very much.

## 🎮 Writing Practice
1. Draw a family tree
2. Write 3 sentences about family
3. Write a paragraph about your family

## 🏆 Evaluation Criteria
✅ Complete family introduction (15 points)
✅ Accurate descriptions (15 points)
✅ Genuine emotional expression (10 points)
            """
        },
        'school': {
            'title_cn': '我的学校生活',
            'title_en': 'My School Life',
            'content_cn': """
# 🏫 我的学校生活 - 写作教案

## 📝 学习目标
1. 学习学校设施和科目的名称
2. 描述日常学校活动
3. 表达对学校生活的感受

## 🎯 重点词汇
- **科目**: English (英语), Math (数学), Chinese (语文), Art (美术)
- **场所**: classroom (教室), library (图书馆), playground (操场)
- **活动**: study (学习), read (阅读), play (玩耍)

## ✍️ 写作结构
1. **开头**: 介绍你的学校
   - My school is...
   - There are... in my school.

2. **中间**: 描述学校生活
   - I study... subjects.
   - My favorite subject is...
   - After class, I...

3. **结尾**: 表达感受
   - I like my school.
   - School life is interesting.

## 📖 范文示例
My school is big and beautiful. There are many classrooms and a big playground. I study English, Math, and Chinese. My favorite subject is English. I like my English teacher. She is very kind. After class, I play football with my friends. I love my school life. It is happy and interesting.

## 🎮 写作练习
1. 画出你最喜欢的教室
2. 列出5个学校里的物品
3. 写一篇学校生活日记

## 🏆 评价标准
✅ 学校描述详细（15分）
✅ 科目活动介绍清楚（15分）
✅ 感受表达真实（10分）
            """,
            'content_en': """
# 🏫 My School Life - Writing Lesson

## 📝 Learning Objectives
1. Learn school facilities and subjects
2. Describe daily school activities
3. Express feelings about school life

## 🎯 Key Vocabulary
- **Subjects**: English, Math, Chinese, Art
- **Places**: classroom, library, playground
- **Activities**: study, read, play

## ✍️ Writing Structure
1. **Introduction**: Introduce your school
   - My school is...
   - There are... in my school.

2. **Body**: Describe school life
   - I study... subjects.
   - My favorite subject is...
   - After class, I...

3. **Conclusion**: Express feelings
   - I like my school.
   - School life is interesting.

## 📖 Example
My school is big and beautiful. There are many classrooms and a big playground. I study English, Math, and Chinese. My favorite subject is English. I like my English teacher. She is very kind. After class, I play football with my friends. I love my school life. It is happy and interesting.

## 🎮 Writing Practice
1. Draw your favorite classroom
2. List 5 things in school
3. Write a diary about school life

## 🏆 Evaluation Criteria
✅ Detailed school description (15 points)
✅ Clear subject introduction (15 points)
✅ Genuine feelings expression (10 points)
            """
        }
    }
    
    VOCABULARY_LIBRARY = {
        'PEP': [
            {'word': 'apple', 'cn': '苹果', 'grade': '3', 'theme': 'food', 'sentence': 'I eat an apple every day.'},
            {'word': 'book', 'cn': '书', 'grade': '3', 'theme': 'school', 'sentence': 'This is my English book.'},
            {'word': 'cat', 'cn': '猫', 'grade': '3', 'theme': 'animals', 'sentence': 'The cat is sleeping.'},
            {'word': 'dog', 'cn': '狗', 'grade': '3', 'theme': 'animals', 'sentence': 'I have a small dog.'},
        ],
        '外研版': [
            {'word': 'school', 'cn': '学校', 'grade': '4', 'theme': 'school', 'sentence': 'My school is very big.'},
            {'word': 'teacher', 'cn': '老师', 'grade': '4', 'theme': 'people', 'sentence': 'Our teacher is very kind.'},
            {'word': 'friend', 'cn': '朋友', 'grade': '4', 'theme': 'people', 'sentence': 'She is my best friend.'},
        ]
    }
    
    @staticmethod
    def generate_writing_lesson(topic, grade, language='en'):
        """生成写作教案"""
        if topic in EnglishContentLibrary.WRITING_LESSONS:
            lesson = EnglishContentLibrary.WRITING_LESSONS[topic]
            return lesson[f'content_{language}']
        
        # 如果没有匹配的主题，生成通用教案
        templates = {
            'cn': f"""
# ✨ 创意写作教案

## 📝 学习目标
1. 学习围绕"{topic}"主题进行写作
2. 掌握相关词汇和表达
3. 培养想象力和创造力

## 🎯 重点词汇
根据"{topic}"主题，学习相关词汇

## ✍️ 写作指导
1. **头脑风暴**: 列出与"{topic}"相关的词语
2. **结构规划**: 
   - 开头：引入主题
   - 中间：详细描述
   - 结尾：总结感受
3. **润色修改**: 检查语法，添加细节

## 📖 写作提示
1. 如果我是{topic}，我会...
2. 描述一次与{topic}相关的经历
3. 创作一个关于{topic}的小故事

## 🎮 创意活动
1. 画出你心中的{topic}
2. 制作词汇卡片
3. 小组分享你的作品

## 🏆 评价标准
✅ 内容相关度（15分）
✅ 语言准确性（15分）
✅ 创意表达（20分）
            """,
            'en': f"""
# ✨ Creative Writing Lesson

## 📝 Learning Objectives
1. Learn to write about "{topic}"
2. Master related vocabulary and expressions
3. Develop imagination and creativity

## 🎯 Key Vocabulary
Learn words related to "{topic}"

## ✍️ Writing Guidance
1. **Brainstorming**: List words related to "{topic}"
2. **Structure Planning**:
   - Introduction: Start with the topic
   - Body: Detailed description
   - Conclusion: Summary and feelings
3. **Polishing**: Check grammar, add details

## 📖 Writing Prompts
1. If I were {topic}, I would...
2. Describe an experience related to {topic}
3. Create a short story about {topic}

## 🎮 Creative Activities
1. Draw your idea of {topic}
2. Make vocabulary cards
3. Share your work in groups

## 🏆 Evaluation Criteria
✅ Relevance to topic (15 points)
✅ Language accuracy (15 points)
✅ Creative expression (20 points)
            """
        }
        return templates.get(language, templates['en'])

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
        {"id": "evaluate", "emoji": "⭐", "label_cn": "作品评价", "label_en": "Evaluation"},
        {"id": "games", "emoji": "🎮", "label_cn": "游戏乐园", "label_en": "Game Park"},
        {"id": "progress", "emoji": "📊", "label_cn": "成长记录", "label_en": "Progress"}
    ]
    
    for item in nav_items:
        label = item[f"label_{st.session_state.language}"]
        is_active = st.session_state.page == item["id"]
        
        if st.button(
            f"{item['emoji']} {label}",
            key=f"nav_{item['id']}",
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.page = item["id"]
            st.rerun()
    
    st.markdown("<hr style='border-color: rgba(255,255,255,0.2)'>", unsafe_allow_html=True)
    
    # 快速工具
    st.markdown("### ⚡ 快速工具")
    quick_col1, quick_col2 = st.columns(2)
    with quick_col1:
        if st.button("🔄 刷新", use_container_width=True):
            st.rerun()
    with quick_col2:
        if st.button("📝 笔记", use_container_width=True):
            st.session_state.page = "writing"
            st.rerun()
    
    # 状态显示
    st.markdown("### ✨ 系统状态")
    st.success("✅ 系统已就绪")
    st.info(f"📚 已加载 {len(EnglishContentLibrary.WRITING_LESSONS)} 个教案")
    st.info(f"🔤 词汇库: {sum(len(v) for v in EnglishContentLibrary.VOCABULARY_LIBRARY.values())} 个单词")

# ==================== 主页面 ====================
# 首页
if st.session_state.page == 'home':
    # 标题区域
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
    
    # 功能展示区
    st.markdown("## 🎪 六大魔法功能" if st.session_state.language == 'cn' else "## 🎪 Six Magic Features")
    
    # 第一行功能卡片
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="feature-card card-orange">
            <div class="card-icon">✏️</div>
            <h3 class="card-title">{
                '智能写作助手' if st.session_state.language == 'cn' else 'Smart Writing Assistant'
            }</h3>
            <p class="card-desc">{
                'AI生成创意写作教案，激发孩子的写作兴趣' if st.session_state.language == 'cn' 
                else 'AI generates creative writing lessons to inspire children'
            }</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="feature-card card-green">
            <div class="card-icon">📖</div>
            <h3 class="card-title">{
                '词汇魔法书' if st.session_state.language == 'cn' else 'Vocabulary Magic Book'
            }</h3>
            <p class="card-desc">{
                '多版本教材词汇库，CEFR分级，智能推荐' if st.session_state.language == 'cn'
                else 'Multi-version textbook vocabulary with CEFR levels'
            }</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="feature-card card-blue">
            <div class="card-icon">⭐</div>
            <h3 class="card-title">{
                '智能评价系统' if st.session_state.language == 'cn' else 'Smart Evaluation'
            }</h3>
            <p class="card-desc">{
                '即时作文评价，个性化改进建议' if st.session_state.language == 'cn'
                else 'Instant essay evaluation with personalized feedback'
            }</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 第二行功能卡片
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown(f"""
        <div class="feature-card card-pink">
            <div class="card-icon">🎮</div>
            <h3 class="card-title">{
                '写作游戏乐园' if st.session_state.language == 'cn' else 'Writing Games'
            }</h3>
            <p class="card-desc">{
                '趣味写作游戏，在玩中学，在学中玩' if st.session_state.language == 'cn'
                else 'Fun writing games, learn through play'
            }</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown(f"""
        <div class="feature-card card-purple">
            <div class="card-icon">📊</div>
            <h3 class="card-title">{
                '成长记录册' if st.session_state.language == 'cn' else 'Progress Tracker'
            }</h3>
            <p class="card-desc">{
                '记录每一次进步，见证写作成长' if st.session_state.language == 'cn'
                else 'Track every progress, witness writing growth'
            }</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col6:
        st.markdown(f"""
        <div class="feature-card card-teal">
            <div class="card-icon">🏆</div>
            <h3 class="card-title">{
                '荣誉勋章系统' if st.session_state.language == 'cn' else 'Achievement System'
            }</h3>
            <p class="card-desc">{
                '激励孩子不断挑战，获得写作勋章' if st.session_state.language == 'cn'
                else 'Motivate children with writing achievements'
            }</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 快速开始区
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## 🚀 立即开始" if st.session_state.language == 'cn' else "## 🚀 Get Started Now")
    
    start_col1, start_col2, start_col3 = st.columns(3)
    
    with start_col1:
        if st.button("✏️ 开始写作", use_container_width=True, type="primary"):
            st.session_state.page = "writing"
            st.rerun()
        st.caption("生成写作教案" if st.session_state.language == 'cn' else "Generate writing lessons")
    
    with start_col2:
        if st.button("📖 学习词汇", use_container_width=True, type="primary"):
            st.session_state.page = "vocabulary"
            st.rerun()
        st.caption("探索词汇库" if st.session_state.language == 'cn' else "Explore vocabulary")
    
    with start_col3:
        if st.button("🎮 玩转游戏", use_container_width=True, type="primary"):
            st.session_state.page = "games"
            st.rerun()
        st.caption("趣味学习" if st.session_state.language == 'cn' else "Fun learning")
    
    # 今日推荐
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## 🔥 今日推荐" if st.session_state.language == 'cn' else "## 🔥 Today's Recommendation")
    
    rec_col1, rec_col2 = st.columns(2)
    
    with rec_col1:
        with st.container():
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea, #764ba2); 
                      padding: 25px; border-radius: 20px; color: white;">
                <h3 style="color: white; margin-top: 0;">🌟 每周写作挑战</h3>
                <p>主题：我的梦想职业</p>
                <p>🏆 完成挑战赢取专属勋章！</p>
            </div>
            """, unsafe_allow_html=True)
    
    with rec_col2:
        with st.container():
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f093fb, #f5576c); 
                      padding: 25px; border-radius: 20px; color: white;">
                <h3 style="color: white; margin-top: 0;">📈 学习进度</h3>
                <p>本月已帮助 128 位小作家</p>
                <p>📚 累计生成 256 篇优秀作品</p>
            </div>
            """, unsafe_allow_html=True)

# 写作工坊页面
elif st.session_state.page == 'writing':
    st.markdown("""
    <div class="title-container">
        <h1 class="main-header">✏️ 写作魔法工坊</h1>
        <div class="decorative-icons">
            <span class="icon-bounce">📝</span>
            <span class="icon-bounce">✨</span>
            <span class="icon-bounce">🎨</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    subtitle = "选择主题，生成专属写作教案" if st.session_state.language == 'cn' else "Choose a topic, generate personalized writing lessons"
    st.markdown(f'<div class="subtitle-text">{subtitle}</div>', unsafe_allow_html=True)
    
    # 主题选择区
    st.markdown("### 🎯 选择写作主题" if st.session_state.language == 'cn' else "### 🎯 Choose Writing Topic")
    
    themes = list(EnglishContentLibrary.WRITING_LESSONS.keys())
    theme_names_cn = [EnglishContentLibrary.WRITING_LESSONS[t]['title_cn'] for t in themes]
    theme_names_en = [EnglishContentLibrary.WRITING_LESSONS[t]['title_en'] for t in themes]
    
    theme_cols = st.columns(3)
    for idx, (theme, name_cn, name_en) in enumerate(zip(themes, theme_names_cn, theme_names_en)):
        with theme_cols[idx % 3]:
            name = name_cn if st.session_state.language == 'cn' else name_en
            emoji = "🐶" if theme == 'animals' else "👨‍👩‍👧‍👦" if theme == 'family' else "🏫"
            
            if st.button(
                f"{emoji} {name}",
                use_container_width=True,
                type="primary" if st.session_state.current_lesson == theme else "secondary"
            ):
                st.session_state.current_lesson = theme
                st.rerun()
    
    # 自定义主题
    st.markdown("### 💡 自定义主题" if st.session_state.language == 'cn' else "### 💡 Custom Topic")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        custom_topic = st.text_input(
            "输入你的写作主题" if st.session_state.language == 'cn' else "Enter your writing topic",
            placeholder="例如：我的假期、未来的城市..." if st.session_state.language == 'cn' else "e.g., My holiday, Future city..."
        )
    
    with col2:
        grade_level = st.selectbox(
            "年级" if st.session_state.language == 'cn' else "Grade Level",
            ["Grade 1-2", "Grade 3-4", "Grade 5-6", "Grade 7-8"]
        )
    
    # 写作设置
    with st.expander("⚙️ 写作设置" if st.session_state.language == 'cn' else "⚙️ Writing Settings", expanded=True):
        col_set1, col_set2 = st.columns(2)
        
        with col_set1:
            writing_type = st.selectbox(
                "写作类型" if st.session_state.language == 'cn' else "Writing Type",
                ["记叙文", "说明文", "议论文", "日记", "书信"] if st.session_state.language == 'cn'
                else ["Narrative", "Descriptive", "Argumentative", "Diary", "Letter"]
            )
            
            difficulty = st.select_slider(
                "难度等级" if st.session_state.language == 'cn' else "Difficulty Level",
                options=["简单", "中等", "挑战"] if st.session_state.language == 'cn'
                else ["Easy", "Medium", "Challenging"]
            )
        
        with col_set2:
            length = st.select_slider(
                "内容长度" if st.session_state.language == 'cn' else "Content Length",
                options=["简短", "适中", "详细"] if st.session_state.language == 'cn'
                else ["Short", "Medium", "Detailed"]
            )
            
            creativity = st.slider(
                "创意指数" if st.session_state.language == 'cn' else "Creativity Level",
                0, 100, 70
            )
    
    # 生成按钮
    if st.button("✨ 生成写作教案" if st.session_state.language == 'cn' else "✨ Generate Writing Lesson", 
                type="primary", use_container_width=True):
        
        if st.session_state.current_lesson or custom_topic:
            topic = st.session_state.current_lesson if st.session_state.current_lesson else custom_topic
            
            with st.spinner("🧙‍♂️ 魔法师正在创作中..." if st.session_state.language == 'cn' else "🧙‍♂️ Creating magic..."):
                # 生成教案
                lesson_content = EnglishContentLibrary.generate_writing_lesson(
                    topic, grade_level, st.session_state.language
                )
                
                # 保存到历史
                st.session_state.writing_history.append({
                    "topic": topic,
                    "grade": grade_level,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "language": st.session_state.language
                })
                
                # 显示教案
                st.markdown("### 📜 写作教案" if st.session_state.language == 'cn' else "### 📜 Writing Lesson")
                st.markdown(f'<div class="content-box">{lesson_content}</div>', unsafe_allow_html=True)
                
                # 操作按钮
                col_btn1, col_btn2, col_btn3 = st.columns(3)
                with col_btn1:
                    st.download_button(
                        "📥 下载教案" if st.session_state.language == 'cn' else "📥 Download",
                        data=lesson_content,
                        file_name=f"写作教案_{datetime.now().strftime('%Y%m%d')}.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                with col_btn2:
                    if st.button("🔄 重新生成" if st.session_state.language == 'cn' else "🔄 Regenerate", 
                                use_container_width=True):
                        st.rerun()
                with col_btn3:
                    if st.button("💾 保存作品" if st.session_state.language == 'cn' else "💾 Save", 
                                use_container_width=True):
                        st.success("作品已保存！" if st.session_state.language == 'cn' else "Saved!")
        else:
            st.warning("请先选择或输入一个主题！" if st.session_state.language == 'cn' 
                      else "Please select or enter a topic first!")

# 词汇魔法页面
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
        "🔍 词汇搜索" if st.session_state.language == 'cn' else "🔍 Search",
        "📚 主题词汇" if st.session_state.language == 'cn' else "📚 Thematic",
        "🎮 词汇游戏" if st.session_state.language == 'cn' else "🎮 Games"
    ])
    
    with tab1:
        st.markdown("### 🔍 智能词汇搜索" if st.session_state.language == 'cn' else "### 🔍 Smart Vocabulary Search")
        
        # 搜索框和筛选
        col_search, col_filter1, col_filter2 = st.columns([2, 1, 1])
        
        with col_search:
            search_keyword = st.text_input(
                "输入关键词搜索" if st.session_state.language == 'cn' else "Enter keyword to search",
                placeholder="英文或中文" if st.session_state.language == 'cn' else "English or Chinese"
            )
        
        with col_filter1:
            textbook_filter = st.selectbox(
                "教材版本" if st.session_state.language == 'cn' else "Textbook",
                ["全部", "人教版", "外研版", "牛津版", "课标词汇"]
            )
        
        with col_filter2:
            grade_filter = st.selectbox(
                "年级" if st.session_state.language == 'cn' else "Grade",
                ["全部", "一年级", "二年级", "三年级", "四年级", "五年级", "六年级"]
            )
        
        # 搜索按钮
        if st.button("🔍 开始搜索" if st.session_state.language == 'cn' else "🔍 Search", 
                    type="primary", use_container_width=True):
            
            # 模拟搜索结果
            if search_keyword:
                # 搜索逻辑
                results = []
                for textbook, words in EnglishContentLibrary.VOCABULARY_LIBRARY.items():
                    if textbook_filter != "全部" and textbook_filter not in textbook:
                        continue
                    
                    for word in words:
                        if (grade_filter == "全部" or grade_filter in word['grade']):
                            if (search_keyword.lower() in word['word'].lower() or 
                                search_keyword in word['cn']):
                                results.append({**word, 'textbook': textbook})
                
                if results:
                    st.markdown(f"### 📊 找到 {len(results)} 个结果" if st.session_state.language == 'cn' 
                               else f"### 📊 Found {len(results)} results")
                    
                    # 分页显示
                    page_size = 10
                    pages = [results[i:i + page_size] for i in range(0, len(results), page_size)]
                    current_page = 1
                    
                    if pages:
                        for word in pages[current_page-1]:
                            # 随机分配卡片颜色
                            card_colors = ['word-card-blue', 'word-card-green', 'word-card-orange']
                            card_class = random.choice(card_colors)
                            
                            st.markdown(f"""
                            <div class="word-card {card_class}">
                                <div style="display: flex; justify-content: space-between; align-items: start;">
                                    <div>
                                        <h4 style="margin: 0; font-size: 1.2rem;">
                                            <strong>{word['word']}</strong>
                                            <span style="color: #666; margin-left: 10px;">{word['cn']}</span>
                                        </h4>
                                        <div style="margin-top: 10px; color: #555;">
                                            <span class="status-badge badge-info">{word['textbook']}</span>
                                            <span class="status-badge badge-success">Grade {word['grade']}</span>
                                            <span class="status-badge badge-warning">{word['theme']}</span>
                                        </div>
                                    </div>
                                </div>
                                <div style="margin-top: 15px; color: #666; font-style: italic;">
                                    📝 {word['sentence']}
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                else:
                    st.info("未找到相关词汇，请尝试其他关键词。" if st.session_state.language == 'cn' 
                           else "No vocabulary found. Try different keywords.")
    
    with tab2:
        st.markdown("### 🎨 主题词汇包" if st.session_state.language == 'cn' else "### 🎨 Thematic Vocabulary")
        
        themes = ["animals", "family", "school", "food", "colors", "weather", "sports", "feelings"]
        theme_names_cn = ["动物", "家庭", "学校", "食物", "颜色", "天气", "运动", "情感"]
        theme_names_en = ["Animals", "Family", "School", "Food", "Colors", "Weather", "Sports", "Feelings"]
        
        theme_cols = st.columns(4)
        for idx, theme in enumerate(themes):
            with theme_cols[idx % 4]:
                name = theme_names_cn[idx] if st.session_state.language == 'cn' else theme_names_en[idx]
                emoji = ["🐶", "👨‍👩‍👧‍👦", "🏫", "🍎", "🎨", "☀️", "⚽", "😊"][idx]
                
                if st.button(f"{emoji} {name}", use_container_width=True):
                    # 显示主题词汇
                    st.session_state.selected_theme = theme
                    st.rerun()
        
        # 显示选中的主题词汇
        if 'selected_theme' in st.session_state:
            theme_idx = themes.index(st.session_state.selected_theme)
            theme_name = theme_names_en[theme_idx]
            
            st.markdown(f"### {['🐶', '👨‍👩‍👧‍👦', '🏫', '🍎', '🎨', '☀️', '⚽', '😊'][theme_idx]} {theme_name}")
            
            # 显示主题相关词汇
            vocab_list = [
                {"word": "dog", "cn": "狗", "sentence": "I have a cute dog."} if theme_name == "Animals" else
                {"word": "father", "cn": "爸爸", "sentence": "My father is tall."} if theme_name == "Family" else
                {"word": "classroom", "cn": "教室", "sentence": "Our classroom is clean."} if theme_name == "School" else
                {"word": "apple", "cn": "苹果", "sentence": "I eat an apple every day."} if theme_name == "Food" else
                {"word": "red", "cn": "红色", "sentence": "The apple is red."} if theme_name == "Colors" else
                {"word": "sunny", "cn": "晴朗", "sentence": "Today is a sunny day."} if theme_name == "Weather" else
                {"word": "football", "cn": "足球", "sentence": "I play football with friends."} if theme_name == "Sports" else
                {"word": "happy", "cn": "开心", "sentence": "I feel happy today."}
            ]
            
            for i in range(5):
                word = {**vocab_list[0], "word": f"word_{i+1}", "cn": f"中文_{i+1}"}
                st.markdown(f"""
                <div class="word-card word-card-{'blue' if i%3==0 else 'green' if i%3==1 else 'orange'}">
                    <div style="display: flex; justify-content: space-between;">
                        <div>
                            <strong>{word['word']}</strong>
                            <span style="color: #666; margin-left: 10px;">{word['cn']}</span>
                        </div>
                        <button style="
                            background: #4D96FF;
                            color: white;
                            border: none;
                            padding: 5px 15px;
                            border-radius: 10px;
                            cursor: pointer;
                        ">+ 学习</button>
                    </div>
                    <div style="margin-top: 10px; color: #666;">
                        📝 {word['sentence']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

# 游戏乐园页面
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
    st.markdown("## 🎯 选择游戏" if st.session_state.language == 'cn' else "## 🎯 Choose a Game")
    
    game_col1, game_col2, game_col3 = st.columns(3)
    
    with game_col1:
        st.markdown(f"""
        <div class="feature-card card-orange">
            <div class="card-icon">🧩</div>
            <h3 class="card-title">{
                '单词拼图' if st.session_state.language == 'cn' else 'Word Puzzle'
            }</h3>
            <p class="card-desc">{
                '将打乱的字母拼成正确的单词' if st.session_state.language == 'cn'
                else 'Arrange letters to form correct words'
            }</p>
            {st.button("开始游戏", use_container_width=True, type="primary")}
        </div>
        """, unsafe_allow_html=True)
    
    with game_col2:
        st.markdown(f"""
        <div class="feature-card card-green">
            <div class="card-icon">📝</div>
            <h3 class="card-title">{
                '句子接龙' if st.session_state.language == 'cn' else 'Sentence Chain'
            }</h3>
            <p class="card-desc">{
                '用上一个单词的最后一个字母开始新单词' if st.session_state.language == 'cn'
                else 'Start new word with last letter of previous word'
            }</p>
            {st.button("开始游戏", use_container_width=True, type="primary")}
        </div>
        """, unsafe_allow_html=True)
    
    with game_col3:
        st.markdown(f"""
        <div class="feature-card card-blue">
            <div class="card-icon">🎲</div>
            <h3 class="card-title">{
                '故事骰子' if st.session_state.language == 'cn' else 'Story Dice'
            }</h3>
            <p class="card-desc">{
                '掷骰子获得随机词语，创作有趣故事' if st.session_state.language == 'cn'
                else 'Roll dice for random words to create stories'
            }</p>
            {st.button("开始游戏", use_container_width=True, type="primary")}
        </div>
        """, unsafe_allow_html=True)
    
    # 游戏区域
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## 🎮 单词拼图游戏" if st.session_state.language == 'cn' else "## 🎮 Word Puzzle Game")
    
    # 游戏界面
    game_container = st.container()
    with game_container:
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; border: 3px solid #FF9A3D;">
            <div style="text-align: center; margin-bottom: 30px;">
                <h3 style="color: #333;">单词: _ _ _ _ _</h3>
                <p style="color: #666;">中文: 苹果</p>
                <div style="margin: 20px 0; font-size: 2rem; letter-spacing: 10px;">
                    P P L E A
                </div>
                <div style="display: flex; gap: 10px; justify-content: center; margin-top: 20px;">
                    <button style="
                        background: #FF9A3D;
                        color: white;
                        border: none;
                        padding: 10px 20px;
                        border-radius: 10px;
                        font-size: 1.1rem;
                        cursor: pointer;
                    ">A</button>
                    <button style="
                        background: #6BCF7F;
                        color: white;
                        border: none;
                        padding: 10px 20px;
                        border-radius: 10px;
                        font-size: 1.1rem;
                        cursor: pointer;
                    ">P</button>
                    <button style="
                        background: #4D96FF;
                        color: white;
                        border: none;
                        padding: 10px 20px;
                        border-radius: 10px;
                        font-size: 1.1rem;
                        cursor: pointer;
                    ">P</button>
                    <button style="
                        background: #FF6B9D;
                        color: white;
                        border: none;
                        padding: 10px 20px;
                        border-radius: 10px;
                        font-size: 1.1rem;
                        cursor: pointer;
                    ">L</button>
                    <button style="
                        background: #9D4DFF;
                        color: white;
                        border: none;
                        padding: 10px 20px;
                        border-radius: 10px;
                        font-size: 1.1rem;
                        cursor: pointer;
                    ">E</button>
                </div>
            </div>
            <div style="text-align: center; margin-top: 30px;">
                <button style="
                    background: linear-gradient(135deg, #4D96FF, #9D4DFF);
                    color: white;
                    border: none;
                    padding: 15px 40px;
                    border-radius: 15px;
                    font-size: 1.2rem;
                    font-weight: bold;
                    cursor: pointer;
                ">🎯 检查答案</button>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 页脚
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns([2, 1, 1])

with footer_col1:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"""
    <div style="color: #666; text-align: center;">
        <p style="margin: 0;">
            <strong>🎨 英思织网 AI写作魔法学院</strong> | 
            📧 contact@yingsizhiwang.com | 
            ⏰ {current_time}
        </p>
        <p style="margin: 5px 0 0 0; font-size: 0.9em;">
            © 2024 英思织网 版权所有 | 让每个孩子爱上写作！
        </p>
    </div>
    """, unsafe_allow_html=True)

with footer_col2:
    if st.button("⬆️ 回到顶部", use_container_width=True):
        st.rerun()

with footer_col3:
    st.caption("🎯 参赛作品展示版")
