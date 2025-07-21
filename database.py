import sqlite3

def create_table():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS chatbot_responses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        question TEXT UNIQUE,
                        answer TEXT)''')

    conn.commit()
    conn.close()

def insert_sample_data():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    sample_data = [
        # Thailand
        ("hello", "Hello! How can I assist you with your travel plans?"),
        ("hi", "Hi there! How can I help you with your trip?"),
        ("What are the most popular tourist attractions in Thailand?", 
         "Some of the top attractions in Thailand include the Grand Palace, Wat Arun, Phi Phi Islands, Chiang Mai, and Ayutthaya."),
        ("What is the best time to visit Thailand?", "The best time to visit Thailand is from November to March."),
        ("What is the currency used in Thailand?", "The currency used in Thailand is Thai Baht (THB)."),
        ("How do I get around in Bangkok?", "You can use BTS Skytrain, MRT subway, tuk-tuks, taxis, and Grab."),
        ("Can you recommend a budget-friendly hotel near the Grand Palace?", 
         "Yes, 'Chetuphon Gate' and 'Baan Wanglang Riverside' are great budget-friendly hotels."),
        ("Where can I try authentic Thai street food?", "Try street food at Yaowarat Road, Khao San Road, or Chatuchak Market."),
        ("What are the visa requirements for Thailand?", 
         "Visa requirements vary by nationality. Many countries get a visa-free entry for 30 days."),
        ("How do I travel from Bangkok to Phuket?", "By flight (1.5 hours), bus (12 hours), or train + bus combination."),
        ("What is the emergency number in Thailand?", "Dial 191 for police, 1155 for tourist police, and 1669 for medical emergencies."),

        # Malaysia
        ("What are the top tourist attractions in Malaysia?", 
         "Popular attractions in Malaysia include Petronas Towers, Langkawi, Batu Caves, and Penang Island."),
        ("What is the best time to visit Malaysia?", "Malaysia is great year-round, but the dry season (March-October) is best."),
        ("What is the currency used in Malaysia?", "The currency in Malaysia is the Malaysian Ringgit (MYR)."),
        ("How do I get around in Kuala Lumpur?", 
         "You can use MRT, LRT, Monorail, buses, taxis, or ride-sharing services like Grab."),
        ("Where can I find the best street food in Malaysia?", 
         "Visit Jalan Alor in Kuala Lumpur or Gurney Drive in Penang for amazing street food."),
        ("What are the visa requirements for Malaysia?", 
         "Many nationalities get a 90-day visa-free entry; check Malaysia’s immigration website."),
        ("How do I travel from Kuala Lumpur to Langkawi?", 
         "You can take a flight (1 hour) or a ferry from Penang (2.5 hours)."),
        ("What is the emergency number in Malaysia?", 
         "Dial 999 for police, fire, and medical emergencies in Malaysia."),
        
        # Singapore
        ("What are the must-visit attractions in Singapore?", 
         "You must visit Marina Bay Sands, Gardens by the Bay, Universal Studios, and Sentosa Island."),
        ("What is the best time to visit Singapore?", "Singapore is great year-round, but December to June is ideal."),
        ("What is the currency used in Singapore?", "The currency used in Singapore is the Singapore Dollar (SGD)."),
        ("How do I get around in Singapore?", 
         "Use the MRT, buses, taxis, or ride-hailing services like Grab."),
        ("Where can I find the best street food in Singapore?", 
         "Hawker centers like Maxwell Food Centre, Lau Pa Sat, and Chinatown Complex."),
        ("What are the visa requirements for Singapore?", 
         "Most nationalities get visa-free entry for 30-90 days; check Singapore’s immigration website."),
        ("How do I travel from Singapore to Malaysia?", 
         "You can take a bus, train, or flight to Kuala Lumpur."),
        ("What is the emergency number in Singapore?", 
         "Dial 999 for police and 995 for medical and fire emergencies."),

         #canada
         ("What are the most popular tourist attractions in Canada?", 
        "Top attractions include Niagara Falls, Banff National Park, CN Tower, Old Quebec, and Stanley Park."),
        ("What is the best time to visit Canada?", "The best time to visit Canada is from June to October for summer and December to February for winter sports."),
        ("What is the currency used in Canada?", "The currency used in Canada is the Canadian Dollar (CAD)."),
        ("How do I get around in Toronto?", "You can use the TTC subway, buses, streetcars, taxis, and Uber."),
        ("Can you recommend a budget-friendly hotel near Niagara Falls?", 
        "Yes, 'Days Inn by Wyndham' and 'Vittoria Hotel & Suites' are budget-friendly options."),
        ("Where can I try authentic Canadian food?", "Try poutine, maple syrup treats, and butter tarts in places like St. Lawrence Market."),
        ("What are the visa requirements for Canada?", 
        "Visa requirements vary by nationality. Many travelers need an eTA or a visitor visa."),
        ("How do I travel from Toronto to Vancouver?", "By flight (5 hours), train (4 days), or bus (3 days)."),
        ("What is the emergency number in Canada?", "Dial 911 for all emergency services."),

        #russia
        ("What are the most popular tourist attractions in Russia?", 
        "Popular attractions include the Red Square, Kremlin, Hermitage Museum, Lake Baikal, and Saint Basil's Cathedral."),
        ("What is the best time to visit Russia?", "The best time to visit Russia is from May to September for warm weather."),
        ("What is the currency used in Russia?", "The currency used in Russia is the Russian Ruble (RUB)."),
        ("How do I get around in Moscow?", "Use the Moscow Metro, taxis, and buses."),
        ("Can you recommend a budget-friendly hotel in Moscow?", 
        "Yes, 'Izmailovo Hotel' and 'Matreshka Hotel' are good budget options."),
        ("Where can I try authentic Russian cuisine?", "Try Russian food at Café Pushkin or Mari Vanna in Moscow."),
        ("What are the visa requirements for Russia?", 
        "Most travelers need a visa, which requires an invitation letter from a Russian host."),
        ("How do I travel from Moscow to Saint Petersburg?", "By high-speed Sapsan train (4 hours), flight (1 hour), or bus (8 hours)."),
        ("What is the emergency number in Russia?", "Dial 112 for police, fire, and medical emergencies."),

        #India
        ("What are the most popular tourist attractions in India?", 
        "Top attractions include the Taj Mahal, Jaipur's palaces, Kerala backwaters, Goa beaches, and Varanasi."),
        ("What is the best time to visit India?", "The best time to visit India is from October to March for pleasant weather."),
        ("What is the currency used in India?", "The currency used in India is the Indian Rupee (INR)."),
        ("How do I get around in Delhi?", "Use Delhi Metro, auto-rickshaws, buses, taxis, and ride-sharing apps like Ola and Uber."),
        ("Can you recommend a budget-friendly hotel near the Taj Mahal?", 
        "Yes, 'Hotel Taj Plaza' and 'Joey’s Hostel Agra' are budget-friendly options."),
        ("Where can I try authentic Indian street food?", "Try Chandni Chowk in Delhi, Bademiya in Mumbai, and Johri Bazaar in Jaipur."),
        ("What are the visa requirements for India?", 
        "Most travelers need an e-Visa, which can be applied online before arrival."),
        ("How do I travel from Delhi to Mumbai?", "By flight (2 hours), train (16 hours), or bus (24 hours)."),
        ("What is the emergency number in India?", "Dial 112 for all emergency services."),

        #Japan
        ("What are the most popular tourist attractions in Japan?", 
        "Must-visit places include Mount Fuji, Kyoto temples, Tokyo Tower, Hiroshima Peace Memorial, and Osaka Castle."),
        ("What is the best time to visit Japan?", "The best time to visit Japan is during cherry blossom season (March-April) and autumn (September-November)."),
        ("What is the currency used in Japan?", "The currency used in Japan is the Japanese Yen (JPY)."),
        ("How do I get around in Tokyo?", "Use the JR trains, subway, buses, and taxis."),
        ("Can you recommend a budget-friendly hotel in Tokyo?", 
        "Yes, 'Hotel Mystays Asakusa' and 'Khaosan Tokyo Samurai' are budget-friendly options."),
        ("Where can I try authentic Japanese sushi?", "Try Tsukiji Outer Market in Tokyo or Dotonbori in Osaka."),
        ("What are the visa requirements for Japan?", 
        "Many nationalities can visit visa-free for up to 90 days; others need a tourist visa."),
        ("How do I travel from Tokyo to Kyoto?", "By Shinkansen bullet train (2.5 hours) or bus (8 hours)."),
        ("What is the emergency number in Japan?", "Dial 110 for police and 119 for fire or medical emergencies."),

        #China 
        ("What are the most popular tourist attractions in China?", 
        "Famous attractions include the Great Wall, Forbidden City, Terracotta Army, Zhangjiajie, and West Lake."),
        ("What is the best time to visit China?", "The best time to visit China is from April to June and September to November."),
        ("What is the currency used in China?", "The currency used in China is the Chinese Yuan (CNY)."),
        ("How do I get around in Beijing?", "Use the Beijing Subway, taxis, and buses."),
        ("Can you recommend a budget-friendly hotel in Beijing?", 
        "Yes, '365 Inn' and 'Beijing Downtown Travelotel' are budget-friendly options."),
        ("Where can I try authentic Chinese food?", "Visit Wangfujing Snack Street in Beijing or Yuyuan Bazaar in Shanghai."),
        ("What are the visa requirements for China?", 
        "Most travelers need a visa; some cities allow a 144-hour transit visa exemption."),
        ("How do I travel from Beijing to Shanghai?", "By bullet train (4.5 hours) or flight (2 hours)."),
        ("What is the emergency number in China?", "Dial 110 for police, 120 for medical emergencies, and 119 for fire."),




        
        # General
        ("bye", "Goodbye! Have a safe and wonderful trip!"),
    ]
    cursor.executemany("INSERT OR IGNORE INTO chatbot_responses (question, answer) VALUES (?, ?)", sample_data)
    
    conn.commit()
    conn.close()
def create_users_table():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        location TEXT,
                        message TEXT NOT NULL)''')

    conn.commit()
    conn.close()

# Run only once to initialize the database
if __name__ == "__main__":
    create_table()
    insert_sample_data()
    create_users_table()
    print("Database initialized successfully!")
