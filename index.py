#%%
from functools import partial
from csmodules.selepy import *
from csmodules.xproxy import proxy_reset
from threading import Thread
import threading
from selenium import webdriver
from time import sleep
from threading import Thread,Lock
import random
from random import randint,choice
from time import sleep


ports = [4000,4001,4002]

list_question_2 = ['Crypto regulation will become clear in 2022.','Bitcoin will break $250,000 USD in 2022.','Should governments be able to ban cryptocurrencies?','I use a hardware wallet.']

list_question_3 = ['How are you feeling about the NFT market today?','How are you feeling about the cryptocurrency market today?','How are you feeling about the defi market today?','How are you feeling about metaverse projects today?']




def lunarcrush_main(index):

    chrome_path = r'E:\1_GOOGLE\chrome_'+str(i)+r'\Data\profile'
    
    proxy = '--proxy-server=http://192.168.1.40:'+str(ports[index])
    (driver,cswait) = open_driver(chrome_path, binary_auto=True, chrome_agrs=proxy,images=True)

    driver.get('https://lunarcrush.com/')
    sleep(1)
    


    loop_number = 0
    while loop_number < 12:
        loop_number = loop_number + 1
        driver.get('https://lunarcrush.com/')

        answer_1 = '//*[@id="lunar-component-wrap"]/div/div/div/div/div[7]/div[3]/div[3]/div/div/div/div/div[3]/div[1]/div/div'
        answer_2 = '//*[@id="lunar-component-wrap"]/div/div/div/div/div[7]/div[3]/div[3]/div/div/div/div/div[3]/div[2]/div/div'
        answer_3 = '//*[@id="lunar-component-wrap"]/div/div/div/div/div[7]/div[3]/div[3]/div/div/div/div/div[3]/div[3]/div/div'
        answer_next = '//*[@id="lunar-component-wrap"]/div/div/div/div/div[7]/div[3]/div[3]/div/div/div/div/div[3]/div[2]/div[1]/div[3]/div/div'

# --------------------------- Home Opinions ---------------------------
        try:
            lunr_question = cswait.get_element_by_xpath(10,'//*[@id="lunar-component-wrap"]/div/div/div/div/div[7]/div[3]/div[3]/div/div/div/div/div[2]/div').text       
            for question_2 in list_question_2:
                if lunr_question == question_2:
                    opinion = 2
                    break
                else:
                    for question_3 in list_question_3:
                        if lunr_question == question_3:
                            opinion = 3
                            break
                        else:
                            opinion = 1

            if opinion == 1:
                cswait.click_by_xpath(2,answer_1)
                sleep(randint(1,2))
                cswait.click_by_xpath(2,answer_next)
            elif opinion == 2:
                cswait.click_by_xpath(2,answer_2)
                sleep(randint(1,2))
                cswait.click_by_xpath(2,answer_next)
            else:
                cswait.click_by_xpath(2,answer_3)
                sleep(randint(2,3))
                cswait.click_by_xpath(2,answer_next)
            
            sleep(5)
        except:
            pass
# --------------------------- !!! Home Opinions ---------------------------


# --------------------------- Random Opinions -----------------------------
        sleep(10000)
        driver.get('https://lunarcrush.com/feeds')
        sleep(randint(1,2))
        cswait.click_by_xpath(1,'//*[@id="feeds-left-scroll"]/div/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[4]')
        sleep(randint(2,3))
        driver.get('https://lunarcrush.com/')
        sleep(randint(2,3))
        try:
            sleep(randint(2,3))
            driver.get('https://lunarcrush.com/markets')
            sleep(randint(2,3))
            driver.get('https://lunarcrush.com/coins/btc/bitcoin')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[3]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[4]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[5]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[6]/div[1]')
        except:
            pass
        sleep(randint(10,25))

        try:
            driver.get('https://lunarcrush.com/influencers')
            sleep(randint(2,3))
        except:
            pass
        sleep(randint(10,25))

        try:
            driver.get('https://lunarcrush.com/markets')
            sleep(randint(2,3))
            driver.get('https://lunarcrush.com/coins/eth/ethereum')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[3]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[4]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[5]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[6]/div[1]')
        except:
            pass
        sleep(randint(10,25))
        try:
            driver.get('https://lunarcrush.com/markets')
            sleep(randint(2,3))
            driver.get('https://lunarcrush.com/coins/bnb/binance-coin')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[3]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[4]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[5]/div[1]')
            sleep(randint(2,3))
            cswait.click_by_xpath(1,'//*[@id="lunar-component-wrap"]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/div[6]/div[1]')

        except:
            pass
# --------------------------- !!! Random Opinions -----------------------------
        sleep(randint(1,3))

    driver.quit()
    proxy_reset(ports[index])

    sleep(3)

    
workers = []
loop_start = 1
loop_end = 2
for loop_chrome in range(1,20):

    print(loop_start)
    print(loop_end)

    for i in range (loop_start,loop_end):
        task = partial(lunarcrush_main,i)
        worker = Thread(target = task)
        worker.start()
        workers.append(worker)
    for worker in workers:
        worker.join()
    loop_start = loop_start + 1
    loop_end =   loop_end + 1

