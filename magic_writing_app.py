# web_app_fun.py - 活泼童真又专业的AI写作教学平台
import streamlit as st
import requests
from datetime import datetime
import time

# ======================== 页面配置 ========================
st.set_page_config(
    page_title="英思织网 - AI写作教学平台",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================== 活泼专业的CSS样式 ========================
st.markdown("""
<style>
    /* 活泼的渐变背景 */
    .stApp {
        background: linear-gradient(135deg, #f5f7ff 0%, #f0f9ff 100%);
    }
    
    /* 主标题 - 彩虹渐变色 */
    .main-title {
        text-align: center;
        background: linear-gradient(90deg, #FF6B6B, #FFD166, #06D6A0, #118AB2, #7209B7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.8em;
        font-weight: 800;
        margin-bottom: 10px;
        padding: 20px;
        position: relative;
    }
    
    .main-title::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 25%;
        width: 50%;
        height: 5px;
        background: linear-gradient(90deg, #FF6B6B, #FFD166, #06D6A0);
        border-radius: 10px;
    }
    
    /* 副标题 */
    .sub-title {
        text-align: center;
        color: #4A5568;
        font-size: 1.2em;
        margin-bottom: 30px;
        font-weight: 400;
    }
    
    /* 彩色功能卡片 */
    .fun-card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        border-top: 6px solid;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .fun-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.8), transparent);
    }
    
    .fun-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.12);
    }
    
    /* 卡片颜色 */
    .card-red { border-color: #FF6B6B; background: linear-gradient(135deg, #fff5f5, #fff); }
    .card-orange { border-color: #FFD166; background: linear-gradient(135deg, #fffaf0, #fff); }
    .card-green { border-color: #06D6A0; background: linear-gradient(135deg, #f0fff4, #fff); }
    .card-blue { border-color: #118AB2; background: linear-gradient(135deg, #f0f9ff, #fff); }
    .card-purple { border-color: #7209B7; background: linear-gradient(135deg, #f9f0ff, #fff); }
    .card-teal { border-color: #0D9488; background: linear-gradient(135deg, #f0fdfa, #fff); }
    
    .card-icon {
        font-size: 2.5em;
        margin-bottom: 15px;
        display: inline-block;
        background: linear-gradient(135deg, currentColor, rgba(255,255,255,0.8));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .card-title {
        font-size: 1.4em;
        font-weight: 700;
        color: #2D3748;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .card-desc {
        color: #718096;
        font-size: 0.95em;
        line-height: 1.6;
    }
    
    /* 彩色按钮 */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 15px;
        font-weight: 600;
        font-size: 1em;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* 特殊按钮 */
    .primary-btn button {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%) !important;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3) !important;
    }
    
    .primary-btn button:hover {
        background: linear-gradient(135deg, #FF8E53 0%, #FF6B6B 100%) !important;
        box-shadow: 0 8px 20px rgba(255, 107, 107, 0.4) !important;
    }
    
    /* 侧边栏 - 彩虹渐变 */
    section[data-testid="stSidebar"] > div {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    
    /* 彩虹导航按钮 */
    .nav-btn {
        width: 100%;
        margin: 8px 0;
        padding: 14px 20px;
        text-align: left;
        background: rgba(255,255,255,0.1);
        border: none;
        color: white;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s;
        font-size: 16px;
        font-weight: 500;
        border-left: 4px solid transparent;
        display: flex;
        align-items: center;
        gap: 12px;
        position: relative;
        overflow: hidden;
    }
    
    .nav-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .nav-btn:hover::before {
        left: 100%;
    }
    
    .nav-btn:hover {
        background: rgba(255,255,255,0.15);
        transform: translateX(5px);
    }
    
    .nav-btn.active {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.8), rgba(118, 75, 162, 0.8));
        border-left: 4px solid #FFD166;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    /* 标签页彩虹效果 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 5px;
        background: linear-gradient(135deg, #f0f9ff, #f5f0ff);
        padding: 8px;
        border-radius: 15px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 12px;
        padding: 12px 20px;
        background: white;
        font-weight: 500;
        color: #4A5568;
        transition: all 0.3s;
        border: 2px solid transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        border: 2px solid #FFD166;
    }
    
    /* 响应框 - 云朵气泡样式 */
    .bubble-box {
        background: white;
        padding: 25px;
        border-radius: 20px;
        margin: 20px 0;
        border: 2px solid #E2E8F0;
        position: relative;
        box-shadow: 0 8px 25px rgba(0,0,0,0.05);
    }
    
    .bubble-box::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(135deg, #FF6B6B, #FFD166, #06D6A0, #118AB2);
        border-radius: 22px;
        z-index: -1;
        opacity: 0.1;
    }
    
    /* 彩虹进度条 */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #FF6B6B, #FFD166, #06D6A0, #118AB2) !important;
    }
    
    /* 彩虹分隔线 */
    .rainbow-divider {
        height: 3px;
        background: linear-gradient(90deg, #FF6B6B, #FFD166, #06D6A0, #118AB2, #7209B7);
        border-radius: 10px;
        margin: 30px 0;
        opacity: 0.7;
    }
    
    /* 可爱的状态标签 */
    .fun-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85em;
        margin: 5px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
    
    .badge-success {
        background: linear-gradient(135deg, #06D6A0, #10B981);
        color: white;
    }
    
    .badge-warning {
        background: linear-gradient(135deg, #FFD166, #F59E0B);
        color: white;
    }
    
    .badge-info {
        background: linear-gradient(135deg, #118AB2, #3B82F6);
        color: white;
    }
    
    .badge-purple {
        background: linear-gradient(135deg, #7209B7, #8B5CF6);
        color: white;
    }
    
    /* 输入框彩虹边框 */
    .stTextArea textarea:focus,
    .stTextInput input:focus {
        border: 2px solid #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    /* 可爱的emoji装饰 */
    .emoji-deco {
        font-size: 1.5em;
        margin: 0 5px;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    /* 响应式调整 */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2em;
        }
        
        .fun-card {
            padding: 20px;
        }
        
        .nav-btn {
            padding: 12px 15px;
            font-size: 14px;
        }
    }
</style>
""", unsafe_allow_html=True)

# ======================== 初始化状态 ========================
if 'api_key' not in st.session_state:
    st.session_state.api_key = ''
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'history' not in st.session_state:
    st.session_state.history = []
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# ======================== API函数 ========================
def call_deepseek_api(prompt, system_message="你是一位专业又有趣的写作教师", max_tokens=2000, temperature=0.7):
    """调用DeepSeek API"""
    if not st.session_state.api_key:
        return None, "请先输入API密钥"
    
    try:
        url = "https://api.deepseek.com/chat/completions"
        headers = {
            "Authorization": f"Bearer {st.session_state.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        
        response = requests.post(url, json=data, headers=headers, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"], None
        else:
            return None, f"API请求失败: {response.status_code}"
            
    except Exception as e:
        return None, f"发生错误: {str(e)}"

# ======================== 彩虹侧边栏 ========================
with st.sidebar:
    # Logo区域
    st.markdown("""
    <div style="text-align: center; padding: 25px 0; border-bottom: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 2.5em; margin-bottom: 10px;">✏️📚🎨</div>
        <h1 style="color: white; margin: 0; font-size: 1.8em;">英思织网</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 5px 0 0 0; font-size: 0.9em;">
            <span class="emoji-deco">🌈</span> AI写作魔法学院 <span class="emoji-deco">✨</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # API设置 - 彩虹卡片
    with st.expander("🔮 **魔法钥匙设置**", expanded=True):
        api_key = st.text_input(
            "DeepSeek API密钥",
            type="password",
            value=st.session_state.api_key,
            placeholder="输入你的魔法钥匙...",
            help="获取地址: https://platform.deepseek.com"
        )
        st.session_state.api_key = api_key
        
        col_test, col_clear = st.columns(2)
        with col_test:
            if st.button("🔗 测试连接", use_container_width=True):
                if api_key:
                    with st.spinner("施展连接魔法..."):
                        response, error = call_deepseek_api("请回复：魔法连接成功！", max_tokens=20)
                        if error:
                            st.error("😢 连接失败")
                        elif response and ("成功" in response or "魔法" in response):
                            st.success("🎉 连接成功！")
                        else:
                            st.warning("🤔 连接有点奇怪...")
                else:
                    st.warning("🔑 请先输入魔法钥匙")
        
        with col_clear:
            if st.button("🔄 重置", use_container_width=True):
                st.session_state.api_key = ''
                st.rerun()
    
    st.markdown("<div class='rainbow-divider'></div>", unsafe_allow_html=True)
    
    # 彩虹导航菜单
    st.markdown("### 📖 **魔法学院导航**")
    
    nav_options = [
        {"id": "home", "label": "🏠 魔法学院大厅", "emoji": "🏠", "color": "#FF6B6B"},
        {"id": "writing", "label": "🤖 写作魔法师", "emoji": "🤖", "color": "#FFD166"},
        {"id": "evaluation", "label": "📝 作文评价官", "emoji": "📝", "color": "#06D6A0"},
        {"id": "chat", "label": "💬 智慧导师", "emoji": "💬", "color": "#118AB2"},
        {"id": "vocab", "label": "🔤 词汇魔法书", "emoji": "🔤", "color": "#7209B7"},
        {"id": "stats", "label": "📊 魔法记录", "emoji": "📊", "color": "#0D9488"},
        {"id": "settings", "label": "⚙️ 学院设置", "emoji": "⚙️", "color": "#4A5568"}
    ]
    
    for option in nav_options:
        is_active = st.session_state.current_page == option["id"]
        btn_class = "nav-btn active" if is_active else "nav-btn"
        
        if st.button(
            f"{option['emoji']} {option['label']}",
            key=f"nav_{option['id']}",
            use_container_width=True
        ):
            st.session_state.current_page = option["id"]
            st.rerun()
    
    st.markdown("<div class='rainbow-divider'></div>", unsafe_allow_html=True)
    
    # 快捷魔法
    st.markdown("### ⚡ **快捷魔法**")
    
    quick_col1, quick_col2 = st.columns(2)
    with quick_col1:
        if st.button("✨ 刷新", use_container_width=True):
            st.rerun()
    with quick_col2:
        if st.button("📖 历史", use_container_width=True):
            st.session_state.current_page = "stats"
    
    # 魔法状态
    st.markdown("<br>", unsafe_allow_html=True)
    if st.session_state.api_key:
        st.markdown('<span class="fun-badge badge-success">✅ 魔法钥匙已激活</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="fun-badge badge-warning">🔑 需要魔法钥匙</span>', unsafe_allow_html=True)

# ======================== 页面内容 ========================
# 魔法学院大厅（首页）
if st.session_state.current_page == 'home':
    st.markdown("<h1 class='main-title'>🎨 英思织网魔法写作学院</h1>", unsafe_allow_html=True)
    st.markdown('<p class="sub-title">🌈 用AI魔法点亮写作天赋，让每个孩子成为小小作家！</p>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 30px;">
        <span class="fun-badge badge-purple">✨ 今日魔法能量: 100%</span>
        <span class="fun-badge badge-info">📅 {datetime.now().strftime('%Y年%m月%d日')}</span>
        <span class="fun-badge badge-success">🎯 {datetime.now().strftime('%H:%M:%S')}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 功能展示区
    st.markdown("### 🎪 **魔法学院六大法宝**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 卡片1: 写作魔法师
        st.markdown("""
        <div class="fun-card card-orange">
            <div class="card-icon">🤖</div>
            <div class="card-title">
                <span style="color: #FFD166;">🤖</span> 写作魔法师
            </div>
            <div class="card-desc">
                智能生成各种题材的写作教案和范文，让写作变得像玩游戏一样有趣！
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 卡片2: 作文评价官
        st.markdown("""
        <div class="fun-card card-green">
            <div class="card-icon">📝</div>
            <div class="card-title">
                <span style="color: #06D6A0;">📝</span> 作文评价官
            </div>
            <div class="card-desc">
                智能评价作文，提供具体的改进建议，帮助小作家们快速进步！
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 卡片3: 词汇魔法书
        st.markdown("""
        <div class="fun-card card-purple">
            <div class="card-icon">🔤</div>
            <div class="card-title">
                <span style="color: #7209B7;">🔤</span> 词汇魔法书
            </div>
            <div class="card-desc">
                丰富的词汇扩展工具，让语言表达更加生动有趣！
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # 卡片4: 智慧导师
        st.markdown("""
        <div class="fun-card card-blue">
            <div class="card-icon">💬</div>
            <div class="card-title">
                <span style="color: #118AB2;">💬</span> 智慧导师
            </div>
            <div class="card-desc">
                24小时在线的AI写作导师，随时解答写作问题！
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 卡片5: 魔法记录
        st.markdown("""
        <div class="fun-card card-teal">
            <div class="card-icon">📊</div>
            <div class="card-title">
                <span style="color: #0D9488;">📊</span> 魔法记录
            </div>
            <div class="card-desc">
                记录每次写作的进步，见证小作家的成长历程！
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 卡片6: 学院设置
        st.markdown("""
        <div class="fun-card" style="border-color: #4A5568; background: linear-gradient(135deg, #f7fafc, #fff);">
            <div class="card-icon">⚙️</div>
            <div class="card-title">
                <span style="color: #4A5568;">⚙️</span> 学院设置
            </div>
            <div class="card-desc">
                个性化设置你的魔法学院，打造专属的写作空间！
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # 快速开始区
    st.markdown("<div class='rainbow-divider'></div>", unsafe_allow_html=True)
    st.markdown("### 🚀 **立即开始魔法写作之旅**")
    
    start_col1, start_col2, start_col3 = st.columns(3)
    
    with start_col1:
        if st.button("🎨 **开始写作**", use_container_width=True):
            st.session_state.current_page = "writing"
            st.rerun()
        st.caption("生成有趣的写作教案")
    
    with start_col2:
        if st.button("🔍 **评价作文**", use_container_width=True):
            st.session_state.current_page = "evaluation"
            st.rerun()
        st.caption("获取专业的写作反馈")
    
    with start_col3:
        if st.button("💬 **咨询导师**", use_container_width=True):
            st.session_state.current_page = "chat"
            st.rerun()
        st.caption("随时解答写作疑问")

# 写作魔法师页面
elif st.session_state.current_page == 'writing':
    st.markdown("<h1 class='main-title'>🤖 写作魔法师工作室</h1>", unsafe_allow_html=True)
    st.markdown('<p class="sub-title">✨ 选择主题，施展写作魔法，生成精彩的写作教案！</p>', unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # 彩虹标签页选择写作类型
            writing_type = st.selectbox(
                "📚 **选择写作类型**",
                ["童话故事", "校园日记", "想象作文", "观察日记", "读后感", "议论文", "说明文", "应用文"],
                help="选择你喜欢的写作类型"
            )
            
            # 创意输入框
            topic = st.text_area(
                "🎯 **写作主题或要求**",
                height=120,
                placeholder="例如：写一个关于勇敢小猫咪的童话故事...\n或者：描述你最喜欢的季节...",
                help="发挥你的想象力，描述你想写的内容"
            )
            
            # 可爱的高级选项
            with st.expander("🎨 **魔法设置**", expanded=True):
                col_a, col_b = st.columns(2)
                with col_a:
                    grade = st.select_slider(
                        "👦 **适合年级**",
                        options=["一年级", "二年级", "三年级", "四年级", "五年级", "六年级", "初中", "高中"]
                    )
                    
                    style = st.selectbox(
                        "✏️ **写作风格**",
                        ["活泼有趣", "生动形象", "简洁明了", "优美动人", "幽默风趣"]
                    )
                
                with col_b:
                    length = st.select_slider(
                        "📏 **内容长度**",
                        options=["短小精悍", "适中标准", "详细丰富", "非常详细"]
                    )
                    
                    include_items = st.multiselect(
                        "📋 **包含内容**",
                        ["魔法范文", "写作技巧", "词语宝库", "结构指导", "修改建议", "评价标准"],
                        default=["魔法范文", "写作技巧", "词语宝库"]
                    )
        
        with col2:
            st.markdown("#### 🎪 **魔法道具**")
            
            # 可爱的滑块和选择器
            creativity = st.slider(
                "✨ **创意指数**",
                0, 100, 70,
                help="控制AI的创意程度"
            )
            
            difficulty = st.select_slider(
                "🎓 **难度等级**",
                options=["简单", "普通", "挑战", "困难", "专家"]
            )
            
            st.markdown("---")
            
            # 生成按钮
            generate_col1, generate_col2 = st.columns([3, 1])
            with generate_col1:
                if st.button("🔮 **施展写作魔法**", type="primary", use_container_width=True):
                    if not st.session_state.api_key:
                        st.error("🔑 请先在侧边栏输入魔法钥匙（API密钥）")
                    elif not topic:
                        st.warning("🎯 请输入写作主题")
                    else:
                        with st.spinner("🧙‍♂️ 魔法师正在创作中..."):
                            # 构建提示词
                            prompt = f"""请为{grade}学生创作一份关于"{topic}"的{writing_type}写作教案。

要求：
- 写作风格：{style}
- 内容长度：{length}
- 难度等级：{difficulty}
- 创意程度：{creativity}%
- 包含内容：{', '.join(include_items)}

请用生动有趣的语言，让写作变得像游戏一样好玩！"""
                            
                            system_msg = "你是一位充满童心和创造力的写作魔法师，善于用生动的语言和有趣的方式教孩子们写作。"
                            
                            response, error = call_deepseek_api(
                                prompt=prompt,
                                system_message=system_msg,
                                max_tokens=2500,
                                temperature=creativity/100
                            )
                            
                            if error:
                                st.error(f"😢 魔法失败: {error}")
                            elif response:
                                # 保存到历史
                                st.session_state.history.append({
                                    "type": "写作魔法",
                                    "time": datetime.now().strftime("%H:%M:%S"),
                                    "topic": topic[:50]
                                })
                                
                                # 显示结果
                                st.markdown("### 📜 **魔法写作教案**")
                                st.markdown(f'<div class="bubble-box">{response}</div>', unsafe_allow_html=True)
                                
                                # 操作按钮
                                st.markdown("<div class='rainbow-divider'></div>", unsafe_allow_html=True)
                                
                                btn_col1, btn_col2, btn_col3 = st.columns(3)
                                with btn_col1:
                                    st.download_button(
                                        label="📥 下载魔法书",
                                        data=response,
                                        file_name=f"魔法写作教案_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                                        mime="text/plain",
                                        use_container_width=True
                                    )
                                with btn_col2:
                                    if st.button("🔄 重新施展", use_container_width=True):
                                        st.rerun()
                                with btn_col3:
                                    if st.button("🎨 换主题", use_container_width=True):
                                        st.session_state.current_page = "writing"
                                        st.rerun()
            with generate_col2:
                if st.button("🎲 随机主题", use_container_width=True):
                    random_topics = [
                        "会说话的玩具",
                        "魔法森林冒险",
                        "未来的学校",
                        "我的梦想职业",
                        "如果我会飞"
                    ]
                    import random
                    st.session_state.random_topic = random.choice(random_topics)
                    st.rerun()

# 作文评价官页面
elif st.session_state.current_page == 'evaluation':
    st.markdown("<h1 class='main-title'>📝 作文评价官工作室</h1>", unsafe_allow_html=True)
    st.markdown('<p class="sub-title">🔍 粘贴作文，获取专业又有趣的写作反馈！</p>', unsafe_allow_html=True)
    
    # 作文输入区
    essay = st.text_area(
        "📖 **请粘贴学生作文**",
        height=300,
        placeholder="在这里粘贴学生的作文...\n\n例如：\n今天天气真好，我和小明一起去公园玩。我们看到了美丽的花朵...",
        help="可以直接复制粘贴整篇作文"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 **评价标准**")
        
        criteria = st.multiselect(
            "选择评价维度",
            ["内容创意", "结构组织", "语言表达", "语法规范", "情感表达", "想象力", "逻辑性"],
            default=["内容创意", "结构组织", "语言表达"],
            label_visibility="collapsed"
        )
        
        feedback_style = st.selectbox(
            "💬 **反馈风格**",
            ["鼓励式（发现闪光点）", "专业式（详细分析）", "趣味式（轻松活泼）", "成长式（进步建议）"]
        )
    
    with col2:
        st.markdown("#### 🎯 **评分选项**")
        
        show_stars = st.checkbox("⭐ 显示星级评价", value=True)
        if show_stars:
            star_system = st.radio(
                "评分体系",
                ["五星制", "十分制", "ABCD等级", "表情评价"]
            )
        
        include_suggestions = st.checkbox("💡 提供改进建议", value=True)
        include_examples = st.checkbox("✏️ 提供修改示例", value=True)
    
    # 评价按钮
    if st.button("🔍 **开始评价作文**", type="primary", use_container_width=True):
        if not st.session_state.api_key:
            st.error("🔑 请先在侧边栏输入魔法钥匙（API密钥）")
        elif not essay:
            st.warning("📝 请输入要评价的作文")
        else:
            with st.spinner("🧐 评价官正在认真阅读..."):
                # 构建提示词
                prompt = f"""请评价以下作文：

作文内容：
{essay}

评价要求：
- 评价维度：{', '.join(criteria)}
- 反馈风格：{feedback_style}
- {"显示" + star_system + "评分" if show_stars else "不显示分数"}
- {"提供具体的改进建议" if include_suggestions else ""}
- {"提供修改示例" if include_examples else ""}

请用专业又亲切的语言进行评价，既要指出优点，也要提供建设性的改进意见。"""
                
                system_msg = "你是一位专业又亲切的作文评价官，善于发现学生作文的闪光点，并用建设性的方式提供改进建议。"
                
                response, error = call_deepseek_api(prompt, system_message=system_msg, max_tokens=2500)
                
                if error:
                    st.error(f"😢 评价失败: {error}")
                elif response:
                    st.markdown("### 📋 **作文评价报告**")
                    st.markdown(f'<div class="bubble-box">{response}</div>', unsafe_allow_html=True)

# 智慧导师页面（交互指导）
elif st.session_state.current_page == 'chat':
    st.markdown("<h1 class='main-title'>💬 智慧导师聊天室</h1>", unsafe_allow_html=True)
    st.markdown('<p class="sub-title">🤔 有什么写作问题？随时问我！</p>', unsafe_allow_html=True)
    
    # 初始化聊天历史
    if 'tutor_messages' not in st.session_state:
        st.session_state.tutor_messages = [
            {"role": "assistant", "content": "👋 你好！我是你的AI写作导师——智慧博士！\n\n🎯 我可以帮助你：\n• 解答写作疑问\n• 提供写作技巧\n• 指导作文修改\n• 分析文章结构\n• 推荐好词好句\n\n💡 例如，你可以问我：\n• '如何写好作文开头？'\n• '怎样描写人物外貌？'\n• '议论文怎么写？'\n• '帮我看看这段文字怎么修改？'\n\n✨ 现在，告诉我你有什么写作问题吧！"}
        ]
    
    # 显示聊天记录
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.tutor_messages:
            if message["role"] == "assistant":
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #e3f2fd, #f3e5f5); 
                          padding: 20px; border-radius: 20px; margin: 10px 0 10px 0;
                          border: 2px solid #bbdefb;">
                    <div style="display: flex; align-items: center; margin-bottom: 10px;">
                        <div style="background: linear-gradient(135deg, #667eea, #764ba2); 
                                  color: white; padding: 8px 15px; border-radius: 15px;
                                  font-weight: bold; margin-right: 10px;">
                            🤖 智慧博士
                        </div>
                        <span style="color: #666; font-size: 0.9em;">正在为你解答...</span>
                    </div>
                    <div style="font-size: 1em; line-height: 1.6;">
                        {message['content'].replace('\n', '<br>')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #fff3e0, #ffecb3); 
                          padding: 20px; border-radius: 20px; margin: 10px 0 10px auto;
                          border: 2px solid #ffd54f; max-width: 80%;">
                    <div style="display: flex; align-items: center; margin-bottom: 10px;">
                        <div style="background: linear-gradient(135deg, #FF6B6B, #FF8E53); 
                                  color: white; padding: 8px 15px; border-radius: 15px;
                                  font-weight: bold; margin-right: 10px;">
                            👤 你
                        </div>
                    </div>
                    <div style="font-size: 1em; line-height: 1.6;">
                        {message['content'].replace('\n', '<br>')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # 聊天输入
    if prompt := st.chat_input("💭 输入你的写作问题..."):
        if not st.session_state.api_key:
            st.error("🔑 请先在侧边栏输入魔法钥匙（API密钥）")
        else:
            # 添加用户消息
            st.session_state.tutor_messages.append({"role": "user", "content": prompt})
            st.rerun()
            
            # 获取AI回复
            with st.spinner("🤔 智慧博士正在思考..."):
                response, error = call_deepseek_api(
                    prompt=prompt,
                    system_message="你是一位智慧又亲切的写作导师，善于用生动有趣的方式解答写作问题，引导学生思考。",
                    max_tokens=1500,
                    temperature=0.8
                )
                
                if error:
                    st.error(f"😢 对话失败: {error}")
                elif response:
                    st.session_state.tutor_messages.append({"role": "assistant", "content": response})
                    st.rerun()
    
    # 快捷问题按钮
    st.markdown("<div class='rainbow-divider'></div>", unsafe_allow_html=True)
    st.markdown("#### 💡 **常见写作问题**")
    
    questions = [
        "如何写好作文开头？",
        "怎样让作文更生动？",
        "写人作文怎么写？",
        "写景作文的技巧？",
        "如何修改作文？"
    ]
    
    cols = st.columns(5)
    for idx, question in enumerate(questions):
        with cols[idx]:
            if st.button(question, use_container_width=True):
                st.session_state.tutor_messages.append({"role": "user", "content": question})
                st.rerun()

# 词汇魔法书页面
elif st.session_state.current_page == 'vocab':
    st.markdown("<h1 class='main-title'>🔤 词汇魔法书房</h1>", unsafe_allow_html=True)
    st.markdown('<p class="sub-title">📚 丰富的词汇宝库，让语言表达更精彩！</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🔍 词汇搜索", "🎨 主题词汇", "✨ 词汇游戏"])
    
    with tab1:
        st.markdown("#### 🎯 **词汇扩展工具**")
        
        word = st.text_input(
            "输入关键词",
            placeholder="例如：美丽、快乐、奔跑、思考...",
            help="输入你想扩展的词汇"
        )
        
        if word:
            col1, col2 = st.columns(2)
            
            with col1:
                expand_types = st.multiselect(
                    "扩展类型",
                    ["同义词", "反义词", "高级词汇", "成语俗语", "短语搭配", "词语辨析"],
                    default=["同义词", "高级词汇", "短语搭配"]
                )
                
                grade_level = st.select_slider(
                    "适合年级",
                    options=["低年级", "中年级", "高年级", "初中", "高中", "通用"]
                )
            
            with col2:
                output_format = st.radio(
                    "展示方式",
                    ["卡片式", "列表式", "表格式", "图文式"]
                )
                
                include_examples = st.checkbox("包含例句", value=True)
            
            if st.button("🔮 **施展词汇魔法**", type="primary", use_container_width=True):
                if not st.session_state.api_key:
                    st.error("🔑 请先在侧边栏输入魔法钥匙（API密钥）")
                else:
                    with st.spinner("📖 正在翻阅词汇魔法书..."):
                        prompt = f"""请为词汇"{word}"提供扩展内容：

扩展类型：{', '.join(expand_types)}
适合年级：{grade_level}
展示方式：{output_format}
{"包含生动例句" if include_examples else ""}

请用有趣的方式呈现，帮助学生学习记忆。"""
                        
                        response, error = call_deepseek_api(prompt, max_tokens=2000)
                        
                        if error:
                            st.error(f"😢 词汇扩展失败: {error}")
                        else:
                            st.markdown("### 📖 **词汇魔法书**")
                            st.markdown(f'<div class="bubble-box">{response}</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("#### 🎨 **主题词汇库**")
        
        themes = ["季节天气", "动物植物", "人物描写", "心情情感", "学校生活", "家庭亲情", "自然风光", "科技未来"]
        selected_theme = st.selectbox("选择主题", themes)
        
        if selected_theme and st.button("生成主题词汇", use_container_width=True):
            if not st.session_state.api_key:
                st.error("🔑 请先在侧边栏输入魔法钥匙（API密钥）")
            else:
                with st.spinner("🎨 正在绘制主题词汇图..."):
                    prompt = f"""请为"{selected_theme}"主题提供丰富的词汇资源：
1. 核心词汇（10-15个）
2. 精彩短语（8-10个）
3. 优美句子（5-8句）
4. 写作小贴士（3-5条）

请用生动有趣的方式呈现。"""
                    
                    response, error = call_deepseek_api(prompt)
                    
                    if error:
                        st.error(f"😢 生成失败: {error}")
                    else:
                        st.markdown(f'<div class="bubble-box">{response}</div>', unsafe_allow_html=True)

# 魔法记录页面（使用统计）
elif st.session_state.current_page == 'stats':
    st.markdown("<h1 class='main-title'>📊 魔法成长记录册</h1>", unsafe_allow_html=True)
    st.markdown('<p class="sub-title">🌟 记录每一次写作的进步与成长！</p>', unsafe_allow_html=True)
    
    # 统计卡片
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="fun-card card-red">
            <div class="card-title">🎯 总使用次数</div>
            <div style="font-size: 2.5em; font-weight: bold; color: #FF6B6B; text-align: center;">
                128
            </div>
            <div style="color: #718096; text-align: center;">次魔法体验</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="fun-card card-orange">
            <div class="card-title">📝 作文生成</div>
            <div style="font-size: 2.5em; font-weight: bold; color: #FFD166; text-align: center;">
                64
            </div>
            <div style="color: #718096; text-align: center;">篇精彩作品</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="fun-card card-green">
            <div class="card-title">🔍 作文评价</div>
            <div style="font-size: 2.5em; font-weight: bold; color: #06D6A0; text-align: center;">
                48
            </div>
            <div style="color: #718096; text-align: center;">次专业评价</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="fun-card card-blue">
            <div class="card-title">💬 导师对话</div>
            <div style="font-size: 2.5em; font-weight: bold; color: #118AB2; text-align: center;">
                96
            </div>
            <div style="color: #718096; text-align: center;">次智慧交流</div>
        </div>
        """, unsafe_allow_html=True)
    
    # 成长记录
    st.markdown("<div class='rainbow-divider'></div>", unsafe_allow_html=True)
    st.markdown("### 📅 **近期魔法活动**")
    
    activities = [
        {"time": "今天 10:30", "type": "📝", "action": "生成了童话故事", "title": "《勇敢的小猫咪》", "badge": "badge-success"},
        {"time": "今天 09:15", "type": "🔍", "action": "评价了作文", "title": "《我的家乡》", "badge": "badge-info"},
        {"time": "昨天 16:45", "type": "💬", "action": "咨询了写作问题", "title": "如何写好开头", "badge": "badge-purple"},
        {"time": "昨天 14:20", "type": "🔤", "action": "学习了词汇", "title": "描写春天的词语", "badge": "badge-warning"},
        {"time": "前天 11:10", "type": "📝", "action": "生成了观察日记", "title": "《校园的梧桐树》", "badge": "badge-success"},
    ]
    
    for activity in activities:
        col_a, col_b, col_c = st.columns([2, 3, 2])
        with col_a:
            st.markdown(f"**{activity['time']}**")
        with col_b:
            st.markdown(f"{activity['type']} **{activity['action']}**：{activity['title']}")
        with col_c:
            st.markdown(f"<span class='fun-badge {activity['badge']}'>完成</span>", unsafe_allow_html=True)
        st.markdown("---")

# 学院设置页面
elif st.session_state.current_page == 'settings':
    st.markdown("<h1 class='main-title'>⚙️ 魔法学院设置中心</h1>", unsafe_allow_html=True)
    st.markdown('<p class="sub-title">🎨 个性化设置你的写作魔法学院！</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🎛️ 学院设置", "🌈 界面主题", "📖 关于学院"])
    
    with tab1:
        st.markdown("#### 🎛️ **学院基础设置**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            auto_save = st.checkbox("自动保存记录", value=True, help="自动保存你的写作记录")
            max_history = st.number_input("最大记录数量", 10, 1000, 100, help="保存的历史记录数量")
            
            notification = st.checkbox("新功能提醒", value=True, help="接收新功能更新提醒")
            
            if st.button("🗑️ 清空所有记录", use_container_width=True):
                st.session_state.history = []
                st.session_state.chat_history = []
                st.session_state.tutor_messages = []
                st.success("✨ 所有记录已清空！")
                time.sleep(1)
                st.rerun()
        
        with col2:
            default_model = st.selectbox(
                "默认魔法模型",
                ["DeepSeek魔法师", "写作精灵", "创意大师", "专业导师"]
            )
            
            timeout = st.slider("魔法响应时间", 10, 120, 30, help="等待AI响应的时间")
            
            if st.button("💾 保存设置", type="primary", use_container_width=True):
                st.success("✅ 学院设置已保存！")
                st.balloons()
    
    with tab2:
        st.markdown("#### 🎨 **界面主题设置**")
        
        theme = st.selectbox(
            "学院主题色",
            ["彩虹魔法", "海洋蓝", "森林绿", "日落橙", "星空紫", "糖果粉"]
        )
        
        font_size = st.select_slider(
            "字体大小",
            ["小", "中", "大", "特大"]
        )
        
        animation = st.checkbox("启用动画效果", value=True)
        sound_effects = st.checkbox("启用音效", value=False)
        
        if st.button("🎨 应用主题", type="primary", use_container_width=True):
            st.success("🌈 主题设置已应用！")
    
    with tab3:
        st.markdown("#### 📖 **关于魔法写作学院**")
        
        st.markdown("""
        <div class="bubble-box">
            <div style="text-align: center; margin-bottom: 20px;">
                <span style="font-size: 3em;">✏️📚🎨</span>
                <h2>英思织网魔法写作学院</h2>
            </div>
            
            **学院使命：**
            > 用AI魔法点亮每个孩子的写作天赋，让写作变得像游戏一样快乐！
            
            **版本信息：**
            - 🏫 学院版本：魔法版 2.0.0
            - 📅 建立时间：2024年1月
            - ✨ 最新更新：2024年1月12日
            
            **技术支持：**
            - 🧙‍♂️ 核心魔法：DeepSeek AI
            - 🏗️ 学院建筑：Streamlit
            - 🎨 界面设计：彩虹设计组
            
            **联系学院：**
            - 📧 魔法邮箱：magic@yingsizhiwang.com
            - 🌐 学院官网：www.yingsizhiwang.com
            - 🐙 魔法仓库：github.com/yingsizhiwang
            
            **特别感谢：**
            感谢所有小作家们的信任与支持！愿你们的写作之路充满欢乐与成长！
            
            ---
            
            <div style="text-align: center; margin-top: 20px;">
                <span class="fun-badge badge-success">🌈 魔法写作学院</span>
                <span class="fun-badge badge-info">✨ 让写作更快乐</span>
                <span class="fun-badge badge-purple">🎯 专业又有趣</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ======================== 彩虹页脚 ========================
st.markdown("<div class='rainbow-divider'></div>", unsafe_allow_html=True)

footer_col1, footer_col2, footer_col3 = st.columns([3, 1, 1])

with footer_col1:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px;">
        <span class="emoji-deco">🌈</span>
        <span style="font-weight: bold; color: #4A5568;">英思织网魔法写作学院</span>
        <span class="emoji-deco">✨</span>
        <span style="color: #718096;">| 让每个孩子爱上写作！</span>
    </div>
    """, unsafe_allow_html=True)

with footer_col2:
    if st.session_state.api_key:
        st.markdown('<span class="fun-badge badge-success">🔑 已激活</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="fun-badge badge-warning">🔑 未激活</span>', unsafe_allow_html=True)

with footer_col3:
    st.caption(f"🕐 {datetime.now().strftime('%H:%M:%S')}")