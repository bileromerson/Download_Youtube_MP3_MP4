
out_folder = 'Music/test' # output folder for downloaded files

# I'm still trying to put the .JPG thumbnail, but it's already working with the video's tumbnail

download_thumbnail = True
allow_duplicate_downloads = False # for duplicate downloads Ex: Music(1).mp3 BETA!!!
show_progress = True # show progress bar during download
Metadata = True  # if you want to add metadata to the files

#           -------------- Quality Settings --------------

audio_quality = '120' #  audio quality kbps
video_quality = '1080'#  video quality Pixels
fps = '30' #  >>>>>>>>>  frames per second FPS

#           -------------- Artists and URLs --------------

artists_urls = { # list of artists and their youtube urls
    'retrospectiva animada':[
        'https://www.youtube.com/watch?v=NEwA9OQmqXw&list=PL2EJlPZ0iJu6PcnlZCoU_PQrHhi0WGKiF' #Playlist completa {MP4}
    ],
     "Ivycomb":[
        'https://www.youtube.com/watch?v=e6xy35omS1A', #LAB RAT {MP4}
    ],
   "Alok": [
        'https://www.youtube.com/watch?v=qUUKIJqx010',# The Book Is On The Table
    ],
    "Arctica The Fox":[
        'https://www.youtube.com/watch?v=jeLQoGnbTsY&list=OLAK5uy_kNpipHajAQjp_hz3UDGTdGFxjWwHskrHc',# Bittersweet
        'https://www.youtube.com/watch?v=E2lZ51VIJ9o&list=OLAK5uy_kv12hbd29HJuL7A_v_dpSUOcJnfQeW57Y',# Dreamscape (playlist)
        'https://www.youtube.com/watch?v=_Mz3QyH3K18&list=OLAK5uy_l1DZq9RhFIIhW2jQ-aIel5fxRCkqwz4ec',# In Your Rain
        'https://www.youtube.com/watch?v=80ezKLZMlhs&list=OLAK5uy_mDCVug3OburoGlGrx2AzJuVIwSCaRAE4g',# Sing For The Void
        'https://www.youtube.com/watch?v=niJZw4kZ7ak&list=OLAK5uy_mtw1Wbrgy1friMCJO-9JX0UzLXgoV9L_s',# Over Amplified
        'https://www.youtube.com/watch?v=e4Lbhd8a4fA&list=OLAK5uy_mM8MEQwubS3fnNinUdur5KVyh-mTTQgLo',# Buttered Toast
        'https://www.youtube.com/watch?v=j-SYw_hNRmc&list=OLAK5uy_lynnyb0rBD3CX0DzTpHIgUmmtPhsa8V2U',# Ain't The Kinda Lovin' I Do
    ],
    "Snuffles":[
        'https://www.youtube.com/watch?v=GS3qN6EIGk4',# I cant stop making mistakes 
        'https://www.youtube.com/watch?v=_dMbSHwtKk8&list=OLAK5uy_mAOoBZjMD2MBnKigNWQjyWqO9oDZqI8D4',# Forgive Me Please (playlist)
        'https://www.youtube.com/watch?v=njowoGhmw6E&list=OLAK5uy_mKdgOUqujhvkqHIONfZKgt9k5wHuCSdxI',# too late 2
        'https://www.youtube.com/watch?v=xp2SzlnzbkA&list=OLAK5uy_nd0U1gYnm4djWbFTeQkeeqMkXmtCcAS7k',# Seven Run
        'https://www.youtube.com/watch?v=pEtcyFBysAg&list=OLAK5uy_nsF0girFJkrpELredpI3I9ZImlZ81r644',# too late
        'https://www.youtube.com/watch?v=kg3ed9NRQJo&list=OLAK5uy_lnsxWpgYrwA8HKloWfrRGlL9OtUduCaMI',# Keep on With It
        'https://www.youtube.com/watch?v=UG1HUOyL9IA&list=OLAK5uy_kEIcrTM3RWwm9j5qBoQmZWQZNKl20MXys',# Won't Go
        'https://www.youtube.com/watch?v=WAX_FEgRuOk&list=OLAK5uy_kIDwFKKJcR6noC1e1JJU-nIrQJzBS3MMg',# what the
        'https://www.youtube.com/watch?v=tc8IhElRJkA&list=OLAK5uy_lzYhwLgaAyHfAQO0iegxNz5hgRfYLn_zQ',# this thought  {mp4}
       'https://www.youtube.com/watch?v=GUZWSxqDJUk&list=OLAK5uy_mRa2eCQmZvj3MR3-az37Rb_8NHDpaVRfo',# SPOTS
       'https://www.youtube.com/watch?v=-cIQJ4v_fgk&list=OLAK5uy_lp4Xk0Xf_4B7eAb9XYmB5k_wayTeNooY4',# ready or not? (all variations)
        'https://www.youtube.com/watch?v=A02vT-I4Dds&list=OLAK5uy_n8FLDf0Iyqhme6uHxJSAIpxYFWf6Eynmo',# i don't wanna {mp4}
      'https://www.youtube.com/watch?v=q7GOk-cE3mY&list=OLAK5uy_mGmWuKY6gPq_iguZ0l19dHlcTLazsBGXE',# NO NICE THINGS (playlist)
      'https://www.youtube.com/watch?v=b4VFkSG4lk8&list=OLAK5uy_nC9wPyRwh8FgxoDoPz8LEwr5Nqbzi9maw'# SPOTS 2 {MP4}
    ],
    
    "Verplex":[
        'https://www.youtube.com/watch?v=9Qjz_nofaTU&list=OLAK5uy_kPMzB4Ikv1IZncGQh6SEjbGjAlRP4SUuQ&index=1',# Furry Youtubers (playlist)
        'https://www.youtube.com/watch?v=MT9mjFmuXrM&list=OLAK5uy_lmNOCPJHrqXVGe-v86N10cEb2qPbpVABA',# On My Way (playlist)
        'https://www.youtube.com/watch?v=j1BBDk7dRU4&list=OLAK5uy_nm3m_s6rTSb7b1VZ4EGRM9prq6pt9zWvA',# Fading Away (playlist)
        'https://youtu.be/2W1430K81fY?si=SqJIowF0tBVLOI4H',# Universe
        'https://youtu.be/MN40SigmSG8?si=DVHzZceDWIRd9cfl',# Check
        'https://youtu.be/6sb4ZJycP10?si=OK_r80DADTXHQOoG',# I Really Want You
        'https://youtu.be/qREZFPu543k?si=wXgwQVHIdZvCoP_s',# Never Too Late
        'https://youtu.be/2-hvzl4ZGAE?si=1MpbiolznUDlSD4I',# Sunset
        'https://youtu.be/S2xcpKl0k98?si=B6q6YfnOpFjgH3IJ',# Bean
        'https://youtu.be/lsWCxrLbUy0?si=iH3BGONfaia2oU5o',# VRChat {MP4}
        'https://youtu.be/wrsSoHogXNY?si=wpo1aK1dyoN4nubt',#  Divergent
        'https://www.youtube.com/watch?v=7phPDKJRoL0&list=OLAK5uy_mZuoOOPSosrDJfeFhhKhpPRl46FuvSxao',# I've Been Gone
        'https://www.youtube.com/watch?v=7r4BvQcp28Q&list=OLAK5uy_lwD8otxu138tB_mndBloSlY3xCRmqujhw',# Reach For The Stars
        'https://www.youtube.com/watch?v=uIkg7CX4H5M&list=OLAK5uy_nEz_7t3XbRqYDrmNyt0gCVY7ZzNmZs-Fs',# Reunite Our Life
        'https://www.youtube.com/watch?v=obEpf-UqmQg&list=OLAK5uy_myJW2KhTgMdxe-QeVB_0LyesJi_gXdIg0',# Future VIP
        'https://www.youtube.com/watch?v=2ha1-PI8O7M&list=OLAK5uy_nEhM5-XkhmKJ_hEtr-EOt6STLuaxgMGFc',# Fallen World
        'https://www.youtube.com/watch?v=ECmFUcgJock&list=OLAK5uy_mAQ7zQ41xr3SO7etS95rbEGaDoyd2OFr8',# Move Into The Light
        'https://www.youtube.com/watch?v=vMUW3B0kbCc&list=OLAK5uy_m2P-8g6Pr8EUKtRfevtOCAl9L_9wtmaYs',# I miss you
        'https://www.youtube.com/watch?v=mzuRmldhgmo&list=OLAK5uy_kM_PEyqDuKrEKBydCinM8x71oQy12fp_M',# Howl
        'https://www.youtube.com/watch?v=fiRnaIOgGWQ&list=OLAK5uy_m2POT2mwpMyxbKprsMMb1vRB10xSUYA6c',# Wag My Tail (playlist)
        'https://www.youtube.com/watch?v=8CDylhggwXA&list=OLAK5uy_m7-Mkbdh3pegmmhMLqliDFYcz2q-ymgNU',# Drivin' To The Moonlight
        'https://www.youtube.com/watch?v=Tcf5ZB5GtbY&list=OLAK5uy_lAyJ9-rcJ_86--ugN4lI2bkz4L5zSYBuE',# Fly Away
        'https://www.youtube.com/watch?v=ThxrRKztpR8&list=OLAK5uy_lhUmLokgXUtNzIoSLGSCAqeVgKNEXmDIc',# Spark
        'https://www.youtube.com/watch?v=-KNWakEZHzE&list=OLAK5uy_lqs_4kn5pJiAMnG7fSA7_Nw3NX2uCj-Tw',# Close To Me
        'https://www.youtube.com/watch?v=ZGIMoV4RPkQ&list=OLAK5uy_nY1zHCaaNvY4c_IsLTbTVbYcIu-RTTS_s',# Galaxy
        'https://www.youtube.com/watch?v=JEDzySz3IN8&list=OLAK5uy_ms-OBAGp-e4G2PkI8uRlSWBZqC8GCQ7Gc',# I need Sombody {MP4}
        'https://www.youtube.com/watch?v=yKsOFf4F3wg&list=OLAK5uy_nz5gC554yL9aOCxTc43oFW8Bk4pa-MN_E',# My Future
        'https://www.youtube.com/watch?v=FBYAfXY-qoQ&list=OLAK5uy_lcQEbbpcIl3Ucl7ZPEpWf7HUhBQxouEAE',# Love and Affection
        'https://www.youtube.com/watch?v=z1IdaICQ8OY&list=OLAK5uy_noP4t1pVxVxMcql71g69IpDFOKJ-kgO-w',# Green N Purple
        'https://www.youtube.com/watch?v=LWQHXAnKC58&list=OLAK5uy_klElLbLXUO-g4impKglD92wRajY9TGwGI',# Dreamscape
        'https://www.youtube.com/watch?v=TVhBWBPmT5w&list=OLAK5uy_ksy082fO2KJ3RgcX2NgwcRdhOpK8uDQpk',# Colors

    ],
    
    "Ivycomb":[
        'https://www.youtube.com/watch?v=e6xy35omS1A', #LAB RAT {MP4}
        'https://www.youtube.com/watch?v=mVPUbGQdx2w', #LOVE LETTER
        'https://www.youtube.com/watch?v=3b8SfbqD7Yw&list=OLAK5uy_nOOLG59VVJRytk9ghYXfylODcv3TzXRsM',# THE RINGMASTER (all variations)
        'https://www.youtube.com/watch?v=xF_gHb4_K98&list=OLAK5uy_nsjRiwOOS4s7KDa02m76YYZJbjHGTEZRw',# Rebirth (playlist)
        'https://www.youtube.com/watch?v=YuHeSoASQPs&list=OLAK5uy_m015vrwWGkEQ6x5jFLXugfQDyD2ZkPcYE',# HYPNOFREAK (all variations)
        'https://www.youtube.com/watch?v=yZfgMgIOS3E&list=OLAK5uy_klD7cqgO1absGEfwSvu7KBnN0G7WsIudI',# INFAMOUS (all variations)
        'https://www.youtube.com/watch?v=hnJr0Fdm0bU&list=OLAK5uy_nH2l1qzxfhji4sUBGF88RLPDzVlZo9K80',# Cybernetic Heart (all variations)
        'https://www.youtube.com/watch?v=eJLbw0Oq2S8&list=OLAK5uy_lUdCOhyBmC0nELUuTr6jMzaVGllIrstFU',# DATA_REJECT (all variations)
        'https://www.youtube.com/watch?v=FNunVRexQ9k&list=OLAK5uy_l2e59OrGenJDIXQ2t1JeRRCfFcJdY5F58',# LDR (all variations)
        'https://www.youtube.com/watch?v=VQywoIhcNC8&list=OLAK5uy_mghX73W3hk4yZ7caMuQcoEniOYltYCTOo',# SAHARA (all variations)
        'https://www.youtube.com/watch?v=VC2WpFKuzZw&list=OLAK5uy_lqXzGNhX9tyXuQcGWGojWxOfZaRJjlW8I',# SLUGCAT PINBALL
        'https://www.youtube.com/watch?v=3Nhn-a2gSlE&list=OLAK5uy_ky_9sKRZ1mOW-HB1RpTvz8RjH5CMNILcQ',# Luminescence (all variations)
        'https://www.youtube.com/watch?v=OWd-oH_Lylc&list=OLAK5uy_n8oHG4vujwYhV1-wbv9KCDNdcBfbLxlEg',# ANTIVILLAIN
        'https://www.youtube.com/watch?v=txeHnnCj9Ow&list=OLAK5uy_lQjgOG7MhQuvpsWgkAtovaQ5nMYQTBnKU',# Fratricide
        'https://www.youtube.com/watch?v=r37UXmf4E3s&list=OLAK5uy_lJjybsq02aIkd_ulWiJ_mzJ7z7sWoAgZo',# Fool's Gold
        'https://www.youtube.com/watch?v=I7RwP8ItO1M&list=OLAK5uy_mBS25bwRE7p09VWaIMvqEfaN-krhZ717I',# Sheep to Goat
        'https://www.youtube.com/watch?v=Y-UPgQOt874&list=OLAK5uy_nIriExSLEHLl96FcCibtIrf4sg0owa2tY',# TOKYO ANNIVERSARY
        'https://www.youtube.com/watch?v=jtnoDnOo_nE&list=OLAK5uy_ne4L36wnflBhLK133CgZfjqVmH3aXBbyc',# ANTIHUMAN
        'https://www.youtube.com/watch?v=Mvik9CTsNrA&list=OLAK5uy_mOXaosw_tSQ7A2nLN_X1Z12XRqrB1TD2I',# NOTORIOUS
        'https://www.youtube.com/watch?v=vUa4yI5pRCE&list=OLAK5uy_kHztMDCVAcidwm-DazpD3fcBURlCNO4D4',# Blue Bird
        'https://www.youtube.com/watch?v=kYELWX1fu18&list=OLAK5uy_lyF21ZxsF6lLnAphVfPLfkteaeJXYg8_o',# I Won't Submit
        'https://www.youtube.com/watch?v=qul3Qd11u90&list=OLAK5uy_lF6xKF62zn2oDnWnCoJqgG3iwP16huGNY',# The Imposter
        'https://www.youtube.com/watch?v=aXHLgy-HQ4w&list=OLAK5uy_keVOA6f55E_ZD8XO2PKYe13WXUUHlwbb0',# Sparkle
        'https://www.youtube.com/watch?v=Pfv18GSX324&list=OLAK5uy_n4eFPw2iCMzDKS-gSTU7ZtmL_0YsU4IE8',# GIZABYTE
        'https://www.youtube.com/watch?v=Lnyw5aJkZjg&list=OLAK5uy_lDU78gf_6ikrHN2-lENlbX4iP1VHj5K8A',# leave a message
        'https://www.youtube.com/watch?v=8G_wgBxnTec&list=OLAK5uy_lnDKaKYg4U3Gx9SErO9-PsQm7E6tCkA84',# TOKYO
        'https://www.youtube.com/watch?v=7hZjuxooNjk&list=OLAK5uy_kJVRPd-JbQEx9PmdT3mvTxxlRoqt61Q7k',# Death Valley
        'https://www.youtube.com/watch?v=r8aqc6AGJKM&list=OLAK5uy_lipx_vH7ncLqrQQC9cBUtq2eYqLaaeSFM',# #FLUTEGANG
        'https://www.youtube.com/watch?v=Uq4Jees1sik&list=OLAK5uy_lBptObrrnFD-qNg7I92uZiq_PIUHA9BN8',# Soul Astray
        'https://www.youtube.com/watch?v=TlDL2G31QLQ&list=OLAK5uy_k5dQ5TFFUGuH2liCVsuFSQlNB48wK_vvk',# Throwback Thursday (playlist)
        
    ],
    
    "narpy":[
        'https://www.youtube.com/watch?v=DpJpdJPndlM&list=OLAK5uy_mkKc5O3pqotX5k3dN4TY-jcpnGdexAuvQ',# fluffy clouds
        'https://www.youtube.com/watch?v=HpXyLcAdnG8&list=OLAK5uy_ndTg0FNTGzp_uow-qc_UZK-8cAU8HaVvw',# affection
        'https://www.youtube.com/watch?v=LaSBPWQWrGk&list=OLAK5uy_khPW1JiqdhRfDo6WfDuLxipb7giUU2jGo',
        'https://www.youtube.com/watch?v=KdAxWr_htj8&list=OLAK5uy_kinRE8M76w_556y6FdwFNjUVuInvp2X88',
        'https://www.youtube.com/watch?v=J4peYh3dOSA&list=OLAK5uy_njzcgFYWx2mwkAFYnP5lY8JWzcuZFVB-A',
        'https://www.youtube.com/watch?v=4y2fOSYyLWk&list=OLAK5uy_koZ9AQ-QkafBUjrRIoRfUl2u2fPyGBnfs',
        'https://www.youtube.com/watch?v=qRpvJEazUfo&list=OLAK5uy_nfB3Wb_Roq5S0fFH6lTpkFLW7Fo8yqen8',

    ],
    
    "When Snakes Sing":[
        'https://www.youtube.com/watch?v=Vjf-x-zngx0&list=PLVs7u8sISshyMDvrUbHHQWO7FazYjXECk',
        'https://www.youtube.com/watch?v=RQYpNAV0rUI&list=PLVs7u8sISshwZaLP6A5mOIv7St7U5SeZO',
        'https://youtu.be/PAigrSsOCyY?si=eB-I9rBmVE_P0lPo',
        'https://www.youtube.com/watch?v=nzay7XJf1qM&list=OLAK5uy_lXX2KqKamBZyIqbOTM8O_aTE1-NkOHCMU',
        'https://www.youtube.com/watch?v=ZwbxqGVCQGc&list=OLAK5uy_m8HWgkAbeNZ0fKANMKpQrmOIHcrCWDqHM',
        'https://www.youtube.com/watch?v=CG_G5FU956E&list=OLAK5uy_neQrN6v7K_mqg32CVS_AUJW0l1k-iGgV8'    
    ],
    "Jakeneutron":[
        'https://www.youtube.com/watch?v=VGD4deEKb88',# Everlasting Fun (Derivative Version) {MP4}
        'https://www.youtube.com/watch?v=2Q_O3l_15xg'# Everlasting Fun (Derivative Vocals Only Version)
        'https://www.youtube.com/watch?v=LnHyMXsvLSc'# Everlasting Fun (Derivative Instrumental Version)
    ],
    
    "The score":[
        'https://www.youtube.com/watch?v=ALXFl6HfKbg',# Visions {MP4}
        'https://youtu.be/ALXFl6HfKbg?si=XxP_zdq_enG2zTOD',# Visions {MP4}
        'https://youtu.be/uf1M263w_fQ?si=R3WwMXwnS3nj6LcL',# Fighting For {MP4}
        'https://youtu.be/uhXW7eqF_SQ?si=b4aEQkulnowWxqtm',# Down With The Wolves {MP4}
        'https://youtu.be/6sl7rTwPJuo?si=h3YUTxeVQ3bbEtoi',# Power {MP4}
        'https://youtu.be/ruw2woPI-fg?si=k50lj6REERE84ZE6',# Don't Need A Hero {MP4} dont nead a hero
        'https://youtu.be/RyBDRS39G_w?si=PxR7i1-Xmt2szVkh',# Survivor {MP4} survivor
        'https://youtube.com/watch?v=jecQcgbyetw&pp=ygURdGhlIHNjb3JlIGxlZ2VuZHM%3D',# Legend {MP4} atlas
        'https://youtu.be/ZRRt8EyYNvg?si=DTt9jPBYCz_CCeiV',# Can't Stop Me Now {MP4}
        'https://www.youtube.com/watch?v=Kj5Vzg21WnI&list=OLAK5uy_kIiPYNXdOHp5LSCE988IwRx-anaU6tskE&index=1',# Metamorph (playlist)
        'https://www.youtube.com/watch?v=oP5S04q6sVo&list=OLAK5uy_nlKCAU567rGd8Fpo86ZnNP5h5SLDZGyms',# Pressure (playlist){MP4}
        'https://www.youtube.com/watch?v=3wZllhP3FZo&list=OLAK5uy_lBTlVQuWRlUeRP65IJPI3jTM6CmpElZMo',# Chucks Flannels and Fenders (playlist){MP4}
        'https://www.youtube.com/watch?v=SYZ4y6iQdvU&list=OLAK5uy_mZWPOQ6IUqEy6rXkKPVpXhuAn3rV4wTbc',# Head Up {MP4}
        'https://www.youtube.com/watch?v=GXDNMinUPXc&list=OLAK5uy_lrUuV_JhYtdwv5NKsWpKtHZAOlzugESEo',# Best Part {MP4}
        'https://www.youtube.com/watch?v=BH8pv4Iht8g&list=OLAK5uy_mbPE50jkLbcCL71dYRxWhiYX6lsxCnPXY',# Bulletproof {MP4}
        'https://www.youtube.com/watch?v=Kj5Vzg21WnI&list=OLAK5uy_mwS4FLjWHxralDm0Dmp-slYn0Hqgu65x8',# Victorious {MP4}
        'https://www.youtube.com/watch?v=8RDy31N0gdY&list=OLAK5uy_nrvMViAVt6zizmPXf0I95h3zP9aEPr_s8',# Carry On (playlist)
        'https://www.youtube.com/watch?v=sjLRh-QPM9c&list=OLAK5uy_m6Rh9aRpZ8NMIs_VBzgPhbporqxcAp9UA',# Top Of The World {MP4}
        'https://www.youtube.com/watch?v=1fG2SqZ-R5Q&list=OLAK5uy_mUinkjduRBkBomGdctjVMV-Iyn8ZozMgs',# Stay (playlist) {MP4}
        'https://www.youtube.com/watch?v=VfRcGxjWboo&list=OLAK5uy_ln3teeQf_C730ud8-DFxtr9RijjM_CXe4',# ATLAS (playlist) {MP4}
        'https://www.youtube.com/watch?v=mz3RwyXlpHc&list=OLAK5uy_m8e7fhAiRfAfeX9-BdLi3C-Br73vp-Dp8',# Enemies {MP4}
        
    ],
    
    "NEFEX":[
        'https://youtu.be/P055h-3L6Sk?si=KJo-RPPddUne3LUA',
        'https://www.youtube.com/watch?v=83RUhxsfLWs',
        'https://www.youtube.com/watch?v=yV6yCNfenJs',
        'https://www.youtube.com/watch?v=DEpO-Oh3MAw',
        'https://www.youtube.com/watch?v=a6j5lbt6OLQ',
        'https://www.youtube.com/watch?v=CYDP_8UTAus',
        'https://www.youtube.com/watch?v=z1MgFIpSqJk',
        'https://www.youtube.com/watch?v=qtSmf-hhHyk',
        'https://www.youtube.com/watch?v=aKfO9o2IPJ0',
        'https://www.youtube.com/watch?v=83RUhxsfLWs',
        'https://www.youtube.com/watch?v=X5cfg26vkOQ',
        'https://www.youtube.com/watch?v=Ccsh_-Cucl4',
        'https://www.youtube.com/watch?v=BVy9MApx9KA',
        'https://www.youtube.com/watch?v=kdYcG9l-fio',
        'https://www.youtube.com/watch?v=ExQ-XgsmL5Y',
        'https://www.youtube.com/watch?v=EgZ39cjAJuM',
        'https://www.youtube.com/watch?v=6WhefAhgeQw&list=PLrxcNWZXdQ2kmHEf4XNOCHs5eHvOzlQ3z',

    ],
    
    "The Chainsmokers":[
        'https://www.youtube.com/watch?v=eACohWVwTOc',# Sick Boy 
        'https://www.youtube.com/watch?v=GnNi_LuMnN4',# Sick Boy (ONEDUO Remix)
        'https://www.youtube.com/watch?v=9339wHfiQXY',# Sick Boy (Owen Norton Remix)
        'https://youtu.be/tlILlcCE8Sc?si=o4j0Q2CEe6BpMek2',# Somebody {MP4}
        'https://www.youtube.com/watch?v=sY8aL17tusg',# Don't Let Me Down
        'https://www.youtube.com/watch?v=PT2_F-1esPk',# Closer {MP4}
        'https://www.youtube.com/watch?v=DrKA7sKOhws&list=OLAK5uy_mYnxqzxYuLidfZyjfi56-rqMWe89loRK0',# Self Destruction Mode
        'https://www.youtube.com/watch?v=FM7MFYoylVs&list=OLAK5uy_m4uQCCuYP056fEpPb3hCg2gRszf570VHM',# Something Just Like This
    ],
    
    "Ruelle":[
        'https://www.youtube.com/watch?v=DjkJ7SUe-4o',# Empires
        'https://www.youtube.com/watch?v=UM3X5pdhVEk',# Hold Your Breath
        'https://www.youtube.com/watch?v=BnSkt6V3qF0',# Madness
        'https://www.youtube.com/watch?v=4NmX5vcNK6E',# Bad Dream
        'https://www.youtube.com/watch?v=UqX6GZ2nz88',# LIVE LIKE LEGENDS
        'https://www.youtube.com/watch?v=lDsSiaSs9Bo',# Daydream
        'https://www.youtube.com/watch?v=-T5eYF9WiRI',# Game of Survival
        'https://www.youtube.com/watch?v=IeFzk1qYSc4',# Closing In
        'https://www.youtube.com/watch?v=PPte8HzjpQk',# Monsters
        'https://www.youtube.com/watch?v=GX7f1Btk1yM',# War Of Hearts 
        'https://www.youtube.com/watch?v=iBqBWleWW0U',# The World We Made 

    ],
    
    "Sam Tinnesz":[
        'https://www.youtube.com/watch?v=EKVZrbitbd8',# Legends Are Made
        'https://www.youtube.com/watch?v=gOMsN0FNg2Y',# Sound Off the Sirens
        'https://www.youtube.com/watch?v=ZaPqkconvIE',# Wolves 
        'https://www.youtube.com/watch?v=yzVQkO92wNw',# Play With Fire
        'https://www.youtube.com/watch?v=50stcfV5fmA',# Ready Set Let's Go
        'https://www.youtube.com/watch?v=ptIhqKgB9AI',# Bloodshot 

    ],
    
    "Kevin McAllister":[
        'https://youtube.com/watch?v=cHK2b3zf4hw&pp=ygUQS2V2aW4gTWNBbGxpc3Rlcg%3D%3D'# Play Dirty
    ],
    
    "ImagineDragons":[
        'https://www.youtube.com/watch?v=w3viBe2Q0P8',# Radioactive
        'https://www.youtube.com/watch?v=V5M2WZiAy6k',# Natural{MP4}
        'https://www.youtube.com/watch?v=e4RMh7NLHPY',# Roots
        'https://youtu.be/7wtfhZwyrcc?si=EbSix9Zy7z9kSHFs',# Believer {MP4}
        'https://youtu.be/IOrbP1OqNsg?si=-1twVzUKIrYp6LSf',# Enemy (Arcane League of Legends)
        'https://youtu.be/pvrkfb1C4tE?si=BYYCBuEt04--DJmH',# Demons
        'https://youtu.be/w3viBe2Q0P8?si=CMQddLKMfLNrYMkz',# Radioactive
        'https://youtu.be/CBDT9LkrrVc?si=FK__JZ4hPFzSMqcV',# My Life 
        'https://youtu.be/uEDhGX-UTeI?si=mFNMi5S7vGrH1Ldo',# Bad Liar 
        'https://youtu.be/78El9Q-_WzU?si=zLhfWqyfK2j8B0RC',# I'm So Sorry 
    ],
    
    "clarx":[
        'https://www.youtube.com/watch?v=iRJiiRmwi_8',# One Of Us
        'https://www.youtube.com/watch?v=5xXNVcKdCZk',# No Money
        'https://www.youtube.com/watch?v=K4xM2C-_MUE',# H.a.Y 
        'https://www.youtube.com/watch?v=i4V_lzH7NKg',# Numb The Pain
        'https://www.youtube.com/watch?v=pWAKZ-6xIxQ',# Warzone
    ],
    
    "TheFatRat":[
        'https://www.youtube.com/watch?v=whFmuLRRPKU',# Hunger
        'https://www.youtube.com/watch?v=i-wYV7OVoTM',# Out Of The Rain 
        'https://www.youtube.com/watch?v=n8X9_MgEdCg',# Unity
        'https://www.youtube.com/watch?v=B7xai5u_tnk',# Monody 
        'https://www.youtube.com/watch?v=cMg8KaMdDYo',# Fly Away
        'https://www.youtube.com/watch?v=KR-eV7fHNbM',# The Calling 
        'https://www.youtube.com/watch?v=gHgv19ip-0c',# Stronger
        'https://www.youtube.com/watch?v=kL8CyVqzmkc',# Jackpot
        'https://www.youtube.com/watch?v=j-2DGYNXRx0',# Rise Up
        'https://www.youtube.com/watch?v=DT61L8hbbJ4',# MAYDAY
        'https://www.youtube.com/watch?v=jqkPqfOFmbY',# Windfall
        'https://www.youtube.com/watch?v=eWOuuwrREh0',# Sail Away
        'https://www.youtube.com/watch?v=6ZDxop2yFao',# Still Here With You
        'https://www.youtube.com/watch?v=XMWJ8tfeS50',#  Myself & I 
        'https://www.youtube.com/watch?v=Ioh0bqty8LY',# Ray Tracer
        'https://www.youtube.com/watch?v=hh_r7jJBvGM',# Genius
        'https://www.youtube.com/watch?v=0MwcJszdqLI',# Killing Me
        'https://www.youtube.com/watch?v=3ESat1K9Sdc',# Out Of Love
        'https://youtu.be/KFhl5mmEYe0?si=UwZ-KNXmoC7TOrJn',# Hiding in the Blue
        'https://www.youtube.com/watch?v=lW9ep22YmlM',# Royalty {MP4}
        'https://www.youtube.com/watch?v=2QdPxdcMhFQ&list=OLAK5uy_levfcdMAj8RELLiK2yEK2qTIyEesAwoXE',# Back One Day (Outro Song)
        'https://www.youtube.com/watch?v=8fXx3efGot8&list=OLAK5uy_mvtk8HtZl57UkDr1DQkzyBf8-VXtkvnbY',# Fly Away (Inukshuk Remix)

    ],
    "reidenshi":[
        'https://youtu.be/0WykZs55UjA?si=k2_r25TycXHomc8a',
        'https://www.youtube.com/watch?v=LlN8MPS7KQs&list=OLAK5uy_ms0XFuveA8zG4xIIzk-0efPZnpfbYazv4',# snowfall
        'https://www.youtube.com/watch?v=gR3nlpwRTRA&list=OLAK5uy_m2S56JgrRFL_IWzEYpdvEmDnhB2mZnjH4',# snowfall (Slowed + Reverb)
        'https://www.youtube.com/watch?v=1beH7w29t34&list=OLAK5uy_nwRvofQrUjfVgOAi7Pz22zAbcQ6h3P790',# snowfall (Sped Up)
        'https://www.youtube.com/watch?v=SKptOBqpB9E&list=OLAK5uy_mOzUStFWqVLMcgm6cbblxX8fbXftucVzE',#distorted memories (Remixes) (playlist)
        'https://www.youtube.com/watch?v=gSwi1Tk1gV8&list=OLAK5uy_lfaWTSCy9w673-6aH11teOGOMU1X1gbkg',# distorted memories
    ],
    "Manu Pilas":[
        'https://www.youtube.com/watch?v=4JVaRloezno',# Manu Pilas (Original full v. Bella Ciao) | LA CASA DE PAPEL
        'https://www.youtube.com/watch?v=OD6p1dPfoT0',# Bella Ciao (Versión Lenta de la Música Original de la Serie la Casa de Papel / Money Heist)
    ]
    
}
 