from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup
import dill as pickle
main_list = [];

for i in range(6,7):
        try:
            browser = webdriver.PhantomJS('./phantomjs');
            browser.get("http://125.17.181.197/StudentView.php");
            if(i <= 9):
                browser.find_element_by_name('reg_no').send_keys('31231410730'+str(i));
            else:
                browser.find_element_by_name('reg_no').send_keys('3123141070'+str(i));
            browser.find_element_by_id('submit').click()
            element_present = ec.presence_of_element_located((By.CLASS_NAME, 'black_overlay1'))
            WebDriverWait(browser, 10).until(element_present)

            soup = BeautifulSoup(browser.page_source.encode('utf-8'), 'html.parser')

            cgpas = soup.find_all('table')[1].find_all('tr')[3].find_all('td')

            list={};
            list['reg_no']='3123141070'+str(i);
            list['name']= soup.find_all('table')[0].find_all('tr')[2].find_all('td')[1].get_text()
            for idx, i in enumerate(cgpas):
                if(idx==9):
                    list["total_cgpa"] = i.get_text();
                    continue;
                if(i.get_text()=="GPA/CGPA"):
                    continue;
                else:
                    list["sem-"+str(idx)] = i.get_text()

            main_list.append(list);
            print list
            browser.close()

        except:
            print("There was an error with rool no : " + str(i));



with open('list.pkl', 'w') as src:
    pickle.dump(main_list, src)
