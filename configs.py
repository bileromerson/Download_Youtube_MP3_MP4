# The main output folder for all downloads.
out_folder = r'./downloads'

# Set to True to download and embed the video thumbnail in the media file.
download_thumbnail = True

# If set to False, the script will skip downloading a file that already exists.
# If set to True, it will append a counter (e.g., "song_1.mp3") to the filename.
allow_duplicate_downloads = False

# Set to True to display the download progress in the terminal.
show_progress = True

# The desired audio or video quality for the conversion.
# For MP3, '320' is a high-quality option.
# For MP4, '720' or '1080' are common video resolutions.
quality = '320'

# A dictionary containing the artist names as keys and a list of YouTube URLs as values.
# The script will create a folder for each artist and download the media files from the provided URLs.
artists_urls = {
    "Arctica The Fox":[
        'https://www.youtube.com/watch?v=jeLQoGnbTsY&list=OLAK5uy_kNpipHajAQjp_hz3UDGTdGFxjWwHskrHc',
        'https://www.youtube.com/watch?v=4RjQ2kiJjUs&list=OLAK5uy_kxYZAqvHeZyhju8UECze1KE3TPY6pvSqE',
        'https://www.youtube.com/watch?v=TGgc8o1qiws&list=OLAK5uy_nr844SDIyJKuPSEswS749Get6nLc1ukXg',
        'https://www.youtube.com/watch?v=j-SYw_hNRmc&list=OLAK5uy_lynnyb0rBD3CX0DzTpHIgUmmtPhsa8V2U',
        'https://www.youtube.com/watch?v=e4Lbhd8a4fA&list=OLAK5uy_mM8MEQwubS3fnNinUdur5KVyh-mTTQgLo',
        'https://www.youtube.com/watch?v=_Mz3QyH3K18&list=OLAK5uy_l1DZq9RhFIIhW2jQ-aIel5fxRCkqwz4ec',
        'https://www.youtube.com/watch?v=niJZw4kZ7ak&list=OLAK5uy_mtw1Wbrgy1friMCJO-9JX0UzLXgoV9L_s',
        'https://www.youtube.com/watch?v=80ezKLZMlhs&list=OLAK5uy_mDCVug3OburoGlGrx2AzJuVIwSCaRAE4g',
        'https://www.youtube.com/watch?v=mpph5nAfy2k&list=OLAK5uy_nGVGVbBVPOhS7prxOmSzmVcpJonVRbduo',
        'https://www.youtube.com/watch?v=E2lZ51VIJ9o&list=OLAK5uy_kv12hbd29HJuL7A_v_dpSUOcJnfQeW57Y'

    ],
    
    "Snuffles":[
        'https://www.youtube.com/watch?v=_dMbSHwtKk8&list=PLlzTn5sGFPUgFrksUTY94JYWI-2RSKjwE',
        'https://www.youtube.com/watch?v=njowoGhmw6E&list=OLAK5uy_mKdgOUqujhvkqHIONfZKgt9k5wHuCSdxI',
        'https://www.youtube.com/watch?v=xp2SzlnzbkA&list=OLAK5uy_nd0U1gYnm4djWbFTeQkeeqMkXmtCcAS7k',
        'https://www.youtube.com/watch?v=pEtcyFBysAg&list=OLAK5uy_nsF0girFJkrpELredpI3I9ZImlZ81r644',
        'https://www.youtube.com/watch?v=kg3ed9NRQJo&list=OLAK5uy_lnsxWpgYrwA8HKloWfrRGlL9OtUduCaMI',
        'https://www.youtube.com/watch?v=UG1HUOyL9IA&list=OLAK5uy_kEIcrTM3RWwm9j5qBoQmZWQZNKl20MXys',
        'https://www.youtube.com/watch?v=WAX_FEgRuOk&list=OLAK5uy_kIDwFKKJcR6noC1e1JJU-nIrQJzBS3MMg',
        'https://www.youtube.com/watch?v=tc8IhElRJkA&list=OLAK5uy_lzYhwLgaAyHfAQO0iegxNz5hgRfYLn_zQ',
        'https://www.youtube.com/watch?v=GUZWSxqDJUk&list=OLAK5uy_mRa2eCQmZvj3MR3-az37Rb_8NHDpaVRfo',
        'https://www.youtube.com/watch?v=-cIQJ4v_fgk&list=OLAK5uy_lp4Xk0Xf_4B7eAb9XYmB5k_wayTeNooY4',
        'https://www.youtube.com/watch?v=A02vT-I4Dds&list=OLAK5uy_n8FLDf0Iyqhme6uHxJSAIpxYFWf6Eynmo',
        'https://www.youtube.com/watch?v=q7GOk-cE3mY&list=OLAK5uy_mGmWuKY6gPq_iguZ0l19dHlcTLazsBGXE',
        'https://www.youtube.com/watch?v=b4VFkSG4lk8&list=OLAK5uy_nC9wPyRwh8FgxoDoPz8LEwr5Nqbzi9maw'
    ],
    
    "Verplex":[
        'https://www.youtube.com/watch?v=9Qjz_nofaTU&list=OLAK5uy_kPMzB4Ikv1IZncGQh6SEjbGjAlRP4SUuQ&index=1',
        'https://www.youtube.com/watch?v=MT9mjFmuXrM&list=OLAK5uy_lmNOCPJHrqXVGe-v86N10cEb2qPbpVABA',
        'https://www.youtube.com/watch?v=j1BBDk7dRU4&list=OLAK5uy_nm3m_s6rTSb7b1VZ4EGRM9prq6pt9zWvA',
        'https://youtu.be/2W1430K81fY?si=SqJIowF0tBVLOI4H',
        'https://youtu.be/MN40SigmSG8?si=DVHzZceDWIRd9cfl',
        'https://youtu.be/6sb4ZJycP10?si=OK_r80DADTXHQOoG',
        'https://youtu.be/qREZFPu543k?si=wXgwQVHIdZvCoP_s',
        'https://youtu.be/2-hvzl4ZGAE?si=1MpbiolznUDlSD4I',
        'https://youtu.be/S2xcpKl0k98?si=B6q6YfnOpFjgH3IJ',
        'https://youtu.be/lsWCxrLbUy0?si=iH3BGONfaia2oU5o',
        'https://youtu.be/wrsSoHogXNY?si=wpo1aK1dyoN4nubt',
        'https://www.youtube.com/watch?v=7phPDKJRoL0&list=OLAK5uy_mZuoOOPSosrDJfeFhhKhpPRl46FuvSxao',
        'https://www.youtube.com/watch?v=7r4BvQcp28Q&list=OLAK5uy_lwD8otxu138tB_mndBloSlY3xCRmqujhw',
        'https://www.youtube.com/watch?v=uIkg7CX4H5M&list=OLAK5uy_nEz_7t3XbRqYDrmNyt0gCVY7ZzNmZs-Fs',
        'https://www.youtube.com/watch?v=obEpf-UqmQg&list=OLAK5uy_myJW2KhTgMdxe-QeVB_0LyesJi_gXdIg0',
        'https://www.youtube.com/watch?v=2ha1-PI8O7M&list=OLAK5uy_nEhM5-XkhmKJ_hEtr-EOt6STLuaxgMGFc',
        'https://www.youtube.com/watch?v=ECmFUcgJock&list=OLAK5uy_mAQ7zQ41xr3SO7etS95rbEGaDoyd2OFr8',
        'https://www.youtube.com/watch?v=vMUW3B0kbCc&list=OLAK5uy_m2P-8g6Pr8EUKtRfevtOCAl9L_9wtmaYs',
        'https://www.youtube.com/watch?v=mzuRmldhgmo&list=OLAK5uy_kM_PEyqDuKrEKBydCinM8x71oQy12fp_M',
        'https://www.youtube.com/watch?v=fiRnaIOgGWQ&list=OLAK5uy_m2POT2mwpMyxbKprsMMb1vRB10xSUYA6c',
        'https://www.youtube.com/watch?v=8CDylhggwXA&list=OLAK5uy_m7-Mkbdh3pegmmhMLqliDFYcz2q-ymgNU',
        'https://www.youtube.com/watch?v=Tcf5ZB5GtbY&list=OLAK5uy_lAyJ9-rcJ_86--ugN4lI2bkz4L5zSYBuE',
        'https://www.youtube.com/watch?v=ThxrRKztpR8&list=OLAK5uy_lhUmLokgXUtNzIoSLGSCAqeVgKNEXmDIc',
        'https://www.youtube.com/watch?v=-KNWakEZHzE&list=OLAK5uy_lqs_4kn5pJiAMnG7fSA7_Nw3NX2uCj-Tw',
        'https://www.youtube.com/watch?v=ZGIMoV4RPkQ&list=OLAK5uy_nY1zHCaaNvY4c_IsLTbTVbYcIu-RTTS_s',
        'https://www.youtube.com/watch?v=JEDzySz3IN8&list=OLAK5uy_ms-OBAGp-e4G2PkI8uRlSWBZqC8GCQ7Gc',
        'https://www.youtube.com/watch?v=yKsOFf4F3wg&list=OLAK5uy_nz5gC554yL9aOCxTc43oFW8Bk4pa-MN_E',
        'https://www.youtube.com/watch?v=FBYAfXY-qoQ&list=OLAK5uy_lcQEbbpcIl3Ucl7ZPEpWf7HUhBQxouEAE',
        'https://www.youtube.com/watch?v=z1IdaICQ8OY&list=OLAK5uy_noP4t1pVxVxMcql71g69IpDFOKJ-kgO-w',
        'https://www.youtube.com/watch?v=LWQHXAnKC58&list=OLAK5uy_klElLbLXUO-g4impKglD92wRajY9TGwGI',
        'https://www.youtube.com/watch?v=TVhBWBPmT5w&list=OLAK5uy_ksy082fO2KJ3RgcX2NgwcRdhOpK8uDQpk'

    ],
    
    "Ivycomb":[
        'https://www.youtube.com/watch?v=3b8SfbqD7Yw&list=OLAK5uy_nOOLG59VVJRytk9ghYXfylODcv3TzXRsM',
        'https://www.youtube.com/watch?v=xF_gHb4_K98&list=OLAK5uy_nsjRiwOOS4s7KDa02m76YYZJbjHGTEZRw',
        'https://www.youtube.com/watch?v=YuHeSoASQPs&list=OLAK5uy_m015vrwWGkEQ6x5jFLXugfQDyD2ZkPcYE',
        'https://www.youtube.com/watch?v=yZfgMgIOS3E&list=OLAK5uy_klD7cqgO1absGEfwSvu7KBnN0G7WsIudI',
        'https://www.youtube.com/watch?v=hnJr0Fdm0bU&list=OLAK5uy_nH2l1qzxfhji4sUBGF88RLPDzVlZo9K80',
        'https://www.youtube.com/watch?v=eJLbw0Oq2S8&list=OLAK5uy_lUdCOhyBmC0nELUuTr6jMzaVGllIrstFU',
        'https://www.youtube.com/watch?v=FNunVRexQ9k&list=OLAK5uy_l2e59OrGenJDIXQ2t1JeRRCfFcJdY5F58',
        'https://www.youtube.com/watch?v=VQywoIhcNC8&list=OLAK5uy_mghX73W3hk4yZ7caMuQcoEniOYltYCTOo',
        'https://www.youtube.com/watch?v=VC2WpFKuzZw&list=OLAK5uy_lqXzGNhX9tyXuQcGWGojWxOfZaRJjlW8I',
        'https://www.youtube.com/watch?v=3Nhn-a2gSlE&list=OLAK5uy_ky_9sKRZ1mOW-HB1RpTvz8RjH5CMNILcQ',
        'https://www.youtube.com/watch?v=OWd-oH_Lylc&list=OLAK5uy_n8oHG4vujwYhV1-wbv9KCDNdcBfbLxlEg',
        'https://www.youtube.com/watch?v=txeHnnCj9Ow&list=OLAK5uy_lQjgOG7MhQuvpsWgkAtovaQ5nMYQTBnKU',
        'https://www.youtube.com/watch?v=r37UXmf4E3s&list=OLAK5uy_lJjybsq02aIkd_ulWiJ_mzJ7z7sWoAgZo',
        'https://www.youtube.com/watch?v=I7RwP8ItO1M&list=OLAK5uy_mBS25bwRE7p09VWaIMvqEfaN-krhZ717I',
        'https://www.youtube.com/watch?v=Y-UPgQOt874&list=OLAK5uy_nIriExSLEHLl96FcCibtIrf4sg0owa2tY',
        'https://www.youtube.com/watch?v=jtnoDnOo_nE&list=OLAK5uy_ne4L36wnflBhLK133CgZfjqVmH3aXBbyc',
        'https://www.youtube.com/watch?v=Mvik9CTsNrA&list=OLAK5uy_mOXaosw_tSQ7A2nLN_X1Z12XRqrB1TD2I',
        'https://www.youtube.com/watch?v=vUa4yI5pRCE&list=OLAK5uy_kHztMDCVAcidwm-DazpD3fcBURlCNO4D4',
        'https://www.youtube.com/watch?v=kYELWX1fu18&list=OLAK5uy_lyF21ZxsF6lLnAphVfPLfkteaeJXYg8_o',
        'https://www.youtube.com/watch?v=qul3Qd11u90&list=OLAK5uy_lF6xKF62zn2oDnWnCoJqgG3iwP16huGNY',
        'https://www.youtube.com/watch?v=aXHLgy-HQ4w&list=OLAK5uy_keVOA6f55E_ZD8XO2PKYe13WXUUHlwbb0',
        'https://www.youtube.com/watch?v=Pfv18GSX324&list=OLAK5uy_n4eFPw2iCMzDKS-gSTU7ZtmL_0YsU4IE8',
        'https://www.youtube.com/watch?v=Lnyw5aJkZjg&list=OLAK5uy_lDU78gf_6ikrHN2-lENlbX4iP1VHj5K8A',
        'https://www.youtube.com/watch?v=8G_wgBxnTec&list=OLAK5uy_lnDKaKYg4U3Gx9SErO9-PsQm7E6tCkA84',
        'https://www.youtube.com/watch?v=7hZjuxooNjk&list=OLAK5uy_kJVRPd-JbQEx9PmdT3mvTxxlRoqt61Q7k',
        'https://www.youtube.com/watch?v=r8aqc6AGJKM&list=OLAK5uy_lipx_vH7ncLqrQQC9cBUtq2eYqLaaeSFM',
        'https://www.youtube.com/watch?v=Uq4Jees1sik&list=OLAK5uy_lBptObrrnFD-qNg7I92uZiq_PIUHA9BN8',
        'https://www.youtube.com/watch?v=TlDL2G31QLQ&list=OLAK5uy_k5dQ5TFFUGuH2liCVsuFSQlNB48wK_vvk',

    ],
    
    "narpy":[
        'https://www.youtube.com/watch?v=DpJpdJPndlM&list=OLAK5uy_mkKc5O3pqotX5k3dN4TY-jcpnGdexAuvQ',
        'https://www.youtube.com/watch?v=HpXyLcAdnG8&list=OLAK5uy_ndTg0FNTGzp_uow-qc_UZK-8cAU8HaVvw',
        'https://www.youtube.com/watch?v=LaSBPWQWrGk&list=OLAK5uy_khPW1JiqdhRfDo6WfDuLxipb7giUU2jGo',
        'https://youtu.be/KdAxWr_htj8?si=h6pK8CiBY63dzfaI',
        'https://youtu.be/fn-_ChY9YfA?si=u70mMlcO9PK24Lva',
        'https://youtu.be/Z5mHLIBF3dA?si=-3QhDt56FD-u83cQ',
        'https://youtu.be/ntvBrIscNDY?si=DI3zyyUwZyjZOc4e',
        'https://www.youtube.com/watch?v=uzk8XuCbyKE',
        'https://www.youtube.com/watch?v=6P0N_jnyBto',

    ],
    
    "When Snakes Sing":[
        'https://www.youtube.com/watch?v=Vjf-x-zngx0&list=PLVs7u8sISshyMDvrUbHHQWO7FazYjXECk',
        'https://www.youtube.com/watch?v=RQYpNAV0rUI&list=PLVs7u8sISshwZaLP6A5mOIv7St7U5SeZO',
        'https://youtu.be/PAigrSsOCyY?si=eB-I9rBmVE_P0lPo',
        'https://www.youtube.com/watch?v=nzay7XJf1qM&list=OLAK5uy_lXX2KqKamBZyIqbOTM8O_aTE1-NkOHCMU',
        'https://www.youtube.com/watch?v=ZwbxqGVCQGc&list=OLAK5uy_m8HWgkAbeNZ0fKANMKpQrmOIHcrCWDqHM',
        'https://www.youtube.com/watch?v=CG_G5FU956E&list=OLAK5uy_neQrN6v7K_mqg32CVS_AUJW0l1k-iGgV8'    
    ],
    
    "The score":[
        'https://www.youtube.com/watch?v=ALXFl6HfKbg',
        'https://www.youtube.com/watch?v=Kj5Vzg21WnI&list=OLAK5uy_kIiPYNXdOHp5LSCE988IwRx-anaU6tskE&index=1',
        'https://www.youtube.com/watch?v=8RDy31N0gdY&list=OLAK5uy_nrvMViAVt6zizmPXf0I95h3zP9aEPr_s8',
        'https://www.youtube.com/watch?v=VfRcGxjWboo&list=OLAK5uy_ln3teeQf_C730ud8-DFxtr9RijjM_CXe4',
        'https://youtu.be/ALXFl6HfKbg?si=XxP_zdq_enG2zTOD',
        'https://youtu.be/uf1M263w_fQ?si=R3WwMXwnS3nj6LcL',
        'https://youtu.be/uhXW7eqF_SQ?si=b4aEQkulnowWxqtm',
        'https://youtu.be/6sl7rTwPJuo?si=h3YUTxeVQ3bbEtoi',
        'https://youtu.be/ruw2woPI-fg?si=k50lj6REERE84ZE6',
        'https://youtu.be/RyBDRS39G_w?si=PxR7i1-Xmt2szVkh',
        'https://www.youtube.com/watch?v=oP5S04q6sVo&list=OLAK5uy_nlKCAU567rGd8Fpo86ZnNP5h5SLDZGyms',
        'https://www.youtube.com/watch?v=3wZllhP3FZo&list=OLAK5uy_lBTlVQuWRlUeRP65IJPI3jTM6CmpElZMo',
        'https://www.youtube.com/watch?v=1fG2SqZ-R5Q&list=OLAK5uy_mUinkjduRBkBomGdctjVMV-Iyn8ZozMgs',
        'https://www.youtube.com/watch?v=SYZ4y6iQdvU&list=OLAK5uy_mZWPOQ6IUqEy6rXkKPVpXhuAn3rV4wTbc',
        'https://www.youtube.com/watch?v=GXDNMinUPXc&list=OLAK5uy_lrUuV_JhYtdwv5NKsWpKtHZAOlzugESEo',
        'https://www.youtube.com/watch?v=BH8pv4Iht8g&list=OLAK5uy_mbPE50jkLbcCL71dYRxWhiYX6lsxCnPXY',
        'https://www.youtube.com/watch?v=Kj5Vzg21WnI&list=OLAK5uy_mwS4FLjWHxralDm0Dmp-slYn0Hqgu65x8',
        'https://www.youtube.com/watch?v=sjLRh-QPM9c&list=OLAK5uy_m6Rh9aRpZ8NMIs_VBzgPhbporqxcAp9UA',
        'https://www.youtube.com/watch?v=mz3RwyXlpHc&list=OLAK5uy_m8e7fhAiRfAfeX9-BdLi3C-Br73vp-Dp8',
        'youtube.com/watch?v=jecQcgbyetw&pp=ygURdGhlIHNjb3JlIGxlZ2VuZHM%3D',
        'https://youtu.be/ZRRt8EyYNvg?si=DTt9jPBYCz_CCeiV',


    ],
    
    "NEFEX":[
        'https://www.youtube.com/watch?v=6WhefAhgeQw&list=PLrxcNWZXdQ2kmHEf4XNOCHs5eHvOzlQ3z',
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
        'https://www.youtube.com/watch?v=EgZ39cjAJuM'

    ],
    
    "The Chainsmokers":[
        'https://www.youtube.com/watch?v=DrKA7sKOhws&list=OLAK5uy_mYnxqzxYuLidfZyjfi56-rqMWe89loRK0',
        'https://www.youtube.com/watch?v=FM7MFYoylVs&list=OLAK5uy_m4uQCCuYP056fEpPb3hCg2gRszf570VHM',
        'https://youtu.be/tlILlcCE8Sc?si=o4j0Q2CEe6BpMek2',
        'https://youtu.be/tlILlcCE8Sc?si=GGqzQq12WlEUII5i',
        'https://www.youtube.com/watch?v=sY8aL17tusg',
        'https://www.youtube.com/watch?v=PT2_F-1esPk'
    ],
    
    "Ruelle":[
        'https://www.youtube.com/watch?v=DjkJ7SUe-4o',
        'https://www.youtube.com/watch?v=UM3X5pdhVEk',
        'https://www.youtube.com/watch?v=BnSkt6V3qF0',
        'https://www.youtube.com/watch?v=4NmX5vcNK6E',
        'https://www.youtube.com/watch?v=UqX6GZ2nz88',
        'https://www.youtube.com/watch?v=lDsSiaSs9Bo',
        'https://www.youtube.com/watch?v=uQoHmfi8FEw',
        'https://www.youtube.com/watch?v=-T5eYF9WiRI',
        'https://www.youtube.com/watch?v=IeFzk1qYSc4',
        'https://www.youtube.com/watch?v=PPte8HzjpQk',
        'https://www.youtube.com/watch?v=GX7f1Btk1yM',
        'https://www.youtube.com/watch?v=iBqBWleWW0U'

    ],
    
    "Sam Tinnesz":[
        'https://www.youtube.com/watch?v=yzVQkO92wNw',
        'https://www.youtube.com/watch?v=EKVZrbitbd8',
        'https://www.youtube.com/watch?v=gOMsN0FNg2Y',
        'https://www.youtube.com/watch?v=ZaPqkconvIE',
        'https://www.youtube.com/watch?v=yzVQkO92wNw',
        'https://www.youtube.com/watch?v=50stcfV5fmA',
        'https://www.youtube.com/watch?v=ptIhqKgB9AI'

    ],
    
    "Kevin McAllister":[
        'youtube.com/watch?v=cHK2b3zf4hw&pp=ygUQS2V2aW4gTWNBbGxpc3Rlcg%3D%3D'
    ],
    
    "ImagineDragons":[
        'https://youtu.be/7wtfhZwyrcc?si=t7B_WnfI7lHNrECg',
        'https://youtu.be/IOrbP1OqNsg?si=-1twVzUKIrYp6LSf',
        'https://youtu.be/pvrkfb1C4tE?si=BYYCBuEt04--DJmH',
        'https://youtu.be/w3viBe2Q0P8?si=CMQddLKMfLNrYMkz',
        'https://youtu.be/CBDT9LkrrVc?si=FK__JZ4hPFzSMqcV',
        'https://youtu.be/uEDhGX-UTeI?si=mFNMi5S7vGrH1Ldo',
        'https://youtu.be/78El9Q-_WzU?si=zLhfWqyfK2j8B0RC',
        'https://youtu.be/7wtfhZwyrcc?si=EbSix9Zy7z9kSHFs',
        'https://www.youtube.com/watch?v=w3viBe2Q0P8',
        'https://www.youtube.com/watch?v=V5M2WZiAy6k',
        'https://www.youtube.com/watch?v=e4RMh7NLHPY',
        'https://www.youtube.com/watch?v=7wtfhZwyrcc'
    ],
    
    "clarx":[
        'https://www.youtube.com/watch?v=iRJiiRmwi_8',
        'https://www.youtube.com/watch?v=_OLrjAWzUR0',
        'https://www.youtube.com/watch?v=K4xM2C-_MUE',
        'https://www.youtube.com/watch?v=L75f9TWj3Mw',
        'https://www.youtube.com/watch?v=_OLrjAWzUR0',
        'https://www.youtube.com/watch?v=pWAKZ-6xIxQ'
    ],
    
    "TheFatRat":[
        'https://www.youtube.com/watch?v=whFmuLRRPKU',
        'https://www.youtube.com/watch?v=i-wYV7OVoTM',
        'https://www.youtube.com/watch?v=n8X9_MgEdCg',
        'https://www.youtube.com/watch?v=B7xai5u_tnk',
        'https://www.youtube.com/watch?v=cMg8KaMdDYo',
        'https://www.youtube.com/watch?v=KR-eV7fHNbM',
        'https://www.youtube.com/watch?v=gHgv19ip-0c',
        'https://www.youtube.com/watch?v=kL8CyVqzmkc',
        'https://www.youtube.com/watch?v=j-2DGYNXRx0',
        'https://www.youtube.com/watch?v=DT61L8hbbJ4',
        'https://www.youtube.com/watch?v=jqkPqfOFmbY',
        'https://www.youtube.com/watch?v=eWOuuwrREh0',
        'https://www.youtube.com/watch?v=6ZDxop2yFao',
        'https://www.youtube.com/watch?v=XMWJ8tfeS50',
        'https://www.youtube.com/watch?v=Ioh0bqty8LY',
        'https://www.youtube.com/watch?v=hh_r7jJBvGM',
        'https://www.youtube.com/watch?v=0MwcJszdqLI',
        'https://www.youtube.com/watch?v=3ESat1K9Sdc',
        'https://youtu.be/KFhl5mmEYe0?si=UwZ-KNXmoC7TOrJn',
        'https://www.youtube.com/watch?v=2QdPxdcMhFQ&list=OLAK5uy_levfcdMAj8RELLiK2yEK2qTIyEesAwoXE',
        'https://www.youtube.com/watch?v=8fXx3efGot8&list=OLAK5uy_mvtk8HtZl57UkDr1DQkzyBf8-VXtkvnbY',
        'https://www.youtube.com/watch?v=lW9ep22YmlM'

    ]
    
}
