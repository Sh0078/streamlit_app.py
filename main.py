import streamlit as st

#@ Shafin Alex
# 01/02/2023

st.set_page_config(layout='wide')


st.markdown("<h1 style='text-align: center;'>Malayalam Song Translation", unsafe_allow_html=True)

activation_function = st.selectbox('Choose a Song',
                                ['None', 'Nee Ente Sangethavum', 'Nanniyode Njan Sthuthi Paadidum',
                                'Ennum Nallavan', 'Ennodulla Nin Sarva', 'Enikkothasha varum parvatham',
                                'Enikkayoruthama Sampathe', 'Vandhanam Yeshupara'])

## Song selection function
if activation_function == 'Nee Ente Sangethavum':
    col1, col2 = st.columns(2)

    col1.markdown("<h3 style ='text-align: center;'>Nee Ente Sangethavum", unsafe_allow_html=True)
    col1.markdown("""
                    <P1 style='text-align: center;'>
    
                        Nee ente sangethavum, 
                        nee ente kottayum, 
                        Nee ente praana naathanee 
                        en Dayvam
                    
                        Aaradhikkum njan purna hryda’yamode, 
                        Thedum nin mukam jeeva kaalam ellam
                        Sevi’chidum njan en sarva’vumay 
                        adiyanitha' Adiya’nitha Deva 
                        Adiya’nitha Deva, 
                        Adiya’nitha Deva, adiya’nitha'
                    
                        Nee ente raksha’kanum, 
                        Nee ente vydhya’num'
                        Nee ente aalamba’vum,
                        nee en Daivam'
                        
                        Nee ente pala’kanum, 
                        nee ente aashwaa’savum'
                        Nee ente maravi’davum, 
                        nee en Daivam 
                        
                        """, unsafe_allow_html=True)

    col2.markdown("<h3 style ='text-align: center;'>You are my refuge", unsafe_allow_html=True)
    col2.write(""" 
                <P2 style='text-align: center;'>
                    
                    You are my refuge 
                    You are my fortress
                    You are my friend in need 
                    You are my God

                    And I will worship you with all of my heart
                    I will seek your face all through my life 
                    I will serve you Lord with all that I am 
                    Here I am..
                    Here I am O Lord (3) 
                    Here I am

                    You are my Savior 
                    You are my healer
                    You are my strength in need 
                    You are my God.

                    You are my shepherd 
                    You are my comfort 
                    You are my hiding place 
                    You are my God.""", unsafe_allow_html=True)

## Song Selection function
if activation_function == 'Nanniyode Njan Sthuthi Paadidum':
    col1, col2 = st.columns(2)

    col1.markdown("<h3 style ='text-align: center;'>Nanniyode Njan Sthuthi Paadidum", unsafe_allow_html=True)
    col1.markdown("""
                       <P1 style='text-align: center;'>

                            Nanniyode Njaan Sthuthi Paadidum
                            Ente Yesu Naatha
                            Enikkyaai Nee Cheythoro Nanmakkyum
                            Innu Nanni Chollunnu Njaan - 2

                            Arhikkyaattha Nanmakalum
                            Enikkekidum Kripaa (Thayaa) Nidhe - 2
                            Yaachikkatha Nanmakal Polume
                            Enikkekiyoney Sthuthi - 2
                            Nanniyode

                            Sathya Daivatthin Yeka Puthranai
                            Angil Viswasikkunnu Njaan - 2
                            Varum kaalamokkeyum Nin Kripaa
                            Varangal Choriga Ennil - 2

                           """, unsafe_allow_html=True)

    col2.markdown("<h3 style ='text-align: center;'>Sing praises with thanksgiving", unsafe_allow_html=True)
    col2.write(""" 
                   <P2 style='text-align: center;'>

                        I will sing praises with thanksgiving
                        My Lord Jesus
                        For a good thing you did for me
                        I am thankful today
                        
                        Don't deserve all goodness from 
                        you Merciful god
                        You give all good things without
                        even asking 
                        
                        Only Son of the true God
                        I believe in you
                        Grace to you for all time to come
                        That the blessings flow
                        Sing Praise (2)

                        """, unsafe_allow_html=True)

## Song Selection function
if activation_function == 'Ennum Nallavan':
    col1, col2 = st.columns(2)

    col1.markdown("<h3 style ='text-align: center;'>Ennum Nallavan", unsafe_allow_html=True)
    col1.markdown("""
                       <P1 style='text-align: center;'>

                            Ennum Nallavan Yeshu Ennum Nallavan
                            Innaleyum Innum Ennum Annyanallavan 

                            Bharamullil Neridum Neramellam Thangkidum
                            Saramillennothidum Than Marvilenne Cherthidum

                            Sambhavangal Kelkkave Kampamullil Cherkkave
                            Thampurante Thiruvachanam Orkkavepomakave

                            Ulakaveyil Kondu Njaan Vaadi Veezhathoduvan
                            Thanalenikku Nalkiduvan Valabhagathaundu Than

                            Vishwasikkuvanum Ennasha Vechidanumee
                            Vishwamathil Ashwasikkan Asrayavum Yeshuvam

                            Ravilum Pakalilum Chelodu Than Palanam
                            Bhuvil Enikkullathinal Malinilla Karanam
                            
                            """, unsafe_allow_html=True)

    col2.markdown("<h3 style ='text-align: center;'>Forever he's good", unsafe_allow_html=True)
    col2.write(""" 
                   <P2 style='text-align: center;'>

                        Jesus is good, he's always good
                        Yesterday today forever he's good

                        The weight of this world hold me down, you hold the time
                        Don't worry of this present troubles, you will hold me close
                        
                        All things hearing and happening in this world
                        It's the coming of word of Jesus foretold
                        
                        You didn't let me wither in this Scorching Sun
                        Because you're on the right side to give me shade
                        
                        Hope to believe and desire to hold on
                        You're the reason we're thankful for this hope
                        
                        Day and night I feel you protection
                        In this earth I have everything I need
                        """, unsafe_allow_html=True)

## Song Selection function
if activation_function == 'Ennodulla Nin Sarva':
    col1, col2 = st.columns(2)

    col1.markdown("<h3 style ='text-align: center;'>Ennodulla Nin Sarva", unsafe_allow_html=True)
    col1.markdown("""
                       <P1 style='text-align: center;'>

                            Ennodulla nin sarva nanmakalkkai njan
                            enthu cheyendu ninakesupara-ippol

                            Nandi kondenteyullam nanne nirayunne
                            sannahamode sthuthi padidunnen-Deva

                            Papathil ninnu enne koriyeduppanai
                            shapa sikshakaletta devalmaja-maha

                            Enneyanpodu dhinam thorum nadathunna
                            ponnidayan anandam vandhaname-ente

                            Thathan sannidhiyilen perkku sada paksha
                            vadam cheyunna mama jeevanatha-paksha

                            Mannidayathil adiyan jeevikkum naalennum
                            Vandhanam cheyyum thirunaamathinu – Deva

                            """, unsafe_allow_html=True)

    col2.markdown("<h3 style ='text-align: center;'>What Should I do", unsafe_allow_html=True)
    col2.write(""" 
                   <P2 style='text-align: center;'>

                        What should I do for Jesus 
                        For all your loving kindness 

                        My heart is filled with joy
                        I will sing praise to you

                        To recuse me from my sin
                        You took my sins upon yourself O Lord Jesus

                        You carry me everyday
                        Thankful to you O Lord
                        
                        You're interceding for us 
                        In the presence of father, life giving God
                        
                        As long I live in this world
                        I will worship you Holy God
                        """, unsafe_allow_html=True)

## Song Selection function
if activation_function == 'Enikkothasha varum parvatham':
    col1, col2 = st.columns(2)

    col1.markdown("<h3 style ='text-align: center;'>Enikkothasha varum parvatham", unsafe_allow_html=True)
    col1.markdown("""
                       <P1 style='text-align: center;'>

                            Enikkothasha varum parvatham
                            Karthave nee maathramennalume

                            Aakasha bhumikalkellam
                            Athi hethuvayaven neye
                            Aasrayam ninnilayathu muthalen
                            Aadikalakannu para

                            En kankal uyarthi njan nokum
                            En karthave nin dayakai
                            Enniyal thera nanmakal thannu
                            Enne anugrahikum

                            En deham mannil marangalum
                            Njan jeevanodirullaum
                            Nee varum nalil ninnodananja-
                            nadicharthidum njan
                            """, unsafe_allow_html=True)

    col2.markdown("<h3 style ='text-align: center;'>My Safe Place", unsafe_allow_html=True)
    col2.write(""" 
                   <P2 style='text-align: center;'>

                        I will rest in the mountain
                        Lord! You are the only one

                        You're the creator 
                        Of Heaven and earth
                        My trust is in you O Lord
                        All my fears are gone
                        
                        I will lift up my eyes and look
                        O Lord for your mercy
                        You give me countless blessings
                        Will bless me again
                        
                        Even if my body is hidden in the soil
                        Even if I were alive
                        The day you come, I will come with you-
                        I'm filled with joy
                        """, unsafe_allow_html=True)

## Song Selection function
if activation_function == 'Enikkayoruthama Sampathe':
    col1, col2 = st.columns(2)

    col1.markdown("<h3 style ='text-align: center;'>Enikkayoruthama Sampathe", unsafe_allow_html=True)
    col1.markdown("""
                       <P1 style='text-align: center;'>

                            Enikkayoruthama Sampathe
                            Svargaraajyathilorukkunnathaal
                            Ini Lokathe Snehichiduvan
                            Oru Kaalathum Pokayilla Njan

                            Ente Ayussin Dinamokeyum
                            Ninne Mathram Njanini Sevikum
                            Ente Prana Nayakanesuve
                            Ninte Sneham Nee Enikekidane

                            Ezhayakunnorenne Snehicha
                            Ninte Snehamethrayo Achariam
                            Ente Papasapangal Neeki Nin
                            Thiru Jeevanal Enne Nirachallo

                            Ente Dehavum Thiru Alayamai
                            Ninte Athmave Enikekiyathal
                            Thiru'namathin Mahathvathinay
                            Ini Jeevippan Krupa Nalkuka

                            Priyan Thejasil Velipedum Nalil
                            Njanum Thejassin Mumpil Nilkuvan
                            Ente Dehavum Dehi Athmavum
                            Sampoornnamai Samarppickunne
                            """, unsafe_allow_html=True)

    col2.markdown("<h3 style ='text-align: center;'>My Treasure", unsafe_allow_html=True)
    col2.write(""" 
                   <P2 style='text-align: center;'>

                        A treasure for me
                        He preparing for me in the kingdom of heaven
                        Now to love the world
                        I will never leave you

                        All the days of my life
                        I will serve you only
                        O Lord of my soul
                        You give me your love

                        You loved thy servant
                        Your love is so amazing
                        My sins are removed
                        You filled me with your everlasting life

                        My body became a temple
                        You give me your spirit
                        For the glory of the holy name
                        Now give me the grace to live
                        
                        On the day when the Beloved will be revealed in glory
                        To stand before his Holiness
                        My body and soul
                        Complete submission
                        """, unsafe_allow_html=True)

## Song Selection function
if activation_function == 'Vandhanam Yeshupara':
    col1, col2 = st.columns(2)

    col1.markdown("<h3 style ='text-align: center;'>Vandhanam Yeshupara", unsafe_allow_html=True)
    col1.markdown("""
                       <P1 style='text-align: center;'>

                            Vandhanam Yeshupara ninakkennum vandhanam yeshupara
                            Vandhanam cheyyunnu ninnadiyar thiru naamathin aadharavaay

                            Innu nin sannidhiyil adiyarkku vannu cheruvathinay
                            Thanna ninnunnathamam krupakkabhi vandhanam cheythidunnu

                            Nin rudhiramathinal prethishticha jeeva puthu vazhiyay
                            Ninnadiyarkku pithavin sannidhou vannidame sathatham

                            Ithra mahathwamulla padhaviye ee puzhukkalkkarulan
                            Paathratha eathumilla ninte krupa ethra vichithramaho

                            Vaana dhootha ganangal manohara gaanangalal sathatham
                            Oonamenye pukazhthy sthuthikkunna vaanavane ninakku

                            Mannaril mannavan nee manukulathinu rekshakaran nee
                            Minnum prebhavamullon pithavinu sannibhan neeyallayo

                            Neeyozhike njangalkku suraloke aarulloo jeeva Nadha
                            Neeyozhike ihathil mattarumillagrahippan paranae
                            """, unsafe_allow_html=True)

    col2.markdown("<h3 style ='text-align: center;'>My Treasure", unsafe_allow_html=True)
    col2.write(""" 
                   <P2 style='text-align: center;'>

                        We welcome you O Lord, you're always welcome O Lord
                        We welcome you and honor your holy name
                        
                        Today I came before your presence O lord
                        I am grateful for the grace that has been given
                        
                        A new way of life established because of your blood
                        Because of you O Lord we could come before the Father
                        
                        What a glorious name we adore O Lord
                        How great your faithfulness I don't desire it
                        
                        Heavenly angels singing beautiful songs
                        You are the only one who desire all praises and glory O Lord
                        
                        You're above all, You're the savior of mankind
                        You're the shining light who sit close the Father
                        
                        Apart from you, we have no one in this world, O Lord
                        There is no one else in this world we desire except you
                        """, unsafe_allow_html=True)