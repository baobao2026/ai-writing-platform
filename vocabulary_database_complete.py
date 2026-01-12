"""
词库数据库 - 基于义务教育英语课程标准 (2022版)
功能：分级词库管理、教材对照、CEFR分级、教学资源生成
版本：2.0
"""

# ==================== 小学1-2年级词库 (Beginner Level) ====================
GRADE_1_2_VOCAB = {
    "categories": {
        "family": {
            "words": ["mother", "father", "sister", "brother", "family", "baby", "grandma", "grandpa"],
            "chinese": ["妈妈", "爸爸", "姐妹", "兄弟", "家庭", "婴儿", "奶奶/外婆", "爷爷/外公"],
            "textbooks": {
                "人教版": ["mother", "father", "sister", "brother", "family"],
                "外研版": ["mother", "father", "sister", "brother", "grandma", "grandpa"],
                "牛津版": ["mother", "father", "family", "baby", "grandma", "grandpa"]
            },
            "cefr_level": "A1",
            "color": "#FF9E6D",
            "icon": "👨‍👩‍👧‍👦",
            "sample_sentences": [
                "This is my mother.",
                "I love my family.",
                "My father is tall."
            ]
        },
        "animals": {
            "words": ["cat", "dog", "bird", "fish", "panda", "rabbit", "tiger", "monkey"],
            "chinese": ["猫", "狗", "鸟", "鱼", "熊猫", "兔子", "老虎", "猴子"],
            "textbooks": {
                "人教版": ["cat", "dog", "bird", "fish", "panda"],
                "外研版": ["cat", "dog", "bird", "rabbit", "monkey"],
                "牛津版": ["cat", "dog", "fish", "tiger", "monkey"]
            },
            "cefr_level": "A1",
            "color": "#4ECDC4",
            "icon": "🐼",
            "sample_sentences": [
                "I like pandas.",
                "The cat is cute.",
                "Look at the bird!"
            ]
        },
        "colors": {
            "words": ["red", "blue", "yellow", "green", "black", "white", "orange", "pink"],
            "chinese": ["红色", "蓝色", "黄色", "绿色", "黑色", "白色", "橙色", "粉色"],
            "textbooks": {
                "人教版": ["red", "blue", "yellow", "green"],
                "外研版": ["red", "blue", "yellow", "green", "black", "white"],
                "牛津版": ["red", "blue", "yellow", "orange", "pink"]
            },
            "cefr_level": "A1",
            "color": "#FFD166",
            "icon": "🎨",
            "sample_sentences": [
                "The sky is blue.",
                "I like red apples.",
                "The flower is yellow."
            ]
        },
        "school": {
            "words": ["book", "pen", "bag", "school", "teacher", "student", "class", "friend"],
            "chinese": ["书", "钢笔", "书包", "学校", "老师", "学生", "班级", "朋友"],
            "textbooks": {
                "人教版": ["book", "pen", "bag", "school"],
                "外研版": ["book", "school", "teacher", "student"],
                "牛津版": ["book", "pen", "friend", "class"]
            },
            "cefr_level": "A1",
            "color": "#06D6A0",
            "icon": "🏫",
            "sample_sentences": [
                "This is my book.",
                "I go to school.",
                "She is my friend."
            ]
        },
        "body": {
            "words": ["head", "eye", "nose", "mouth", "hand", "foot", "ear", "face"],
            "chinese": ["头", "眼睛", "鼻子", "嘴巴", "手", "脚", "耳朵", "脸"],
            "textbooks": {
                "人教版": ["head", "eye", "nose", "mouth"],
                "外研版": ["head", "hand", "foot", "face"],
                "牛津版": ["eye", "nose", "mouth", "ear"]
            },
            "cefr_level": "A1",
            "color": "#EF476F",
            "icon": "👦",
            "sample_sentences": [
                "I have two eyes.",
                "Touch your nose.",
                "Wash your hands."
            ]
        },
        "numbers": {
            "words": ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"],
            "chinese": ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"],
            "textbooks": {
                "人教版": ["one", "two", "three", "four", "five"],
                "外研版": ["one", "two", "three", "six", "seven", "ten"],
                "牛津版": ["one", "two", "five", "eight", "nine"]
            },
            "cefr_level": "A1",
            "color": "#FF6B6B",
            "icon": "🔢",
            "sample_sentences": [
                "I have two hands.",
                "There are three apples.",
                "Count from one to ten."
            ]
        },
        "toys": {
            "words": ["ball", "doll", "car", "kite", "block", "bear", "plane", "boat"],
            "chinese": ["球", "娃娃", "小汽车", "风筝", "积木", "熊", "飞机", "船"],
            "textbooks": {
                "人教版": ["ball", "doll", "car", "kite"],
                "外研版": ["ball", "bear", "plane", "boat"],
                "牛津版": ["doll", "car", "block", "boat"]
            },
            "cefr_level": "A1",
            "color": "#4ECDC4",
            "icon": "🧸",
            "sample_sentences": [
                "This is my red ball.",
                "I play with a car.",
                "She has a doll."
            ]
        },
        "actions": {
            "words": ["run", "jump", "walk", "sing", "dance", "play", "eat", "drink", "sleep", "read"],
            "chinese": ["跑", "跳", "走", "唱", "跳舞", "玩", "吃", "喝", "睡觉", "读"],
            "textbooks": {
                "人教版": ["run", "jump", "sing", "play"],
                "外研版": ["walk", "dance", "eat", "drink"],
                "牛津版": ["run", "play", "sleep", "read"]
            },
            "cefr_level": "A2",
            "color": "#118AB2",
            "icon": "🏃",
            "sample_sentences": [
                "I can run fast.",
                "Let's sing together.",
                "Don't jump on the bed."
            ]
        },
        "classroom_objects": {
            "words": ["desk", "chair", "pencil", "ruler", "eraser", "crayon", "box", "glue"],
            "chinese": ["课桌", "椅子", "铅笔", "尺子", "橡皮", "蜡笔", "盒子", "胶水"],
            "textbooks": {
                "人教版": ["desk", "chair", "pencil", "ruler"],
                "外研版": ["pencil", "eraser", "crayon", "box"],
                "牛津版": ["desk", "chair", "glue", "crayon"]
            },
            "cefr_level": "A1",
            "color": "#FFD166",
            "icon": "✏️",
            "sample_sentences": [
                "My pencil is red.",
                "The ruler is on the desk.",
                "Can I use your eraser?"
            ]
        }
    },
    "sentence_patterns": [
        {"pattern": "This is a [noun].", "example": "This is a cat.", "difficulty": 1},
        {"pattern": "I like [noun].", "example": "I like dogs.", "difficulty": 1},
        {"pattern": "It is [adjective].", "example": "It is red.", "difficulty": 1},
        {"pattern": "I can [verb].", "example": "I can run.", "difficulty": 2},
        {"pattern": "My [noun] is [adjective].", "example": "My bag is big.", "difficulty": 2}
    ],
    "writing_prompts": [
        "Draw your family and write their names.",
        "What is your favorite animal? Draw it and write one sentence.",
        "Find three red things in your classroom. Write their names."
    ]
}

# ==================== 小学3-4年级词库 (Elementary Level) ====================
GRADE_3_4_VOCAB = {
    "categories": {
        "food": {
            "words": ["apple", "banana", "rice", "noodles", "milk", "water", "bread", "egg", "juice", "cake"],
            "chinese": ["苹果", "香蕉", "米饭", "面条", "牛奶", "水", "面包", "鸡蛋", "果汁", "蛋糕"],
            "textbooks": {
                "人教版": ["apple", "banana", "rice", "milk"],
                "外研版": ["noodles", "water", "bread", "egg"],
                "牛津版": ["juice", "cake", "banana", "bread"]
            },
            "cefr_level": "A1",
            "color": "#FF9E6D",
            "icon": "🍎",
            "sample_sentences": [
                "I eat an apple every day.",
                "Do you like bananas?",
                "Milk is good for you."
            ]
        },
        "seasons": {
            "words": ["spring", "summer", "autumn", "winter", "weather", "sunny", "rainy", "windy", "snow", "warm"],
            "chinese": ["春天", "夏天", "秋天", "冬天", "天气", "晴朗的", "下雨的", "有风的", "雪", "温暖的"],
            "textbooks": {
                "人教版": ["spring", "summer", "autumn", "winter"],
                "外研版": ["weather", "sunny", "rainy", "snow"],
                "牛津版": ["spring", "winter", "windy", "warm"]
            },
            "cefr_level": "A2",
            "color": "#4ECDC4",
            "icon": "🍂",
            "sample_sentences": [
                "Spring is warm and green.",
                "I like winter because of snow.",
                "It is sunny today."
            ]
        },
        "hobbies": {
            "words": ["drawing", "singing", "dancing", "swimming", "reading", "running", "playing", "watching", "listening", "writing"],
            "chinese": ["画画", "唱歌", "跳舞", "游泳", "阅读", "跑步", "玩", "观看", "听", "写作"],
            "textbooks": {
                "人教版": ["drawing", "singing", "reading", "playing"],
                "外研版": ["swimming", "running", "watching", "listening"],
                "牛津版": ["dancing", "writing", "reading", "playing"]
            },
            "cefr_level": "A2",
            "color": "#FFD166",
            "icon": "🎨",
            "sample_sentences": [
                "I like drawing pictures.",
                "She enjoys singing songs.",
                "We go swimming in summer."
            ]
        },
        "home": {
            "words": ["house", "room", "bed", "table", "chair", "door", "window", "kitchen", "bathroom", "garden"],
            "chinese": ["房子", "房间", "床", "桌子", "椅子", "门", "窗户", "厨房", "浴室", "花园"],
            "textbooks": {
                "人教版": ["house", "room", "bed", "table"],
                "外研版": ["door", "window", "kitchen", "bathroom"],
                "牛津版": ["house", "garden", "chair", "window"]
            },
            "cefr_level": "A1",
            "color": "#06D6A0",
            "icon": "🏠",
            "sample_sentences": [
                "My house has three rooms.",
                "The table is in the kitchen.",
                "I sleep in my bed."
            ]
        },
        "clothes": {
            "words": ["shirt", "dress", "shoes", "hat", "coat", "skirt", "trousers", "socks", "jacket", "uniform"],
            "chinese": ["衬衫", "连衣裙", "鞋子", "帽子", "外套", "裙子", "裤子", "袜子", "夹克", "校服"],
            "textbooks": {
                "人教版": ["shirt", "shoes", "hat", "coat"],
                "外研版": ["dress", "skirt", "trousers", "jacket"],
                "牛津版": ["shoes", "socks", "uniform", "jacket"]
            },
            "cefr_level": "A1",
            "color": "#9D4EDD",
            "icon": "👕",
            "sample_sentences": [
                "I wear a uniform to school.",
                "Put on your coat, it's cold.",
                "These shoes are new."
            ]
        }
    },
    "sentence_patterns": [
        {"pattern": "I am [verb]-ing.", "example": "I am reading.", "difficulty": 2},
        {"pattern": "There is/are [noun].", "example": "There are three apples.", "difficulty": 2},
        {"pattern": "I have a [noun].", "example": "I have a brother.", "difficulty": 2},
        {"pattern": "[Noun] can [verb].", "example": "Birds can fly.", "difficulty": 3},
        {"pattern": "I want to [verb].", "example": "I want to play.", "difficulty": 3}
    ],
    "writing_prompts": [
        "Describe your favorite season. What can you see, hear, and feel?",
        "Write about what you did last weekend (3-5 sentences).",
        "Make a shopping list for a picnic and write why you chose each item."
    ]
}

# ==================== 小学5-6年级词库 (Upper Elementary) ====================
GRADE_5_6_VOCAB = {
    "categories": {
        "environment": {
            "words": ["tree", "flower", "river", "mountain", "sky", "sun", "moon", "star", "cloud", "rainbow"],
            "chinese": ["树", "花", "河流", "山", "天空", "太阳", "月亮", "星星", "云", "彩虹"],
            "textbooks": {
                "人教版": ["tree", "flower", "river", "sun"],
                "外研版": ["mountain", "sky", "moon", "star"],
                "牛津版": ["cloud", "rainbow", "flower", "tree"]
            },
            "cefr_level": "A2",
            "color": "#06D6A0",
            "icon": "🌳",
            "sample_sentences": [
                "Trees give us clean air.",
                "The river flows to the sea.",
                "Look at the beautiful rainbow!"
            ]
        },
        "sports": {
            "words": ["basketball", "football", "running", "jumping", "cycling", "swimming", "skating", "tennis", "badminton", "exercise"],
            "chinese": ["篮球", "足球", "跑步", "跳跃", "骑自行车", "游泳", "滑冰", "网球", "羽毛球", "锻炼"],
            "textbooks": {
                "人教版": ["basketball", "football", "running", "swimming"],
                "外研版": ["jumping", "cycling", "skating", "exercise"],
                "牛津版": ["tennis", "badminton", "football", "swimming"]
            },
            "cefr_level": "A2",
            "color": "#FF9E6D",
            "icon": "⚽",
            "sample_sentences": [
                "I play basketball after school.",
                "Swimming is good exercise.",
                "We enjoy playing football together."
            ]
        },
        "occupations": {
            "words": ["doctor", "teacher", "policeman", "driver", "farmer", "cook", "nurse", "worker", "scientist", "artist"],
            "chinese": ["医生", "老师", "警察", "司机", "农民", "厨师", "护士", "工人", "科学家", "艺术家"],
            "textbooks": {
                "人教版": ["doctor", "teacher", "policeman", "driver"],
                "外研版": ["farmer", "cook", "nurse", "worker"],
                "牛津版": ["scientist", "artist", "doctor", "teacher"]
            },
            "cefr_level": "A2",
            "color": "#4ECDC4",
            "icon": "👨‍⚕️",
            "sample_sentences": [
                "My mother is a teacher.",
                "Doctors help sick people.",
                "I want to be a scientist."
            ]
        },
        "transportation": {
            "words": ["bus", "car", "bike", "train", "plane", "boat", "taxi", "subway", "walk", "drive"],
            "chinese": ["公交车", "汽车", "自行车", "火车", "飞机", "船", "出租车", "地铁", "走路", "开车"],
            "textbooks": {
                "人教版": ["bus", "car", "bike", "train"],
                "外研版": ["plane", "boat", "taxi", "subway"],
                "牛津版": ["walk", "drive", "bus", "plane"]
            },
            "cefr_level": "A1",
            "color": "#FFD166",
            "icon": "🚗",
            "sample_sentences": [
                "I go to school by bus.",
                "My father drives a car.",
                "We traveled by plane to Beijing."
            ]
        },
        "feelings": {
            "words": ["happy", "sad", "excited", "tired", "hungry", "angry", "scared", "surprised", "proud", "worried"],
            "chinese": ["开心的", "悲伤的", "兴奋的", "疲倦的", "饥饿的", "生气的", "害怕的", "惊讶的", "骄傲的", "担心的"],
            "textbooks": {
                "人教版": ["happy", "sad", "tired", "hungry"],
                "外研版": ["excited", "angry", "scared", "surprised"],
                "牛津版": ["proud", "worried", "happy", "sad"]
            },
            "cefr_level": "A2",
            "color": "#EF476F",
            "icon": "❤️",
            "sample_sentences": [
                "I feel happy when I play.",
                "Don't be sad, it's okay.",
                "She was excited about the trip."
            ]
        }
    },
    "sentence_patterns": [
        {"pattern": "I will [verb] tomorrow.", "example": "I will go to school tomorrow.", "difficulty": 3},
        {"pattern": "[Noun] is [comparative] than [noun].", "example": "The elephant is bigger than the cat.", "difficulty": 3},
        {"pattern": "I like [noun] because [reason].", "example": "I like pandas because they are cute.", "difficulty": 4},
        {"pattern": "First, [action]. Then, [action].", "example": "First, I wash my face. Then, I eat breakfast.", "difficulty": 4},
        {"pattern": "If [condition], [result].", "example": "If it rains, I will stay at home.", "difficulty": 4}
    ],
    "writing_prompts": [
        "Imagine you could have any job. What would it be and why?",
        "Describe your dream vacation. Where would you go and what would you do?",
        "Write a short story about helping someone in need."
    ]
}

# ==================== 词库管理器类 ====================
class VocabularyManager:
    """词库管理器 - 综合管理所有词汇资源"""
    
    def __init__(self):
        # 年级词库映射
        self.grade_vocab = {
            "1": GRADE_1_2_VOCAB,
            "2": GRADE_1_2_VOCAB,
            "3": GRADE_3_4_VOCAB,
            "4": GRADE_3_4_VOCAB,
            "5": GRADE_5_6_VOCAB,
            "6": GRADE_5_6_VOCAB
        }
        
        # CEFR级别词汇映射
        self.cefr_vocab = {
            "A1": ["cat", "dog", "red", "blue", "mother", "father", "book", "pen", 
                   "one", "two", "ball", "desk", "apple", "house", "shirt", "bus", "car"],
            "A2": ["panda", "rabbit", "green", "yellow", "sister", "brother", 
                   "teacher", "student", "run", "jump", "sing", "dance", "spring",
                   "summer", "happy", "sad", "basketball", "doctor"],
            "B1": ["grandma", "grandpa", "orange", "pink", "family", "baby", 
                   "class", "friend", "exciting", "beautiful", "important", "different"]
        }
        
        # 支持的教材列表
        self.supported_textbooks = ["人教版", "外研版", "牛津版"]
    
    def get_vocab_for_grade(self, grade, category=None):
        """获取指定年级的词库"""
        vocab = self.grade_vocab.get(str(grade), GRADE_3_4_VOCAB)
        
        if category:
            return vocab["categories"].get(category, {})
        return vocab
    
    def get_categories_for_grade(self, grade):
        """获取年级可用的词汇分类"""
        vocab = self.get_vocab_for_grade(grade)
        return list(vocab["categories"].keys())
    
    def get_sentence_patterns(self, grade, max_difficulty=5):
        """获取适合年级的句型"""
        vocab = self.get_vocab_for_grade(grade)
        patterns = vocab.get("sentence_patterns", [])
        
        # 过滤难度
        return [p for p in patterns if p["difficulty"] <= max_difficulty]
    
    def get_writing_prompts(self, grade):
        """获取写作提示"""
        vocab = self.get_vocab_for_grade(grade)
        return vocab.get("writing_prompts", [])
    
    def get_words_by_cefr(self, level="A1", textbook=None):
        """根据CEFR级别获取词汇"""
        words = self.cefr_vocab.get(level, [])
        
        if textbook and textbook in self.supported_textbooks:
            # 如果指定了教材，进一步筛选
            filtered = []
            for grade in ["1", "2", "3"]:
                vocab = self.get_vocab_for_grade(grade)
                for category_name, category_data in vocab["categories"].items():
                    textbook_words = category_data.get("textbooks", {}).get(textbook, [])
                    for word in textbook_words:
                        if word in words and word not in filtered:
                            filtered.append(word)
            return filtered
        
        return words
    
    def get_textbook_coverage(self, textbook="人教版", grade="1"):
        """获取教材覆盖率统计"""
        vocab = self.get_vocab_for_grade(grade)
        total_words = 0
        covered_words = 0
        
        for category_name, category_data in vocab["categories"].items():
            words_in_category = len(category_data["words"])
            total_words += words_in_category
            
            textbook_words = category_data.get("textbooks", {}).get(textbook, [])
            covered_words += len(textbook_words)
        
        if total_words > 0:
            coverage_rate = (covered_words / total_words) * 100
        else:
            coverage_rate = 0
        
        return {
            "textbook": textbook,
            "grade": grade,
            "total_words": total_words,
            "covered_words": covered_words,
            "coverage_rate": f"{coverage_rate:.1f}%",
            "missing_words": total_words - covered_words
        }
    
    def generate_picture_dictionary(self, grade="1", category=None):
        """生成图片词典数据"""
        vocab = self.get_vocab_for_grade(grade, category)
        
        if not vocab:
            return None
        
        picture_dict = []
        words = vocab.get("words", [])
        chinese_list = vocab.get("chinese", [])
        
        for i, word in enumerate(words):
            chinese = chinese_list[i] if i < len(chinese_list) else ""
            entry = {
                "word": word,
                "chinese": chinese,
                "image_url": f"images/{word}.png",
                "audio_url": f"audio/{word}.mp3",
                "category": category,
                "grade": grade
            }
            picture_dict.append(entry)
        
        return picture_dict
    
    def generate_spiral_review(self, grade="1", weeks=4):
        """生成螺旋式复习计划"""
        vocab = self.get_vocab_for_grade(grade)
        all_words = []
        
        for category_data in vocab["categories"].values():
            all_words.extend(category_data["words"])
        
        # 去重
        all_words = list(set(all_words))
        
        # 按周分配
        weekly_plan = {}
        words_per_week = min(8, len(all_words) // weeks)
        
        for week in range(1, weeks + 1):
            start_idx = (week - 1) * words_per_week
            end_idx = min(start_idx + words_per_week, len(all_words))
            weekly_plan[f"第{week}周"] = all_words[start_idx:end_idx]
        
        return weekly_plan
    
    def export_for_flashcards(self, grade="1", category=None, format="json"):
        """导出为闪卡格式"""
        vocab = self.get_vocab_for_grade(grade, category)
        
        if not vocab:
            return None
        
        words = vocab.get("words", [])
        chinese_list = vocab.get("chinese", [])
        sentences = vocab.get("sample_sentences", [])
        
        if format == "json":
            cards = []
            for i, word in enumerate(words):
                chinese = chinese_list[i] if i < len(chinese_list) else ""
                example = sentences[i % len(sentences)] if sentences else ""
                
                card = {
                    "front": word,
                    "back": chinese,
                    "example": example,
                    "pronunciation": f"/.../{word}/",
                    "category": category,
                    "difficulty": 1 if i < 3 else 2 if i < 6 else 3  # 简单难度分级
                }
                cards.append(card)
            
            return {
                "grade": grade,
                "category": category,
                "total_cards": len(cards),
                "cards": cards
            }
        elif format == "csv":
            # CSV格式
            csv_lines = ["front,back,example,category,difficulty"]
            for i, word in enumerate(words):
                chinese = chinese_list[i] if i < len(chinese_list) else ""
                example = sentences[i % len(sentences)] if sentences else ""
                difficulty = 1 if i < 3 else 2 if i < 6 else 3
                csv_lines.append(f'"{word}","{chinese}","{example}","{category}",{difficulty}')
            
            return "\n".join(csv_lines)
    
    def generate_word_game(self, grade, category, game_type="match"):
        """生成词汇游戏"""
        vocab = self.get_vocab_for_grade(grade, category)
        
        if not vocab:
            return None
        
        words = vocab.get("words", [])[:6]  # 取前6个词
        chinese_list = vocab.get("chinese", [])[:6]
        
        if game_type == "match":
            # 配对游戏：英文-中文
            game_data = {
                "type": "match",
                "title": f"{category}词汇配对游戏",
                "english_words": words,
                "chinese_words": chinese_list,
                "instructions": "将英文单词与对应的中文意思连线配对"
            }
            return game_data
        
        elif game_type == "fill":
            # 填空游戏
            sentences = vocab.get("sample_sentences", [])[:3]
            game_data = {
                "type": "fill",
                "title": f"{category}填空练习",
                "sentences": sentences,
                "answer_key": words[:3],
                "instructions": "从方框中选择正确的单词填入句子空白处"
            }
            return game_data
        
        elif game_type == "quiz":
            # 小测验
            quiz_questions = []
            for i, word in enumerate(words[:5]):
                question = {
                    "question": f"{word} 的中文意思是什么？",
                    "options": [
                        chinese_list[i] if i < len(chinese_list) else "未知",
                        chinese_list[(i+1) % len(chinese_list)] if chinese_list else "选项1",
                        chinese_list[(i+2) % len(chinese_list)] if len(chinese_list) > 2 else "选项2",
                        "以上都不对"
                    ],
                    "correct_answer": 0,
                    "explanation": f"{word} 的意思是 {chinese_list[i] if i < len(chinese_list) else '未知'}"
                }
                quiz_questions.append(question)
            
            return {
                "type": "quiz",
                "title": f"{category}词汇小测验",
                "questions": quiz_questions,
                "instructions": "选择每个单词的正确中文意思"
            }
    
    def get_grade_summary(self, grade):
        """获取年级词库统计摘要"""
        vocab = self.get_vocab_for_grade(grade)
        
        total_words = 0
        categories_count = len(vocab["categories"])
        
        for category_data in vocab["categories"].values():
            total_words += len(category_data["words"])
        
        return {
            "grade": grade,
            "categories_count": categories_count,
            "total_words": total_words,
            "sentence_patterns": len(vocab.get("sentence_patterns", [])),
            "writing_prompts": len(vocab.get("writing_prompts", []))
        }
    
    def search_vocabulary(self, keyword, search_in="all"):
        """搜索词汇"""
        results = []
        
        for grade in ["1", "2", "3", "4", "5", "6"]:
            vocab = self.get_vocab_for_grade(grade)
            
            for category_name, category_data in vocab["categories"].items():
                words = category_data.get("words", [])
                chinese_list = category_data.get("chinese", [])
                
                for i, word in enumerate(words):
                    chinese = chinese_list[i] if i < len(chinese_list) else ""
                    
                    # 根据搜索范围决定搜索字段
                    should_add = False
                    if search_in == "all":
                        should_add = (keyword.lower() in word.lower() or 
                                     keyword in chinese or
                                     keyword.lower() in category_name.lower())
                    elif search_in == "english":
                        should_add = keyword.lower() in word.lower()
                    elif search_in == "chinese":
                        should_add = keyword in chinese
                    
                    if should_add:
                        results.append({
                            "word": word,
                            "chinese": chinese,
                            "category": category_name,
                            "grade": grade,
                            "sample_sentence": category_data.get("sample_sentences", [""])[0]
                        })
        
        return results

# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=== 词库数据库测试 ===\n")
    
    # 1. 初始化管理器
    manager = VocabularyManager()
    
    # 2. 测试基本功能
    print("1. 一年级词库分类:")
    categories = manager.get_categories_for_grade("1")
    print(f"   {categories}")
    
    print("\n2. 人教版一年级覆盖率:")
    coverage = manager.get_textbook_coverage("人教版", "1")
    print(f"   总词汇数: {coverage['total_words']}")
    print(f"   覆盖词汇: {coverage['covered_words']}")
    print(f"   覆盖率: {coverage['coverage_rate']}")
    
    print("\n3. A1级别词汇（前10个）:")
    a1_words = manager.get_words_by_cefr("A1", "人教版")
    print(f"   {a1_words[:10]}")
    
    print("\n4. 生成图片词典（动物类）:")
    picture_dict = manager.generate_picture_dictionary("1", "animals")
    if picture_dict:
        print(f"   生成 {len(picture_dict)} 个词条")
        print(f"   示例: {picture_dict[0]}")
    
    print("\n5. 螺旋复习计划（4周）:")
    review_plan = manager.generate_spiral_review("1", 4)
    for week, words in review_plan.items():
        print(f"   {week}: {words[:3]}...")
    
    print("\n6. 导出闪卡（JSON格式）:")
    flashcards = manager.export_for_flashcards("1", "family")
    if flashcards:
        print(f"   生成 {flashcards['total_cards']} 张闪卡")
        print(f"   示例闪卡: {flashcards['cards'][0]['front']} - {flashcards['cards'][0]['back']}")
    
    print("\n7. 生成词汇游戏:")
    game = manager.generate_word_game("1", "animals", "quiz")
    if game:
        print(f"   游戏类型: {game['type']}")
        print(f"   题目数量: {len(game['questions'])}")
    
    print("\n8. 年级统计摘要:")
    summary = manager.get_grade_summary("1")
    for key, value in summary.items():
        print(f"   {key}: {value}")
    
    print("\n9. 词汇搜索测试（搜索'dog'）:")
    search_results = manager.search_vocabulary("dog")
    if search_results:
        print(f"   找到 {len(search_results)} 个结果")
        for result in search_results[:2]:
            print(f"   - {result['word']} ({result['chinese']}) - {result['category']} (Grade {result['grade']})")
    
    print("\n=== 测试完成 ===")