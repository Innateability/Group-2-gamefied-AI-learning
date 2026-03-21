import random

question_bank = {

"AI Basics": {
    "Introduction": [
        ("AI stands for?", "Artificial Intelligence", ["Artificial Intelligence","automatic input","advanced internet","artificial interaction"]),
        ("AI is branch of?", "Computer Science", ["Computer Science","biology","chemistry","physics"]),
        ("Goal of AI?", "Simulate human intelligence", ["Simulate human intelligence","replace electricity","create hardware","design chairs"])
    ],
    "Components": [
        ("Which is a component of intelligence?", "Learning", ["Learning","jumping","running","sleeping"]),
        ("AI system should be?", "Intelligent", ["Intelligent","slow","manual","random"])
    ]
},

"Agents": {
    "Agent Concepts": [
        ("A rational agent acts to?", "Maximize performance", ["Maximize performance","minimize thinking","avoid actions","ignore environment"]),
        ("Omniscient agent means?", "Knows everything", ["Knows everything","knows nothing","random behavior","limited knowledge"])
    ],
    "Agent Structure": [
        ("Agent perceives through?", "Sensors", ["Sensors","legs","hands","wheels"]),
        ("Agent acts using?", "Actuators", ["Actuators","eyes","ears","brain"])
    ]
},

"Search": {
    "Search Basics": [
        ("State space refers to?", "All possible states", ["All possible states","only final state","initial state","goal only"]),
        ("Search problem includes?", "Initial state", ["Initial state","color","shape","sound"]),
        ("Goal state is?", "Desired solution", ["Desired solution","random state","start point","loop"])
    ],
    "Search Techniques": [
        ("Search strategy BFS uses?", "Queue", ["Queue","stack","tree only","array only"]),
        ("DFS uses?", "Stack", ["Stack","queue","list","set"]),
        ("Heuristic function is used in?", "Informed search", ["Informed search","random search","blind search","sorting"])
    ]
},

"Problem Solving": {
    "Concepts": [
        ("Problem solving involves?", "Finding solution path", ["Finding solution path","ignoring problem","random guessing","no planning"]),
        ("Cycle means?", "Repeating states", ["Repeating states","new state","end state","goal"]),
        ("Branching factor means?", "Number of child nodes", ["Number of child nodes","depth of tree","cost value","goal nodes"])
    ]
},

"Expert Systems": {
    "Basics": [
        ("Expert system is?", "AI system with knowledge base", ["AI system with knowledge base","simple calculator","game only","hardware device"]),
        ("Expert system example?", "Medical diagnosis system", ["Medical diagnosis system","keyboard","mouse","printer"])
    ],
    "Components": [
        ("Knowledge base stores?", "Facts and rules", ["Facts and rules","images only","videos","numbers only"]),
        ("Inference engine does?", "Reasoning", ["Reasoning","drawing","printing","typing"])
    ]
},

"NLP": {
    "Basics": [
        ("NLP stands for?", "Natural Language Processing", ["Natural Language Processing","neural learning process","new language program","natural logic processing"]),
        ("NLU means?", "Natural Language Understanding", ["Natural Language Understanding","neural logic unit","network learning unit","none"])
    ],
    "Applications": [
        ("NLP is used in?", "Chatbots", ["Chatbots","printers","routers","keyboards"]),
        ("ChatGPT is example of?", "NLP system", ["NLP system","hardware","printer","router"]),
        ("Language helps AI in?", "Communication", ["Communication","movement","storage","electricity"])
    ]
},

"Ethics": {
    "Issues": [
        ("Ethical issue in AI?", "Bias", ["Bias","speed","storage","size"]),
        ("Another AI ethical issue?", "Privacy", ["Privacy","color","design","shape"])
    ]
},

"Computer Vision": {
    "Basics": [
        ("Image recognition uses?", "Computer vision", ["Computer vision","audio processing","text typing","keyboard"]),
        ("First step in image processing?", "Image acquisition", ["Image acquisition","classification","output","storage"])
    ],
    "Processing": [
        ("Feature extraction means?", "Finding important patterns", ["Finding important patterns","removing data","printing image","deleting image"]),
        ("Classification means?", "Assigning labels", ["Assigning labels","deleting data","copying file","saving image"])
    ]
},

"Machine Learning": {
    "Concepts": [
        ("Machine learning is part of?", "Artificial Intelligence", ["Artificial Intelligence","mechanical engineering","biology","math only"]),
        ("Data is important for?", "Training AI", ["Training AI","drawing","printing","design"]),
        ("AI decision making uses?", "Algorithms", ["Algorithms","paper","ink","pen"]),
        ("Accuracy means?", "Correct predictions", ["Correct predictions","speed","size","shape"])
    ]
},

"Search Trees": {
    "Structure": [
        ("Search tree root is?", "Initial node", ["Initial node","leaf node","goal node","branch"]),
        ("Leaf node is?", "End node", ["End node","start node","middle node","random"])
    ]
},

"Applications": {
    "General": [
        ("AI helps in?", "Automation", ["Automation","manual work","writing only","drawing only"])
    ]
}

}

def get_random_question():
    topic = random.choice(list(question_bank.keys()))
    subtopic = random.choice(list(question_bank[topic].keys()))
    q, ans, options = random.choice(question_bank[topic][subtopic])

    random.shuffle(options)

    return topic, subtopic, q, ans, options